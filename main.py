from config import CONFIG
from src.gather_data import gather_data
from src.asset_statistics import asset_statistics
from src.simulations import simulations
from src.optimizer import optimizer
from src.plot import plot

def main():
    universe = CONFIG['universe']
    start_date = CONFIG['Start Date']
    end_date = CONFIG['End Date']

    close_prices = gather_data(universe = universe, start_date = start_date, end_date = end_date)
    annualized_avg_returns, annualized_cov_matrix = asset_statistics(close_prices = close_prices)
    simulations_list, weightings_list = simulations(annualized_avg_daily_return = annualized_avg_returns, annualized_cov_matrix = annualized_cov_matrix)
    highest_sharpe_ratio_index, lowest_volatility_index  = optimizer(simulation_data = simulations_list)
    lowest_volatility_weightings, highest_sharpe_ratio_weightings  = plot(weightings_list = weightings_list, simulations_results = simulations_list, lowest_volatility_index = lowest_volatility_index, highest_sharpe_ratio_index = highest_sharpe_ratio_index)
    
    print('REPORT:')
    print(f"Lowest Volatility Weightings: {lowest_volatility_weightings}")
    print(f"Highest Sharpe Ratio Weightings: {highest_sharpe_ratio_weightings}")

if __name__ == '__main__':
    main()