# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from AlexaMusic import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**❤️‍🔥 Senin Id**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**💬 Chat Id**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**❤️‍🔥 Senin Id**: `{message.from_user.id}`\n**💬 Chat Id**: `{message.chat.id}`"
        )
