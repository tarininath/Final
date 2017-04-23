import requests
import Tkinter

print('The Following Currencies are Supported')
print ('US Dollar: USD')
print ('Indian Rupee: INR')
print ('Pound Sterling: GBP')
print ('European Euro: EUR')
print ('South African Rand: ZAR')
print ('Hong Kong Dollar: HKD')
print ('Singapore Dollar: SGD')
print ('Thai Baht: THB')
print ('Swiss Franc: CHF')
print ('Japanse Yen: JPY')

x=0

while x<10:
    i=raw_input('Enter First Currency')
    s=raw_input('Enter Second Currency')
    t=input('Enter Amount to be converted')

    url = 'https://v3.exchangerate-api.com/pair/0590ded83b96e28eebc919b0/%s/%s' %(i,s)

    response = requests.get(url)
    data = response.json()

    y=data['rate']
    print y
    print y*t
    x+=1

