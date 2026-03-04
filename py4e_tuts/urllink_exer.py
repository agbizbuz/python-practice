import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
url_count = int(input('Enter count: '))
url_pos = int(input('Enter position: '))

while url_count > 0:
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[url_pos-1].get('href', None)
    # for tag in tags:
    # print(tag.get('href', None))
    url_count -= 1

print(urllib.parse.urlsplit(url).path)