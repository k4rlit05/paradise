
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from engine.ai_president import AIPresident
from engine.director import Director
from engine.manager import Manager
from engine.trader import Trader

class TradingUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        trader = Trader()
        manager = Manager(trader)
        director = Director(manager)
        self.president = AIPresident(director)

        self.status = Label(text="AI Trading System Ready", font_size=20)
        self.add_widget(self.status)

        btn1 = Button(text="High Drawdown")
        btn1.bind(on_press=lambda x: self.trigger("High drawdown"))
        self.add_widget(btn1)

        btn2 = Button(text="Low Win Rate")
        btn2.bind(on_press=lambda x: self.trigger("Low win rate"))
        self.add_widget(btn2)

        btn3 = Button(text="Manual Adjust")
        btn3.bind(on_press=lambda x: self.trigger("User command: Adjust now"))
        self.add_widget(btn3)

    def trigger(self, issue):
        self.status.text = f"Triggered: {issue}"
