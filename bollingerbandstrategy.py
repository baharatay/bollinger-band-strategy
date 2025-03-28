
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
ticker = "AAPL"
df = yf.download(ticker, start="2020-01-01", end="2024-01-01")



# Calculate 20-day moving average and standard deviation
df["Moving_Avg"] = df["Close"].rolling(window=20).mean()
df["Std_Dev"] = df["Close"].rolling(window=20).std()

# Define Upper and Lower Bollinger Bands
df["Upper_Band"] = df["Moving_Avg"] + (df["Std_Dev"] * 2)
df["Lower_Band"] = df["Moving_Avg"] - (df["Std_Dev"] * 2)

# Plot the stock price and Bollinger Bands
plt.figure(figsize=(12,6))
plt.plot(df["Close"], label="Stock Price", color="blue")
plt.plot(df["Moving_Avg"], label="Moving Average", color="orange")
plt.plot(df["Upper_Band"], label="Upper Band", linestyle="--", color="green")
plt.plot(df["Lower_Band"], label="Lower Band", linestyle="--", color="red")
plt.legend()
plt.title(f"{ticker} Bollinger Bands Strategy")
plt.show()


# Define trading signals
df["Close"], df["Lower_Band"] = df["Close"].align(df["Lower_Band"], axis=0, copy=False)
df["Buy_Signal"] = df[("Close", "AAPL")] < df[("Lower_Band", "")]
df["Sell_Signal"] = df[("Close", "AAPL")] > df[("Upper_Band", "")]

# Visualizing Buy and Sell Signals
plt.figure(figsize=(12,6))
plt.plot(df["Close"], label="Stock Price", color="blue", alpha=0.6)
plt.scatter(df.index[df["Buy_Signal"]], df["Close"][df["Buy_Signal"]], label="Buy Signal", marker="^", color="green", alpha=1)
plt.scatter(df.index[df["Sell_Signal"]], df["Close"][df["Sell_Signal"]], label="Sell Signal", marker="v", color="red", alpha=1)
plt.legend()
plt.title(f"{ticker} Trading Signals")
plt.show()

# backtesting performance
df["Daily_Return"] = df["Close"].pct_change()
df["Position"] = np.where(df["Buy_Signal"], 1, np.where(df["Sell_Signal"], -1, 0))
df["Position"] = df["Position"].shift(1)  # Shift to execute trades the next day
df["Strategy_Return"] = df["Position"] * df["Daily_Return"]
df["Cumulative_Strategy"] = (1 + df["Strategy_Return"]).cumprod()
df["Cumulative_Buy_Hold"] = (1 + df["Daily_Return"]).cumprod()

# Plot cumulative returns
plt.figure(figsize=(12,6))
plt.plot(df["Cumulative_Strategy"], label="Strategy Performance", color="purple")
plt.plot(df["Cumulative_Buy_Hold"], label="Buy & Hold", color="gray", linestyle="--")
plt.legend()
plt.title("Strategy vs Buy & Hold Performance")
plt.show()

# Sharpe Ratio (annualized)
sharpe_ratio = df["Strategy_Return"].mean() / df["Strategy_Return"].std() * np.sqrt(252)

# Maximum drawdown (worst peak-to-trough Loss)
df["Cumulative_Strategy_High"] = df["Cumulative_Strategy"].cummax()
max_drawdown = (df["Cumulative_Strategy"] / df["Cumulative_Strategy_High"] - 1).min()

# print performance metrics
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")

plt.figure(figsize=(12,6))
drawdown = df["Cumulative_Strategy"] / df["Cumulative_Strategy"].cummax() - 1
plt.plot(drawdown, color="red", label="Drawdown")
plt.title("Strategy Drawdown Over Time")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.legend()
plt.show()
