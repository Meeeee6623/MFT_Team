import pandas as pd
from math import fabs


class Trader:
    def __init__(self, n_stocks=4):
        # Add any additional info you want
        self.last_stock3 = 0.0

    def MakeTrades(self, time, stock_prices):
        """
        Grader will call this once per timestep to determine your buys/sells.
        Args:
            time: int
            stock_prices: dict[string -> float]
        Returns:
            trades: dict[string -> float] of your trades (quantity) for this timestep.
                Positive is buy/long and negative is sell/short.
        """
        trades = {}
        return trades


class Stock4Trader(Trader):
    """
    Lighter version of trader that only trades on stock4 from stock3 info, doesn't use database
    Only records stock3 data back one timestep to determine sign of purchase
    """

    def MakeTrades(self, time, stock_prices):
        trades = {}

        if time > 1:
            # buy stock4 based on sign of stock3 returns
            if stock_prices["Stock3"] - self.last_stock3 > 0:
                trades["Stock4"] = 600000 // stock_prices["Stock4"]
            else:
                trades["Stock4"] = -600000 // stock_prices["Stock4"]
            print(f"Buying Stock4 at time {time} with {trades['Stock4']} shares")
            self.last_stock3 = stock_prices["Stock3"]

        return trades

# %%
