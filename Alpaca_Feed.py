import streamlit as st
import alpaca_trade_api as tradeapi
import pandas as pd


def app():

    api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

    Positions = api.list_positions()
    Orders = api.list_orders(status='closed')
    Orders

    df = []
    df2 = []
    df3 = []
    for position in Positions:
        df.append(position.symbol)
        df2.append(position.side)
        df3.append(position.qty)

    Total_Positions = pd.DataFrame(df)
    Total_Positions['Side'] = df2
    Total_Positions['Qty'] = df3
    Total_Positions = Total_Positions.rename(columns={0:'Symbol'}).set_index('Symbol')
    Total_Positions

    d = []
    d2 = []
    d3 = []
    d4=[]
    d5=[]
    for order in Orders: 
        d.append(order.submitted_at)
        d2.append(order.symbol)
        d3.append(order.side)
        d4.append(order.filled_avg_price)
        d5.append(order.qty)

    Order = pd.DataFrame(d)
    Order['Symbol'] = d2
    Order['Side'] = d3
    Order['Qty'] = d5
    Order['Filled_Avg_Price'] = d4
    Order = Order.rename(columns={0:'Timestamp'}).set_index('Timestamp')
    Order

    st.header("Risk Ranges Algorithm Trades")

    st.write(Total_Positions)

    st.write(Order)



  