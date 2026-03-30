class TradingEngine:
  def __init__(self, strategy, data_feed, order_manager, risk_manager):
      self.strategy = strategy
      self.data_feed = data_feed
      self.order_manager = order_manager
      self.risk_manager = risk_manager

  def run(self):
      print("Engine running...")

      price = self.data_feed.get_price()
      signal = self.strategy.generate_signal(price)

      if self.risk_manager.approve(signal):
          self.order_manager.execute(signal)