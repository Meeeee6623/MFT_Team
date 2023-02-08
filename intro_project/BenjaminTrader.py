import pandas as pd
from math import fabs


class Trader:
    def __init__(self, n_stocks=4):
        # Add any additional info you want
        self.prices = pd.DataFrame({f"Stock{s}": [] for s in range(1, n_stocks + 1)})
        # Add returns columns
        self.prices = self.prices.append({f"Stock{s}_Returns": [] for s in range(1, n_stocks + 1)}, ignore_index=True)
        # Add timestep column
        self.prices = self.prices.append({"Time": []}, ignore_index=True)

        self.not_4 = 0
        self.n_stocks = n_stocks
        # would read stock line data from txt files, but small enough to hardcode...
        self.regression_info = {
            "Stock1_slope": 5.497074833211426093e-01,
            "Stock1_intercept": -3.523151382211264023e-04,
            "Stock2_slope": 8.864750887889283337e-01,
            "Stock2_intercept": 5.846269499677095131e-04,
            "Stock4_slope": 6.496858238837070587e+01,
            "Stock4_intercept": 3.281726902349381414e-03
        }

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


class RegressionTrader(Trader):
    """
    More complicated trader that uses regression lines to predict returns
    Database is leftover and mostly used for debugging, can be replaced with a single variable for each stock
    """
    def decide_purchase(self) -> (str, int):
        # get max return from regression line for each stock
        max_return = 0.0
        to_buy = ""
        # precdict stock1, stock2 returns with stock1 returns
        for i in range(1, 3):
            stock_return = self.regression_info[f"Stock{i}_slope"] * self.prices[f"Stock1_Returns"].iloc[-1] + \
                           self.regression_info[f"Stock{i}_intercept"]
            if fabs(stock_return) > fabs(max_return):
                max_return = stock_return
                to_buy = f"Stock{i}"
        # predict stock4 returns with stock3 returns
        stock_return = self.regression_info[f"Stock4_slope"] * self.prices[f"Stock3_Returns"].iloc[-1] + \
                       self.regression_info[f"Stock4_intercept"]
        if fabs(stock_return) > fabs(max_return):
            max_return = stock_return
            to_buy = f"Stock4"
        print(f"Predicted {to_buy} return: {max_return}")
        return to_buy, 1 if max_return > 0 else -1

    # given that stock3 returns closely resemble stock4 returns, trade stock4 on stock3 info
    def MakeTrades(self, time, stock_prices):
        # update data
        stock_prices["Time"] = time
        self.prices = self.prices.append(stock_prices, ignore_index=True)
        # update returns columns by pct change of normal prices
        # was getting errors with adding only new data, so just recalculate everything
        for i in range(1, self.n_stocks + 1):
            self.prices[f"Stock{i}_Returns"] = self.prices[f"Stock{i}"].pct_change()

        trades = {}
        if time > 1:
            # buy based on regression lines
            to_buy, buy_or_sell = self.decide_purchase()
            trades[to_buy] = buy_or_sell * 600000 // self.prices[to_buy].iloc[-1] + 1
            print(f"Buying {to_buy} at time {time} with {trades[to_buy]} shares")
            if to_buy != "Stock4":
                self.not_4 += 1

        return trades
# %%
