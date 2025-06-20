import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("TikTok-Trend-Tracker/data/tiktok_trend_mock_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Page config
st.set_page_config(page_title="TikTok Trend Tracker", layout="wide")

st.title("📊 TikTok Trend Tracker Dashboard")
st.markdown("Explore weekly trends in top TikTok hashtags using mock data.")

# Sidebar filters
hashtags = df['hashtag'].unique()
selected_tags = st.sidebar.multiselect("Select hashtags to view", options=hashtags, default=hashtags[:3])

# Filter data
filtered_df = df[df['hashtag'].isin(selected_tags)]

# Line chart: Views over time
st.subheader("📈 Views Over Time")
fig1 = px.line(filtered_df, x='date', y='views', color='hashtag', markers=True, title="Hashtag Views")
st.plotly_chart(fig1, use_container_width=True)

# Bar chart: Total Views per Hashtag
st.subheader("📊 Total Views by Hashtag")
totals = filtered_df.groupby("hashtag")["views"].sum().reset_index().sort_values(by="views", ascending=False)
fig2 = px.bar(totals, x="hashtag", y="views", title="Total Views by Hashtag")
st.plotly_chart(fig2, use_container_width=True)

# Data preview
with st.expander("🔍 View Raw Data"):
    st.dataframe(filtered_df.sort_values(by="date"))
