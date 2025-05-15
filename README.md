# 📊 Social Media Analytics Dashboard

This project is a data-driven analysis and interactive dashboard built to understand and visualize social media performance metrics. The objective is to extract insights from post-level data and help identify the factors contributing to reach, engagement, and growth.

---

## 📁 Project Structure

- `social_media_metrics.xlsx` – Raw dataset from Kaggle
- `notebooks/Social Media Analytics.ipynb` – EDA and visualization notebook
- `app/streamlit_app.py` – Streamlit app for interactive dashboard
- `requirements.txt` – List of Python dependencies
- `README.md` – Project overview

---

## 🧾 Dataset

- **Source**: [Kaggle - Sentiment Dataset (used social media metrics subset)](https://www.kaggle.com/)
- The dataset includes metrics such as:
  - **Likes**
  - **Shares**
  - **Saves**
  - **Reach**
  - **Impressions**
  - **Profile Visits**
  - **Follows**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy** – Data manipulation
- **Matplotlib**, **Seaborn** – Data visualization
- **Streamlit** – Web app development
- **VS Code** – IDE for development
- **Virtual Environment** – Isolated Python environment for clean dependency management

---

## 📊 Exploratory Data Analysis (EDA)

Performed in a Jupyter Notebook:

- Summary statistics of key metrics
- Correlation matrix to uncover relationships
- Visualizations to compare engagement across posts
- Insights into what drives growth (e.g., saves and shares → more reach)

---

## 🌐 Streamlit App

An interactive web dashboard to visualize social media data. Users can:

- View post metrics and filter by engagement type
- Explore dynamic charts and graphs
- Gain insights for content strategy

> 📍 **To run the app:**

```bash
# Clone the repository
git clone https://github.com/yourusername/social-media-analytics.git
cd social-media-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
Local URL: http://localhost:8501
Network URL: http://192.168.29.55:8501
```
## Author 
**M V Nikhitha**

