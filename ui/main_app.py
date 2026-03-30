from kivy.app import App
from kivy.lang import Builder


class ParadiseApp(App):
    def build(self):
        return Builder.load_file("ui/app.kv")

    def start_engine(self):
        from core.engine import TradingEngine
        from core.order_manager import OrderManager
        from core.risk_manager import RiskManager
        from strategies.simple_ma import SimpleMAStrategy
        from services.data_feed import DataFeed

        engine = TradingEngine(
            strategy=SimpleMAStrategy(),
            data_feed=DataFeed(),
            order_manager=OrderManager(),
            risk_manager=RiskManager()
        )
        engine.run()