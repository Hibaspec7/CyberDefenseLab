import random
import time

import database as db
from score_manager import ScoreManager
import questions as Q


class GameController:
    ATTACKS_PER_SESSION = 4
    ATTACK_TYPES = ["phishing", "bruteforce", "ddos", "sqli"
                    
   def __init__(self, user_id, difficulty="beginner"):
    self.user_id = user_id
    self.difficulty = difficulty
    self.score_mgr = ScoreManager(difficulty)

    self.attack_queue = []
    self.current_index = 0
    self.round_start_time = None
    self.hint_used_this_round = False
    self.session_active = False
    self._used_ids = []
    def start_session(self):
    self._used_ids = []
    selected = []

    types = self.ATTACK_TYPES[:]
    random.shuffle(types)

    for atype in types:
        q = Q.get_question(atype, self.difficulty, exclude_ids=self._used_ids)
        if q:
            q["attack_type"] = atype
            selected.append(q)
            self._used_ids.append(q["id"])

    self.attack_queue = selected[:self.ATTACKS_PER_SESSION]
    self.current_index = 0
    self.score_mgr.reset()
    self.session_active = True
    def session_complete(self):
    return self.current_index >= len(self.attack_queue)
    
    def get_current_attack(self):
    if self.session_complete():
        return None
    return self.attack_queue[self.current_index]
    def start_round_timer(self):
    self.round_start_time = time.time()
    self.hint_used_this_round = False
    
    def elapsed_time(self):
    if self.round_start_time is None:
        return 0
    return time.time() - self.round_start_time
    def use_hint(self):
    granted = self.score_mgr.use_hint()
    if granted:
        self.hint_used_this_round = True
    return granted
    def _validate(self, atk, answer):
    atype = atk["attack_type"]

    if atype == "phishing":
        return str(answer) == "malicious_link"

    elif atype == "bruteforce":
        return str(answer) == atk.get("attacker_ip", "")

    elif atype == "ddos":
        expected = {
            ip: ("block" if flood else "allow")
            for ip, _, flood in atk.get("traffic", [])
        }

        if not isinstance(answer, dict):
            return False
            
        return all(answer.get(ip) == action for ip, action in expected.items())

    elif atype == "sqli":
        return str(answer) == "parameterized_queries"

    return False
    def submit_answer(self, answer):
    atk = self.get_current_attack()
    if atk is None:
        return {"correct": False, "points": 0, "message": "No active round"}

    elapsed = self.elapsed_time()
    correct = self._validate(atk, answer)

    points = self.score_mgr.apply_round(
        atk["attack_type"],
        correct,
        elapsed,
        self.hint_used_this_round
    )

    result = "pass" if correct else "fail"

    db.save_session(self.user_id, atk["attack_type"], result,
                    points, round(elapsed, 1), self.difficulty)

    db.add_log(self.user_id, atk["attack_type"], str(answer)[:120], result)
    db.update_user_score(self.user_id, points)

    self.current_index += 1

    msg = "[OK] SUCCESS" if correct else "[FAIL] WRONG"
    return {"correct": correct, "points": points, "message": msg}
    
    
