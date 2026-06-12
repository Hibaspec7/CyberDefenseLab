import random
import time

import database as db
from score_manager import ScoreManager
import questions as Q


class GameController:
    ATTACKS_PER_SESSION = 4
    ATTACK_TYPES = ["phishing", "bruteforce", "ddos", "sqli"]
