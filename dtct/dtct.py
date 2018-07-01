import re
import sys
import urllib.request
from bs4 import BeautifulSoup


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def normalize_beer_name(beer):
    regex = r"(\d.\s)"
    return re.sub(regex, '', str(beer.contents[0]))


def fetch_live_html(url):
    return AppURLopener().open(url).read()


def write_html_to_file(html):
    file = 'dtct.html'
    html_file = open(file, 'w')
    html_file.write(str(html))


def load_test_html():
    file = 'dtct.html'
    html_file = open(file, 'r')
    return html_file.read()


def get_html():
    if len(sys.argv) > 1 and sys.argv[1] == 'live':
        return fetch_live_html('https://untappd.com/v/downtown-city-tavern/601787')
    else:
        return load_test_html()


print(str(sys.argv))
contents = get_html()
soup = BeautifulSoup(contents, 'html.parser')
menu = soup.findAll("div", {"class": "beer-details"})

for item in menu:
    '''print(str(item))'''
    item_soup = BeautifulSoup(str(item), 'html.parser')
    a_beer = item_soup.find(attrs={"data-href": ":beer"})
    a_brewery = item_soup.find(attrs={"data-href": ":brewery"})

    print(normalize_beer_name(a_beer) + ' - ' + str(item.em.contents[0]) + ' - ' + str(a_brewery.contents[0]) + '\n')
