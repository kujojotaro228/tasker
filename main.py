import os
import glob
import pandas as pd
from bs4 import BeautifulSoup

def extract_info_from_html(html_file):
    """
    Extracts relevant information from an HTML file and returns it in a tuple.

    Args:
        html_file (str): Path to the HTML file to extract information from.

    Returns:
        Tuple containing the extracted information, in the following order:
        - Name
        - Surname
        - Organization
        - Title
    """
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Here, you can use BeautifulSoup's methods to extract the relevant information from the HTML file.
        # For example:
        name = soup.find('span', {'class': 'name'}).text.strip()
        surname = soup.find('span', {'class': 'surname'}).text.strip()
        organization = soup.find('span', {'class': 'organization'}).text.strip()
        title = soup.find('h1', {'class': 'title'}).text.strip()

        # Here, you can add additional processing if some data is missing.

        return name, surname, organization, title

def process_html_files(folder_path):
    """
    Processes all HTML files in a folder, extracts relevant information from them,
    and saves the information in an Excel file.

    Args:
        folder_path (str): Path to the folder containing the HTML files.
    """
    html_files = glob.glob(os.path.join(folder_path, '*.html'))
    data = []
    
    for html_file in html_files:
        name, surname, organization, title = extract_info_from_html(html_file)
        # Here, you can request missing information if necessary.
        # For example:
        if not name:
            name = input("Enter name for file {}: ".format(html_file))

        data.append({
            'Name': name,
            'Surname': surname,
            'Organization': organization,
            'Title': title
        })
    
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    print("List successfully created and saved to 'output.xlsx' file.")

# Example usage:
folder_path = 'path/to/folder'
process_html_files(folder_path)
