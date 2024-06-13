from urllib.parse import urljoin, urlparse
import requests

start_url = "http://127.0.0.1:5500/page1.html"

urls = [
    "/page2.html",
    "page2.html#bookmark",
    "page2.html",
    "http://127.0.0.1:5500/page2.html",
    "page2.html?foo=bar&ben=tall"
]

# normalize all these urls into a consistent format

for url in urls:
    if urlparse(url).netloc == urlparse(start_url).netloc:
        base = urlparse(start_url).netloc
    else:
        #
        pass
    print(urljoin(start_url, urlparse(url).path))


# webcrawler

response = requests.get(start_url)
print(response)




