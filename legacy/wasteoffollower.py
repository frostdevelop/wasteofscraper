import requests, json, os

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True
os.system('cls')
name = input("\033[1;32m\033[1m" + "Enter wasteof username>" + "\033[0m")
while running:
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
    result = requests.post("https://api.wasteof.money/users/" + name + "/followers", headers={"Authorization":token})
    if result.status_code == 200:
        data = result.json()    
        print("\033[1;33m"+"Success"+"\033[0m")
        printDat("New Count",str(data["new"]["followers"]))
        #print(data["ok"])
    else:
        print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False