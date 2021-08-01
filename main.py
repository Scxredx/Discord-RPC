from pypresence import Presence
from time import time
 
RPC = Presence("client id from https://discord.com/developers/applications")
btns = [
    {
        "label": "Invite Bot <3",
        "url": "https://discord.com/api/oauth2/authorize?client_id=851444367250948136&permissions=8&scope=bot%20applications.commands"
    },
    {
        "label": "Join Server",
        "url": "https://discord.gg/WNWAUsDQPY"
    }
]
 
RPC.connect()
RPC.update(
    state="With many nice commands ^^",
    details="Sleepy Discord Bot <3",
    start=time(),
    buttons=btns,
    large_image="sleepy",
    small_image="sleepy",
    large_text="Sleepy <3",
    small_text="Sleepy <3"
)
 
input()

#U can change anything <3

#Made by | Scxred#8967 |