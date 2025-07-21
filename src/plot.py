def plot(weightings_list, simulations_results, lowest_volatility_index, highest_sharpe_ratio_index):
    """
    Plots the volatilities of the simulations vs. average returns of the simulations wioth the drawdown when the maximum is higher than the simulation's return.

    Parameters:
        weightings_list (list of list): A list of all of the weightings used in the simulations
        simulations_results (list): A list containing the return, standard deviation, Sharpe ratio, and weightings of the portfolio in the current simulation.
        lowest_volatility_index (int): The index position of the simulation with the lowest volatility.
        highest_sharpe_ratio_index (int): The index position of the simulation with the highest sharpe ratio.
    
    Returns:
        None
    """
    import matplotlib.pyplot as plt

    simulations = 10000

    avg_returns = []
    volatilities = []
    sharpe_ratios = []

    
    for i in range(simulations):
        avg_return = simulations_results[i][0]
        avg_returns.append(avg_return)

        volatility = simulations_results[i][1]
        volatilities.append(volatility)

        sharpe_ratio = simulations_results[i][2]
        sharpe_ratios.append(sharpe_ratio)

    
    highest_sharpe_ratio_avg_return = simulations_results[highest_sharpe_ratio_index][0]
    highest_sharpe_ratio_volatility = simulations_results[highest_sharpe_ratio_index][1]
    highest_sharpe_ratio_weightings = weightings_list[highest_sharpe_ratio_index]

    lowest_volatility = simulations_results[int(lowest_volatility_index)][1]
    lowest_volatility_avg_return = simulations_results[int(lowest_volatility_index)][0]
    lowest_volatility_weightings = weightings_list[int(lowest_volatility_index)]

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