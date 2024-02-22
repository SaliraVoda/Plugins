import os
import re

import requests
from telethon.utils import get_extension
from TelethonHell.plugins import *


@hell_cmd(pattern="paste(?:\s|$)([\s\S]*)")
async def _(event):
    hell = await eor(event, "`Pasting ....`")
    lists = event.text.split(" ", 1)
    reply = await event.get_reply_message()
    if not reply and not len(lists) == 2:
        return await parse_error(hell, "Nothing given to paste.")
    if len(lists) == 2:
        ext = re.findall(r"~\w+", lists[1])
        input_str = lists[1]
        try:
            extension = ext[0].replace("~", "")
            input_str = lists[1].replace(ext[0], "").strip()
        except IndexError:
            extension = None
    else:
        input_str = None
        extension = None
    text_to_print = ""
    if input_str:
        text_to_print = input_str
    if text_to_print == "" and reply.media:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
            if extension is None:
                extension = get_extension(reply.document)
            with open(d_file_name, "r") as f:
                text_to_print = f.read()
        else:
            return await parse_error(hell, "Reply to a document only.")
    if text_to_print == "":
        if reply.text:
            text_to_print = reply.raw_text
        else:
            return await parse_error(hell, "Nothing to paste.")
    if extension and extension.startswith("."):
        extension = extension[1:]
    try:
        response = await pasty(event, text_to_print, extension)
        if "error" in response:
            return await parse_error(hell, "Error while pasting text.")
        result = f"<b><i>📍 Pasted To</i> <a href={response['url']}>Here</a></b>"
        if response["raw"] != "":
            result += f"\n<b><i>📃 Raw link:</i> <a href={response['raw']}>Raw</a></b>"
        await hell.edit(result, link_preview=False, parse_mode="html")
    except Exception as e:
        await parse_error(hell, e)





CmdHelp("paste").add_command(
    "paste", "<reply> or <text ~txt>", "Create a paste or a shortened url using pasty.lus.pm"
).add_info(
    "Paste contents to a pastebin."
).add_warning(
    "✅ Harmless Module."
).add()
