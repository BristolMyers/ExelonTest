# Copyright (C) 2020 BristolMyers
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# ExelonUserBot - BristolMyers

from .. import CMD_HELP
from ..utils import admin_cmd, sudo_cmd
from telethon.tl.types import InputMediaDice

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
# EMOJI CONSTANTS


@borg.on(
    admin_cmd(
        pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI}|{FOOT_E_MOJI}) ?(.*)"))
@bot.on(
    sudo_cmd(
        pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI}|{FOOT_E_MOJI}) ?(.*)",
        allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass


CMD_HELP.update({"dice_dart_ball": "**PLUGİN İSMİ:** `dice_dart_ball`\
      \n\n**📌Komut ➥ **`.🎯` `[1-6]`\
      \n**Kullanım ➥ ** her numara farklı bir animasyon gösterir.\
      \n\n**📌Komut ➥ **`.🎲` `[1-6]`\
      \n**Kullanım ➥ ** her numara farklı bir animasyon gösterir.\
      \n\n**📌Komut ➥ ** `.🏀` `[1-5]`\
      \n**Kullanım ➥ ** her numara farklı bir animasyon gösterir.\
      \n\n**📌Komut ➥ **`.⚽️` `[1-5]`\
      \n**Kullanım ➥ ** her numara farklı bir animasyon gösterir."
                 })
