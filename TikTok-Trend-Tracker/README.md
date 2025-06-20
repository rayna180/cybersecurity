# 📊 TikTok Trend Tracker Dashboard

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://tiktok-trend-tracker-aevtmbojcazffktbdypmxj.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-orange?logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Visuals-Plotly-9cf?logo=plotly)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

The **TikTok Trend Tracker** is an interactive Streamlit dashboard that visualizes trending TikTok hashtags over an 8-week period using mock data. It’s designed to simulate real-world social media analytics and is perfect for beginners building a data science portfolio.

🔗 **[Live Demo](https://tiktok-trend-tracker-aevtmbojcazffktbdypmxj.streamlit.app/)** – try it out now!

---

## 🎯 Project Goals

- Practice time-series and categorical data analysis
- Visualize trends using Matplotlib, Seaborn, and Plotly
- Simulate a real data science use case in social media analytics

---

## 🗂️ Dataset Details

The mock dataset includes:

- 10 popular hashtags (e.g., `#challenge`, `#dance`, `#funny`)
- Weekly data for 8 weeks
- Metrics: total views and number of videos

📁 [Explore the dataset](data/tiktok_trend_mock_data.csv)

---

## 🧪 Exploratory Notebook

The notebook contains:

- Synthetic data generation
- Time-series and categorical trend visualizations
- Analysis of top-performing hashtags

📓 [Open the notebook](data/explore_trends.ipynb)

---

## 🖼️ Dashboard Preview

### 📈 Views Over Time
![Views Over Time](./data/viewsovertime.png)

### 📊 Total Views by Hashtag
![Total Views by Hashtag](./data/totalviewsbyhashtag.png)

---

## ⚙️ Tech Stack

- **Python 3.11**
- **Pandas** for data manipulation
- **Matplotlib & Seaborn** for static visualizations
- **Plotly** for interactive charts
- **Streamlit** for dashboard deployment

---

## 🚀 Getting Started

To run the project locally:

```bash
git clone https://github.com/rayna180/cybersecurity.git
cd cybersecurity/TikTok-Trend-Tracker
pip install -r requirements.txt
streamlit run dashboard.py


