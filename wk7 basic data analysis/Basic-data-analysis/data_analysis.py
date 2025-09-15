import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
    print("First few rows of the dataset:")
    print(df.head())
    print("\nData types and missing values:")
    print(df.dtypes)
    print(df.isnull().sum())
    # No missing values to clean in this dataset
except Exception as e:
    print(f"An error occurred: {e}")

# Basic Data Analysis
print("\nBasic statistics of numerical columns:")
print(df.describe())
print("\nMean sepal length by target (species):")
print(df.groupby('target')['sepal length (cm)'].mean())

# Identify patterns
print("\nObservation: Sepal length varies significantly across different species.")

# Visualizations
# Line chart (simulated time trend)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Trend of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='target', y='sepal length (cm)', data=df, estimator=np.mean)
plt.title('Average Sepal Length by Species')
plt.xlabel('Species (Target)')
plt.ylabel('Average Sepal Length (cm)')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, color='skyblue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['target'], cmap='viridis')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.colorbar(label='Species')
plt.show()