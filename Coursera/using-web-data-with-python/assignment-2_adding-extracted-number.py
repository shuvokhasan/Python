# Summetion of extracted numbers from website table

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1796664.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Innitializing sum
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    sum = sum + number
print(sum)