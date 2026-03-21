import random
from dataclasses import replace as _dc_replace
from game.player import Player
from game.enemy import get_random_enemy, make_boss_with_modifiers
from game.ui import UI
from game.combat import (player_attack, player_magic, enemy_turn,
                         player_turn_start, enemy_turn_start, SPELLS)
from game.status import consume_stun
from game.items import ITEMS
from game.shop import run_shop
from game.story import get_event, resolve_ending, apply_effect
from game.i18n import t


class Dungeon:
    def __init__(self, player: Player, ui: UI):
        self.player = player
        self.ui = ui
        self.floor = 1
        self.max_floors = 7

    def run(self):
        self.ui.print(f"\n[bold]{t('welcome', name=self.player.name, cls=self.player.player_class)}[/bold]")
        self.ui.print(f"[dim]{t('dungeon_intro')}[/dim]")
        self.ui.pause()

        while self.floor <= self.max_floors:
            self.ui.show_floor(self.floor, self.max_floors)

            if self.floor == self.max_floors:
                # Cleanse status effects before boss fight
                self.player.status_effects = []
                # Resolve story ending and apply Dragon modifiers
                self.player.active_ending = resolve_ending(self.player.story_flags)
                modifier = dict(self.player.active_ending.get("dragon_modifier", {}))

                self.ui.print(f"\n[bold red]{t('boss_rumble')}[/bold red]")
                if "bonus_msg" in modifier:
                    self.ui.print(f"[italic yellow]{t(modifier['bonus_msg'])}[/italic yellow]")
                def_bonus = modifier.get("player_def_bonus", 0)
                if def_bonus:
                    self.player.apply_bonus(defense=def_bonus)
                self.ui.pause(t("prepare_dragon"))

                enemy = make_boss_with_modifiers(self.floor, modifier)
                result = self._combat(enemy, modifier)

            else:
                self.ui.pause(t("floor_explore", floor=self.floor))
                result = "win"
                for _ in range(random.randint(2, 3)):
                    enemy = get_random_enemy(self.floor)
                    self.ui.print(f"\n[red]{t('enemy_appears', name=enemy.name)}[/red]")
                    self.ui.pause()
                    result = self._combat(enemy, {})
                    if result == "dead":
                        break
                    self._rest_event()

            if result == "dead":
                self.ui.show_game_over(self.player)
                return

            if self.floor == self.max_floors:
                self.ui.show_victory(self.player, self.player.active_ending)
                return

            # Between-floor: story event then shop
            self.ui.print(f"\n[bold green]{t('floor_cleared', floor=self.floor)}[/bold green]")

            # Prisoner return bonus (floor 3, spared on floor 1)
            if self.floor == 3 and self.player.story_flags.get("spared_prisoner"):
                self._prisoner_return_bonus()

            event = get_event(self.floor)
            if event:
                self.ui.pause(t("story_event_hint"))
                # Filter to choices valid for this player's class
                filtered = [c for c in event.choices
                            if not c.class_only or c.class_only == self.player.player_class]
                idx = self.ui.show_story_event(_dc_replace(event, choices=filtered))
                choice = filtered[idx]
                self.player.story_flags[choice.flag] = True
                apply_effect(self.player, choice.effect)
                self.ui.pause()

            # Shop — stash floor number on player temporarily
            self.player._shop_floor = self.floor
            self.ui.pause(t("shop_hint"))
            run_shop(self.player, self.ui)

            self.ui.pause(t("descend"))
            self.floor += 1

    # ── Combat loop ────────────────────────────────────────────────────────────

    def _combat(self, enemy, modifier: dict) -> str:
        self.ui.clear_log()
        magic_mult = modifier.get("player_magic_mult", 1.0)
        revive_used = False
        combat_turn = 0
        last_ability = ""

        while self.player.is_alive() and enemy.is_alive():

            # ── Player turn ───────────────────────────────────────────────────
            for msg, _ in player_turn_start(self.player):
                self.ui.add_log(msg)

            if not self.player.is_alive():
                break

            if consume_stun(self.player):
                self.ui.add_log(f"[yellow]{t('player_stunned')}[/yellow]")
                self.ui.show_combat(self.player, enemy)
            else:
                self.ui.show_combat(self.player, enemy)
                choice = self.ui.show_combat_menu(self.player)

                spells    = list(SPELLS.get(self.player.player_class, {}).keys())
                num_spells = len(spells)
                item_num   = 2 + num_spells
                run_num    = item_num + 1
                c = int(choice)

                if c == 1:
                    dmg, crit = player_attack(self.player, enemy)
                    crit_txt  = f" [bold yellow]{t('critical_hit')}[/bold yellow]" if crit else ""
                    self.ui.add_log(f"[green]{t('player_attack', dmg=dmg)}{crit_txt}[/green]")

                elif 2 <= c <= 1 + num_spells:
                    spell_name = spells[c - 2]
                    dmg, name, fx = player_magic(self.player, enemy, spell_name, magic_mult)
                    if dmg == 0:
                        self.ui.add_log(f"[yellow]{fx}[/yellow]")
                    else:
                        self.ui.add_log(f"[blue]{t('player_cast', name=name, dmg=dmg)}{fx}[/blue]")

                elif c == item_num:
                    idx = self.ui.show_inventory(self.player)
                    if idx < 0:
                        continue
                    msg = self.player.use_item(idx)
                    self.ui.add_log(f"[green]{msg}[/green]")

                elif c == run_num:
                    if random.random() < 0.5:
                        self.ui.add_log(f"[yellow]{t('fled')}[/yellow]")
                        self.ui.show_combat(self.player, enemy)
                        self.ui.pause()
                        return "run"
                    else:
                        self.ui.add_log(f"[red]{t('escape_failed')}[/red]")

            # ── Enemy turn ────────────────────────────────────────────────────
            if not enemy.is_alive():
                break

            for msg, _ in enemy_turn_start(enemy):
                self.ui.add_log(msg)

            if not enemy.is_alive():
                break

            if consume_stun(enemy):
                self.ui.add_log(f"[yellow]{t('enemy_stunned', name=enemy.name)}[/yellow]")
                combat_turn += 1
            else:
                dmg, msg, ability = enemy_turn(enemy, self.player, combat_turn, last_ability)
                last_ability = ability
                combat_turn += 1
                if dmg > 0:
                    self.ui.add_log(f"[red]{msg}[/red]")
                elif dmg < 0:
                    self.ui.add_log(f"[italic dim]{msg}[/italic dim]")
                else:
                    self.ui.add_log(f"[dim]{msg}[/dim]")

            # ── Story modifier: ally damage ────────────────────────────────────
            ally_dmg = modifier.get("ally_dmg_per_turn", 0)
            if ally_dmg and enemy.is_alive():
                enemy.hp = max(0, enemy.hp - ally_dmg)
                self.ui.add_log(f"[magenta]{t('dark_spirits', name=enemy.name, dmg=ally_dmg)}[/magenta]")

            # ── Revive once (martyred saint) ──────────────────────────────────
            if not self.player.is_alive() and modifier.get("revive_once") and not revive_used:
                revive_used = True
                modifier.pop("revive_once")
                self.player.hp = self.player.max_hp // 2
                self.ui.add_log(f"[bold cyan]{t('revive')}[/bold cyan]")

        # Final display
        self.ui.show_combat(self.player, enemy)

        if not self.player.is_alive():
            return "dead"

        # Victory
        leveled = self.player.gain_xp(enemy.xp)
        self.player.gold += enemy.gold
        self.ui.print(f"[bold green]{t('enemy_defeated', name=enemy.name)}[/bold green]  "
                      f"[yellow]{t('xp_gold', xp=enemy.xp, gold=enemy.gold)}[/yellow]")
        if leveled:
            self.ui.print(f"[bold yellow]{t('level_up', level=self.player.level)}[/bold yellow]")

        # Random drop
        if random.random() < 0.35:
            drop = random.choice(["health_potion", "mana_potion"])
            self.player.inventory.append(ITEMS[drop])
            self.ui.print(f"[green]{t('item_drop', name=ITEMS[drop].name)}[/green]")

        self.ui.pause()
        return "win"

    # ── Prisoner return bonus ──────────────────────────────────────────────────

    def _prisoner_return_bonus(self):
        self.ui.print(f"\n[italic dim]{t('prisoner_returns')}[/italic dim]")
        self.player.gold += 10
        self.player.apply_bonus(max_hp=5)
        self.player.inventory.append(ITEMS["elixir_dragon"])
        self.ui.print(f"[bold cyan]{t('prisoner_gift')}[/bold cyan]")
        self.ui.pause()

    # ── Rest events ────────────────────────────────────────────────────────────

    def _rest_event(self):
        events = [
            ("rest_hp",     "hp"),
            ("rest_gold",   "gold"),
            ("rest_mp",     "mp"),
            ("rest_potion", "item"),
            ("rest_none",   "none"),
        ]
        key, kind = random.choice(events)
        self.ui.print(f"\n[italic dim]{t(key)}[/italic dim]")

        if kind == "hp":
            heal = int(self.player.max_hp * 0.2)
            self.player.heal(heal)
            self.ui.print(f"[green]{t('gained_hp', n=heal)}[/green]")
        elif kind == "gold":
            g = random.randint(5, 20)
            self.player.gold += g
            self.ui.print(f"[yellow]{t('gained_gold', n=g)}[/yellow]")
        elif kind == "mp":
            restore = int(self.player.max_mp * 0.3)
            self.player.restore_mp(restore)
            self.ui.print(f"[blue]{t('gained_mp', n=restore)}[/blue]")
        elif kind == "item":
            self.player.inventory.append(ITEMS["health_potion"])
            self.ui.print(f"[green]{t('found_potion', name=ITEMS['health_potion'].name)}[/green]")
