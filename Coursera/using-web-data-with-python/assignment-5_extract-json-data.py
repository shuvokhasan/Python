import urllib.request, urllib.parse, urllib.error
import json

u=urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1796667.json')
dat=u.read()
data=json.loads(dat)

total=0
for tags in data['comments']:
    total+=tags["count"]
print(total)