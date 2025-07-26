import pandas as pd
import numpy as np

def simulations(annualized_avg_daily_return: pd.Series, annualized_cov_matrix: pd.DataFrame):
    '''
    Runs 10,000 Monte Carlo simulations using randomly generated portfolio weightings.
    For each simulation, computes expected return, volatility, and Sharpe raito based on the
    provided annulized average returns and covariance matrix.

    Saves simulation results to 'results/simulations.csv'

    Args:
        annualized_avg_daily_return (pd.DataFrame): DataFrame consisting of the average annualized daily returns of each asset, indexed by date with assets as columns.
        annualized_cov_matrix (pd.DataFrame): pd.DataFrame: Annualized covariance matrix of asset returns (tickers as both rows and columns).

    Returns:
        list[tuple]: List of tuples containing:
            - float: Simulated portfolio return
            - float: Simulated portfolio volatility
            - float: Sharpe ratio
            - np.ndarray: Portfolio weightings
        np.ndarray: All weight vectors used in the simulations.
    '''
    
    simulations = 10000
    n_assets = 12

    simulation_data_list = []
    simulation_weightings_list = []
    for i in range(simulations):
        weightings = np.random.random(n_assets)
        weightings = weightings/sum(weightings)
        simulation_weightings_list.append(weightings)

        avg_daily_return_dict = {}
        for asset, weighting in zip(annualized_avg_daily_return.index, weightings):
            avg_daily_return_dict[asset] = annualized_avg_daily_return.loc[asset] * weighting
        
        annualized_portfolio_avg_daily_return = sum(avg_daily_return_dict.values())
        
        portfolio_variance = np.dot(weightings.T, np.dot(annualized_cov_matrix, weightings))
        annualized_portfolio_volatility = np.sqrt(portfolio_variance)

        sharpe_ratio = annualized_portfolio_avg_daily_return / annualized_portfolio_volatility
        
        simulation_data_list.append((annualized_portfolio_avg_daily_return, annualized_portfolio_volatility, sharpe_ratio, weightings))
    
    simulations_series = pd.Series(simulation_data_list)
    simulations_series.to_csv('results/simulations.csv')

    return(simulation_data_list, simulation_weightings_list)