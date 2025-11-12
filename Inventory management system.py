# DATABASE OF FRUITS
fruits = []
quantity = []
price = []
cost_price = []

# TO STORE CUSTOMER DATA
customer_name = []
customer_mobile = []  
cart = []
cart_qty = []
cart_amt = []
sold_item = []
sold_qty = []
sold_amt = []

# TO STORE PURCHASE HISTORY (for reports)
purchased_cust = []
purchased_mobile = []  
purchased_cart = []
purchased_qty = []
purchased_amt = []
purchased_total = []

# STARTING THE FRUIT MARKET
while True:
    print('*' * 10, 'FRUIT MARKET', '*' * 10)
    print('1.OWNER')
    print('2.CUSTOMER')
    print('3.EXIT')

    Role = input('Enter your role (1, 2, 3): ').lower()

    # ---------------------- OWNER SECTION ---------------------- #
    if Role == '1':
        password = input('Enter the password: ')
        if password != 'Lokesh':
            print('Incorrect password')
            print('Access denied')
            continue

        while True:
            print('\nOWNER SECTION')
            print('1.Add items')
            print('2.Remove items')
            print('3.Update items')
            print('4.View Inventory')
            print('5.View Customer Details')
            print('6.View Sales Report')
            print('7.Item Wise Profit')
            print('8.Total Profit')
            print('9.Exit')

            ch = input('Enter your choice: ')

            # ADD FRUIT
            if ch == '1':
                item = input('Enter fruit name: ').lower()
                qty = float(input('Enter quantity in Kgs: '))
                sp = float(input('Enter selling price per Kg: '))
                cp = float(input('Enter cost price per Kg: '))
                fruits.append(item)
                quantity.append(qty)
                price.append(sp)
                cost_price.append(cp)
                print(item, 'added successfully to inventory.')

            # REMOVE FRUIT
            elif ch == '2':
                item = input('Enter fruit name to remove: ').lower()
                if item in fruits:
                    idx = fruits.index(item)
                    fruits.pop(idx)
                    quantity.pop(idx)
                    price.pop(idx)
                    cost_price.pop(idx)
                    print(item, 'removed successfully from inventory.')
                else:
                    print(item, 'not found in inventory.')

            # UPDATE FRUIT
            elif ch == '3':
                item = input('Enter fruit name to update: ').lower()
                if item in fruits:
                    idx = fruits.index(item)
                    qty = float(input('Enter new quantity (in Kgs): '))
                    sp = float(input('Enter new selling price per Kg: '))
                    cp = float(input('Enter new cost price per Kg: '))
                    quantity[idx] = qty
                    price[idx] = sp
                    cost_price[idx] = cp
                    print(item, 'updated successfully.')
                else:
                    print(item, 'not found in inventory.')

            # VIEW INVENTORY
            elif ch == '4':
                print('*' * 10, 'INVENTORY REPORT', '*' * 10)
                if len(fruits) == 0:
                    print('No fruits available.')
                else:
                    for report in zip(fruits, quantity, price, cost_price):
                        print(f"{report[0]} -- {report[1]}Kg -- SP: Rs.{report[2]} -- CP: Rs.{report[3]}")

            # VIEW CUSTOMER DETAILS
            elif ch == '5':
                print('*' * 10, 'CUSTOMER DETAILS', '*' * 10)
                if len(purchased_cust) == 0:
                    print('No customers yet.')
                else:
                    for i in range(len(purchased_cust)):
                        print(f"\nCustomer Name : {purchased_cust[i].title()}")
                        print(f"Mobile Number : {purchased_mobile[i]}")
                        for j in range(len(purchased_cart[i])):
                            print(purchased_cart[i][j], '--', purchased_qty[i][j], 'Kgs --', purchased_amt[i][j], 'Rs')
                        print('Total Bill :', purchased_total[i], 'Rs')

            # SALES REPORT
            elif ch == '6':
                print('*' * 10, 'SALES REPORT', '*' * 10)
                if len(sold_item) == 0:
                    print('No sales yet.')
                else:
                    for sale in zip(sold_item, sold_qty, sold_amt):
                        print(sale[0], '--', sale[1], 'Kgs -- Rs.', sale[2])
                    print('Total sales amount:', sum(sold_amt), 'Rs')

            # ITEM-WISE PROFIT
            elif ch == '7':
                print('*' * 10, 'ITEM-WISE PROFIT', '*' * 10)
                if len(sold_item) == 0:
                    print('No sales yet.')
                else:
                    total_profit = 0
                    for i in range(len(fruits)):
                        item = fruits[i]
                        qty = 0
                        for j in range(len(sold_item)):
                            if sold_item[j] == item:
                                qty += sold_qty[j]
                        if qty > 0:
                            profit = (price[i] - cost_price[i]) * qty
                            print(item, '--', qty, 'Kgs -- Profit:', profit, 'Rs')
                            total_profit += profit
                    print('Total Profit:', total_profit, 'Rs')

            # TOTAL PROFIT
            elif ch == '8':
                print('*' * 10, 'TOTAL PROFIT', '*' * 10)
                total_profit = 0
                for i in range(len(sold_item)):
                    item = sold_item[i]
                    if item in fruits:
                        idx = fruits.index(item)
                        profit = (price[idx] - cost_price[idx]) * sold_qty[i]
                        total_profit += profit
                print('Overall Profit:', total_profit, 'Rs')

            # EXIT OWNER SECTION
            elif ch == '9':
                print('Exiting Owner Section...')
                break

            else:
                print('Invalid Input!')

    # ---------------------- CUSTOMER SECTION ---------------------- #
    elif Role == '2':
        name = input('Enter your name: ').lower()
        mobile = input('Enter your mobile number: ') 
        # Avoid duplicate customer entries
        if mobile in customer_mobile:
            print('This mobile number is already registered. Please use a different one.')
            continue

        customer_name.append(name)
        customer_mobile.append(mobile)

        while True:
            print('\nCUSTOMER SECTION')
            print('1.View Fruits')
            print('2.Add to Cart')
            print('3.Remove from Cart')
            print('4.Modify Cart')
            print('5.View Cart')
            print('6.Billing')
            print('7.Exit')

            ch = input('Enter your choice: ')

            # VIEW FRUITS
            if ch == '1':
                print('*' * 10, 'AVAILABLE FRUITS', '*' * 10)
                if len(fruits) == 0:
                    print('No fruits available.')
                else:
                    for item in zip(fruits, quantity, price):
                        print(item[0], '--', item[1], 'Kgs -- Rs.', item[2])

            # ADD TO CART
            elif ch == '2':
                item = input('Enter fruit name: ').lower()
                if item in fruits:
                    qty = float(input('Enter quantity (in Kgs): '))
                    idx = fruits.index(item)
                    if qty <= quantity[idx]:
                        cart.append(item)
                        cart_qty.append(qty)
                        amt = qty * price[idx]
                        cart_amt.append(amt)
                        print(item, 'added to cart. Amount:', amt, 'Rs')
                    else:
                        print('Only', quantity[idx], 'Kgs available.')
                else:
                    print(item, 'not available.')

            # REMOVE FROM CART
            elif ch == '3':
                item = input('Enter fruit name to remove: ').lower()
                if item in cart:
                    idx = cart.index(item)
                    cart.pop(idx)
                    cart_qty.pop(idx)
                    cart_amt.pop(idx)
                    print(item, 'removed successfully.')
                else:
                    print(item, 'not in cart.')

            # MODIFY CART
            elif ch == '4':
                item = input('Enter fruit name to modify: ').lower()
                if item in cart:
                    idx = cart.index(item)
                    qty = float(input('Enter new quantity (in Kgs): '))
                    price_idx = fruits.index(item)
                    cart_qty[idx] = qty
                    cart_amt[idx] = qty * price[price_idx]
                    print(item, 'updated successfully.')
                else:
                    print(item, 'not found in cart.')

            # VIEW CART
            elif ch == '5':
                print('*' * 10, 'CART ITEMS', '*' * 10)
                if len(cart) == 0:
                    print('Cart is empty.')
                else:
                    for c in zip(cart, cart_qty, cart_amt):
                        print(c[0], '--', c[1], 'Kgs -- Rs.', c[2])

            # BILLING
            elif ch == '6':
                print('*' * 10, 'BILLING', '*' * 10)
                if len(cart) == 0:
                    print('Cart is empty.')
                else:
                    total = sum(cart_amt)
                    print(f"Customer Name: {name.title()}")
                    print(f"Mobile Number: {mobile}")
                    print('-' * 30)
                    for c in zip(cart, cart_qty, cart_amt):
                        print(c[0], '--', c[1], 'Kgs -- Rs.', c[2])

                        vidx = fruits.index(c[0])
                        quantity[vidx] -= c[1]

                        sold_item.append(c[0])
                        sold_qty.append(c[1])
                        sold_amt.append(c[2])

                    print('-' * 30)
                    print('Total Amount:', total, 'Rs')
                    print('Thanks for shopping!')

                    purchased_cust.append(name)
                    purchased_mobile.append(mobile)
                    purchased_cart.append(cart.copy())
                    purchased_qty.append(cart_qty.copy())
                    purchased_amt.append(cart_amt.copy())
                    purchased_total.append(total)

                    cart.clear()
                    cart_qty.clear()
                    cart_amt.clear()

            # EXIT CUSTOMER SECTION
            elif ch == '7':
                print('Exiting Customer Section...')
                break

            else:
                print('Invalid Input!')

    # ---------------------- EXIT MARKET ---------------------- #
    elif Role == '3':
        print('Thank you for visiting the Fruit Market!')
        print('Please come again!')
        break

    else:
        print('Invalid Input! Please enter 1, 2, or 3.')
