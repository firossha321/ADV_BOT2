import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6834853102:AAFgAgU7nmAnezFaGKEhIEcEWEg7v67hc6k")

API_ID = int(os.environ.get("API_ID", "17432758"))

API_HASH = os.environ.get("API_HASH", "c9e31fda0ce722e3f3033a9d4f140783")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6103642139').split()]

DB_URL = os.environ.get("DB_URL", "mongodb+srv://firossha321:firossha321@cluster0.xdtpx.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "Cluster0")

RemoveBG_API = os.environ.get("RemoveBG_API", "")

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL","-1002031293626")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""












