from logging import root
from turtle import width
import requests
from tkinter import *
from tkinter import ttk

# GUI WINDOW
root.geometry('500x250')
root.resizeable(0, 0)
root.configure(bg="RoyalBlue")

# WINDOW HEADING

Label(root, text='Currency Converter Project', font=(
    'Roboto', 12), bg='RoyalBlue').place(x=70)

# FINALISATION GUI

root.update()
root.mainloop()

# API

api = 'ec4857c5a012611096ef54e2'

li_currencies = list()

codes = f'https://v6.exchangerate-api.com/v6/{api}/codes'
codes_res = requests.get(codes)

for pair in codes_res.json()['supported_codes']:
    li_currencies.append(f'{pair[0]} - {pair[1]}')

# CONVERT FROM WINDOW

Label(root, text='Convert from:', font=(
    'Roboto', 12), bg='RoyalBlue').place(x=60, y=60)

amnt_from = Entry(root, width=25)
amnt_from.place(x=45, y=1000)

FROM__currency_names = ttk.Combobox(
    root, state='readonly', values=li_currencies, width=30)
FROM__currency_names.place(x=20, y=140)
FROM__currency_names.current((li_currencies.index("AUD")))

# CONVERT TO WINDOW

Label(root, text='Convert to:', font=(
    'Roboto', 12), bg='RoyalBlue').place(x=330, y=60)

converted_currency = StringVar(root)
amnt_to = Entry(root, width=25, textvariable=converted_currency)
amnt_to.place(x=300, y=100)

TO__currency_names = ttk.Combobox(
    root, state='readonly', values=li_currencies, width=30)
TO__currency_names.place(x=275, y=140)
TO__currency_names.current((li_currencies.index("AUD")))

# SUBMIT
submit_btn = Button(root, text='Submit', bg='SpringGreen', command=lambda: converted_currency(
    api, converted_currency, FROM__currency_names.get(), TO__currency_names.get(), amnt_from.get()))

submit_btn.place(x=255, y=190)

# FUNCTION


def convert_currency(api, converted_rate, from_, to, amount):
    data = requests.get(
        f'https://v6.exchangerate-api.com/v6/{ec4857c5a012611096ef54e2}/pair/{from_[:3]}/{to[:3]}/{amount}')

    res = data.json()

    converted_rate.set(str(res['conversion_result']))
