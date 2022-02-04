import subprocess as sp
import requests
import threading
import os

tokencount = 0
test_list = []
#token checker function
def check_token(token):
    global tokencount
    request = requests.get("https://discordapp.com/api/v6/users/@me/library", headers={'Content-Type': 'application/json', 'authorization': token})
    if request.status_code == 200:
        open("valid.txt", "a").write(token+"\n")
        tokencount+=1
        print(f"[+] Saved token to valid.txt | {tokencount}")
#find all tokens on computer
output = sp.getoutput('find /home -name tokens.txt').splitlines()
for path in output:
    for x in open(path, "r").read().splitlines():
        test_list.append(x)
#remove dupes
res = []
[res.append(x) for x in test_list if x not in res]
#check if tokens are valid
for token in res:
    threading.Thread(target=check_token, args=(token, )).start()
def do(token):
    os.system(f"python3 login.py {token}")
for token in open("valid.txt", "r").read().splitlines():
    threading.Thread(target=do, args=(token, )).start()