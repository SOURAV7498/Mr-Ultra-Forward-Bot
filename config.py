import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "21140176")
    API_HASH = environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8382484520:AAHHy5CMDLJAq9SQiUYQFuBbYuEIM8n4H1U") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://sbmod88_db_user:XCLxrjdGlaHTG6mz@cluster0.qndjonz.mongodb.net/?autobot=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "autobot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6222491731').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003202129936'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002593429847 -100309672279 -1003016878831") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
