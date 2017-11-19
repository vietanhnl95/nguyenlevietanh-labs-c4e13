from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html")
html_content = website.read().decode('utf8')
website.close()

soup = BeautifulSoup(html_content,'html.parser')
chart_title = soup.find('div','widget-title').a
title_content = chart_title['title']
print(title_content)
print('-' * 20)

song_chart = soup.find('ul', 'box-song')
li_list = song_chart.find_all('li')
for index,li in enumerate(li_list):
    song = li.h3.a.string.replace('  ','').replace('\n','').replace('\r','')
    rank = index + 1
    print(rank, song, sep = '. ')
