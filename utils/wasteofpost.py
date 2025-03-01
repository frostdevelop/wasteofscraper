import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,promptEnum,printPost

running = True
os.system('cls')
token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
mode = promptEnum("Mode 0:Post 1:Comment 2:Wall 3:Delete Comment 4:Edit Post 5:Delete Post 6:Pin Post 7:Unpin Post>",7)
while running:
    match(mode):
        case 0:
            post = input("\033[1;32m\033[1m" + "Enter post content>" + "\033[0m")
            repost = input("\033[1;32m\033[1m" + "Enter repost ID>" + "\033[0m") or None
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.post("https://api.wasteof.money/posts", data=json.dumps({"post":post,"repost":repost}), headers={"Authorization":token,"Content-Type":"application/json"})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data);
                printDat("Id",str(data["id"]))
                printDat("Action",str(data["ok"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1 | 2:
            comment = input("\033[1;32m\033[1m" + "Enter comment content>" + "\033[0m")
            urlID = input(("\033[1;32m\033[1m" + "Enter post ID>" + "\033[0m") if(mode==1) else ("\033[1;32m\033[1m" + "Enter wall user>" + "\033[0m"))
            parent = input("\033[1;32m\033[1m" + "Replying (comment ID) (press enter for none)>" + "\033[0m") or None
            #if(mode == 1)
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.post(("https://api.wasteof.money/posts/"+urlID+"/comments") if(mode==1) else ("https://api.wasteof.money/users/"+urlID+"/wall"), data=json.dumps({"content":comment,"parent":parent}), headers={"Authorization":token,"Content-Type":"application/json"})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data);
                printDat("Id",str(data["id"]))
                printDat("Action",str(data["ok"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 3:
            commID = input("\033[1;32m\033[1m" + "Enter comment ID>" + "\033[0m")
            result = requests.delete("https://api.wasteof.money/comments/"+commID,headers={"Authorization":token})
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
            postID = input("\033[1;32m\033[1m" + "Enter post ID>" + "\033[0m")
            post = input("\033[1;32m\033[1m" + "Enter new post content>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.put("https://api.wasteof.money/posts/"+postID, data=json.dumps({"post":post}), headers={"Authorization":token,"Content-Type":"application/json"})
            except Exception as e:
                print("\033[0;31mERR: "+str(e)+"\033[0m")
                continue
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Action",data["ok"])
                printPost(data["new"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 5:
            postID = input("\033[1;32m\033[1m" + "Enter post ID>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.delete("https://api.wasteof.money/posts/"+postID, headers={"Authorization":token})
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
        case 6|7:
            postID = input("\033[1;32m\033[1m" + "Enter post ID>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            try:
                result = requests.post("https://api.wasteof.money/posts/"+postID+("/pin" if(mode==6) else "/unpin"), headers={"Authorization":token})
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
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False