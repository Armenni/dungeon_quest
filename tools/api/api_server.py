"""
Dungeon Quest API

Stateless REST API for the game.

Run:
    python tools/api/api_server.py

Port: 5000

Endpoints:
    POST /new_game   {"name": "Aric", "class": "Mage"}
    POST /action     {"input": "1"}
    GET  /state
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from flask import Flask, request, jsonify
from game.engine import GameEngine

app = Flask(__name__)
engine = GameEngine()


@app.route("/new_game", methods=["POST"])
def new_game():
    data = request.get_json(force=True) or {}
    name = data.get("name", "Hero")
    cls = data.get("class", "Warrior")
    return jsonify(engine.new_game(name, cls))


@app.route("/action", methods=["POST"])
def action():
    data = request.get_json(force=True) or {}
    value = str(data.get("input", ""))
    if not value:
        return jsonify({"error": 'Provide {"input": "..."}'}), 400
    return jsonify(engine.action(value))


@app.route("/state", methods=["GET"])
def state():
    if engine.player is None:
        return jsonify({"error": "No game in progress. POST /new_game first."})
    return jsonify(engine._response())


if __name__ == "__main__":
    print("Dungeon Quest API — http://localhost:5000")
    print('  POST /new_game  {"name": "Aric", "class": "Mage"}')
    print('  POST /action    {"input": "1"}')
    print("  GET  /state")
    app.run(debug=False, port=5000)
