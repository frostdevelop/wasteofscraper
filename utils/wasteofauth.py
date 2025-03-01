import requests, json, os, getpass
from datetime import datetime
from wasteofdisplay import printDat,printUser,promptEnum,printSession

running = True
os.system('cls')

while running:
    mode = promptEnum("Category\n0:Data from Token\n1:Login\n2:Logout (Invalidate Token)\n3:Join\n4:Oauth Links\n5:User oauth links (Change authentication)\n6:Check username availability\n>",6)
    match(mode):
        case 0:
            token = input("\033[1;32m\033[1m" + "Token>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
            
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("user" in data.keys()):
                    printSession(data)
                else:
                    printDat("Error","User not found!")
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1:
            username = input("\033[1;32m\033[1m" + "Username>" + "\033[0m")
            password = getpass.getpass("\033[1;32m\033[1m" + "Passcode>" + "\033[0m")
            result = requests.post("https://api.wasteof.money/session",data=json.dumps({"username":username,"password":password}),headers={"Content-Type":"application/json"})
            
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                elif("token" in data.keys()):
                    printDat("Token",data["token"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 2:
            token = input("\033[1;32m\033[1m" + "Token>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.delete("https://api.wasteof.money/session",headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 3:
            username = input("\033[1;32m\033[1m" + "Username>" + "\033[0m")
            password = getpass.getpass("\033[1;32m\033[1m" + "Passcode>" + "\033[0m")
            captcha = input("\033[1;32m\033[1m" + "Captcha ID>" + "\033[0m")
            result = requests.post("https://api.wasteof.money/session",data=json.dumps({"username":username,"password":password,"captcha":captcha}),headers={"Content-Type":"application/json"})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    print(data)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 4:
            print("\033[0;34m\033[1m" + "Sending google request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/sessions/oauth/google/url")
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Url",data["url"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            print("\033[0;34m\033[1m" + "Sending github request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/sessions/oauth/github/url")
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Url",data["url"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 5:
            token = input("\033[1;32m\033[1m" + "Token>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/settings/oauth/google/url",headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Url",data["url"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            print("\033[0;34m\033[1m" + "Sending github request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/settings/oauth/github/url",headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Url",data["url"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 6:
            name = input("\033[1;32m\033[1m" + "Username>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/username-available?username=" + name)
            
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Available",str(data["available"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False