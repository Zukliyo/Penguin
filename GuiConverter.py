from tkinter import *
import requests
from bs4 import BeautifulSoup
import html5lib

def getter():
  url = "http://www.tbcbank.ge/web/ka/web/guest/exchange-rates"
  response = requests.get(url)
  content = BeautifulSoup(response.content, 'html5lib')
  div = content.find_all('div', attrs={'class': 'currency rounded-corners'})
  global keys
  global values
  global sorted_values
  keys = [
    'USD',
    'EUR',
    'GBP'
  ]
  values= []
  sorted_values = []

  for text in div:
    text = text.text
    text = text.split()
    values.append(text)


def setter():
  getter()
  for i in range(0,3):
    c= values[i]

    str_values = ' '.join(c[0:3])
    str_values_currency = ''.join(c[3])
    str_values+= ': ' + str_values_currency
    sell = ''.join(c[7]+': '+c[8])
    buy = ''.join(c[9]+': '+c[10])

    sorted_values.append([str_values,sell,buy])

  currency = dict(zip(keys,sorted_values))
  print(currency)


def converter():
  getter()
  global usd_rate
  global eur_rate
  global gbp_rate
  usd_rate= float(values[0][3])
  eur_rate= float(values[1][3])
  gbp_rate= float(values[2][3])


def get_usd():
    converter()
    global inpt
    number=inpt.get()

    if number != '':

        try:
            float(number)
            convertation = round(float(number) * usd_rate, 2)
            info.configure(text=f'{number} GEL  >>  {convertation} USD')

        except ValueError:
            info.configure(text='Please enter integer or float')
    else:
        convertation = round(1 * usd_rate, 2)
        info.configure(text=f'1 GEL  >>  {convertation} USD ')

    root.update()


def get_eur():
    global inpt
    number = inpt.get()

    if number != '':

        try:
            float(number)
            convertation = round(float(number) * eur_rate, 2)
            info.configure(text=f'{number} GEL  >>  {convertation} EUR')

        except ValueError:
            info.configure(text='Please enter integer or float')
    else:
        convertation = round(1 * eur_rate, 2)
        info.configure(text=f'1 GEL  >>  {convertation} EUR')
    root.update()


def get_gbp():
    global inpt
    number = inpt.get()

    if number != '':

        try:
            float(number)
            convertation = round(float(number) * gbp_rate, 2)
            info.configure(text=f'{number} GEL  >>  {convertation} GBP')

        except ValueError:
            info.configure(text='Please enter integer or float')
    else:
        convertation = round(1 * gbp_rate, 2)
        info.configure(text=f'1 GEL  >>  {convertation} GBP')
    root.update()


root=Tk()
root.geometry('400x200')
Label(root, text='GEL amount ', heigh=1, width=10).grid(row=0)
inpt=Entry(root, width=35)
inpt.grid(row=0, column=1)
info=Label(root,text='', heigh=1)
info.grid(row=5, column=1)
get_USD=Button(root,text='Convert to USD (Dollar)', width=23, command=get_usd)
get_USD.grid(row=2, column=1)
get_EUR=Button(root,text='Convert to EUR (Euro)', width=23, command=get_eur)
get_EUR.grid(row=3, column=1)
get_GBP=Button(root,text='Convert to GBP (British pound)', width=23, command=get_gbp)
get_GBP.grid(row=4, column=1)
mainloop()
