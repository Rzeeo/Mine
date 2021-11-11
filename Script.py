class script(object):
    START_TXT = """<b>Hello {},
ഈ ബോട്ട് മൂവി ക്ലബ്‌ ഗ്രൂപ്പിലേക്ക് ഉള്ളത് എന്ന് ഇനി വീണ്ടും വീണ്ടും പറയണോ??
അപ്പോ പിന്നെ എന്തിനാ വീണ്ടും വീണ്ടും സ്റ്റാർട്ട് കുത്തി കളിക്കാൻ വരുന്നേ... എന്തായാലും സ്റ്റാർട്ട് അടിച്ചതല്ലെ ഇനി ആ താഴെ കാണുന്ന നമ്മുടെ ഒഫീഷ്യൽ ചന്നെൽ കൂടി Subscribe ചെയ്തിട്ട് പൊക്കോ 😎😎</b>"""
    HELP_TXT = """<b>Hey {}
Here Is The Help For My Commands.</b>"""
    ABOUT_TXT = """
<b>➥  My Name</b> : <b><i><a href="https://t.me/MC_MovieBot">Mᴏᴠɪᴇ Bᴏᴛ 😎</a></i></b>
<b>➥  Owner</b> : <b><i><a href="https://t.me/NickxFury">Nɪᴄᴋ Fᴜʀʏ 🇮🇳</a></i></b>
<b>➥ Credits</b> : <code>Everyone in this journey</code>
<b>➥ Data base</b> : <b><a href="https://www.mongodb.com/">MongoDB</a></b>
<b>➥ Language</b> : <code>Python3</code>
<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>
<b>➥ Server</b> : <code>AWS</code>
<b>➥ Build Stats</b> : <code>V6.0 [BETA]</code>

©️MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=https://t.me/MOVIECLUB_CHAT>Mᴏᴠɪᴇ Cʟᴜʙ</a>"""
    SOURCE_TXT = """
<b>➥ Source Code</b> : <i><a href="https://github.com/NickxFury/My-Source-Code">Click Me</a></i>
<b>➥ Updates</b> : <i><a href="https://t.me/MCMovieBot">Click Here</a></i>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- <a href=https://t.me/MC_MovieBot>This Bot</a> Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MOVIECLUB_CHAT)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code> 𝙼𝚒𝙱
★ Free Storage: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
