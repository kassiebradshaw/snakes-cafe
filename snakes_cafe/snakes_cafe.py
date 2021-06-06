from helpers import decor, list_menu, item_added
from textwrap import dedent

# this is the welcome text
def print_welcome():
    print("**    Welcome to the Snakes Cafe!    **")
    print("**    Please see our menu below.     **")
    print("**                                   **")
    print("**  To quit at any time, type \"quit\" **")

# this is the order prompt text
def order_prompt():
    print("** What would you like to order?  **")

# these are the texts wrapped in the decorator function
decorated_welcome = decor(print_welcome)
decorated_order_prompt = decor(order_prompt)

# these are the lists of each menu section

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

menu_section = dedent("""
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

if __name__ == "__main__":
    item = ""
    while item != "quit":
        decorated_welcome()
        print("")

        print(menu_section)

        decorated_order_prompt()
        item = input('> ')
        order = []
        print(item_added(item))