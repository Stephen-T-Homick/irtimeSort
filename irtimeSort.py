#!/usr/bin/python3

# Written by Stephen Homick - Team Lead, Security Operations (CIRT)
# April 2023
# Purpose: The purpose of this script is to extract timestamp information from multiple log files that are provided in CSV or Excel format, and organize them into a single, master timeline. 
## Once this timeline is achieved, this can be used in a forensic report.

import argparse
import os
import pandas as pd

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Combine dates or timestamps from XLSX or CSV files')
parser.add_argument('output_file', type=str, help='path to the output file')
parser.add_argument('input_files', nargs='+', type=str, help='paths to the input files')

# Parse the command-line arguments
args = parser.parse_args()

# Create an empty DataFrame to hold the dates/timestamps
dates = pd.DataFrame()

# Iterate over the input files
for input_file in args.input_files:
    # Determine the file type (CSV or XLSX)
    _, extension = os.path.splitext(input_file)
    if extension == '.csv':
        # Read the CSV file and check if there's a 'date' column
        df = pd.read_csv(input_file)
        if 'date' not in df.columns:
            # Search for a column containing a date/timestamp
            date_columns = df.select_dtypes(include=['datetime']).columns
            if len(date_columns) == 0:
                raise ValueError(f'No date or timestamp column found in file {input_file}')
            elif len(date_columns) > 1:
                raise ValueError(f'Multiple date or timestamp columns found in file {input_file}')
            else:
                # Rename the date/timestamp column to 'date'
                df.rename(columns={date_columns[0]: 'date'}, inplace=True)
    elif extension == '.xlsx':
        # Read the XLSX file and check if there's a 'date' column
        df = pd.read_excel(input_file)
        if 'date' not in df.columns:
            # Search for a column containing a date/timestamp
            date_columns = df.select_dtypes(include=['datetime']).columns
            if len(date_columns) == 0:
                raise ValueError(f'No date or timestamp column found in file {input_file}')
            elif len(date_columns) > 1:
                raise ValueError(f'Multiple date or timestamp columns found in file {input_file}')
            else:
                # Rename the date/timestamp column to 'date'
                df.rename(columns={date_columns[0]: 'date'}, inplace=True)
    else:
        raise ValueError(f'Unsupported file type: {extension}')

    # Add the dates/timestamps to the DataFrame
    dates = pd.concat([dates, df['date']])

# Sort the dates/timestamps in descending order
dates = dates.sort_values(ascending=False)

# Write the dates/timestamps to the output file
dates.to_csv(args.output_file, index=False)

