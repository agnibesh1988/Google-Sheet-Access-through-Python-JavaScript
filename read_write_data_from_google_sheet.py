# -*- coding: utf-8 -*-
"""
Read data from Google Sheet and then Write it on Another Google Sheet

"""

import pandas as pd
from google.colab import auth
import gspread
from google.auth import default # Import the new authentication library

auth.authenticate_user()

# Authorize the clientsheet
creds, _ = default()  # Get credentials using the new library
gc = gspread.authorize(creds)  # Pass the credentials to gspread



# Read data from source Google Sheet, handling duplicate column names
def read_google_sheet(sheet_url, sheet_name):
    sheet = gc.open_by_url(sheet_url).worksheet(sheet_name)
    data = sheet.get_all_values()  # Get all values instead of records

    # Get header row and make column names unique
    header = data[0]
    unique_header = []
    for i, col in enumerate(header):
        count = header.count(col)
        if count > 1:
            unique_header.append(col + "_" + str(i))  # Append index to duplicate names
        else:
            unique_header.append(col)

    # Create DataFrame with unique column names
    df = pd.DataFrame(data[1:], columns=unique_header)
    return df



def write_google_sheet(sheet_url, sheet_name, df):
    # Open the Google Sheet
    sheet = gc.open_by_url(sheet_url).worksheet(sheet_name)

    # Clear the existing content
    sheet.clear() # This line clears the sheet before writing

    # Convert DataFrame to list of lists
    data = [df.columns.values.tolist()] + df.values.tolist()

    # Update the Google Sheet with the new data
    sheet.update('A1', data)
    
    

def main():
  # Authenticate and authorize the clientsheet
  # Read data
  source_sheet_url = 'https://docs.google.com/spreadsheets/d/1MZ6ERzEUb/edit#gid=1959776648'
  target_sheet_url = 'https://docs.google.com/spreadsheets/d/1XqaTbzg23fvvvrvwec/edit#gid=0'

  df = read_google_sheet(source_sheet_url, 'Campaign - Audit')
  df.head()

  write_google_sheet(target_sheet_url, 'Meta Campaign Test', df)
  
  

if __name__ == '__main__':
  main()