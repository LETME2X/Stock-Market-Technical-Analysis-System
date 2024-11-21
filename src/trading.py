import numpy as np
import pandas as pd

class TradingStrategy:
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.positions = 0
        self.trades = []
    
    def backtest_strategy(self, df, strategy_type='sma_crossover'):
        """
        Backtests trading strategy on historical data
        """
        df['Position'] = 0
        
        if strategy_type == 'sma_crossover':
            df['Position'] = np.where(df['SMA_20'] > df['SMA_50'], 1, -1)
        
        df['Returns'] = df['Close'].pct_change()
        df['Strategy_Returns'] = df['Position'].shift(1) * df['Returns']
        df['Cumulative_Returns'] = (1 + df['Strategy_Returns']).cumprod()
        
        return self.calculate_performance_metrics(df)
    
    def calculate_performance_metrics(self, df):
        """
        Calculates various performance metrics
        """
        total_return = df['Cumulative_Returns'].iloc[-1] - 1
        annual_return = (1 + total_return) ** (252 / len(df)) - 1
        
        risk_free_rate = 0.02
        excess_returns = df['Strategy_Returns'] - risk_free_rate/252
        sharpe_ratio = np.sqrt(252) * excess_returns.mean() / excess_returns.std()
        
        cumulative = df['Cumulative_Returns']
        running_max = cumulative.cummax()
        drawdown = (cumulative - running_max) / running_max
        max_drawdown = drawdown.min()
        
        return {
            'Total Return': total_return,
            'Annual Return': annual_return,
            'Sharpe Ratio': sharpe_ratio,
            'Max Drawdown': max_drawdown
        }
