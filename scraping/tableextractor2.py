import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_tables_from_webpage(webpage_url, output_folder):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(webpage_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all table elements
        tables = soup.find_all('table')
        print(tables)
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Iterate over each table found
        for i, table in enumerate(tables):
            # Create a list to hold table rows
            table_data = []
            
            # Find all rows in the table
            rows = table.find_all('tr')
            
            for row in rows:
                # Get all cell data for each row using list comprehensions
                cells = row.find_all(['td', 'th'])
                cell_data = [cell.get_text(strip=True) for cell in cells]
                table_data.append(cell_data)
            
            
            # Create a DataFrame from the table data
            df = pd.DataFrame(table_data)
            
            # Generate a CSV file name
            csv_filename = os.path.join(output_folder, f'table_{i+1}.csv')
            
            # Save the DataFrame to a CSV file
            df.to_csv(csv_filename, index=False, header=False)
            
            print(f"Table {i+1} successfully saved to {csv_filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Example usage
webpage_url = 'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro'  # Replace with the actual webpage URL
output_folder = 'extracted_tables'   # Folder where CSV files will be saved

extract_tables_from_webpage(webpage_url, output_folder)

"""

List comprehensions:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = [x for x in input_list if x % 2 == 0]

Dictionary Comprehensions:
states = ['Gujarat', 'Maharashtra', 'Rajasthan']
capitals = ['Gandhinagar', 'Mumbai', 'Jaipur']
state_capitals = {state: capital for state, capital in zip(states, capitals)}

Set Comprehension
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
even_set = {x for x in input_list if x % 2 == 0}

"""