import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Set Kaggle config directory if using project folder (uncomment if needed)
# os.environ['KAGGLE_CONFIG_DIR'] = r'E:\Power Learn Project\PLP CODES\PYTHON\frameworks.py\.kaggle'

# Kaggle dataset details (corrected identifier)
DATASET = 'allen-institute-for-ai/CORD-19-research-challenge'  # Updated slug
ZIP_FILE = 'cord-19-research-challenge.zip'  # Updated ZIP name
CSV_FILE = 'metadata.csv'  # Target file in the ZIP

@st.cache_data
def download_dataset():
    """Download dataset using Kaggle API if not already present."""
    if not os.path.exists(CSV_FILE):
        if not os.path.exists(ZIP_FILE):
            try:
                print("Downloading dataset from Kaggle...")
                api = KaggleApi()
                api.authenticate()
                api.dataset_download_files(DATASET, path='.', unzip=False)
                print("Download complete!")
            except Exception as e:
                if "403" in str(e):
                    st.error("403 Forbidden: Please accept the CORD-19 competition rules on Kaggle[](https://www.kaggle.com/competitions/CORD-19-research-challenge/rules) and regenerate your API token.")
                else:
                    st.error(f"Error downloading dataset: {e}")
                return False
        # Unzip the dataset
        try:
            with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
                # Extract all files (CORD-19 ZIP has multiple CSVs/JSONs; adjust if needed)
                zip_ref.extractall('.')
            print("Unzipped dataset.")
            # Rename if needed (ZIP root might be 'CORD-19-research-challenge/')
            if not os.path.exists(CSV_FILE):
                possible_csv = 'CORD-19-research-challenge/metadata.csv'
                if os.path.exists(possible_csv):
                    os.rename(possible_csv, CSV_FILE)
        except Exception as e:
            st.error(f"Error unzipping dataset: {e}")
            return False
    return True

@st.cache_data
def load_data():
    """Load CORD-19 metadata.csv."""
    if not download_dataset():
        return None
    try:
        df = pd.read_csv(CSV_FILE, on_bad_lines='skip', encoding='utf-8')
        return df
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return None

# Initialize the app
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Add interactive elements
year_range = st.slider("Select year range", 2019, 2022, (2019, 2022))

# Load data
df = load_data()
if df is None:
    st.error("Failed to load data. Please check Kaggle rules acceptance or try the direct download alternative below.")
    st.stop()

# Filter data based on year range
try:
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df_filtered = df[(df['publish_time'].dt.year >= year_range[0]) & 
                     (df['publish_time'].dt.year <= year_range[1])]
except Exception as e:
    st.error(f"Error filtering data: {e}")
    st.stop()

# Add visualizations based on selection
st.write("### Publications Over Time")
year_counts = df_filtered['publish_time'].dt.year.value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values, color='#1f77b4')
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Publications Over Time")
st.pyplot(plt)

# Show a sample of the data
st.write("### Sample Data")
st.dataframe(df_filtered.head())