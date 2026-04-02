# manager.py

class Manager:
    def __init__(self, trader=None):
        self.task_queue = []
        self.trader = trader

    def receive_instruction(self, instruction):
        print(f"[MANAGER] Received instruction: {instruction}")
        self.task_queue.append(instruction)
        self.process_tasks()

    def process_tasks(self):
        print("[MANAGER] Processing tasks...")
        while self.task_queue:
            task = self.task_queue.pop(0)
            print(f"[MANAGER] Executing task: {task}")

            # Send action to Trader
            if self.trader:
                self.trader.execute(f"Action from Manager: {task}")

        print("[MANAGER] All tasks completed.")