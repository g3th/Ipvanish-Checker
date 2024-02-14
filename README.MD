# IPvanish Account Checker
## Account Checker Using Selenium Webdriver

Load up any combo-lists, and check whether accounts for the IPVanish VPN service are valid or not.


Either use Selenium, or just send a request to IPVanish's api endpoint, whichever seems to work. With the second option you might get blocker quicker without rotating proxies.


Combos are placed in a file named "ipvanish" (no extension) placed in the ```combos``` folder.


Valid accounts are stored in the ```valid``` folder.


NOTE: False negatives can occurr if checking accounts too quickly, due to cloudflare protection.