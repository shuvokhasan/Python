import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())