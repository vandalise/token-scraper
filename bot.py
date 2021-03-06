import subprocess as sp
import requests
import threading
import sys
import time
from colorama import Fore as COL

print(COL.YELLOW + f"Token Scraper | by King Herod | Scraping tokens...")

valid = open("valid.txt", "w")
locked = open("locked.txt", "w")
tokencount = 0
templist = []
#token checker function
def Check(auth):
    global tokencount
    try:
        halfauth = auth[:len(auth)//2]
        x = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': auth})
        if x.status_code == 200:
            y = requests.get('https://discord.com/api/v9/users/@me/affinities/users', headers={'Authorization': auth})
            json = x.json()
            if y.status_code == 200:
                print(COL.GREEN + f'VALID: {halfauth}***** {json["username"]}#{json["discriminator"]}')
                valid.write(f'{auth}\n')
                tokencount += 1
            elif y.status_code == 403:
                print(COL.YELLOW + f'LOCKED: {halfauth}***** {json["username"]}#{json["discriminator"]}')
                locked.write(f'{auth}\n')
            elif y.status_code == 429:
                print(COL.YELLOW + f"You're being rate limited")
                time.sleep(y.headers['retry-after'])
            elif x.status_code == 429:
                print(COL.YELLOW + f"You're being rate limited")
                time.sleep(y.headers['retry-after'])
            else:
                print(COL.RED + f'INVALID: {auth}')
    except:
        pass
#find all tokens on computer
m = 0
output = sp.getoutput('find /home -name tokens.txt').splitlines()
for path in output:
    for x in open(path, "r").read().splitlines():
        templist.append(x)
#remove dupes
res = []
for token in templist:
    if token in res:
        pass
    else:
        res.append(token)
        m += 1

#ask if you want to check tokens or not
print(COL.YELLOW + f"Token Scraper | by King Herod | Loaded {m} tokens")
opt = input("Check tokens? (y/n): ")
if opt not in("y", "Y"):
    print(templist)
    sys.exit()
else:
    pass

#check if tokens are valid
threads = []
for token in res:
    t = threading.Thread(target=Check, args=(token, ))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(COL.GREEN + f"Finished scraping | {tokencount} tokens saved to valid.txt.")
