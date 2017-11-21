from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/1/1/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode('utf-8')
website.close()

soup = BeautifulSoup(html_content,'html.parser')
key_list = ['---------------']
new_dict = {}
excel_input = []

#Create Keys
table_grid = soup.find('table', id = 'tblGridData').tr
td_list = table_grid.find_all('td')
td_list.remove(td_list[5])
td_list.remove(td_list[0])
for td in td_list:
    key = td.string
    if key != None:
        key = key.replace('  ','').replace('\n','').replace('\r','')
    # print(key)
    key_list.append(key)
# print(key_list)

table = soup.find('table', id = 'tableContent')
tr_list = table.find_all('tr', recursive = False)
for tr in tr_list:
    td_list = tr.find_all('td', recursive = False, limit = 5)
    for i,td in enumerate(td_list):
        data = td.string
        if data == None:
            data = "NA"
        else:
            data = data.replace('  ','').replace('\n','').replace('\r','')
        print(key_list[i])
        print(data)
