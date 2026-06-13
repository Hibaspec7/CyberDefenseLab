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
