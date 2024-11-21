# Stock Market Technical Analysis System

A comprehensive Python-based stock analysis tool that combines technical indicators, machine learning predictions, and interactive visualizations for market analysis and trading strategy backtesting.

## Features

- **Real-time Data Fetching**: Automated data collection from Yahoo Finance API
- **Technical Analysis**: 
  - Simple Moving Averages (20 & 50 day)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- **Machine Learning Predictions**: 5-day price movement forecasting using Random Forest
- **Trading Strategy Backtesting**: SMA crossover strategy with performance metrics
- **Interactive Visualizations**: Dynamic charts using Plotly
- **Data Persistence**: SQLite database integration

## Performance Metrics
- Total Return
- Annual Return
- Sharpe Ratio
- Maximum Drawdown

## Tech Stack
- Python 3.x
- yfinance
- pandas, numpy
- scikit-learn
- SQLAlchemy
- Plotly
- BeautifulSoup4


## Installation and Usage

```bash
# 1. Clone the repository
git clone https://github.com/LETME2X/Stock-Market-Technical-Analysis-System.git
cd Stock-Market-Technical-Analysis-System

# 2. Create and activate a virtual environment
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analysis
python src/main.py
```
## Project Structure
```plaintext
src/
├── main.py              # Main application entry point
├── analysis.py          # Technical indicators and ML predictions
├── data_collection.py   # Data fetching from Yahoo Finance
├── data_management.py   # Database operations
├── trading.py           # Trading strategy and backtesting
└── visualization.py     # Interactive dashboards
```

## Sample Output
Strategy Results for AAPL:
Total Return: 26.20%
Annual Return: 26.32%
Sharpe Ratio: 106.34%
Max Drawdown: -11.75%

