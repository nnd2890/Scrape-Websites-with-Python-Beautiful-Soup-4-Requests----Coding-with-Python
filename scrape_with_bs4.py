import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/miami-fl/coffee-shops'
url_page_2 = url + '?page=' + str(2)

r  = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
links = soup.find_all('a')

# for link in links:
#     print('<a href="%s">%s</a>'%(link.get('href'),link.text))

g_data = soup.find_all('div',{'class':'info'})
for item in g_data:
    print('Shop is: ' + item.contents[0].find_all('a', {'class':'business-name'})[0].text)
    
    try:
        print(item.contents[1].find_all('p', {'class':'adr'})[0].text)
    except:
        pass
    try:
        print(item.contents[1].find_all('div', {'class':'primary'})[0].text)
    except:
        pass
    