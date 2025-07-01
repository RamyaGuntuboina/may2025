# Generate grocery imvoice

print("---------Thanks for choosing Ramya SuperMaerket----------")
name = input("Enter your name: ")

list = '''
Mango     Rs 100/Box
Nuts      Rs 300/Box
Sugar     Rs 40/Kg
Milk      Rs 30/Bottle
Honey     Rs 50/Bottle
Rice      Rs 50/Kg
'''
items = {'mango': '100', 'nuts':'300', 'sugar':'40', 'milk': '30', 'honey': '50', 'rice':'50'}

price = 0
pricelist = []
finalprice = 0
totalprice = 0
itemlist = []
quantitylist = []
pricelist = []


while True:
    option1 = int(input("Press 1 for the list or 2 to exit: ")) 
    if option1 == 1:
        print(list)
        while True:
            option2 = int(input("Press 1 to buy or 2 to exit: "))
            if option2 == 2:
                if itemlist:
                    print("Thank you for choosing us. Please find the final bill")
                    print("==================Ramya Super Market====================")
                    print("----------------------Hyderabad-------------------------")
                    print(f"Name: {name}")
                    print("--------------------------------------------------------")
                    print("Sno.\tItems\tQuantity\tPrice")
                    for i in range(len(pricelist)):
                      item, quantity, rate, price = pricelist[i]
                      print(f"{i+1}\t{item}\t{quantity}\t\t{price}")
                    print("--------------------------------------------------------")
                    discount = totalprice * 0.05
                    finalprice = totalprice - discount
                    print(f"{'Total':}\t\t\t\t\t{'Rs'} {totalprice}")
                    print(f"{'Discount (5%)'}\t\t\t\tRs {discount:.2f}")
                    print(f"{'Final Price':}\t\t\t\tRs {finalprice:.2f}")
                    print("--------------------------------------------------------")
                    print("               Thanks for shopping with us!")
                else:
                    print("Thank you for choosing us. See you again")
                exit()

            elif option2 ==1:
                item = input("Enter the item: ").lower()
                if item in items:
                    itemlist.append(item)
                    quantity_input = input("Enter the quantity: ")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        price = quantity * int(items[item])
                        pricelist.append((item,quantity,items[item],price))
                        totalprice += price
                    else:
                        print("Please enter a number.")
                else:
                    print("Please enter the right option.")
            else:
                print("Please enter the right option.")
    elif option1 ==2:
        if itemlist:
            print("Thank you for choosing us. Please find the final bill")
            print("==================Ramya Super Market====================")
            print("----------------------Hyderabad-------------------------")
            print(f"Name: {name}")
            print("--------------------------------------------------------")
            print("Sno.\tItems\tQuantity\tPrice")
            for i in range(len(pricelist)):
                item, quantity, rate, price = pricelist[i]
                print(f"{i+1}\t{item}\t{quantity}\t\t\t\t{price}")
            print("--------------------------------------------------------")
            discount = totalprice * 0.05
            finalprice = totalprice - discount
            print(f"{'Total':}\t\t\t\t\t{'Rs'} {totalprice}")
            print(f"{'Discount (5%)'}\t\t\t\tRs {discount:.2f}")
            print(f"{'Final Price':}\t\t\t\tRs {finalprice:.2f}")
            print("--------------------------------------------------------")
            print("               Thanks for shopping with us!")
        else:
            print("Thank you for choosing us. See you again")
        exit()
    else:
        print("Wrong option, Kindly choose the right option")

        





