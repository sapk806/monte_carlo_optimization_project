## Monte Carlo Portfolio Optimization

## Overview
My project uses simulations to generate random weights for each asset in a universe and find the weightings to yield the lowest volatility and highest Sharpe ratio.

## Dependencies 
- Python 3.13+
- pandas
- numpy
- matplotlib
- yfinance
- jupyter

## How to Run
- Activate the virtual environment with the required packages and run the script in the main.py file: 

1. Activate the virtual environment.
```bash
source .venv/bin/activate
```
2. Install dependencies.
```bash
pip install -r requirements.txt
```
3. Run the full backtest.
```bash
python main.py
```


## Output
- Plot of the simulation's volatility vs. average return and drawdown.
- Lowest volatility simulation's asset weightings.
- Highest Sharpe ratio simulation's asset weightings.