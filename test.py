import requests
from bs4 import BeautifulSoup


url = 'http://www.topology-zoo.org/dataset.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs and "graphml" in link['href']:
        print(link['href'][6:][:-8])