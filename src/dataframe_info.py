class DataFrameInfo:
    def describe_data(self, df):
        """Describes all columns in the DataFrame."""
        return df.describe()

    def count_nulls(self, df):
        """Counts null values in each column."""
        return df.isnull().sum()

    def column_stats(self, df, column_name):
        """Returns median, mean, and standard deviation of a column."""
        return {
            "mean": df[column_name].mean(),
            "median": df[column_name].median(),
            "std": df[column_name].std()
        }
