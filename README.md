# online_shopping_analysis

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

