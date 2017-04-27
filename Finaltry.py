import requests
from Tkinter import Tk, StringVar
from Tkinter import *
import ttk
import json

root = Tk()
root.title("Currency Converter")
root.geometry('800x250+0+0')
root.configure (background='black')

Title=Label(root, text="Currency Converter")
Title.config(font=('century gothic',(25)),bg='yellow',width=0,relief=RAISED)
Title.pack(expand=1, anchor='center')

LeftMain=Frame(root, width=660, height=400, bd=8, relief="raise")
LeftMain.pack(side=LEFT)
RightMain=Frame(root, width=200, height=400, bd=8, relief="raise")
RightMain.pack(side=RIGHT)
DateofOrder = StringVar()
valueO = StringVar()
value1=StringVar()
convert = DoubleVar()
currency = DoubleVar()

EntCurrency= Entry(LeftMain,font=('arial',20,'bold'), textvariable=convert,bd=2,width=20, justify='center')
EntCurrency.grid(row=0,column=1)
# now we have the amount to be converted in the variable "convert"

box = ttk.Combobox (LeftMain, textvariable=valueO, state='randomly',font=('Arial',20,'bold'),width=20)
box['values'] = (' ', 'US Dollar', 'Indian Rupee', 'British Pound', 'European Euro', 'South African Rand', 'Hong Kong Dollar', 'Singapore Dollar', 'Thai Baht', 'Swiss Franc', 'Japanese Yen')
box.current(0)
box.grid(row=0, column=3)
# now we have the currency of the country FROM which we intend to convert in variable "valueO"

box = ttk.Combobox (LeftMain, textvariable=value1, state='randomly',font=('Arial',20,'bold'),width=20)
box['values'] =(' ', 'US Dollar', 'Indian Rupee', 'British Pound', 'European Euro', 'South African Rand', 'Hong Kong Dollar', 'Singapore Dollar', 'Thai Baht', 'Swiss Franc', 'Japanese Yen')
box.current(0)
box.grid(row=4, column=3)

#url = 'https://v3.exchangerate-api.com/pair/0590ded83b96e28eebc919b0/%s/%s' %(valueO,value1)

#response = requests.get(url)
#data = response.json()

#Rate=data['rate']
#Ans=Rate*convert

lblCurrency= Label (LeftMain, font=('arial',20,'bold'), textvariable=currency, bd=2, width=20, bg='white', pady=2, padx=2, relief='sunken')
lblCurrency.grid(row=4,column=1)

btnConvert = Button(RightMain, text='Convert', padx=2, pady=2, bd=2, fg="black",
                   font=('arial',20,'bold'), width=12, height=1).grid(row=1,column=0)


# now we have the currency of the country TO which we intend to convert in variable "value1"
# now make the API call with valueO and value1

# then get the rate in a variable, say y
# then, multiply rate with convert to calculate "currency"

#EntCurrency=Entry(LeftMain,font=('arial',20,'bold'), textvariable=currency,bd=2,width=20, justify='center')
#EntCurrency.grid(row=1,column=1)

root.mainloop()
