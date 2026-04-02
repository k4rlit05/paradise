# director.py

class Director:
    def __init__(self, manager):
        self.strategy = "normal"
        self.risk_level = 1.0
        self.manager = manager

    def adjust_risk(self, reason):
        print("[DIRECTOR] Re-evaluating strategy and risk...")

        # Reduce risk
        self.risk_level -= 0.1
        print(f"[DIRECTOR] Reducing risk. New risk level: {self.risk_level}")

        # Send instruction to Manager
        self.manager.receive_instruction(f"Risk adjusted due to: {reason}")

        print("[DIRECTOR] Adjustment complete.")