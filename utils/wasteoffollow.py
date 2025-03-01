import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,printUser

'''
def capital
def getMode(num):
    match(num):
       case 0:
           return "/followers"
       case 1:
           return "/following"
       case _:
          raise Exception("CosmicErr: invalid getmode enum!")
'''

modeenum = ["followers","following"]
running = True
os.system('clear')
os.system('cls')
while running:
    mode = -1
    while(not (mode >= 0 & mode <= 3)):
        try:
            mode = int(input("\033[1;32m\033[1m" + "Enter type (0:Followers, 1:Following, 2:IsFollowing, 3:Follow someone)>" + "\033[0m"))
        except Exception as e:
            print("Error! " + str(e))
    
    user = input("\033[1;32m\033[1m" + "Enter followee username>" + "\033[0m")
    match(mode):
        case 0 | 1:
            page = 1
            retries = 3
            while True:
                print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
                try:
                    result = requests.get("https://api.wasteof.money/users/"+user+"/"+modeenum[mode]+"?page="+str(page))
                except Exception as e:
                    print("\033[0;31mERR: "+str(e)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        break
                    retries -= 1;
                    continue
                
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    userLen = len(data[modeenum[mode]])
                    print("\033[1;33m"+modeenum[mode].title()+": "+"\033[0m")
                    for i in range(userLen):
                        printUser(data[modeenum[mode]][i]);
                    
                    if(userLen == 0 or data["last"]):
                        break
                    page += 1
                    retries = 3
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        break
                    retries -= 1;
        case 2:
            #fluser = input("\033[1;32m\033[1m" + "Enter follower username>" + "\033[0m")
            fltoken = input("\033[1;32m\033[1m" + "Enter follower token>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":fltoken})
                if sresp.status_code == 200:
                    fluser = (sresp.json())["user"]["name"]
                    result = requests.get("https://api.wasteof.money/users/" + user + "/followers/" + fluser, headers={"Authorization":fltoken})
                    if result.status_code == 200:
                        print("\033[1;33m"+"Success"+"\033[0m")
                        printDat("Following?",result.text)
                    else:
                        print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                else:
                    print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
        case 3:
            token = input("\033[1;32m\033[1m" + "Enter follower token>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.post("https://api.wasteof.money/users/" + user + "/followers", headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("New Count",str(data["new"]["followers"]))
                printDat("Action",str(data["ok"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False