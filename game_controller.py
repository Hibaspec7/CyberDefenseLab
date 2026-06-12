


Class GameController:
    ATTACKS_PER_SESSION = 4
    ATTACK_TYPES = [“phishing”, “bruteforce”, “ddos”, “sqli”]

    Def __init__(self, user_id, difficulty=”beginner”):
        Self.user_id   = user_id
        Self.difficulty = difficulty
        Self.score_mgr = ScoreManager(difficulty)
        Self.attack_queue     = []   # list of question dicts
        Self.current_index    = 0
        Self.round_start_time = None
        Self.hint_used_this_round = False
        Self.session_active   = False
        Self._used_ids        = []   # track used question Ids this session


