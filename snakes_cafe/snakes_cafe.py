from textwrap import dedent

# this is the welcome text
def print_welcome():
    print("*" *39)
    print("**    Welcome to the Snakes Cafe!    **")
    print("**    Please see our menu below.     **")
    print("**                                   **")
    print("**  To quit at any time, type \"quit\" **")
    print("*" *39)

# this is the order prompt text
def order_prompt():
    print("*" *39)
    print("** What would you like to order?  **")
    print("*" *39)

menu = {
    "Wings": 0, 
    "Cookies": 0,
    "Spring Rolls": 0, 
    "Salmon": 0, 
    "Steak": 0, 
    "Meat Tornado": 0, 
    "A Literal Garden": 0, 
    "Ice Cream": 0, 
    "Cake": 0, 
    "Pie": 0, 
    "Coffee": 0, 
    "Tea": 0, 
    "Unicorn Tears": 0,
}

menu_section = ("""
Appetizers
----------
{}
{}
{}

Entrees
----------
{}
{}
{}
{}

Desserts
----------
{}
{}
{}

Drinks
----------
{}
{}
{}
""".format(*menu)
)

# if __name__ == "__main__":
print_welcome()

print(menu_section)

order_prompt()
order = {}
item = input('> ')

while item != 'quit':

    if item.lower() not in [key.lower() for key in menu.keys()]:
        print("**  Please order from the menu or type 'quit' **")
        item = input ('> ')

    if item.lower() in [key.lower() for key in menu.keys()]:
        if item.lower() not in [key.lower() for key in order.keys()]:
           order[item] = 0
        order[item.lower()] += 1
        print(f"** {order[item.lower()]} order of {item.lower()} have been added to your meal **")
        item = input('> ')

if item == 'quit':
    if order == {}:
        print("**  Thank you, have a nice day  **")
    else:
        print(f"** Your order of {order}  is coming right up**")
    