import matplotlib.pyplot as plt
import numpy as np

def plot(simulation_weightings_list: list, simulation_data_list: list, lowest_volatility_index: int, highest_sharpe_ratio_index: int):
    """
    Plots the efficient frontier from 10,000 Monte Carlo portfolio simulations.
    Plot is saved to 'plots/efficient_frontier.png'

    Args:
        simulation_weightings_list (list[np.ndarray]): List of all of the weightings used in the simulations
        simulation_data_results (list[tuple[float, float, float, np.ndarray]]): List containing the return, standard deviation, Sharpe ratio, and weightings of the portfolio in the current simulation.
        lowest_volatility_index (int): Index of the simulation with the lowest volatility.
        highest_sharpe_ratio_index (int): Index of the simulation with the highest Sharpe ratio.
    
    Returns:
        np.ndarray: Weights of the portfolio with the lowest volatility.
        np.ndarray: Weights of the portfolio with the highest Sharpe ratio.
    """

    simulations = 10000

    avg_returns = []
    volatilities = []
    sharpe_ratios = []

    
    for i in range(simulations):
        avg_return = simulation_data_list[i][0]
        avg_returns.append(avg_return)

        volatility = simulation_data_list[i][1]
        volatilities.append(volatility)

        sharpe_ratio = simulation_data_list[i][2]
        sharpe_ratios.append(sharpe_ratio)

    
    highest_sharpe_ratio_avg_return = simulation_data_list[highest_sharpe_ratio_index][0]
    highest_sharpe_ratio_volatility = simulation_data_list[highest_sharpe_ratio_index][1]
    highest_sharpe_ratio_weightings = simulation_weightings_list[highest_sharpe_ratio_index]

    lowest_volatility = simulation_data_list[int(lowest_volatility_index)][1]
    lowest_volatility_avg_return = simulation_data_list[int(lowest_volatility_index)][0]
    lowest_volatility_weightings = simulation_weightings_list[int(lowest_volatility_index)]

    plt.figure(figsize = (12, 6))
    plt.scatter(volatilities, avg_returns, c = sharpe_ratios)
    plt.scatter(highest_sharpe_ratio_volatility, highest_sharpe_ratio_avg_return, marker = '*', color = 'r', s = 200, label = 'Highest Sharpe Ratio')
    plt.scatter(lowest_volatility, lowest_volatility_avg_return, marker = 'X', color = 'b', s = 200, label = 'Lowest Volatility')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volatility')
    plt.ylabel('Expected Return')
    plt.title('Simulated Portfolios: Efficient Frontier')

    plt.savefig("plots/efficient_frontier.png", dpi=300, bbox_inches='tight')

    plt.show()

    return lowest_volatility_weightings, highest_sharpe_ratio_weightings