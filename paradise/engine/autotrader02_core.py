# ===============================
# AUTOTRADER CORE - VERSION 6
# UNIVERSAL BROKER MODE
# ===============================

import time
import random
from broker_connector import BrokerConnector
from ai_engine import AIEngine
print("AutoTrader Core (Universal Broker Mode) is running...\n")

broker = BrokerConnector()
broker.detect_broker()
ai = AIEngine()

symbols = ["EURUSD", "GBPUSD", "USDJPY"]

prices = {
    "EURUSD": 1.1000,
    "GBPUSD": 1.2700,
    "USDJPY": 149.50
}

def strategy(symbol, price):
    if price > 1.0950:
        return "BUY"
    return "WAIT"

def human_delay():
    delay = random.uniform(1.2, 3.8)
    print(f"⏳ Human-like delay: {delay:.2f}s")
    time.sleep(delay)

def run_engine():
    cycle = 0

    while True:
        cycle += 1
        print(f"\n===== NEW CYCLE {cycle} =====")

        for symbol in symbols:
            price = prices[symbol]
            decision = strategy(symbol, price)

            print(f"{symbol} | Price: {price} | Decision: {decision}")

            if decision == "BUY":
                broker.send_order(symbol, "BUY", 0.01)

            human_delay()

        print("Cycle complete. Waiting...\n")
        time.sleep(2)

run_engine()