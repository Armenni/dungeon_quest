"""
File-bridge between Claude and the API.
- Watches pending_action.txt for new content written by Claude
- Submits it to the API
- Writes the full response to game_state.json

Run:  python watcher.py
"""
import requests, json, time, os, hashlib, re

ACTION_FILE = "pending_action.txt"
STATE_FILE  = "game_state.json"
BASE        = "http://127.0.0.1:5000"

last_hash = ""

def write_state(data: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def submit(action: str) -> dict:
    action = action.strip()
    if action.startswith("new_game:"):
        # format: new_game:Name:Class
        parts = action.split(":", 2)
        name  = parts[1] if len(parts) > 1 else "Hero"
        cls   = parts[2] if len(parts) > 2 else "Warrior"
        r = requests.post(f"{BASE}/new_game", json={"name": name, "class": cls}, timeout=10)
    else:
        r = requests.post(f"{BASE}/action", json={"input": action}, timeout=10)
    return r.json()

print("Watcher running — waiting for Claude's moves in pending_action.txt")
print("Claude reads results from game_state.json")
print("─" * 50)

while True:
    try:
        if os.path.exists(ACTION_FILE):
            content = open(ACTION_FILE).read().strip()
            h = hashlib.md5(content.encode()).hexdigest()
            if content and h != last_hash:
                last_hash = h
                # Strip turn marker suffix e.g. "2:t3" -> "2"
                clean = re.sub(r':t\d+$', '', content.strip())
                print(f"\n[→] Claude wrote: {content!r}  (sending: {clean!r})")
                data = submit(clean)
                write_state(data)
                state = data.get("state", "?")
                msgs  = data.get("messages", [])
                clog  = data.get("combat_log", [])
                print(f"[←] State: {state}")
                for m in msgs: print(f"    {m}")
                for m in clog: print(f"    » {m}")
                if data.get("options"):
                    print("    Options:")
                    for o in data["options"]: print(f"      {o}")
    except Exception as e:
        print(f"[!] {e}")
    time.sleep(0.4)
