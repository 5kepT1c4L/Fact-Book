from bs4 import BeautifulSoup
import requests
from tkinter import *

fact_list = []

info_website = requests.get('https://bestlifeonline.com/useless-facts/').text

soup = BeautifulSoup(info_website, 'lxml')

facts = soup.find_all('h2', class_ = "header-mod")

for fact in facts:

    the_fact = fact.find('div', class_ = "title").text.replace(".", "")

    fact_list.append(the_fact)


print(fact_list)d



tk = Tk()
tk.title('Fact Book')
tk.geometry('500x500')
tk.configure(bg="pink")