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
