import yfinance as yahooFinance
import datetime
import numpy as np
import tkinter as tk
from tkinter import simpledialog

# calculate returns
def calculate_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i] - prices[i-1]) / prices[i-1])
    return returns

# calculate hedge ratio
def calculate_hedge_ratio():
    # Create a new Tk root window
    root = tk.Tk()
    root.withdraw()

    # Ask for the tickers, start date, and end date
    ticker1 = simpledialog.askstring("Input", "Enter the first ticker:")
    ticker2 = simpledialog.askstring("Input", "Enter the second ticker:")
    start_date = simpledialog.askstring("Input", "Enter the start date (YYYY-MM-DD):")
    end_date = simpledialog.askstring("Input", "Enter the end date (YYYY-MM-DD):")

    # Convert the dates to datetime objects
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    # Get the closing prices
    ticker1_info = yahooFinance.Ticker(ticker1)
    ticker2_info = yahooFinance.Ticker(ticker2)
    ticker1_prices = ticker1_info.history(start=start_date, end=end_date)["Close"].tolist()
    ticker2_prices = ticker2_info.history(start=start_date, end=end_date)["Close"].tolist()

    # Calculate the returns
    ticker1_returns = calculate_returns(ticker1_prices)
    ticker2_returns = calculate_returns(ticker2_prices)

    # Calculate the covariance and variance
    cov_matrix = np.cov(ticker1_returns, ticker2_returns)
    covariance = cov_matrix[0, 1]
    variance_ticker1 = np.var(ticker1_returns)

    # Calculate the Truman Special Number (beta)
    beta = covariance / variance_ticker1

    # Get hedge ratio
    hedgeRatio = 1/beta

    print(hedgeRatio)
    tk.messagebox.showinfo("Hedge Ratio", f"The hedge ratio is: {hedgeRatio}")

calculate_hedge_ratio()