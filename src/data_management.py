from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    
    date = Column(DateTime, primary_key=True)
    ticker = Column(String, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class DataManager:
    def __init__(self, db_path='sqlite:///financial_data.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def store_stock_data(self, data_frame, ticker):
        """
        Stores processed data into SQLite database
        """
        try:
            data_frame['ticker'] = ticker
            data_frame.to_sql('stock_data', self.engine, 
                            if_exists='append', 
                            index=True)
            print(f"Successfully stored data for {ticker}")
        except Exception as e:
            print(f"Error storing data for {ticker}: {str(e)}")
    
    def get_stock_data(self, ticker, start_date=None, end_date=None):
        """
        Retrieves stock data from database
        """
        query = f"SELECT * FROM stock_data WHERE ticker='{ticker}'"
        if start_date:
            query += f" AND date >= '{start_date}'"
        if end_date:
            query += f" AND date <= '{end_date}'"
        return pd.read_sql(query, self.engine)
