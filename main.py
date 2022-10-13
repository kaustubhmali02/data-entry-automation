import requests
from bs4 import BeautifulSoup
from form import Form
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=m21ktnlnm6gj68tbprq6ksase2",
    "Dnt": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

response = requests.get(url=ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
property_card_address = soup.find_all(attrs={"data-test": "property-card-addr"})
property_card_prices = soup.find_all(name="span", attrs={"data-test": "property-card-price"})
property_card_links = soup.find_all(name="a", href=True, class_="property-card-link", attrs={"tabindex": "0"})


def add_host(link: str):
    if link[0] == "/":
        return link.replace(link, "https://www.zillow.com" + link)
    return link


# List of address, prices, links
addresses = [address.text for address in property_card_address]
prices = [price.text.strip("+ 1 bd").strip("+/mo") for price in property_card_prices]
links = [add_host(link['href']) for link in property_card_links]

form = Form()

for index in range(len(addresses)):
    form.add_address(addresses[index])
    form.add_price(prices[index])
    form.add_link(links[index])
    form.submit()
    time.sleep(2)
form.driver_quit()
