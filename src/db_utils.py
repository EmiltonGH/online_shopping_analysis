import yaml
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import logging

# Initialize logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

    def init_db_engine(self):
        '''Initializes the SQLAlchemy engine.'''
        try:
            engine = sqlalchemy.create_engine(
                f"postgresql://{self.credentials['RDS_USER']}:"
                f"{self.credentials['RDS_PASSWORD']}@"
                f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/"
                f"{self.credentials['RDS_DATABASE']}"
            )
            logging.info('Database engine initialized successfully')
            return engine
        except SQLAlchemyError as e:
            logging.error(
                f'Error occurred while connecting to the database: {e}')
            return None

    def load_data_from_rds(self, table_name):
        '''Extracts data from the RDS database.'''
        engine = self.init_db_engine()
        if engine:
            try:
                query = f"SELECT * FROM {table_name}"
                df = pd.read_sql(query, con=engine)
                logging.info(f"Data loaded from table {table_name}")
                return df
            except Exception as e:
                logging.error(f"Error loading data from {table_name}: {e}")
                return None

        return None


