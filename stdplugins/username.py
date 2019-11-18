import os
from telethon import events
from uniborg.util import admin_cmd
from telethon.tl import functions
from telethon.tl.functions.account UpdateUsernameRequest


USERNAME_UPDATED = "```Username Successfully Updated.```"
USERNAME_DENIED = "```This Username Already Reserved.```"



@borg.on(admin_cmd(pattern="usr"))
async def update_username(username):

    newusername = username.pattern_match.group(1)
    try:
        await borg(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_UPDATED)
    except UsernameOccupiedError:
        await username.edit(USERNAME_DENIED)

