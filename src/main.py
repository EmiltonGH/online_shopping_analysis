from db_utils import RDSDatabaseConnector
from data_transform import DataTransform
from plotter import Plotter
from dataframe_info import DataFrameInfo

# Load credentials
import yaml
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

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


    # Group by weekend and calculate sales (revenue)
    sales_by_weekend = df_cleaned.groupby('weekend')['revenue'].sum().reset_index()

    # Visualization
    plt.figure(figsize=(8, 6))
    sns.barplot(x='weekend', y='revenue', data=sales_by_weekend)
    plt.title('Sales Comparison: Weekends vs Weekdays')
    plt.xlabel('Weekend')
    plt.ylabel('Total Revenue')
    plt.show()


    # Group by region and calculate revenue
    region_revenue = df_cleaned.groupby('region')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)

    # Visualization
    plt.figure(figsize=(10, 8))
    sns.barplot(x='revenue', y='region', data=region_revenue, palette='viridis')
    plt.title('Revenue by Region')
    plt.xlabel('Total Revenue')
    plt.ylabel('Region')
    plt.show()


    # Group by traffic type and calculate sales (revenue)
    traffic_revenue = df_cleaned.groupby('traffic_type')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x='traffic_type', y='revenue', data=traffic_revenue, palette='rocket')
    plt.title('Revenue by Traffic Source')
    plt.xlabel('Traffic Type')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.show()


    # Calculate total time spent on different activities
    total_time_spent = df_cleaned[['administrative_duration', 'informational_duration', 'product_related_duration']].sum()

    # Convert to percentages
    total_time_spent_percent = (total_time_spent / total_time_spent.sum()) * 100

    # Visualization
    plt.figure(figsize=(8, 6))
    total_time_spent_percent.plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Percentage of Time Spent on Administrative/Product/Informational Tasks')
    plt.ylabel('')
    plt.show()


    # Group by month and calculate sales (revenue)
    monthly_sales = df_cleaned.groupby('month')['revenue'].sum().reset_index()

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='month', y='revenue', data=monthly_sales, marker='o')
    plt.title('Monthly Sales Breakdown')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.show()


    # Count of operating systems used to visit the site
    os_count = df_cleaned['operating_systems'].value_counts(normalize=True) * 100

    # Visualization for operating systems
    plt.figure(figsize=(8, 6))
    os_count.plot(kind='bar', color='skyblue')
    plt.title('Operating Systems Used to Visit the Site')
    plt.ylabel('Percentage of Users')
    plt.xlabel('Operating Systems')
    plt.show()

    # Breakdown of browsers by mobile vs desktop
    browser_usage = df_cleaned.groupby(['browser', 'operating_systems']).size().unstack().fillna(0)

    # Visualization for browsers
    browser_usage.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='coolwarm')
    plt.title('Browser Usage Breakdown by Operating System')
    plt.ylabel('User Count')
    plt.xlabel('Browser')
    plt.show()

    # Group by region and traffic type, calculate revenue
    region_traffic_revenue = df_cleaned.groupby(['region', 'traffic_type'])['revenue'].sum().unstack().fillna(0)

    # Visualization
    plt.figure(figsize=(12, 8))
    sns.heatmap(region_traffic_revenue, cmap='YlGnBu', annot=True, fmt='.1f')
    plt.title('Revenue Breakdown by Traffic and Region')
    plt.ylabel('Region')
    plt.xlabel('Traffic Source')
    plt.show()


    # Group by traffic type and calculate average bounce rate
    traffic_bounce_rate = df_cleaned.groupby('traffic_type')['bounce_rates'].mean().reset_index()

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x='traffic_type', y='bounce_rates', data=traffic_bounce_rate, palette='magma')
    plt.title('Average Bounce Rate by Traffic Type')
    plt.xlabel('Traffic Type')
    plt.ylabel('Bounce Rate')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()

