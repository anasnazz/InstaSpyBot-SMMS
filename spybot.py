import instaloader
import telegram_send
import pytz
from datetime import datetime

#Date and Time
intz = pytz.timezone('Asia/Kolkata')
nowdttemp = str(datetime.today())
nowdt = nowdttemp.replace(":","-")
nowdt = nowdt.replace("."," ")

#Log
#telegram_send.send(messages=['Starting...'])
with open(r'logs/'+nowdt+'.log','w') as temp:
    temp.write("Log "+nowdttemp+2*"\n")

try:
    #1.Information Gathering

    #Instaloader

    L = instaloader.Instaloader()

    try:
        L.load_session_from_file('#Username', filename=None)
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Loaded session from file for #Username.\n")
        #print("True")
    except:
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Failed to load session from file for #Username.\n"+nowdttemp+"Trying to login using credentials.\n")
        L.login('#Username', '#Password')
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Logged in using credentials.\n")
        #print("False")

    #http = urllib3.PoolManager()

    #inputs()
    pro = ("Account to track")
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  Initiating process to gather informations from 'Tracking account name'.\n")
    followers = []
    followings = []

    try:

        profile = instaloader.Profile.from_username(L.context, pro)

        for person in profile.get_followers():
            followers.append(person.username)
        #print(followers)
        for person in profile.get_followees():
            followings.append(person.username)
        #print(followings)

        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Information gathering completed successfully.\n")

    except:
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Information gathering failed.")
        telegram_send.send(messages=['Information gathering failed.'])
        #print('Error Code: 02',pro)

    #2.Processing

    file = list(set(followings) - set(followers))
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  Informations Processing completed.\n")
    #print(file)


    def writer(temp,proc):
        with open(temp+'.shw','w') as temp:
            for i in [proc]:
                temp.write(','.join(proc))

    def reader(temp):
        with open(temp+'.shw','r') as proc:
            content = proc.read()
            #print(content)
            temp = content.split(",")
            return temp
            #print(temp)

    def main(self):
        Temp = list(set(file) - set(A))
        Temp = list(set(Temp) - set(B))
        Temp = list(set(Temp) - set(C1))
        Temp = list(set(Temp) - set(C2))
        Temp = list(set(Temp) - set(D))
        if Temp != []:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"Change in unfollowers\n")
            #writer("D",Temp)
            Temp = '\n'.join([str(item) for item in Temp])
            telegram_send.send(messages=['Unfollowers:', Temp])
            #telegram_send.send(messages=[Temp])

        else:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  No change in unfollowers\n")
            telegram_send.send(messages=['No change in unfollowers!'])

    def phase1(self):
        Temp = list(set(C1) - set(followers))
        #print('\n')
        #print('\n',Temp)
        Temp.sort()
        C1.sort()
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Phase 1 sorting completed.\n")
        if Temp == []:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Nothing in C1.\n")
            telegram_send.send(messages=['Nothing in C1'])
        elif Temp == C1:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  No change in C1.\n")
            telegram_send.send(messages=['No change in C1'])
        else:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Change in C1.\n")
            writer('C1',Temp)
            Temp = '\n'.join([str(item) for item in Temp])
            telegram_send.send(messages=['Change in C1:', Temp])
            #telegram_send.send(messages=[Temp])
            print(Temp)

    def phase2(self):
        Temp = list(set(C2) - set(followers))
        #print('\n')
        #print('\n',Temp)
        Temp.sort()
        C2.sort()
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Phase 2 sorting completed.\n")
        if Temp == []:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Nothing in C2.\n")
            telegram_send.send(messages=['Nothing in C2'])
        elif Temp == C2:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  No change in C2.\n")
            telegram_send.send(messages=['No change in C2'])
        else:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Change in C2.\n")
            writer('C2',Temp)
            Temp = '\n'.join([str(item) for item in Temp])
            telegram_send.send(messages=['Change in C2:', Temp])
            #telegram_send.send(messages=[Temp])

    def phase3(self):
        Temp = list(set(D) - set(followers))
        #print('\n')
        #print('\n',Temp)
        Temp.sort()
        D.sort()
        with open(r'logs/'+nowdt+'.log','a') as temp:
            temp.write(nowdttemp+"  Phase 3 sorting completed.\n")
        if Temp == []:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Nothing in D.\n")
            telegram_send.send(messages=['Nothing in D'])
        elif Temp == D:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  No change in D.\n")
            telegram_send.send(messages=['No change in D'])
        else:
            with open(r'logs/'+nowdt+'.log','a') as temp:
                temp.write(nowdttemp+"  Change in D.\n")
            writer('D',Temp)
            Temp = '\n'.join([str(item) for item in Temp])
            telegram_send.send(messages=['Change in D:', Temp])
            #telegram_send.send(messages=[Temp])


    #telegram_send.send(messages=['Hello sir'])
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  Sending salutation completed.\n")
    C1 = reader('C1')
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  C1 defined.\n")
    phase1(C1)
    C2 = reader('C2')
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  C2 defined.\n")
    phase2(C2)
    D = reader('D')
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  D defined.\n")
    phase3(D)
    B = reader('B')
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  B defined.\n")
    A = reader('A')
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  A defined.\n")
    main(file)
    #telegram_send.send(messages=['Goodnight! See you tomorrow.'])
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  Completed.\n")
    

except:
    with open(r'logs/'+nowdt+'.log','a') as temp:
        temp.write(nowdttemp+"  Error in main process.\n")
