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


print(fact_list)



tk = Tk()
tk.title('Fact Book')
tk.geometry('500x498')
tk.configure(bg="white")


#Frame to store the fact
fact_frame = Frame(tk, highlightbackground="blue", highlightthickness=1,width=500, height=380, bd= 0, bg='light green')
fact_frame.pack(expand=True)
fact_frame.pack_propagate(False)


#Frame to store the buttons
button_frame = Frame(tk, highlightbackground="blue", highlightthickness=1,width=500, height=120, bd= 0, bg='pink')
button_frame.pack()
button_frame.pack_propagate(False)


#Buttons
back_button = Button(button_frame, text="<<", width=20, height=7)
back_button.grid(row=0, column=0, padx=3)

exit_button = Button(button_frame, text="EXIT", width=27, height=7)
exit_button.grid(row=0, column=1)

forward_button = Button(button_frame, text=">>", width=20, height=7)
forward_button.grid(row=0, column=2, padx=3)



fact_label = Label(fact_frame, text=fact_list[20], font = ('Times', 15))
fact_label.place(x=100, y=150)

tk.mainloop()
