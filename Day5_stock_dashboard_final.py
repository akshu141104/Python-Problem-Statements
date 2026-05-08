import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Dashboard")

# ---------------- OPTION ----------------
option = st.radio("Select Data Source", ["Live Stock Data", "Upload CSV"])

# ---------------- LIVE DATA ----------------
if option == "Live Stock Data":

    stock = st.selectbox("Select Company",
                         ["AAPL", "MSFT", "TSLA", "GOOGL", "RELIANCE.NS", "TCS.NS"])

    start = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
    end = st.date_input("End Date", pd.to_datetime("today"))

    data = yf.download(stock, start=start, end=end)

    # FIX 1: reset index
    data = data.reset_index()

    # FIX 2: handle multi-index (MAIN ERROR FIX)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

# ---------------- CSV ----------------
else:

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file is None:
        st.stop()

    data = pd.read_csv(file)

    # clean column names
    data.columns = data.columns.str.strip()

    # check columns
    if not all(col in data.columns for col in ['Date', 'Close', 'Volume']):
        st.error("CSV must have Date, Close, Volume")
        st.stop()

    # date fix
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# ---------------- CLEAN ----------------

# convert numeric (safe)
data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
data['Volume'] = pd.to_numeric(data['Volume'], errors='coerce')

# remove nulls
data = data.dropna()

# sort
data = data.sort_values('Date')

# moving avg
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# ---------------- SHOW ----------------

st.subheader("Data")
st.dataframe(data.tail())

# ---------------- PRICE ----------------

st.subheader("Price Chart")

fig, ax = plt.subplots()

ax.plot(data['Date'], data['Close'], label="Close")
ax.plot(data['Date'], data['MA20'], label="MA20")
ax.plot(data['Date'], data['MA50'], label="MA50")

ax.legend()
st.pyplot(fig)

# ---------------- VOLUME ----------------

st.subheader("Volume")

fig2, ax2 = plt.subplots()
ax2.bar(data['Date'], data['Volume'])

st.pyplot(fig2)