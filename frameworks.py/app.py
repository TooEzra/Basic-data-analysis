import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Load the CORD-19 metadata
@st.cache_data
def load_data():
    try:
        #df = pd.read_csv('metadata.csv', quoting=csv.QUOTE_ALL, encoding='utf-8')
        df = pd.read_csv("metadata.csv", on_bad_lines="skip")
        return df
    except pd.errors.ParserError as e:
        st.error(f"Error loading CSV: {e}")
        return None

# Initialize the app
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research paper:")

# Add interactive elements
year_range = st.slider("Select year range", 2019, 2022, (2019, 2022))

# Load data
df = load_data()
if df is None:
    st.stop()

# Filter data based on year range
try:
    df_filtered = df[(df['publish_time'].str[:4].astype(float) >= year_range[0]) & 
                    (df['publish_time'].str[:4].astype(float) <= year_range[1])]
except Exception as e:
    st.error(f"Error filtering data: {e}")
    st.stop()

# Add visualizations based on selection
st.write("### Publications Over Time")
year_counts = df['publish_time'].str[:4].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values, color='#1f77b4')
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Publications Over Time")
st.pyplot(plt)

# Show a sample of the data
st.write("### Sample Data")
st.dataframe(df_filtered.head())