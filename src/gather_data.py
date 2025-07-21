def gather_data(universe, start_date, end_date):
    """
    Gathers the clean adjusted close prices of a list of tickers between the start and end date.

    Parameters:
        universe (list of str): A list of tickers from Yahoo Finance.
        start_date (str): Start date in (YYYY-MM-DD) format.
        end_date (str): End date in (YYYY-MM-DD) format.

    Returns:
        pd.DataFrame: A DataFrame consisting of the adjusted close prices of each asset, indexed by date with assets as columns.
    """
    import yfinance as yf
    import pandas as pd
    
    close_prices = yf.download(universe, start = start_date, end = end_date, auto_adjust = True)['Close']
    close_prices = close_prices.dropna()
    close_prices.to_csv('results/close_prices.csv')

    return close_prices