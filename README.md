# 🛡️ Cyber-Attack Simulator & Defense Lab

> A gamified cybersecurity education platform where you play as a Security Officer defending against real-world cyber attacks — built with Python & Tkinter.

---

## 📖 Project Description

**Cyber-Attack Simulator & Defense Lab** is a Python Tkinter desktop application developed as an OSSD Final Term Project (CLO 4). Users take on the role of a Security Officer and must identify and stop incoming cyber attacks within a time limit to earn points. The game teaches real cybersecurity concepts through interactive, hands-on defense challenges.

---

## ✨ Features

### 🖥️ Window 1 — Attack Lab
- Live scrolling terminal-style attack logs
- 30/20/12 second countdown timer (per difficulty)
- 4 attack types: Phishing, Brute Force, DDoS, SQL Injection
- Animated log feed with color-coded severity

### 🔐 Window 2 — Defense Terminal
| Attack | Widget | Your Action |
|--------|--------|-------------|
| Phishing | Clickable email elements | Click the malicious link |
| Brute Force | Entry + Button | Type attacker IP and block |
| DDoS | Allow/Block buttons | Classify each traffic source |
| SQL Injection | Radio buttons | Choose correct parameterized fix |

### 📊 Window 3 — Dashboard
- Personal stats: score, win rate, sessions, breaches
- Bar chart of score per attack type (Canvas-drawn)
- Leaderboard — Top 10 players (Treeview-style)
- Full attack history with results and scores
- Weakness detection: shows which attack type you fail most
- Achievements system with unlockable badges

### 🏆 Scoring System
| Action | Points |
|--------|--------|
| Correct + Fast | +100 pts |
| Correct + Slow | +50 pts |
| Wrong Answer | -10 / -25 / -50 pts (by difficulty) |
| Hint Used | -10 / -20 / -40 pts |
| Time Runs Out | 0 pts + BREACH recorded |

---

## 🛠️ Tools & Technologies
| Technology | Purpose |
|------------|---------|
| Python 3.x | Core language |
| Tkinter | All GUI windows |
| SQLite3 | Local database (built-in) |
| hashlib | Password hashing (SHA-256 + salt) |
| Git + GitHub | Version control & collaboration |

---

## ⚙️ Setup & Installation

### Requirements
- Python 3.7 or higher
- Tkinter (usually bundled with Python)

### Clone the Repository
```bash
git clone https://github.com/Hibaspec7/CyberDefenseLab.git
cd CyberDefenseLab
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the App

**Windows:**
```bash
python main.py
```

**Linux/macOS:**
```bash
sudo apt-get install python3-tk
brew install python-tk
python3 main.py
```

---

## 📁 Project Structure
cyber_simulator/

├── main.py               ← App entry point (run this)

├── login_screen.py       ← Login + Register UI

├── home_screen.py        ← Difficulty selection

├── auth.py               ← Login/register logic + hashing

├── theme.py              ← Colors, fonts, style helpers

├── attack_lab.py         ← Window 1: Attack Lab

├── questions.py          ← Attack questions and answer data

├── defense_screen.py     ← Window 2: Defense Terminal

├── dashboard.py          ← Window 3: Dashboard

├── achievements.py       ← Achievement tracking and rewards

├── database.py           ← SQLite setup + all queries

├── game_controller.py    ← Round flow, answer validation

├── score_manager.py      ← Scoring rules per difficulty

├── requirements.txt

├── README.md

└── cyber_simulator.db    ← Auto-created on first run

---

## 🗄️ Database & Backend

### Schema
```sql
users         (id, username, password_hash, total_score, level, sessions_played)
attacks       (id, attack_type, description, correct_answer, hint, difficulty, log_lines)
game_sessions (id, user_id, attack_type, result, score, time_taken, difficulty)
logs          (id, user_id, timestamp, attack_type, action_taken, outcome)
```

### Game Flow
1. User logs in → selects difficulty
2. `game_controller.py` picks random attack
3. `attack_lab.py` displays attack logs
4. User responds in `defense_screen.py`
5. `score_manager.py` calculates points
6. Result saved to database
7. `dashboard.py` renders stats + leaderboard

---

## 👥 Team Contributions
| Member | Role | Files |
|--------|------|-------|
| **Hiba** | Leader — Core & Auth | `main.py`, `auth.py`, `theme.py`, `requirements.txt`, `README.md` |
| **Owais** | Login + Database | `login_screen.py`, `database.py` |
| **Huraira** | Home + Defense Terminal | `home_screen.py`, `defense_screen.py` |
| **Laiba** | Attack Lab | `attack_lab.py`, `questions.py` |
| **Ibrahim** | Dashboard + Achievements | `dashboard.py`, `achievements.py` |
| **Sehar** | Game Logic + Scoring | `game_controller.py`, `score_manager.py` |

---

## 🔀 GitHub Workflow
| Branch | Purpose |
|--------|---------|
| `main` | Final submission only |
| `dev` | Merge all features here first |
| `feature/login` | Login + Register screens |
| `feature/attack-lab` | Window 1 |
| `feature/defense` | Window 2 |
| `feature/dashboard` | Window 3 |
| `feature/database` | SQLite models |
| `feature/game-logic` | Game controller + scoring |

---

## 🔗 Major Pull Requests
| PR | Description | Author |
|----|-------------|--------|
| [PR #__]() | Feature: Login Screen | Owais |
| [PR #__]() | Feature: Attack Lab | Laiba |
| [PR #__]() | Feature: Defense Terminal | Huraira |
| [PR #__]() | Feature: Dashboard | Ibrahim |
| [PR #__]() | Feature: Database Setup | Owais |
| [PR #__]() | Feature: Game Logic | Sehar |

---

## 📸 Screenshots
