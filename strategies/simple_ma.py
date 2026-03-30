from .base_strategy import BaseStrategy

class SimpleMAStrategy(BaseStrategy):
    def generate_signal(self, price):
        print(f"Price received: {price}")
        return "BUY" if price > 50 else "SELL"