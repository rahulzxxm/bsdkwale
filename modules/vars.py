import os

api_id = int(os.environ.get("API_ID", '27862677'))
api_hash = os.environ.get("API_HASH", 'e343ce2c81b2b6c2c0d6bee58284e3bd')
bot_token = os.environ.get("BOT_TOKEN", '6611654088:AAE_ACVRTLoucGh_YpnJcuqauyRI3c1cHbw')




OWNER = int(os.environ.get("OWNER", '5881684718'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '5881684718').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
