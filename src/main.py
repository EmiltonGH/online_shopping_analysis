from db_utils import RDSDatabaseConnector
from data_transform import DataTransform
from plotter import Plotter
from dataframe_info import DataFrameInfo

# Load credentials
import yaml
import psycopg2

def load_credentials(filepath='config/credentials.yaml'):
    """Loads credentials from a YAML file."""
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Step 1: Load credentials
    credentials = load_credentials()
    
    # Step 2: Initialize the RDS connector and extract data
    rds_connector = RDSDatabaseConnector(credentials)
    df = rds_connector.load_data_from_rds('customer_activity')

    if df is not None:
        # Step 3: Transform and save data
        transformer = DataTransform()
        df_cleaned = transformer.clean_data(df)
        transformer.save_to_csv(df_cleaned, 'data/processed/customer_activity_cleaned.csv')

        # Step 4: Perform EDA
        info = DataFrameInfo()
        print(info.describe_data(df_cleaned))

        # Step 5: Visualize data
        plotter = Plotter()
        plotter.plot_distribution(df_cleaned, 'revenue')
        plotter.plot_correlation(df_cleaned)  # This uses only numeric data

if __name__ == "__main__":
    main()

