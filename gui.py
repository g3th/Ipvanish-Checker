from header import title


def text_user_interface(is_using_proxies):
    title()
    print("Choose Option:")
    print("\n1) Check with Selenium")
    print("2) Check with Requests")
    print("3) Use Proxies [{}]".format(is_using_proxies))
    print("4) Quit")
    choice = input("\nChoose: ")
    return choice


def sub_menu():
    title()
    print("\nPlease enter your IpVanish proxies credentials:")
    proxy_user = input("\nEnter user name: ")
    proxy_password = input("\nEnter password: ")
    return proxy_user, proxy_password
