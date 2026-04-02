# main.py

from ai_president import AIPresident
from director import Director
from manager import Manager
from trader import Trader

# Create the Trader (bottom layer)
trader = Trader()

# Create the Manager and connect it to the Trader
manager = Manager(trader)

# Create the Director and connect it to the Manager
director = Director(manager)

# Create the President and connect it to the Director
president = AIPresident(director)

# Trigger the full chain
president.detect_issue("High drawdown")
president.detect_issue("Low win rate")
president.detect_issue("User command: Adjust now")