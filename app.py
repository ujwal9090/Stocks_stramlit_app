import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Nifty Stocks Dashboard", layout="wide")

# Title
st.title("📈 Nifty Stocks Visualization Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
categories = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)

filtered_df = df[df['Category'] == selected_category]
symbols = filtered_df['Symbol'].unique()
selected_symbol = st.sidebar.selectbox("Select Symbol", symbols)

# Filtered final data
final_df = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Lineplot
st.subheader(f"📊 Closing Price Trend for {selected_symbol}")
fig, ax = plt.subplots(figsize=(15, 6))
sb.lineplot(data=final_df, x='Date', y='Close', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Show data if needed
with st.expander("Show Raw Data"):
    st.write(final_df)
