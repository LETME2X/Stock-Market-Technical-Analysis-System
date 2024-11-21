def create_dashboard(data, ticker):
    """
    Creates a simple dashboard for a single stock
    """
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    fig = make_subplots(rows=2, cols=1, 
                       subplot_titles=(f'{ticker} Price and Moving Averages', 
                                     'Volume'))

    fig.add_trace(go.Candlestick(x=data.index,
                                open=data['Open'],
                                high=data['High'],
                                low=data['Low'],
                                close=data['Close'],
                                name='OHLC'),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=data.index, 
                            y=data['SMA_20'],
                            name='SMA 20',
                            line=dict(color='orange')),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=data.index, 
                            y=data['SMA_50'],
                            name='SMA 50',
                            line=dict(color='blue')),
                  row=1, col=1)

    fig.add_trace(go.Bar(x=data.index, 
                        y=data['Volume'],
                        name='Volume'),
                  row=2, col=1)

    fig.update_layout(
        title=f'{ticker} Stock Analysis',
        yaxis_title='Stock Price ($)',
        yaxis2_title='Volume'
    )

    fig.show()
