# ===============================
# AUTOTRADER CORE - VERSION 2
# MULTI-PAIR SYSTEM
# ===============================

print("AutoTrader Core is running...\n")

# List of symbols
symbols = ["EURUSD", "GBPUSD", "USDJPY"]

# Example prices (later these will come from real data)
prices = [1.1000, 1.2700, 149.50]

# Strategy loop
for i in range(len(symbols)):

    symbol = symbols[i]
    price = prices[i]

    print("Symbol:", symbol)
    print("Price:", price)

    if price > 1.0950:
        decision = "BUY"
    else:
        decision = "WAIT"

    print("Decision:", decision)
    print("-------------------")