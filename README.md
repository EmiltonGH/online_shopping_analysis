# Online Shopping Analysis Project

## Project Overview

This project performs an analysis of online shopping data to answer key business questions and generate insights that will help the marketing and tech teams optimize strategies for improving sales, traffic, and system performance.

The analysis covers:
- Sales behavior (weekend vs. weekday)
- Revenue generation by region
- Website traffic and its contribution to sales
- Task time distribution (administrative, informational, product-related)
- System usage (operating systems, browsers) and regional discrepancies
- Marketing performance (bounce rates, ad traffic, and their impact on sales)

## Folder Structure

online_shopping_analysis/
├── config/                        # Configurations like credentials
│   └── credentials.yaml
├── data/                          # Data storage
│   └── raw/                       # Raw data from RDS
│   └── processed/                 # Processed data
├── logs/                          # Log files for debugging
│   └── app.log                    # Log file
├── src/                           # Source code for data extraction, transformation, and visualization
│   ├── db_utils.py                # Database connector and extraction functions
│   ├── data_transform.py          # Data transformations like dealing with NULLs, formatting, etc.
│   ├── plotter.py                 # Visualization scripts
│   ├── dataframe_info.py          # EDA utility methods
│   └── main.py                    # Main script to run the project
├── .gitignore                     # Ignore credentials and sensitive files
├── README.md                      # Project documentation
├── requirements.txt               # List of Python dependencies


## Installation

To get started with this project, clone the repository and install the necessary dependencies.

### Step 1: Clone the Repository

git clone https://github.com/EmiltonGH/online_shopping_analysis.git
cd online_shopping_analysis

## Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Run the following command to create and activate a virtual environment:
python3 -m venv onlineenv
source onlineenv/bin/activate  # On Windows, use `env\Scripts\activate`

## Install the required Python libraries by running

pip install -r requirements.txt

## Create a credentials.yaml file inside the data/ folder. The file should include the necessary database credentials to connect to your AWS RDS instance. Example format
host: your_host
port: your_port
user: your_username
password: your_password
database: your_database_name

## To run the entire analysis and generate all insights at once, execute the main.py script located in the src/ folder
python src/main.py

## Project Components

data/: Contains sensitive data like database credentials. The credentials.yaml file should store your AWS RDS credentials securely.
src/:
db_utils.py: Handles database connection and SQL queries.
data_transform.py: Performs data transformations such as handling missing values and skewness.
data_info.py: Provides insights into the DataFrame, including null values and summary statistics.
plotter.py: Contains functions to generate visualizations such as bar charts, pie charts, and line graphs.
main.py: Main script that combines all analysis and generates outputs.
requirements.txt: Contains a list of all Python libraries required to run the project.
README.md: This documentation file that describes the project, its structure, and how to run it.
.gitignore: Ensures that sensitive files like credentials.yaml and unnecessary files are not committed to the repository.


## Visualizations

Some of the key visualizations generated in this project include:

Sales Analysis: Comparison of weekend vs. weekday sales.
Revenue by Region: Bar charts showing which regions generate the most revenue.
Traffic Sources: Visualizations of website traffic that contribute to sales.
System Usage: Pie charts and bar charts displaying the breakdown of operating systems and browsers.
Task Time Distribution: Time spent by users on different tasks like product search, admin-related activities, etc.

## Conclusion

The insights derived from this analysis can assist the marketing and tech teams in making data-driven decisions to optimize website traffic strategies, resolve system-related issues, and maximize revenue generation.

## Contact
For any questions or contributions, please contact:

Your Name: semilton@gmail.com
GitHub: https://github.com/EmiltonGH

