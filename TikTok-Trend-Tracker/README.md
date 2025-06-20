# TikTok Trend Tracker Dashboard 📈

This project analyzes trending TikTok hashtags over an 8-week period using mock data. It includes visualizations of hashtag performance (views and video counts) over time and is designed as a beginner-friendly data science portfolio project.

## 🔍 Project Goals

- Practice working with time-series and categorical data
- Build visual insights using Matplotlib and Seaborn
- Simulate real-world data exploration for social media analytics

# 📊 TikTok Trend Tracker Dashboard

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://tiktok-trend-tracker-aevtmbojcazffktbdypmxj.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Powered%20By-Pandas-orange?logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Charts-Plotly-9cf?logo=plotly)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔥 Live Dashboard on Streamlit

This interactive dashboard analyzes trending TikTok hashtags over an 8-week period using mock data. Built with Streamlit, Plotly, and Pandas — it's a beginner-friendly data science project that visualizes hashtag performance over time.
[Live Dashboard on Streamlit](https://tiktok-trend-tracker-aevtmbojcazffktbdypmxj.streamlit.app/)

## 🗃️ Dataset

Mock dataset includes:
- 10 popular TikTok hashtags (e.g., `#challenge`, `#dance`, `#funny`)
- Weekly data for 8 weeks
- Metrics: total views and video counts

📁 [View dataset](data/tiktok_trend_mock_data.csv)

## 📊 Notebook

The notebook includes:
- Data generation and preprocessing
- Grouped and time-series visualizations
- Insights into the most engaging hashtags

📓 [View the notebook](data/explore_trends.ipynb)

## 🖼️ Preview

### 📈 Views Over Time
![Views Over Time](./data/viewsovertime.png)

### 📊 Total Views by Hashtag
![Total Views by Hashtag](./data/totalviewsbyhashtag.png)

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib & Seaborn
- Jupyter Notebook

## 🚀 Future Ideas

- Build a Streamlit dashboard for interactive viewing
- Integrate real TikTok data via APIs
- Compare hashtag trends across different content categories

## 🚀 Running it Yourself

Clone the repo, install dependencies, and launch locally:

```bash
git clone https://github.com/rayna180/cybersecurity.git
cd cybersecurity/TikTok-Trend-Tracker
pip install -r requirements.txt
streamlit run dashboard.py

