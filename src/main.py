from data_collection import fetch_stock_data
from data_management import DataManager
from analysis import MarketAnalyzer
from trading import TradingStrategy
from visualization import create_dashboard
from datetime import datetime, timedelta

def main():
    # 1. Set up parameters
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    initial_capital = 100000

    # 2. Fetch Data
    print("Fetching stock data...")
    stock_data = fetch_stock_data(tickers, start_date, end_date)

    # 3. Process and store data
    data_manager = DataManager()
    for ticker, data in stock_data.items():
        data_manager.store_stock_data(data, ticker)

    # 4. Analyze data
    analyzer = MarketAnalyzer()
    for ticker, data in stock_data.items():
        print(f"\nAnalyzing {ticker}...")
        data_with_indicators = analyzer.calculate_technical_indicators(data)
        
        strategy = TradingStrategy(initial_capital)
        results = strategy.backtest_strategy(data_with_indicators)
        
        print(f"\nStrategy Results for {ticker}:")
        for metric, value in results.items():
            print(f"{metric}: {value:.2%}")
        
        create_dashboard(data_with_indicators, ticker)

if __name__ == "__main__":
    main()
