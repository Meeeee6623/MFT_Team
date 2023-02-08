import pandas as pd


class Trader:
    def __init__(self, n_stocks=4):
        # Add any additional info you want
        self.prices = pd.DataFrame({f"Stock{s}": [] for s in range(1, n_stocks + 1)})
        # Add returns columns
        self.prices = self.prices.append({f"Stock{s}_Returns": [] for s in range(1, n_stocks + 1)}, ignore_index=True)
        # Add timestep column
        self.prices = self.prices.append({"Time": []}, ignore_index=True)

        self.t_wrong = 0
        self.o_wrong = 0
        self.n_stocks = n_stocks

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


class BullishTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        return {"Stock1": 1000000, "Stock2": 1000000, "Stock3": 1000000, "Stock4": 1000000}


class BearishTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        return {"Stock1": -1000000, "Stock2": -1000000, "Stock3": -1000000, "Stock4": -1000000}


class SampleTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        trades = {}
        # TODO: PICK HOW TO MAKE TRADES.
        trades['Stock1'] = 1000
        if 'Stock2' in stock_prices:
            if stock_prices['Stock2'] > 123:
                trades['Stock2'] = 1000
            else:
                trades['Stock2'] = -1000
        return trades


class MyTrader(Trader):

    # given that stock3 returns closely resemble stock4 returns, trade stock4 on stock3 info
    def MakeTrades(self, time, stock_prices):
        # update data
        stock_prices["Time"] = time
        self.prices = self.prices.append(stock_prices, ignore_index=True)
        # update returns columns by pct change of normal prices
        for i in range(1, self.n_stocks + 1):
            self.prices[f"Stock{i}_Returns"] = self.prices[f"Stock{i}"].pct_change()

        # print if last trade was profitable or not, log if in threshold
        if time > 0:
            if self.prices["Stock4_Returns"].iloc[-1] > 0 and self.prices["Stock3_Returns"].iloc[-2] > 0:
                print("Last trade was profitable")
            elif self.prices["Stock4_Returns"].iloc[-1] < 0 and self.prices["Stock3_Returns"].iloc[-2] < 0:
                print("Last trade was profitable")
            else:
                print("Last trade was not profitable")


        trades = {}
        if time > 1:
            # buy stock4 based on sign of stock3 returns
            if self.prices["Stock3_Returns"].iloc[-1] > 0:
                trades["Stock4"] = 600000 // stock_prices["Stock4"] + 1
            else:
                trades["Stock4"] = -600000 // stock_prices["Stock4"] - 1

            print(f"Buying stock4 at time {time} with {trades['Stock4']} shares")
        return trades


class DumbTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        trades = {}
        trades['Stock4'] = 1
        return trades

# %%
