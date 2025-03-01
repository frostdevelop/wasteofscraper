from datetime import datetime

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")
    
def promptEnum(msg,maxi):
    num = -1
    while(not (num >= 0 & num <= maxi)):
        try:
            num = int(input("\033[1;32m\033[1m" + msg + "\033[0m"))
        except Exception as e:
            print("Error! " + str(e))
    return num

def printPost(post,showrep=True):
    printDat("ID",post["_id"])
    printDat("Poster",post["poster"]["name"])
    printDat("PosterID",post["poster"]["id"])
    printDat("PosterColor",post["poster"]["color"])
    printDat("Content",post["content"])
    printDat("Post Date",str(datetime.fromtimestamp(post["time"]/1000)))
    printDat("Comments ",str(post["comments"]))
    printDat("Loves ",str(post["loves"]))
    revlen = len(post["revisions"])
    print("\033[1;33m"+"Revisions: "+"\033[0m"+str(revlen))
    for i in range(0,revlen-1):
        print("--")
        printDat("Content",post["revisions"][i]["content"])
        printDat("Post Date",str(datetime.fromtimestamp(post["revisions"][i]["time"]/1000)))
        printDat("EditorID",post["revisions"][i]["editor"])
        print("--")
    printDat("Reposts ",str(post["reposts"]))
    if(showrep):
        if("repost" in post.keys() and post["repost"] is not None):
            print("\033[1;33m"+"Repost: "+"\033[0m")
            print("--")
            printPost(post["repost"])
            print("--")
    if("edited" in post.keys()):
        printDat("Edit Date",str(datetime.fromtimestamp(post["edited"]/1000)))

def printComm(post):
    printDat("ID",post["_id"])
    printDat("Parent PostID",post["post"])
    printDat("Poster",post["poster"]["name"])
    printDat("PosterID",post["poster"]["id"])
    printDat("PosterColor",post["poster"]["color"])
    printDat("Content",post["content"])
    printDat("Post Date",str(datetime.fromtimestamp(post["time"]/1000)))    
    printDat("HasReplies",str(post["hasReplies"]))
    if("parent" in post.keys() and post["parent"] is not None):
        printDat("Parent reply",post["parent"])
        printDat("Top reply",post["top"])
        
def printMsg(message):
    printDat("ID",message["_id"])
    printDat("Type",message["type"])
    printDat("Reciever",message["to"]["name"])
    printDat("RecieverID",message["to"]["id"])
    printDat("Read?",str(message["read"]))
    printDat("Time",str(datetime.fromtimestamp(message["time"]/1000)))
    match(message["type"]):
        case "comment" | "comment_reply":
            printDat("ActorName",message["data"]["actor"]["name"])
            printDat("ActorID",message["data"]["actor"]["id"])
            print("--")
            print("\033[1;33m"+"Comment Parent Post:"+"\033[0m")
            printPost(message["data"]["post"])
            print("--")
            print("\033[1;33m"+"Comment:"+"\033[0m")
            printComm(message["data"]["comment"])
            print("--")
        case "follow":
            #Das it
            printDat("ActorName",message["data"]["actor"]["name"])
            printDat("ActorID",message["data"]["actor"]["id"])
        case "repost":
            printDat("ActorName",message["data"]["actor"]["name"])
            printDat("ActorID",message["data"]["actor"]["id"])
            print("--")
            print("\033[1;33m"+"Post:"+"\033[0m")
            printPost(message["data"]["post"])
            print("--")

def printUser(user):
    printDat("Name",user["name"])
    printDat("ID",user["id"])
    printDat("Bio",user["bio"])
    printDat("Verified",str(user["verified"]))
    printDat("HasAdmin",str(user["permissions"]["admin"]))
    printDat("Banned",str(user["permissions"]["banned"]))
    printDat("HasBeta",str(user["beta"]))
    printDat("Color",user["color"])
    printDat("Join Date",str(datetime.fromtimestamp(user["history"]["joined"]/1000)))
    
def printSession(data):
    printUser(data["user"])
    printDat("Admin Impersionation",str(data["flags"]["isAdminImpersonating"]))
    printDat("Showing recovery message",str(data["flags"]["showRecoveryMessage"]))