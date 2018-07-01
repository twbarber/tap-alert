import re
from bs4 import BeautifulSoup
from common.beer import Beer
from common import scraping_client

URL = 'https://untappd.com/v/downtown-city-tavern/601787'


def parse_name(soup):
    a_beer = soup.find(attrs={"data-href": ":beer"})
    regex = r"(\d.\s)"
    return re.sub(regex, '', str(a_beer.contents[0]))


def parse_brewery(soup):
    a_brewery = soup.find(attrs={"data-href": ":brewery"})
    return str(a_brewery.contents[0])


def parse_style(soup):
    return str(soup.em.contents[0])


def parse_abv(soup):
    return str(soup.h6.text.split('%')[0] + '%')


def get_menu():
    contents = scraping_client.get_html(URL, True)
    soup = BeautifulSoup(contents, 'html.parser')
    menu_html = soup.findAll("div", {"class": "beer-details"})

    menu = []

    for item in menu_html:
        item_soup = BeautifulSoup(str(item), 'html.parser')
        beer = Beer(
            parse_name(item_soup),
            parse_brewery(item_soup),
            parse_style(item_soup),
            parse_abv(item_soup)
        )
        menu.append(beer)

    return menu


def menu_as_sms():
    menu = get_menu()
    message = 'Downtown City Tavern - Glens Falls, NY\n\n'

    for i in menu:
        message += str(i.sms()) + '\n'

    return message.strip()
