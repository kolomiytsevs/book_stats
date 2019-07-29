import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()  # use decode for UTF8 decoding
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)

# can also read web pages

webpage = urllib.request.urlopen('https://www.google.com')

for line in webpage:
    print(line.decode('cp1252').encode('utf-8').strip())

