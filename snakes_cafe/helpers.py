def decor(func):
    def wrap():
        print("****************************************")
        func()
        print("****************************************")
    return wrap

def list_menu(list):
    for section in list:
        print(section)
        print("----------")
            
    print("")
    print("")

# function that takes user input and adds it to order
def item_added(item):
    print(f"** {item} has been added to your order  **")
