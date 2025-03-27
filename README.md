# Bollinger Bands Trading Strategy — AAPL (2020–2024)

This project implements a simple **Bollinger Bands-based trading strategy** using historical price data from Yahoo Finance (via `yfinance`). The strategy identifies **buy and sell signals** based on the relative position of the stock price to its moving average and volatility bands.

---

## Key Features

- **Data**: Apple (AAPL) stock data from 2020–2024
- **Indicators**: 20-day moving average, standard deviation
- **Strategy Logic**:
  - Buy when price drops below lower Bollinger Band
  - Sell when price rises above upper Bollinger Band
- **Backtesting**:
  - Position logic with 1-day trade delay
  - Strategy returns vs Buy & Hold
  - Sharpe Ratio and Max Drawdown
- **Visualization**:
  - Bollinger Bands with signals
  - Cumulative return comparison
  - Drawdown chart

---

## Performance Metrics

- **Sharpe Ratio**: Measures risk-adjusted returns  
- **Max Drawdown**: Worst peak-to-trough loss  
These are common metrics used in evaluating trading strategies.

---

## Dependencies

- `numpy`
- `pandas`
- `matplotlib`
- `yfinance`

You can install them using:

```bash
pip install numpy pandas matplotlib yfinance


