def simulations(annualized_avg_daily_return, annualized_cov_matrix):
    """
    Runs 10,000 simulations using different weightings for each asset to calculate the portfolio value in combination with the annualized average daily return and the annualized covariance matrix.

    Parameters
        annualized_avg_daily_return (pd.DataFrame): A DataFrame consisting of the average annualized daily returns of each asset, indexed by date with assets as columns.
        annualized_cov_matrix (np.ndarray): An array representing the covariance matrix of the daily returns of each asset.

    Returns:
        list: A list containing the return, standard deviation, Sharpe ratio, and weightings of the portfolio in the current simulation.
        list of list: A list of all of the weightings used in the simulations.
    """
    import pandas as pd
    import numpy as np
    
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