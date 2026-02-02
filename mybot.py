import random
import json
import math

class ImperialSeekerBot:
    """
    The ImperialSeekerBot controls units in the 'Trials of Ascension' environment.
    It prioritizes resource expansion but must react to 'Divine Intervention' (User Inputs).
    """

    def __init__(self, name="Vader_v1"):
        self.name = name
        self.status = "AWAITING_ORDERS"
        self.units = []
        self.enemy_units = []
        self.resources = 0

    def perceive_state(self, game_state_json):
        """
        Parses the JSON state from the GDevelop engine.
        """
        data = json.loads(game_state_json)
        self.units = data.get("my_units", [])
        self.enemy_units = data.get("enemies", [])
        self.resources = data.get("flux_count", 0)
        
        # Check for the 'Force Choke' status effect
        for unit in self.units:
            if unit.get("status") == "CHOKED":
                self.emergency_protocol(unit)

    def emergency_protocol(self, unit):
        """
        Triggered when the Human Player activates the Force Choke.
        Logic: Abandon the choked unit, reroute others to avoid the area.
        """
        print(f"⚠️ ALERT: Unit {unit['id']} is being crushed by the Force.")
        # Logic to mark this coordinate as a 'Danger Zone' for other units
        self.mark_danger_zone(unit['x'], unit['y'])

    def mark_danger_zone(self, x, y):
        # Placeholder for pathfinding weight adjustment
        print(f"Avoidance vector set for sector {x},{y}")

    def calculate_move(self):
        """
        Decides the next action based on current state.
        """
        if self.resources > 50:
            return self.expand_territory()
        else:
            return self.gather_resources()

    def expand_territory(self):
        return {"action": "SPAWN_UNIT", "type": "TIE_FIGHTER"}

    def gather_resources(self):
        return {"action": "MOVE_TO_NODE", "target": "nearest_planet"}

    def run_cycle(self, mock_state=None):
        if mock_state:
            self.perceive_state(mock_state)
            decision = self.calculate_move()
            return decision

# --- SIMULATION TEST ---
if __name__ == "__main__":
    # Mock data to simulate the GDevelop engine sending a state
    mock_game_state = json.dumps({
        "my_units": [{"id": 101, "x": 10, "y": 20, "status": "ACTIVE"}, 
                     {"id": 102, "x": 15, "y": 25, "status": "CHOKED"}],
        "enemies": [],
        "flux_count": 60
    })

    bot = ImperialSeekerBot()
    print(f"Initializing {bot.name}...")
    
    # Run a test cycle
    decision = bot.run_cycle(mock_game_state)
    print(f"Decision: {decision}")
