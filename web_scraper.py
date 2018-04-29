from bs4 import BeautifulSoup
import requests

page_link = 'https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, 'html.parser')

# extract all html elements where row is stored
row = page_content.find(id='tab-1')

if row is None:
    print('lelelele')
else:
    print(row)

