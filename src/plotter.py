import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

class Plotter:
    def plot_distribution(self, df, column_name):
        """Plots distribution of the given column."""
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column_name], kde=True)
        plt.title(f"Distribution of {column_name}")
        plt.show()

    def plot_correlation(self, df):
        """Plots correlation heatmap of the DataFrame."""
        df_numerical = df.select_dtypes(include=[np.number])  # Select only numeric columns
        plt.figure(figsize=(12, 8))
        sns.heatmap(df_numerical.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

