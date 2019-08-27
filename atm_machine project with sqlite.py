from tkinter import *
import sqlite3
db=sqlite3.connect('atm db')
obj1=db.cursor()
class ATM:
    def create(self):
        obj1.execute('create table if not exists atm(card_number INTEGER,name TEXT,pin INTEGER,balance INTEGER)')
#inseert your data if you want to add new data otherwise you can run this code with this data(19814,'ram',814,20000) 
        obj1.execute("insert into atm values(19814,'ram',814,50000)")
        obj1.execute('select *from atm')
        obj.first()
    def first(self):
        obj1.execute("select *from atm ")
        global line ,list1
        line=0
        list1=[]
        for line in obj1:
            list1.append(line)
        #print(list1)
    def withdrawl(self):
        global total_balance
        amount=int(input('enter amount'))
        if amount<balance:
            print('ok transaction succfully')
            print('you received ',amount)
            print('\n')
            total_balance=balance-amount
            obj.update()
            user1=input('do you want to check your balance yes/no ')
            if user1=='1':
               print('your total  balance is',total_balance)

        else:
                print('sorry your ancount has insufficient balance')

    def fast_cash(self):
            user2=input('choose anyone 100,200,500,1000,2000,5000,10000,20000,40000')
            global total_balance
            if user2=='1':
                 if data[3]>=100:
                     print('ok transaction succfully')
                     print('you received 100')
                     print('\n')
                     total_balance=balance-100
                     obj.update()
                     user21=input('do you want to check your balance yes/no ')
                     if user21=='1':
                         print('your total balance is ',total_balance)

                 else:
                        print('you have insufficient balance')
            elif user2=='2':
                 if data[3]>=200:
                     print('ok transaction succfully')
                     print('you received 200')
                     print('\n')
                     total_balance=balance-200
                     obj.update()
                     user22=input('do you want to check your balance yes/no ')
                     if user22=='1':
                         print('your total balance is ',total_balance)

                 else:
                         print('you have insufficient balance')
            elif user2=='3':
                 if data[3]>=500:
                     print('ok transaction succfully')
                     print('you received 500')
                     print('\n')
                     total_balance=balance-500
                     obj.update()
                     user23=input('do you want to check your balance yes/no ')
                     if user23=='1':

                        print('your total balance is ',total_balance)
                 else:
                     print('you have insufficient balance')
            elif user2=='4':
                 if data[3]>=1000:
                     print('ok transaction succfully')
                     print('you received 1000')
                     print('\n')
                     total_balance=balance-1000
                     obj.update()
                     user23=input('do you want to check your balance yes/no ')
                     if user23=='1':
                         print('your total balance is ',total_balance)

                 else:
                     print('you have insufficient balance')
            elif user2=='5':
                 if data[3]>=2000:
                     print('ok transaction succfully')
                     print('you received 2000')
                     print('\n')
                     total_balance=balance-2000
                     obj.update()

                     user23=input('do you want to check your balance yes/no ')
                     if user23=='1':
                         print('your total balance is ',total_balance)

                 else:
                     print('you have insufficient balance')

            elif user2=='6':
                 if 5000<=data[3]:
                     print('ok transaction succfully')
                     print('you received 5000')
                     print('\n')
                     total_balance=balance-5000
                     obj.update()

                     user23=input('do you want to check your balance yes/no ')
                     if user23=='1':
                         print('your total balance is ',total_balance)

                 else:
                     print('you have insufficient balance')


            elif user2=='7':
                  if data[3]>=10000:
                      print('ok transaction succfully')
                      print('you received 10000')
                      print('\n')
                      total_balance=balance-10000
                      obj.update()
                      user23=input('do you want to check your balance yes/no ')
                      if user23=='1':
                          print('your total balance is ',total_balance)
                  else:
                          print('you have insufficient balance')


            elif user2=='8':
                  if data[3]>=20000:
                      print('ok transaction succfully')
                      print('you received 20000')
                      print('\n')
                      total_balance=balance-20000
                      obj.update()
                      user23=input('do you want to check your balance yes/no ')
                      if user23=='1':

                           print('your total balance is ',total_balance)

                  else:
                          print('you have insufficient balance')


            elif user2=='9':
                  if data[3]>=40000:
                      print('ok transaction succfully')
                      print('you received 40000')
                      print('\n')
                      total_balance=balance-40000
                      obj.update()
                      user23=input('do you want to check your balance yes/no ')
                      if user23=='1':
                          print('your total balance is ',total_balance)

                  else:
                      print('you have insufficient balance')


    def exit(self):
          print('\n')
          print('thanx for visiting here')
    def deposit(self):
        global total_balance
        amount=int(input('enter your deposited amount'))
        print('\n')
        print('your transaction successfully')
        user23=input('do you want to check your balance yes/no ')
        if user23=='1':
            total_balance=balance+amount
            print('your total balace is ',total_balance)
    def balance_enquiry(self):
        global balance
        print( 'your total balance is',balance)
    def pin_change(self):
        global new_pin
        new_pin=int(input('enter your  new pin'))
        sqll='update atm set pin=? where pin=?'
        val=[new_pin,data[2]]
        obj1.execute(sqll,val)
        db.commit()
        print('congatulation your pin is succesfully changeed')
    def update(self):
        global total_balance
        sqll='update atm set balance=? where name=?'
        val=[total_balance,data[1]]
        obj1.execute(sqll,val)
        db.commit()




    def start(self):
        global balance,data
        global total_balance,card_number,pin
        card_number=int(input('enter your card number '))
        pin=int(input('enter your pin'))
        for data in list1:
            pass
        print(data[2])
        if card_number in data and pin in data:
                print(f'welcome {data[1]} in our ATM')
                user0=input("choose anyone :withdrawl / fast_cash/ deposit/ balance_enquiry/pin_change ")
                balance=data[3]
                name=data[1]
                if user0=='1':
                     obj.withdrawl()
                elif user0=='2':
                        obj.fast_cash()
                elif user0=='3':
                     obj.deposit()
                     obj.update()

                elif user0=='4':
                     obj.balance_enquiry()
                elif user0=='5':
                    obj.pin_change()
                else:
                     obj.exit()

        else:
                print('your card number or pin is not valid')
                obj.exit()
obj=ATM()
obj.create()
obj.start()
db.close()
