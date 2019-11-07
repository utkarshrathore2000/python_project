import mysql.connector
import datetime
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='super_market')
obj=db.cursor()
class market:
    def __init__(self):
        obj.execute('select *from costumer')
        global list1
        list1=[]
        for line in obj:
            list1.append(line)

    def kirana_store(self):
        obj.execute('select *from kirana_store')
        list1=[]
        for line in obj:
            list1.append(line)
        user=input('hello dear what do you want from here  dal/rice/oil/mungwali')
        global td
        if user=='dal':
            for data in list1:
                if user in data:
                    how_much=int(input('how much dal you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update kirana_store set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update kirana_store set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_dal=data[4]+td
                        sql2='update kirana_store set income=%s where product_name=%s'
                        val2=[total_income_dal,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'dal',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} kg dal your total amount is {td} ')
                        obj1.mall_kirana_store()
                        
        elif user=='rice':
            for data in list1:
                if user in data:
                    how_much=int(input('how much rice you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update kirana_store set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update kirana_store set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_rice=data[4]+td
                        sql2='update kirana_store set income=%s where product_name=%s'
                        val2=[total_income_rice,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'rice',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} kg rice your total amount is {td} ')
                        obj1.mall_kirana_store()
        elif user=='mungwali':
            for data in list1:
                if user in data:
                    how_much=int(input('how much mungwali you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update kirana_store set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update kirana_store set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_rice=data[4]+td
                        sql2='update kirana_store set income=%s where product_name=%s'
                        val2=[total_income_mungwali,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'mungwali',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        db.commit()
                        print(f'you purchases {how_much} kg mungwali your total amount is {td} ')
                        obj1.mall_kirana_store()
        elif user=='oil':
            for data in list1:
                if user in data:
                    how_much=int(input('how much oil you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update kirana_store set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update kirana_store set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_oil=data[4]+td
                        sql2='update kirana_store set income=%s where product_name=%s'
                        val2=[total_income_oil,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'oil',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} litre oil your total amount is {td} ')
                        obj1.mall_kirana_store()
        else:
            print("sorry we don't have this")
    def mall_kirana_store(self):
       global td
       obj.execute('select *from mall')
       list2=[]
       for line1 in obj:
            list2.append(line1)
       user='kirana_store'
       for data1 in list2:
            if user in data1:
                total_income=data1[3]
                total_income+=td
                sql20='update mall set earn_money=%s where shop_name=%s'
                val21=[total_income,data1[0]]
                obj.execute(sql20,val21)
                db.commit()
    def mobile_shop(self):
        obj.execute('select *from mobile_shop')
        list1=[]
        for line in obj:
            list1.append(line)
        user=input('hello dear what do you want from here  iphone/oneplus/redmi/samsung')
        global td
        if user=='oneplus':
            for data in list1:
                if user in data:
                    how_much=int(input('how much oneplus you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update mobile_shop set quantity=%s where mobile_brand=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update mobile_shop set sell=%s where mobile_brand=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_oneplus=data[4]+td
                        sql2='update mobile_shop set income=%s where mobile_brand=%s'
                        val2=[total_income_oneplus,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'oneplus',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        db.commit()
                        print(f'you purchases {how_much} mobile_phone   your total amount is {td} ')
                        obj1.mall_mobile_shop()
        elif user=='iphone':
            for data in list1:
                if user in data:
                    how_much=int(input('how much  iphone you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update mobile_shop set quantity=%s where mobile_brand=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update mobile_shop set sell=%s where mobile_brand=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_iphone=data[4]+td
                        sql2='update mobile_shop set income=%s where mobile_brand=%s'
                        val2=[total_income_iphone,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'iphone',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} mobile_phone   your total amount is {td} ')
                        obj1.mall_mobile_shop()
        elif user=='samsung':
            for data in list1:
                if user in data:
                    how_much=int(input('how much samsung you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update mobile_shop set quantity=%s where mobile_brand=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update mobile_shop set sell=%s where mobile_brand=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_samsung=data[4]+td
                        sql2='update mobile_shop set income=%s where mobile_brand=%s'
                        val2=[total_income_samsung,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'samsung',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} mobile_phone   your total amount is {td} ')
                        obj1.mall_mobile_shop()
        elif user=='redmi':
            for data in list1:
                if user in data:
                    how_much=int(input('how much redmi you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update mobile_shop set quantity=%s where mobile_brand=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update mobile_shop set sell=%s where mobile_brand=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_redmi=data[4]+td
                        sql2='update mobile_shop set income=%s where mobile_brand=%s'
                        val2=[total_income_redmi,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'redmi',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} mobile_phone   your total amount is {td} ')
                        
                        obj1.mall_mobile_shop()
        else:
            print("sorry we don't have this")
    def mall_mobile_shop(self):
       global td
       obj.execute('select *from mall')
       list2=[]
       for line1 in obj:
            list2.append(line1)
       user='mobile_shop'
       for data1 in list2:
            if user in data1:
                total_income=data1[3]
                total_income+=td
                sql20='update mall set earn_money=%s where shop_name=%s'
                val21=[total_income,data1[0]]
                obj.execute(sql20,val21)
                db.commit()
    def restaurent(self):           
        obj.execute('select *from restaurent')
        list1=[]
        for line in obj:
            list1.append(line)
        user=input('hello dear what do you want from here  jalebi/kachori/pattize/samosa')
        global td
        if user=='jalebi':
            for data in list1:
                if user in data:
                    how_much=int(input('how much jalebi you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update restaurent set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update restaurent set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_jalebi=data[4]+td
                        sql2='update restaurent set income=%s where product_name=%s'
                        val2=[total_income_jalebi,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'jalebi',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} plate jalebi   your total amount is {td} ')
                        obj1.mall_restaurent()
        elif user=='kachori':
            for data in list1:
                if user in data:
                    how_much=int(input('how much kachori you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update restaurent set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update restaurent set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_iphone=data[4]+td
                        sql2='update restaurent  set income=%s where product_name=%s'
                        val2=[total_income_iphone,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'kachori',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} kachori  your total amount is {td} ')
                        obj1.mall_restaurent()
        elif user=='samosa':
            for data in list1:
                if user in data:
                    how_much=int(input('how much samosa you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update restaurent set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update restaurent set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_samsung=data[4]+td
                        sql2='update restaurent set income=%s where product_name=%s'
                        val2=[total_income_samsung,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'samosa',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} samosa   your total amount is {td} ')
                        obj1.mall_restaurent()
        elif user=='pattize':
            for data in list1:
                if user in data:
                    how_much=int(input('how much pattize you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update restaurent set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update restaurent set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_redmi=data[4]+td
                        sql2='update restaurent set income=%s where product_name=%s'
                        val2=[total_income_redmi,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'pattizze',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} pattize   your total amount is {td} ')
                        obj1.mall_restaurent()
        else:
            print("sorry we don't have this")
    def mall_restaurent(self):
       global td
       obj.execute('select *from mall')
       list2=[]
       for line1 in obj:
            list2.append(line1)
       user='restaurent'
       for data1 in list2:
            if user in data1:
                total_income=data1[3]
                total_income+=td
                sql20='update mall set earn_money=%s where shop_name=%s'
                val21=[total_income,data1[0]]
                obj.execute(sql20,val21)
                db.commit()
    def cloth_shop(self):           
        obj.execute('select *from cloth_shop')
        list1=[]
        for line in obj:
            list1.append(line)
        user=input('hello dear what do you want from here  armani/berberry/chanel/fendi')
        global td
        if user=='armani':
            for data in list1:
                if user in data:
                    how_much=int(input('how much armani you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update cloth_shop set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update cloth_shop set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_armani=data[4]+td
                        sql2='update restaurent set income=%s where product_name=%s'
                        val2=[total_income_armani,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'armani',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} armani cloth   your total amount is {td} ')
                        obj1.mall_cloth_shop()
        elif user=='berberry':
            for data in list1:
                if user in data:
                    how_much=int(input('how much berberry you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update cloth_shop set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update cloth_shop set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_berberry=data[4]+td
                        sql2='update cloth_shop set income=%s where product_name=%s'
                        val2=[total_income_berberry,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'berberry',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} berberry cloth   your total amount is {td} ')
                        obj1.mall_cloth_shop()
        elif user=='chanel':
            for data in list1:
                if user in data:
                    how_much=int(input('how much chanel you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update cloth_shop set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update cloth_shop set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_chanel=data[4]+td
                        sql2='update cloth_shop set income=%s where product_name=%s'
                        val2=[total_income_chanel,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'chanel',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} chanel cloth   your total amount is {td} ')
                        obj1.mall_cloth_shop()
        elif user=='fendi':
            for data in list1:
                if user in data:
                    how_much=int(input('how much fendi you want'))
                    if data[2]>how_much:
                        total_quantity=data[2]-how_much                                  
                        sql='update cloth_shop set quantity=%s where product_name=%s'
                        val=[total_quantity,data[0]]
                        obj.execute(sql,val)
                        db.commit()
                        how_much1=how_much+data[3]
                        sql1='update cloth_shop set sell=%s where product_name=%s'
                        val1=[how_much1,data[0]]
                        obj.execute(sql1,val1)
                        db.commit()
                        td=how_much*data[1]
                        total_income_fendi=data[4]+td
                        sql2='update cloth_shop set income=%s where product_name=%s'
                        val2=[total_income_fendi,data[0]]
                        obj.execute(sql2,val2)
                        db.commit()
                        currentdate=datetime.datetime.now()
                        sql="insert into costumer_shopping_detailed(costumer_name,c_p_name,c_p_quantity,c_p_price,c_s_date) values (%s,%s,%s,%s,%s)"
                        val=[data0[0],'fendi',how_much,td,currentdate]
                        obj.execute(sql,val)
                        db.commit()
                        print(f'you purchases {how_much} fendi cloth   your total amount is {td} ')
                        obj1.mall_cloth_shop()
        else:
            print("sorry we don't have this")
    def mall_cloth_shop(self):
       global td
       obj.execute('select *from mall')
       list2=[]
       for line1 in obj:
            list2.append(line1)
       user='cloth_shop'
       for data1 in list2:
            if user in data1:
                total_income=data1[3]
                total_income+=td
                sql20='update mall set earn_money=%s where shop_name=%s'
                val21=[total_income,data1[0]]
                obj.execute(sql20,val21)
                db.commit()
obj1=market()
list2=[]
user=input('are you come here for first time yes/no')
if user=='2':
    costumer_id=int(input('sir please enter your costumer_id'))
    for data0 in list1:
        if costumer_id in data0:
                    print(f'hello mr/miss {data0[0]} welcome to our mall')
                    user01=input('what type of shopping you would like to do there are  have four type of shop in our mall kirana_store/mobile_shop/restaurent/cloth_shop')
                    if user01=='1':
                        obj1.kirana_store()
                        break
                    elif user01=='2':
                        obj1.mobile_shop()
                        break
                    elif user01=='3':
                        obj1.restaurent()
                        break
                    elif user01=='4':
                        obj1.cloth_shop()
                        break
                    else:
                        print('sorry sir this shop is not in our mall')
                        break
    else:
                print('sorry your id is wrong')
elif user=='1':
            user1=input('first you would have to registered here after that you can start shopping in our mall are you interested or not yes/no')
            if user1=='1':
                global name
                name=input(' please tell  your name')
                sql=("insert into costumer(costumer_name) values(%s) ")
                val=[name]
                obj.execute(sql,val)
                db.commit()
                obj.execute('select *from costumer')
                for line in obj:
                    list2.append(line)
                for data1 in list2:
                    if name in data1:
                        print(f"thanx mr/miss.{name} now you are a costumer of our mall  you'r id is {data1[1]}")
            else:
                print('ok')
