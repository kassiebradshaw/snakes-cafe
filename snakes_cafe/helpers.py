def decor(func):
    def wrap():
        print("****************************************")
        func()
        print("****************************************")
    return wrap

def list_menu(name, list):
    print(name)
    print("----------")
    for i in range(len(list)):
        print(list[i])
    print("")
    print("")

def item_added(item):
    print(item + ' has been added to your order')
