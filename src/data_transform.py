import pandas as pd   
import logging

class DataTransform:
    def save_to_csv(self, df, filepath):
        '''Saves the DataFrame to a CSV file'''
        try:
            df.to_csv(filepath, index = False)
            logging.info(f'Data saved successfully at {filepath}')
        except Exception as e:
            logging.error(f'Error saving data to CSV: {e}')

    def load_from_csv(self, filepath):
        '''Loads the data from a CSV file into a DataFrame.'''
        try:
            df = pd.read_csv(filepath)
            logging.info(f'Data loaded from {filepath}')
            return df
        except Exception as e:
            logging.error(f'Error loading data from CSV: {e}')
            return None
        
    def clean_data(self, df):
        '''Handles missing values and cleans data.'''
        try:
            df = df.dropna(subset = ['revenue'])
            logging.info('Data cleaned successfully')
            return df
        except Exception as e:
            logging.error(f'Error cleaning data: {e}')
            return df