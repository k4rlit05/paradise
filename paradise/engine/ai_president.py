# ai_president.py

class AIPresident:
    def __init__(self, director):
        self.director = director

    def detect_issue(self, issue):
        print(f"[AI PRESIDENT] Issue detected: {issue}")
        print("[AI PRESIDENT] Triggering Director adjustment...")
        self.director.adjust_risk(issue)