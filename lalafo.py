import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagn').find('li', class_='pagn-last').find_all('a')[-1].get('href')
    total_pages = pages.split('=')[-1]
    return int(total_pages)


def write_csv(data):
    with open('lalafo.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['url'],
                         data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.findAll('article', class_='listing-item')

    for ad in ads:
        try:
            title = ad.find('div', class_='listing-item-main').find('a', class_='listing-item-title').text.strip()
        except:
            title = 'Title'
        try:
            url = ad.find('img', class_='listing-item-photo').get('src').strip()
        except:
            url = 'URL'
        try:
            price = ad.find('div', class_='listing-item-main').find('p', class_='listing-item-title').text.strip()
        except:
            price = 'Price'

        data = {'title': title,
                'url': url,
                'price': price}

        write_csv(data)


def main():
    url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary?page=1'
    base_url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary'
    page_part = '?page='
    total_pages = get_total_pages(get_html(url))

    for i in range(1, 10):
        url_gen = base_url + page_part + str(i)
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == "__main__":
    main()
