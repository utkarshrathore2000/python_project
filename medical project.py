import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='shop')
obj=db.cursor()
class medical_shop:
    def __init__(self):
        obj.execute("select *from medical ")
        global line ,list1
        line=0
        list1=[]
        for line in obj:
            list1.append(line)
   
    def shop(self):
                sqll='select *from medical where name= %s'
                val=[user]
                obj.execute(sqll,val)
                for i in obj:
                        print(i)
    def m_quantity(self):
             sqll="update medical set quantity=%s where name=%s"
             val=[total,data[0]]
             obj.execute(sqll,val)
             db.commit()
    def income(self):
             sqll1="update medical set income=%s where name=%s"
             val1=[payment,data[0]]
             obj.execute(sqll1,val1)
             db.commit()
    def whole(self):
             sqll2="update medical set quantity=%s where name=%s"
             val2=[total,data[0]]
             obj.execute(sqll2,val2)
             db.commit()
    def totals(self):
                sqll3="select * from medical"
                obj.execute(sqll3)
                tot=0
                for i in obj:
                    tot+=(i[4])
                print(f'your total income is {tot}')
   
        
            
             
obj1=medical_shop()
user=input('hello sir what type of  medicine you want')
for data in list1:
        if user  in data:
                obj1.shop()
                how_much=int(input('sir how much medicine you should'))
                if data[3]>how_much:
                        total=data[3]-how_much
                        payment=data[4]+(data[1]*how_much)
                        obj1.m_quantity()
                        obj1.income()
                        obj1.totals()
                        print('thanx sir for visiting here')
                        break
                        
                else:
                        print(f' sorry sir we only have {data[3]} medicine')
                        whole_saler=input('dear shopkepper  do you wants to some medicine  yes/no')
                        if whole_saler=='yes':
                                how_much=int(input('how much medicine'))
                                total=how_much+data[3]
                                obj1.whole()
                                print('thanku dear wholesaler')
                        break
else:
    print("sorry sir we don't have")
    


