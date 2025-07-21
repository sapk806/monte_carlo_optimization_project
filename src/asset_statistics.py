def asset_statistics(close_prices):
    """
    Gathers the daily returns and annualizes them, and finds the annualized covariance matrix of the daily returns.

    Parameters:
        close_price (pd.DataFrame): A DataFrame consisting of the adjusted close prices of each asset, indexed by date with assets as columns.
    
    Returns:
        pd.DataFrame: A DataFrame consisting of the average annualized daily returns of each asset, indexed by date with assets as columns.
        np.ndarray: An array representing the covariance matrix of the daily returns of each asset.
    """
    import pandas as pd
    import numpy as np

    daily_returns = close_prices.pct_change().dropna(how = 'all') 
    annualized_avg_daily_returns = daily_returns.mean() * 252

    annualized_cov_matrix = daily_returns.cov() * 252

    daily_returns.to_csv('results/daily_returns.csv')
    return annualized_avg_daily_returns, annualized_cov_matrix