print('*'*6,'WELCOME TO THE SHOP','*'*6)
print()
#print()
print('*'*11,'INVENTORY','*'*11)

fruits=[]
quantity=[]
cost_price=[]
selling_price=[]

cart=[]
kgs=[]

sold_items = []
sold_kgs = []
sold_amount = []

customer_names = []
customer_phones = []
customer_bills = []
customer_purchases = [] 

while True:
    psw=input('Enter a password: ')
    if psw=='Lokesh':
        print('Access granted')
        #break
    else:
        print('Incorrect password')
        #break
        print('Try again')
        continue
    print('1.Owner')
    print('2.User')
    print('3.Exit')
    A=input('Enter a option: ')
    
#-----------------------OWNER SECTION-------------------------------#
    
    if A=="1":
        while True:
            print('--','OWNER SECTION','--')
            print('1.Add items')
            print('2.Remove items')
            print('3.Update items')
            print('4.View Inventory')
            print('5.Report')
            print('6.Customer_details')
            print('7.Exiting owner section' )

            B=int(input('Choose option: '))
            if B==1:
                fruit=input('Enter a fruit: ')
                qty=int(input('Enter a quantity: '))
                cp=int(input('Enter a cost price: '))
                sp=int(input('Enter a selling price: '))

                fruits.append(fruit)
                quantity.append(qty)
                cost_price.append(cp)
                selling_price.append(sp)
                print('Fruit is added successfully:',fruit)
                #break
            elif B==2:
                fruit = input('Enter a fruit to remove: ')
                if fruit in fruits:
                    idx = fruits.index(fruit)
                    fruits.pop(idx)
                    quantity.pop(idx)
                    cost_price.pop(idx)
                    selling_price.pop(idx)
                    print('Fruit is removed successfully:', fruit)
                else:
                    print('Fruit not found in inventory.')
            elif B==3:
                #while True:
                    item=input('Enter a fruit name: ')
                    if item in fruits:
                        idx=fruits.index(item)
                        qty=int(input('Enter a quantity: '))
                        cp=int(input('Enter a cost price: '))
                        sp=int(input('Enter a selling price: '))
                        quantity[idx]=qty
                        selling_price[idx]=sp
                        cost_price[idx]=cp
                        print('Item updated successfully:',item)
                    else:
                        print('Item is not in Inventory')
                        #break
                        #print(cost_price)
                
                
            elif B==4:
                print('*'*6,'FRUITS LIST','*'*6)
                if len(fruits) == 0:
                    print("No fruits in inventory.")
                else:
                    for i in zip(fruits,quantity,cost_price,selling_price):
                        print(i[0],'--',i[1],'kg -- CP:',i[2],'--SP:',i[3])

            elif B == 5:
                print('*' * 5, 'SALES REPORT', '*' * 5)
                if len(sold_items) == 0:
                    print("No sales yet.")
                else:
                    total_sales = 0
                    total_profit = 0
                    for i in range(len(sold_items)):
                        item = sold_items[i]
                        qty = sold_kgs[i]
                        amount = sold_amount[i]
                        idx = fruits.index(item)
                        cp = cost_price[idx]
                        sp = selling_price[idx]
                        profit = (sp - cp) * qty
                        total_sales += amount
                        total_profit += profit
                        print(f"{item} -- {qty}kg sold -- Rs.{amount} -- Profit: Rs.{profit}")
                    print("-" * 30)
                    print("Total Sales Amount:", total_sales)
                    print("Total Profit:", total_profit)

            elif B==6:
                print('*'*6,'CUSTOMER DETAILS','*'*6)
                if len(customer_names)==0:
                    print("No customers yet.")
                else:
                    for i in range(len(customer_names)):
                        print(f"\nCustomer: {customer_names[i]} | Phone: {customer_phones[i]}")
                        print("Items Bought:")
                        for item in customer_purchases[i]:
                            print(f"  - {item[0]}: {item[1]}kg x Rs.{item[2]} = Rs.{item[3]}")
                        print(f"Total Bill: Rs.{customer_bills[i]}")
                        print("-"*40)
                                  

            elif B==7:
                print('Exiting owner section')
                break
                    
                    
            else:
                print('Choose correct option')

#---------------------USER SECTION--------------------#   
    
    elif A=="2":

        print("-- Please enter your details --")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")

        customer_names.append(name)
        customer_phones.append(phone)

        while True:
            print('--','USER SECTION','--')
            print('1.Add cart')
            print('2.Remove cart')
            print('3.Modify cart')
            print('4.View cart')
            print('5.Billing')
            print('6.Exit')
            C=int(input('Enter a number: '))
            if C == 1:
                if len(fruits) == 0:
                    print("No fruits available in the shop right now.")
                    continue

                item = input('What do you want: ')
                q = int(input('How many kgs you want: '))

                if item in fruits:
                    idx = fruits.index(item)
                    if q <= quantity[idx]:
                        cart.append(item)
                        kgs.append(q)
                        print(item, 'is added to the cart')
                    else:
                        print('Not enough Stock:', item)
                else:
                    print(item, 'is not available')

                

            elif C==2:
                item=input('What do you want:')
                if item in cart:
                    idx = cart.index(item)
                    cart.pop(idx)
                    kgs.pop(idx)
                    print(item,'is removed from cart successfully')
                else:
                    print(item,'is not in cart')
                #else:
                    #print('Cart is empty')
            elif C==3:
                item=input('Enter a fruit name: ')
                if item in cart:
                    idx=cart.index(item)
                    new_qty=int(input('Enter a fruit quntity in kgs: '))
                    kgs[idx]=new_qty
                    print(item,'quantity updated to',new_qty,'kg')
                else:
                    print(item,'is not in cart.')
                    

            elif C == 4:
                print('*' * 6, 'CART LIST', '*' * 6)

                if len(cart) == 0:
                    print("Cart is empty")
                else:
                    for i in zip(cart, kgs):
                        print(">>", i[0], '--', i[1], "kg")

            elif C==5:
                if len(cart)==0:
                    print("Cart is empty! Add items first.")
                else:
                    print(">>"*3, "BILL", "<<"*3)
                    print(f"Customer: {name}")
                    print(f"Phone: {phone}")
                    print("-"*35)
                    total = 0
                    
                for i in range(len(cart)):
                    item = cart[i]
                    qty = kgs[i]
                    idx = fruits.index(item)
                    sp = selling_price[idx]
                    cost = qty * sp
                    print(f"{item} -- {qty}kg x {sp} = {cost}")
                    total += cost
                    if quantity[idx] >= qty:
                        quantity[idx] -= qty
                    else:
                        print(f"Not enough stock for {item}. Only {quantity[idx]}kg left.")
                    sold_items.append(item)
                    sold_kgs.append(qty)
                    sold_amount.append(cost)
                    customer_purchases.append((item, qty, sp, cost))

                print("-"*30)
                print("Total Amount to Pay:", total)
                print("-"*30)
                print('Thanks for shopping')

                cart.clear()
                kgs.clear()

            elif C==6:
                print('Exiting user section')
                break


            else:
                print('choose correct option')
                    
                    
    elif A=="3":
        print('Shop is closing')
        print('Thank you')
        print('Visit Again')
        break
    else:
        print('Choose correct option: ')
    
    
        
                    
                

