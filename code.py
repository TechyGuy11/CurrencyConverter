from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

bg = '#272727'
fg = '#ECE6DB'

# Getting list
response = requests.get(
    'https://v6.exchangerate-api.com/v6/f685bd91d04226253133a16b/latest/AED')
response = response.json()
response = response.get('conversion_rates')
response = list(response.keys())

# Defining window
root = Tk()
root.geometry('500x300')
root.configure(bg=bg)
root.resizable(False, False)

def convert_currency():
    currency = currencyFromMoney.get()
    x1 = clicked.get().upper()
    x2 = clicked2.get().upper()
    try:
        showLabel.config(text=float(currency) * float(requests.get(
            'https://v6.exchangerate-api.com/v6/f685bd91d04226253133a16b/latest/' + x1).json().get('conversion_rates').get(x2)))
    except ValueError:
        messagebox.showwarning(
            title='Error', message='Please enter a valid number')


print('App Started')

# Adding clicking values
clicked = StringVar()
clicked2 = StringVar()
clicked.set('AED')
clicked2.set('AED')

# Heading
heading = Label(root, text='Currency Converter', bg=bg, fg=fg,
                font=('Helvetica', 18, 'bold')).place(x=140, y=30)

# From currency
currencyFrom = ttk.Combobox(root, textvariable=clicked, value=response)
currencyFrom.place(x=60, y=100)

# To currency
currencyTo = ttk.Combobox(root, textvariable=clicked2, value=response)
currencyTo.place(x=310, y=100)

# 'to' text
to = Label(root, text='to', bg=bg, fg=fg, font=(
    'Helvetica', 12, 'bold')).place(x=240, y=115)

# From money input
currencyFromMoney = ttk.Entry(root, width=23)
currencyFromMoney.place(x=60, y=130)

# Convert now button
convertNow = Button(root, text='Convert', font=('Helvetica', 12, 'bold'), height=2, width=10,
                    command=convert_currency).place(x=200, y=190)

showLabel = Label(root, text='', bg=bg, fg=fg, font=('Helvetica', 12, 'bold'))
showLabel.place(x=310, y=126)

root.title('Currency Converter')

# Title and show loop
root.mainloop()
