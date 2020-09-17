# Copyright (C) 2020 BristolMyers
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# ExelonUserBot - BristolMyers

import re
from userbot import CMD_HELP, fonts
from userbot.utils import admin_cmd
import random


@borg.on(admin_cmd(pattern="str(?: |$)(.*)"))
async def stretch(stret):
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = random.randint(3, 10)
    reply_text = re.sub(
        r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
        (r"\1" * count),
        message
    )
    await stret.edit(reply_text)


@borg.on(admin_cmd(pattern="zal(?: |$)(.*)"))
async def zal(zgfy):
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            randint = random.randint(0, 2)

            if randint == 0:
                charac = charac.strip() + \
                    random.choice(fonts.ZALG_LIST[0]).strip()
            elif randint == 1:
                charac = charac.strip() + \
                    random.choice(fonts.ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + \
                    random.choice(fonts.ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@borg.on(admin_cmd(pattern="cp(?: |$)(.*)"))
async def copypasta(cp_e):
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = random.choice(fonts.EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = random.choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += random.choice(fonts.EMOJIS)
        elif owo in fonts.EMOJIS:
            reply_text += owo
            reply_text += random.choice(fonts.EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(random.getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += random.choice(fonts.EMOJIS)
    await cp_e.edit(reply_text)


@borg.on(admin_cmd(pattern="weeb(?: |$)(.*)"))
async def weebify(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`Ne Weebify Yapmam Gerekiyor `")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in fonts.normiefont:
            weebycharacter = fonts.weebyfont[fonts.normiefont.index(
                normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@borg.on(admin_cmd(pattern="downside(?: |$)(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("Neyi değiştirmem gerekiyor, metin ver")
        return
    string = '  '.join(args).lower()
    for upsidecharacter in string:
        if upsidecharacter in fonts.upsidefont:
            downsidecharacter = fonts.downsidefont[fonts.upsidefont.index(
                upsidecharacter)]
            string = string.replace(upsidecharacter, downsidecharacter)
    await event.edit(string)


@borg.on(admin_cmd(pattern="subscript(?: |$)(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("Neyi değiştirmem gerekiyor, metin ver")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            subscriptcharacter = fonts.subscriptfont[fonts.normaltext.index(
                normaltextcharacter)]
            string = string.replace(normaltextcharacter, subscriptcharacter)
    await event.edit(string)


@borg.on(admin_cmd(pattern="superscript(?: |$)(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("Neyi değiştirmem gerekiyor, metin ver")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            superscriptcharacter = fonts.superscriptfont[fonts.normaltext.index(
                normaltextcharacter)]
            string = string.replace(normaltextcharacter, superscriptcharacter)
    await event.edit(string)


CMD_HELP.update({"funnyfonts": "**PLUGİN İSMİ:** `funnyfonts`\
      \n\n**📌Komut ➥ **`.cp (metin)` veya `.cp mesajı cevapla` \
      \n**Kullanım ➥ ** metinlerin arasına bazı emojiler ekler.\
      \n\n**📌Komut ➥ **`.str (metin)` veya `.str mesajı cevapla`\
      \n**Kullanım ➥ ** Verilen mesajı uzatır.\
      \n\n**📌Komut ➥ **`.zal (metin)` veya `.zal mesajı cevapla` \
      \n**Kullanım ➥ ** Kaos hissini uyandırın.\
      \n\n**📌Komut ➥ **`.weeb (metin)` veya `.weeb mesajı cevapla`\
      \n**Kullanım ➥ ** farklı bir alfabe stili."
                 })
