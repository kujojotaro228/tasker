import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_info_from_html(html_text):
    """
    Extracts information from HTML page using BeautifulSoup library.

    Args:
        html_text (str): HTML code of the page as a string.

    Returns:
        Tuple containing extracted information as strings.
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    # Here you can write code to extract the required information from the HTML page
    # For example, using BeautifulSoup methods, you can find and extract the necessary tags and their contents
    
    # Example:
    name = soup.find('span', {'class': 'name'}).text.strip()
    surname = soup.find('span', {'class': 'surname'}).text.strip()
    organization = soup.find('span', {'class': 'organization'}).text.strip()
    title = soup.find('h1', {'class': 'title'}).text.strip()

    # Here you can add additional processing if some data is missing

    return name, surname, organization, title


def process_html_urls(urls):
    """
    Processes list of URLs pointing to HTML pages, extracts required information from them
    and saves the data to an Excel file.

    Args:
        urls (list of str): List of URLs pointing to HTML pages.
    """
    data = []
    
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {url}")
            continue
        
        name, surname, organization, title = extract_info_from_html(response.text)
        # Here you can request missing information if necessary
        # For example:
        if not name:
            name = input(f"Enter name for URL {url}: ")

        data.append({
            'Name': name,
            'Surname': surname,
            'Organization': organization,
            'Title': title
        })
    
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    print("List successfully created and saved to 'output.xlsx' file.")

# List of URLs pointing to HTML pages
urls = [
    'https://example.com/page1.html',
    'https://example.com/page2.html',
    'https://example.com/page3.html',
]

# Process the HTML URLs and save the data to Excel file
process_html_urls(urls)
