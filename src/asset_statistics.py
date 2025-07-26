import pandas as pd
import numpy as np

def asset_statistics(close_prices: pd.DataFrame):
    '''
    Calculates the daily returns and annualizes them, and finds the annualized covariance matrix of the daily returns.
    Saves daily returns to 'results/daily_returns.csv'.
    
    Args:
        close_prices (pd.DataFrame): DataFrame consisting of the adjusted close prices of each asset, indexed by date with assets as columns.
    
    Returns:
        pd.Series: Annualized average returns for each asset (indexed by ticker).
        pd.DataFrame: Annualized covariance matrix of asset returns (tickers as both rows and columns).
    '''

    daily_returns = close_prices.pct_change().dropna(how = 'all') 
    annualized_avg_daily_returns = daily_returns.mean() * 252

    annualized_cov_matrix = daily_returns.cov() * 252

    daily_returns.to_csv('results/daily_returns.csv')
    return annualized_avg_daily_returns, annualized_cov_matrix