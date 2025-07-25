import numpy as np

def optimizer(simulation_data: list[tuple]):
    """
    Finds the simulation with the lowest volatility and highest sharpe ratio, and takes the position in the simiulations list of those simulations.

    Args:
        simulation_data(list): List of tuples containing:
            - float: Simulated portfolio return
            - float: Simulated portfolio volatility
            - float: Sharpe ratio
            - np.ndarray: Portfolio weightings
 
    Returns:
        int: Index of the simulation with the highest sharpe ratio.
        int: Index of the simulation with the lowest volatility.
    """
    
    n_simulations = 10000
    
    lowest_volatility = np.inf
    highest_sharpe_ratio = -np.inf
    for i in range(n_simulations):
        annualized_volatility = simulation_data[i][1]
        sharpe_ratio = simulation_data[i][2]
        
        if annualized_volatility < lowest_volatility:
            lowest_volatility = annualized_volatility
            lowest_volatility_index = i
        
            
        if sharpe_ratio > highest_sharpe_ratio:
            highest_sharpe_ratio = sharpe_ratio
            highest_sharpe_ratio_index = i

    return highest_sharpe_ratio_index, lowest_volatility_index 