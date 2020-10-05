# Bot information
SESSION ='Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'

# Bot settings
MAX_RESULTS = 10
CACHE_TIME = 300

# Admins & Channels
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME ='channel_files' # If you going to use same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I am Game Searcher bot**
@BLACKPSYCHOBOT 
I will send apk to you. Install it. 
Here you can search Games in inline mode. Just press follwing buttons and start searching. Can't find desired game? Then contact @Darklester and request your game name. 
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
