import yfinance as yf
import pandas as pd

def gather_data(universe: list[str], start_date: str, end_date: str):
    '''
    Downloads adjusted close prices for multiple tickers over a date range.
    Saves close prices to 'results/close_prices.csv'.
    
    Args:
        universe (list[str]): List of tickers from Yahoo Finance.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        pd.DataFrame: DataFrame consisting of the adjusted close prices of each asset, indexed by date with assets as columns.
    '''
    
    close_prices = yf.download(universe, start = start_date, end = end_date, auto_adjust = True)['Close']
    # Rows with missing data are removed to ensure time series between all tickers are aligned
    close_prices = close_prices.dropna()
    close_prices.to_csv('results/close_prices.csv')

    return close_prices