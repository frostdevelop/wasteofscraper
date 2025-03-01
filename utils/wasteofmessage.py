import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,promptEnum,printPost,printComm,printMsg

runenum = ["unread","read"]
running = True
os.system('cls')
while running:
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    mode = promptEnum("Mode\n0:Display Unread Messages\n1:Display Read Messages\n2:Mark Messages as Unread\n3:Mark Messages as Read\n4:Delete Message (Unavailable to Regular Users)\n>",4)
    match(mode):
        case 0 | 1:
            page = 1
            retries = 3
            while True:
                print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
                try:
                    result = requests.get("https://api.wasteof.money/messages/" + runenum[mode] + "?page=" + str(page), headers={"Authorization":token})
                except Exception as e:
                    print("\033[0;31mERR: "+str(e)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[0;31m\033[1mMax retries exceeded\033[0m")
                        break
                    retries -= 1;
                    continue
				
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    msglen = len(data[runenum[mode]])
                    for i in range(msglen):
                        printMsg(data[runenum[mode]][i])
                        print("------")
                        
                    if(data["last"] or msglen==0):
                        print("\033[1;33m"+"End of Stream"+"\033[0m")
                        break
                    
                    page += 1
                    retries = 3
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[0;31m\033[1mMax retries exceeded\033[0m")
                        break
                    retries -= 1;
        case 2 | 3:
            msglist = []
            while True:
                msg = input("\033[1;32m\033[1m" + "Message#" + str(len(msglist)) + ">\033[0m")
                msglist.append(msg)
                cont = input("\033[1;32m\033[1m" + "Continue? (y/n)>" + "\033[0m")
                if(cont == "n"):
                    break
                    
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.post("https://api.wasteof.money/messages/mark/"+runenum[mode-2], headers={"Authorization":token,"Content-Type": "application/json"}, data=json.dumps({"messages":msglist}))
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
                    #print(data)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 4:
            msgID = input("\033[1;32m\033[1m" + "Enter message ID>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.delete("https://api.wasteof.money/messages/"+msgID,headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
                    print(data)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False