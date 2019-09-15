with open('currency data') as f:
    lines=f.readlines()
    currency_dict={}
    for line in lines:
        parsed=line.split('\t')
        currency_dict[parsed[0]]=parsed[1]

amount=int(input('enter the amount you want to convert = '))
for items in currency_dict.keys():
    print(items)
currency=input('choose any one values to convert = ')
print(f'{amount}INR is  equal to {amount*float(currency_dict[currency])}')
