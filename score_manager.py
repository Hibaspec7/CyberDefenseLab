
DIFFICULTY_SETTINGS = {
    "beginner":     {"time": 30, "hint_cost": 10, "wrong_penalty": 10, "fast_threshold": 15, "hints_allowed": 3},
    "intermediate": {"time": 20, "hint_cost": 20, "wrong_penalty": 25, "fast_threshold": 10, "hints_allowed": 3},
    "expert":       {"time": 12, "hint_cost": 40, "wrong_penalty": 50, "fast_threshold": 6,  "hints_allowed": 0},
}


class ScoreManager:
    def __init__(self, difficulty="beginner"):
        self.difficulty = difficulty
        self.settings = DIFFICULTY_SETTINGS[difficulty]
        self.session_score = 0
        self.hints_remaining = self.settings["hints_allowed"]
        self.rounds_played = 0
        self.rounds_passed = 0
        self.round_log = []
def calc_round_score(self, correct, time_taken, hint_used):
    if not correct:
        return -self.settings["wrong_penalty"]

    if time_taken <= self.settings["fast_threshold"]:
        pts = 100
    else:
        pts = 50

    if hint_used:
        pts = max(0, pts - self.settings["hint_cost"])

    return pts
