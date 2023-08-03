# import dask

import os
import sqlite3
import pandas as pd
from datetime import datetime


def csv_to_sqlite(directory):
    # Generate a unique database name based on the current date and time
    database = datetime.now().strftime('%Y%m%d%H%M%S') + '_TEC contribs.db'

    # Establish a connection to the SQLite database
    conn = sqlite3.connect(database)

    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # For each CSV file, read the file into a pandas DataFrame and write it to the SQLite database
    for file in csv_files:
        # Read and write the file in chunks
        chunksize = 10 ** 6  # Adjust this value based on your memory capacity
        for chunk in pd.read_csv(os.path.join(directory, file), chunksize=chunksize):
            chunk.to_sql('contribs', conn, if_exists='append', index=False)

    # Close the connection to the SQLite database
    conn.close()

    # Return the name of the database
    return database


if __name__ == "__main__":
    csv_to_sqlite("contribs")
