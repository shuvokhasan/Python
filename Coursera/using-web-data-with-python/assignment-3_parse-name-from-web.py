# Summetion of extracted numbers from website table

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL:')
# link = 'http://py4e-data.dr-chuck.net/known_by_Limbiadhe.html'
count = int(input('Enter count'))
# count = 7
pos = int(input('Enter position:'))
# pos = 18

print('Retriving: ', link)
for i in range(0, count):
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

    link = tags[pos-1].get('href')

result = tags[pos-1].contents[0]
print(result)