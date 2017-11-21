from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Download HTML content
website = urlopen("http://dantri.com.vn")
html_content = website.read().decode('utf8')
website.close()

#2. Create BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')
# print(soup.prettify())
ul_news = soup.find('ul','ul1 ulnew')
# print(ul_news.prettify())
li_news_list = ul_news.find_all('li')

for li in li_news_list:
    a_link = li.h4.a
    title = a_link['title'] #attribute indexing
    print(title)
    content = a_link.string #content/string/value indexing
    print(content)
    print("-" * 20)
