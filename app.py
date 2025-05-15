import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.analysis import load_data
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="📊 Social Media Analytics", layout="wide")
st.title("📊 Social Media Analytics Dashboard")

data_path = r'C:\Users\mvnik\OneDrive\Desktop\social-media-analytics\data\sentimentdataset.csv'
df = load_data(data_path)

# Sidebar filters
st.sidebar.header("Filters")
selected_platform = st.sidebar.multiselect("Select Platform", options=df["Platform"].unique(), default=df["Platform"].unique())
selected_country = st.sidebar.multiselect("Select Country", options=df["Country"].unique(), default=df["Country"].unique())
df = df.drop(columns=["Unnamed: 0", "Unnamed: 0.1"])
filtered_df = df[(df["Platform"].isin(selected_platform)) & (df["Country"].isin(selected_country))]

# Show data preview
st.subheader("Data Preview")
st.dataframe(filtered_df.head())


# Clean and standardize sentiment values
filtered_df["Sentiment"] = filtered_df["Sentiment"].str.strip().str.capitalize()

# Keep only expected sentiment values
valid_sentiments = ["Positive", "Negative", "Neutral"]
filtered_df = filtered_df[filtered_df["Sentiment"].isin(valid_sentiments)]

# Visualizations
st.subheader("Sentiment Distribution")

# Check if filtered_df is not empty after cleaning
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size if needed
    sns.countplot(data=filtered_df, x="Sentiment", palette="pastel", ax=ax)
    ax.set_title("Sentiment Distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    st.pyplot(fig)
else:
    st.warning("No data available for selected filters.")


st.subheader("Engagement Over Time")

# Ensure 'date' exists and data is available
if 'date' in filtered_df.columns and not filtered_df.empty:
    # Convert to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(filtered_df['date']):
        filtered_df['date'] = pd.to_datetime(filtered_df['date'], errors='coerce')

    # Drop NaT values after coercion
    filtered_df = filtered_df.dropna(subset=['date'])

    # Group and plot
    engagement = filtered_df.groupby("date")[["Likes", "Retweets"]].sum().reset_index()

    # Plot engagement over time
    fig2, ax2 = plt.subplots()
    engagement.plot(x="date", y=["Likes", "Retweets"], ax=ax2)
    st.pyplot(fig2)
else:
    st.warning("Date column not found or no data to display.")


st.subheader("Sentiment Proportion (Pie Chart)")
if "Sentiment" in filtered_df.columns and not filtered_df["Sentiment"].dropna().empty:
    sentiment_counts = filtered_df['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']

    if not sentiment_counts.empty:
        fig = px.pie(sentiment_counts, values='Count', names='Sentiment',
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)
    else:
        st.warning("Sentiment counts are empty. Cannot generate pie chart.")
else:
    st.warning("Sentiment data is not available or missing.")

st.subheader("Monthly Sentiment Trend")

filtered_df['month'] = filtered_df['date'].dt.to_period('M').astype(str)
monthly_sentiment = filtered_df.groupby(['month', 'Sentiment']).size().reset_index(name='Count')

fig = px.line(monthly_sentiment, x='month', y='Count', color='Sentiment',
              markers=True)
st.plotly_chart(fig)

st.subheader("Sentiment by Platform")

fig = px.histogram(filtered_df, x='Sentiment', color='Platform',
                   barmode='group',
                   color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig)


st.subheader("Word Cloud of User Texts")

text_data = ' '.join(filtered_df['Text'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

