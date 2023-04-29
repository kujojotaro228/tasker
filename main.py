import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract_info_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Здесь вам нужно написать код для извлечения нужной информации из HTML-страницы
    # Например, используя методы BeautifulSoup, вы можете найти и извлечь нужные теги и их содержимое

    # Пример:
    name = soup.find('span', {'class': 'name'}).text.strip()
    surname = soup.find('span', {'class': 'surname'}).text.strip()
    organization = soup.find('span', {'class': 'organization'}).text.strip()
    title = soup.find('h1', {'class': 'title'}).text.strip()

    # Здесь вы можете добавить дополнительную обработку, если какие-то данные отсутствуют

    return name, surname, organization, title


def process_html_files(urls):
    data = []

    for url in urls:
        name, surname, organization, title = extract_info_from_html(url)
        # Здесь можно запросить недостающую информацию, если требуется
        # Например:
        if not name:
            name = input("Введите имя для URL-адреса {}: ".format(url))

        data.append({
            'Имя': name,
            'Фамилия': surname,
            'Организация': organization,
            'Название': title
        })

    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    print("Список успешно создан и сохранен в файл 'output.xlsx'.")


# Список URL-адресов для обработки
urls = ['https://www.example.com/page1.html', 'https://www.example.com/page2.html']
process_html_files(urls)
