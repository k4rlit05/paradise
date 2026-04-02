class BrokerConnector:

    def __init__(self):
        self.mode = "NO_API"

    def detect_broker(self):
        print("Broker detected: NO API mode")

    def send_order(self, symbol, direction, volume):
        if self.mode == "API":
            return self.send_order_api(symbol, direction, volume)
        else:
            return self.send_order_no_api(symbol, direction, volume)

    def send_order_api(self, symbol, direction, volume):
        print(f"[API] Sending {direction} order for {symbol} ({volume})")
        return True

    def send_order_no_api(self, symbol, direction, volume):
        print(f"[NO API] Simulating {direction} order for {symbol} ({volume})")
        return True