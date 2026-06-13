"""
score_manager.py - Scoring rules and session score tracking
Cyber-Attack Simulator & Defense Lab
"""

DIFFICULTY_SETTINGS = {
    "beginner": {
        "time": 30,
        "hint_cost": 10,
        "wrong_penalty": 10,
        "fast_threshold": 15,
        "hints_allowed": 3
    },
    "intermediate": {
        "time": 20,
        "hint_cost": 20,
        "wrong_penalty": 25,
        "fast_threshold": 10,
        "hints_allowed": 3
    },
    "expert": {
        "time": 12,
        "hint_cost": 40,
        "wrong_penalty": 50,
        "fast_threshold": 6,
        "hints_allowed": 0
    },
    "daily": {
        "time": 20,
        "hint_cost": 20,
        "wrong_penalty": 25,
        "fast_threshold": 10,
        "hints_allowed": 2
    }
}

COMBO_MULTIPLIERS = {
    0: 1.0,
    1: 1.0,
    2: 1.2,
    3: 1.5,
    4: 1.8,
    5: 2.0,
}


class ScoreManager:
    def __init__(self, difficulty="beginner"):
        self.difficulty = difficulty
        self.settings = DIFFICULTY_SETTINGS[difficulty]

        self.session_score = 0
        self.hints_remaining = self.settings["hints_allowed"]
        self.hint_used_any = False
        self.current_streak = 0
        self.rounds_played = 0
        self.rounds_passed = 0
        self.round_log = []

    def calc_round_score(self, correct, time_taken, hint_used):
        """Return points earned (or lost) for one round."""
        if not correct:
            return -self.settings["wrong_penalty"]

        pts = 100 if time_taken <= self.settings["fast_threshold"] else 50
        if hint_used:
            pts = max(0, pts - self.settings["hint_cost"])
        return pts

    def apply_round(self, attack_type, correct, time_taken, hint_used, breach=False):
        """Apply round result and update session stats."""
        if breach:
            pts = 0
            result = "breach"
            self.current_streak = 0
        else:
            pts = self.calc_round_score(correct, time_taken, hint_used)
            next_streak = self.current_streak + 1 if correct else 0
            self.current_streak = next_streak
            combo = COMBO_MULTIPLIERS.get(min(self.current_streak, 5), 2.0)
            pts = round(pts * combo) if correct else pts
            result = "pass" if correct else "fail"

        self.session_score = max(0, self.session_score + pts)
        self.rounds_played += 1

        if result == "pass":
            self.rounds_passed += 1

        self.round_log.append({
            "attack_type": attack_type,
            "result": result,
            "score": pts,
            "time_taken": round(time_taken, 1),
            "streak": self.current_streak,
        })

        return pts

    def use_hint(self):
        """Deduct hint cost. Returns True if hint is granted."""
        if self.hints_remaining > 0 and self.difficulty != "expert":
            self.hints_remaining -= 1
            self.hint_used_any = True
            return True
        return False

    def get_win_rate(self):
        """Return win percentage."""
        if self.rounds_played == 0:
            return 0
        return round((self.rounds_passed / self.rounds_played) * 100)

    def reset(self):
        """Reset session data."""
        self.session_score = 0
        self.hints_remaining = self.settings["hints_allowed"]
        self.hint_used_any = False
        self.current_streak = 0
        self.rounds_played = 0
        self.rounds_passed = 0
        self.round_log = []
