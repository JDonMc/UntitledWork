from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Which page would you like to check? Enter Full URL: ")
keyword = input("What is your SEO keyword? ")

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)

data = BeautifulSoup(html, "html.parser")


def seo_title(keyword, data):

    if keyword.casefold() in data.title.text.casefold():
        status = "Found"
    else:
        status = "Not Found"

    return status

print(seo_title(keyword, data))
