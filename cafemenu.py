menu = {
    "Pizza":90,
    "Rasmalai":55,
    "Burger":60,
    "Chowmein":70,
    "Coffee":90,
}
#greet
print("welcome to sweet cafe")
print("Pizza: Rs 90\nRasmalai: Rs 55\nBurger: Rs 60\nChowmein: Rs70\nCoffee: 90")
 
total_order = 0
#70+60 = 130

item_01 = input("enter the name of the item you wants to order = ")
if item_01 in menu:
    total_order += menu[item_01]#0+70
    print(f"Your item {item_01} has been added to your order")

else:
    print(f"ordered item {item_01}is not available yet")

another_order = input("Do you want to order something else? (Yes/No)")
if another_order =="Yes":
    item_02 = input("enter the name of second item = ")
    if item_02 in menu:
        total_order += menu[item_02]
        print(f"Item{item_02} has been added to order")
    else:
        print(f"ordered item{item_02}is not available")

    print(f"The total amount of items to give is {total_order}")
