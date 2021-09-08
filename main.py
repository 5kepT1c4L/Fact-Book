from bs4 import BeautifulSoup
import requests

info_website = requests.get('https://bestlifeonline.com/useless-facts/').text

soup = BeautifulSoup(info_website, 'lxml')

facts = soup.find_all('h2', class_ = "header-mod")

for fact in facts:

    the_fact = fact.find('div', class_ = "title").text

    print(the_fact)

