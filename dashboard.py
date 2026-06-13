"""
dashboard.py - Window 3: Dashboard  v3
Stats, leaderboard, history, achievements, bar chart, weakness report.
"""
import tkinter as tk
import database as db
import theme as T
import datetime


class DashboardWindow(tk.Frame):
    def __init__(self, master, user, session_summary, on_play_again, on_logout):
        super().__init__(master, bg=T.BG_DARK)
        self.user     = db.get_user_by_id(user["id"]) or user
        self.summary  = session_summary
        self.on_play_again = on_play_again
        self.on_logout     = on_logout
        self._build()

    def _build(self):
        self.pack(fill="both", expand=True)

        # ── Top bar ──────────────────────────────────────────────────────────
        top = tk.Frame(self, bg=T.BG_PANEL,
                       highlightthickness=1, highlightbackground=T.BORDER_PANEL)
        top.pack(fill="x", padx=12, pady=(12,0))
        tk.Label(top, text="[=] SOC DASHBOARD",
                 bg=T.BG_PANEL, fg=T.CYAN,
                 font=("Courier New",12,"bold")).pack(side="left",padx=12,pady=8)
        for txt,cmd,col in [("LOGOUT",self.on_logout,T.MUTED),
                             ("PLAY AGAIN",self.on_play_again,T.GREEN)]:
            tk.Button(top, text=f"[ {txt} ]", command=cmd,
                      bg=T.BG_PANEL, fg=col,
                      activebackground=T.BG_HOVER, activeforeground=col,
                      relief="flat", bd=0, cursor="hand2",
                      font=("Courier New",9,"bold"),
                      highlightthickness=0, padx=10).pack(side="right",padx=4)

        # ── Tab bar ──────────────────────────────────────────────────────────
        tab_row = tk.Frame(self, bg=T.BG_DARK)
        tab_row.pack(fill="x", padx=12, pady=(8,0))
        self.tab_btns   = {}
        self.tab_frames = {}
        for tid, label in [("stats","STATS"),("leaderboard","LEADERBOARD"),
                           ("history","LOG"),("achievements","BADGES")]:
            btn = tk.Button(tab_row, text=label,
                            command=lambda t=tid: self._switch_tab(t),
                            bg=T.BG_DARK, fg=T.MUTED,
                            activebackground=T.BG_HOVER, activeforeground=T.CYAN,
                            relief="flat", bd=0, cursor="hand2",
                            font=("Courier New",10,"bold"),
                            padx=14, pady=5,
                            highlightthickness=1, highlightbackground=T.BORDER_PANEL)
            btn.pack(side="left", padx=(0,6))
            self.tab_btns[tid] = btn

        # ── Content area ─────────────────────────────────────────────────────
        self.content = tk.Frame(self, bg=T.BG_DARK)
        self.content.pack(fill="both", expand=True, padx=12, pady=6)

        for tid in ("stats","leaderboard","history","achievements"):
            f = tk.Frame(self.content, bg=T.BG_DARK)
            self.tab_frames[tid] = f

        # Placeholders for tab builders (will fill in next commits)
        self._build_stats(self.tab_frames["stats"])
        self._build_leaderboard(self.tab_frames["leaderboard"])
        self._build_history(self.tab_frames["history"])
        self._build_achievements(self.tab_frames["achievements"])

        self._switch_tab("stats")

    def _switch_tab(self, tid):
        for t, btn in self.tab_btns.items():
            active = (t == tid)
            btn.config(fg=T.CYAN if active else T.MUTED,
                       highlightbackground=T.CYAN if active else T.BORDER_PANEL)
        for t, frame in self.tab_frames.items():
            if t == tid: frame.pack(fill="both", expand=True)
            else:        frame.pack_forget()
