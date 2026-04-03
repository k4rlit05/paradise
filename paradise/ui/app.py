from kivy.app import App
from ui.trading_ui import TradingUI

class TradingApp(App):
    def build(self):
        return TradingUI()
