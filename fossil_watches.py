import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.fossil.com/us/en/men/watches/view-all.pageSize131.html")
soup = BeautifulSoup(r.content, 'html.parser')
i = 0
for result in soup.findAll("article"):
    print result.find('a', {"link-product-result-path text-ellipsis"}).text
    print result.find('span', {"text-price"}).text
    import ipdb;

    print result.find('img')['data-src']

print "total number of articles present on the website are ", i

