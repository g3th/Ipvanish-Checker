from pathlib import Path
from header import title


def text_user_interface(is_using_proxies, chrome_version, chromedriver_is_installed):
    title()
    chrome_directory = str(Path(__file__).parent) + '/chromedriver/'
    proxies = ['No Account', 'Logged in']
    print("Installed Chrome Version: {}".format(chrome_version))
    if not chromedriver_is_installed:
        print('Chromedriver was not found in "{}"'.format(chrome_directory))
        return 0
    else:
        print('Chromedriver was found in "{}"'.format(chrome_directory))
        print("\nOptions:")
        print("\n1) Check with Selenium")
        print("2) Check with Requests")
        print("3) Ipvanish Proxies [{}]".format(proxies[is_using_proxies]))
        print("4) Quit")
        choice = input("\nChoose: ")
        return choice


def sub_menu():
    title()
    print("\nPlease enter your IpVanish proxies credentials:")
    proxy_user = input("\nEnter user name: ")
    proxy_password = input("\nEnter password: ")
    return proxy_user, proxy_password
