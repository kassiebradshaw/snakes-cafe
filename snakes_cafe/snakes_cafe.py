from helpers import decor
from helpers import list_menu
from helpers import item_added

def print_welcome():
    print("**    Welcome to the Snakes Cafe!    **")
    print("**    Please see our menu below.     **")
    print("**                                   **")
    print("**  To quit at any time, type \"quit\" **")

def order_prompt():
    print("** What would you like to order?  **")

decorated_welcome = decor(print_welcome)
decorated_order_prompt = decor(order_prompt)

appetizers_list = ["Wings", "Cookies", "Spring Rolls"]
entrees_list = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts_list = ["Ice Cream", "Cake", "Pie"]
drinks_list = ["Coffee", "Tea", "Unicorn Tears"]

if __name__ == "__main__":

    decorated_welcome()
    print("")
    print(list_menu('Appetizers', appetizers_list))
    print(list_menu('Entrees', entrees_list))
    print(list_menu('Desserts', desserts_list))
    print(list_menu('Drinks', drinks_list))

    decorated_order_prompt()
    item = input('> ')
    print(item_added(item))