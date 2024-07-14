#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21145186"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002159492954"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6011680723"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "2"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝐻𝐸𝐿𝐿𝒪 𝒯𝐻𝐸𝑅𝐸 {mention} ✌\n\n𝐼 𝒜𝑀 𝒜 𝐹𝐼𝐿𝐸 𝒮𝐻𝒜𝑅𝐼𝒩𝒢 𝐵𝒪𝒯 𝒰𝒮𝐸𝒟 𝒜𝒩𝒟 𝒟𝐸𝒱𝐸𝐿𝒪𝒫𝐸𝒟 𝐵𝒴 InfoHub Networks. 🍂\n\n𝐼 𝒜𝑀 𝒩𝒪𝒯 𝒟𝐸𝒮𝐼𝒢𝒩𝐸𝒟 𝒯𝒪 𝑅𝐸𝒞𝐸𝐼𝒱𝐸 𝒟𝐼𝑅𝐸𝒞𝒯 𝒯𝐸𝒳𝒯 𝑀𝐸𝒮𝒮𝒜𝒢𝐸𝒮 𝐻𝐸𝑅𝐸. 🍂\n\n𝒯𝐻𝒜𝒩𝒦𝒮 𝐹𝒪𝑅 𝒰𝒮𝐼𝒩𝒢 𝒪𝒰𝑅 𝒮𝐸𝑅𝒱𝐼𝒞𝐸𝒮. 🍂")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6011680723 1524169222").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝒮𝒪𝑅𝑅𝒴 𝒯𝒪 𝐼𝒩𝒯𝐸𝑅𝑅𝒰𝒫𝒯 𝒴𝒪𝒰 𝒯𝐻𝐸𝑅𝐸, 𝐵𝒰𝒯 𝒯𝒪 𝒞𝒪𝒩𝒯𝐼𝒩𝒰𝐸 𝐹𝒰𝑅𝒯𝐻𝐸𝑅, 𝒴𝒪𝒰 𝒩𝐸𝐸𝒟 𝒯𝒪 𝒥𝒪𝐼𝒩 𝒪𝒰𝑅 𝒞𝐻𝒜𝒩𝒩𝐸𝐿 𝐹𝐼𝑅𝒮𝒯 🫶")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "💀 𝒲𝐻𝒴 𝐼𝒩 𝒯𝐻𝐸 𝒲𝒪𝑅𝐿𝒟 𝒲𝐼𝐿𝐿 𝒴𝒪𝒰 𝑀𝐸𝒮𝒮𝒜𝒢𝐸 𝑀𝐸?? 𝐼'𝑀 𝒥𝒰𝒮𝒯 𝒜 𝐹𝐼𝐿𝐸 𝒮𝐻𝒜𝑅𝐸 𝐵𝒪𝒯 𝒲𝒪𝑅𝒦𝐼𝒩𝒢 𝐹𝒪𝑅 InfoHub Networks!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6011680723)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
