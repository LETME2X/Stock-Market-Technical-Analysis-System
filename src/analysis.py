import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class MarketAnalyzer:
    def calculate_technical_indicators(self, df):
        """
        Calculates various technical indicators
        """
        # Moving averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = exp1 - exp2
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
        
        return df
    
    def predict_price_movement(self, df, prediction_days=5):
        """
        Predicts future price movements using Random Forest
        """
        df['Target'] = df['Close'].shift(-prediction_days)
        features = ['SMA_20', 'SMA_50', 'RSI', 'MACD', 'Signal_Line']
        
        X = df[features].dropna()
        y = df['Target'].dropna()
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        return model.predict(X_test)
