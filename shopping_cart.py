import os
from tkinter import *
import datetime
import pandas

#database as dictionary
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Receipt
now = datetime.datetime.now()

#User Input

product_ids = []

while True:
    product_id = input ("Please Input a Product Identifier or Done: ")
    if product_id == "Done":
        break
    else:
        product_ids.append(int(product_id))

Running_total_price = 0

print("______Customer Copy__________")
print("ESL405 Groceries")
print("Phone: 800-PYT-2335")
print(now.strftime("%A, %B, %d, %Y at %I: %M, %p"))
print("_____________________________")
print("Purchased Items: ")
for product_id in product_ids:
    matching_products = [product for product in products if product["id"] == product_id]
    matching_product = matching_products [0]
    Running_total_price += matching_product["price"]
    price_usd= ' (${0:0.2f})'.format(matching_product["price"])
    print(" + " + matching_product["name"]+ price_usd)

print ("_____________________________")
Running_total_price_usd = '${0:.2f}'.format(Running_total_price)
print("Running Total: " + str(Running_total_price_usd))
tax_owed = Running_total_price * 0.08875
tax_owed_usd = '${0:.2f}'.format(tax_owed)
print("Taxes: " + str(tax_owed_usd))
total_owed = Running_total_price+tax_owed
total_owed_usd= '${0:.2f}'.format(total_owed)
print("Total: " + str(total_owed_usd))
print("Thank you.")

root=Tk()
root.geometry('500x1000')
root.title("Store Copy")
Store_Name = Label(None, text='ESL405 Groceries').pack()
Store_Number = Label(None, text='800-PYT-2335').pack()
Date_Time = Label(None, text=now.strftime("%A, %B, %d, %Y at %I: %M, %p")).pack()
Item_number = Label(None, text="Total Items: " + str(len(product_ids))).pack()
Sub_Total = Label(None, text="Running Total: " + str(Running_total_price_usd)).pack()
Tax = Label(None, text="Taxes: " + str(tax_owed_usd)).pack()
Total = Label(None, text="Total: " + str(total_owed_usd)).pack()
End_Message = Label(None, text='Thank You').pack()
root.mainloop()







#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#product_id = int(input ("Please input values: "))
#
#product_ids = []
#try:
#    while int(product_id)<(len(products)):
#        product_ids.append(int(product_id))
#        product = input("Please input values: ")
#    else:
#        print("Please Choose Another Value or 'Quit'")
#        product_id = input("Please input values: ")
#        while int(product_id)<(len(products)):
#            product_ids.append(int(product_id))
#            product_id = input("Please input values: ")
#        else:
#            print("Please Choose Another Value or 'Quit'")
#except ValueError:
#    #print(user_choice)
#    root=Tk()
#    root.geometry('300x200')
#    Store_Name = Label(None, text='Fake Groceries').pack()
#    Store_Number = Label(None, text='xxx-xxx-xxxx').pack()
#    Date_Time = Label(None, text=now.isoformat()).pack()
#    Items_Price = Label(None, text='xxx-xxx-xxxx').pack()
#    Sub_Total = Label(None, text="Total: " + 'temp').pack()
#    Tax = Label(None, text="Total: " + 'temp').pack()
#    Total = Label(None, text="Total: " + 'temp').pack()
#    End_Message = Label(None, text='Thank You').pack()
#    root.mainloop()
#    



#print(products)

