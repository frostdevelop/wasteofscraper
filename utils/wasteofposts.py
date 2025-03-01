import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,printPost

running = True
os.system('clear')
mode = -1
while(not (mode >= 0 & mode <= 3)):
    try:
        mode = int(input("\033[1;32m\033[1m" + "Enter type (0:Post data, 1:User posts, 2:User Homepage, 3:Report Post, 4:Love post, 5:Loved post? (check if loved))>" + "\033[0m"))
    except Exception as e:
        print("Error! " + str(e))

while running:
    match(mode):
        case 0:
            postID = input("\033[1;32m\033[1m" + "Enter postID>" + "\033[0m")
            result = requests.get("https://api.wasteof.money/posts/"+postID)
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printPost(data)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1 | 2:
            page = 1
            retries = 3
            user = input("\033[1;32m\033[1m" + "Enter wasteof username>" + "\033[0m")
            while True:
                print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
                
                try:
                    #result = requests.get("https://api.wasteof.money/users/"+user+"/posts", data={"page":page})
                    result = requests.get("https://api.wasteof.money/users/"+user+("/posts" if(mode == 1) else "/following/posts")+"?page="+str(page)) #(mode == 1 ? "/posts" : "/following/posts")
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
                    if(mode == 1):
                        pinlen = len(data["pinned"])
                        if(page == 1 and pinlen > 0):
                            print("\033[1;33m"+"Pinned: "+"\033[0m")
                            for i in range(pinlen):
                                printPost(data["pinned"][i]);
                    
                    postlen = len(data["posts"])
                    print("\033[1;33m"+"Posts: "+"\033[0m")
                    for i in range(postlen):
                        printPost(data["posts"][i])
                        print("------")
                    
                    if(postlen == 0 or data["last"]):
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
        case 3:
            token = input("\033[1;32m\033[1m" + "Enter token>" + "\033[0m")
            postID = input("\033[1;32m\033[1m" + "Enter postID>" + "\033[0m")
            reason = input("\033[1;32m\033[1m" + "Enter report reason>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.post("https://api.wasteof.money/posts/"+postID+"/report", data=json.dumps({"type":"none","reason":reason}), headers={"Authorization":token,"Content-Type":"application/json"})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 4:
            token = input("\033[1;32m\033[1m" + "Enter token>" + "\033[0m")
            postID = input("\033[1;32m\033[1m" + "Enter postID>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.post("https://api.wasteof.money/posts/"+postID+"/loves", headers={"Authorization":token})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data)
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
                    printDat("Loving",str(data["new"]["isLoving"]))
                    printDat("New count",str(data["new"]["loves"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 5:
            token = input("\033[1;32m\033[1m" + "Enter token>" + "\033[0m")
            postID = input("\033[1;32m\033[1m" + "Enter postID>" + "\033[0m")
            username = input("\033[1;32m\033[1m" + "Enter username\n(Regular accounts can only access themselves)\n(Leave blank for your name)>" + "\033[0m")
            sresp = None
            if(username==""):
                print("\033[0;34m\033[1m" + "Sending session request..." + "\033[0m")
                try:
                    sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
                except Exception as e:
                    print("\033[0;31mERR: "+str(e)+"\033[0m")
                    continue
                if(sresp.status_code == 200):
                    username = (sresp.json())["user"]["name"]
                else:
                    print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
                    continue
            
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.get("https://api.wasteof.money/posts/"+postID+"/loves/"+username, headers={"Authorization":token})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Loving",result.text)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False