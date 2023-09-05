import pandas as pd
import streamlit as st
import yfinance as yf

# Setting the configurations of the page
st.set_page_config(page_title="Stock Analysis Dashboard", page_icon="📈", layout="wide")
st.title("Stock Analysis Dashboard")
st.write("""
#### Welcome to the Stock Analysis Dashboard. Analyze stock data with interactive charts and metrics.""")

# User-inputs
ticker_symbol = st.text_input("Enter the ticker symbol", "GOOGL")
start_date = st.date_input("Select the start date", value=pd.to_datetime("2004-10-06"))
end_date = st.date_input("Select the end date", value=pd.to_datetime("2008-12-24"))
period = st.selectbox("Choose the period ", ["1wk", "1d", "1mo"])

# Fetching the historical data
ticker = yf.Ticker(ticker_symbol)
history_frame = ticker.history(period=period, start=start_date, end=end_date)

#Defining CSS for checkbox

st.write(
    """
    <style>
    
   
    .stCheckbox input:checked + .stCheckmark {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


boolValue = st.checkbox(label="Display raw data", value=False, )
if boolValue:
    st.write(history_frame)

selected_metric = st.selectbox("Select Metric to Visualize:", ["Close", "Volume", "High", "Low", "Open"])

st.subheader(f"Stock price of {selected_metric}")
st.line_chart(history_frame[selected_metric])

# This is for metric calculations :
st.sidebar.header("Stock Statistics")
st.sidebar.write("No of datapoints : ", len(history_frame))
st.sidebar.write("Mean price for close data : ", history_frame["Close"].mean())
st.sidebar.write("Standard deviation of close price data :", history_frame["Close"].std())

# footer and personal details

st.sidebar.markdown("---")  ## Used for line breaks
st.sidebar.markdown("## Created by Nadeem Shaik")
st.sidebar.markdown("[GitHub Repository](https://github.com/snadeem03)")


