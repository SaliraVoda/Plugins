import os
import base64
import ipaddress
import random
import struct

try:
    from pyrogram import Client as PClient
except:
    os.system("pip install pyrogram")
    from pyrogram import Client as PClient

try:
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient


def main():
    while True:
        print("T E A M    E X T E N D E D   ! !")
        print("Hello!! Welcome to Extended Session Generator\n")
        if generate_extended_session():
            print("\nYour EXTENDED SESSION is saved in your Telegram saved messages.")
            break
        else:
            print("Done!!")  #done/error

def generate_extended_session():
    print("!!! Extended SESSION !!!")
    print("One session for all Extended Project.")
    api_id = int(input("\nEnter APP ID here: "))
    api_hash = input("\nEnter API_HASH here: ")
    with PClient(name="extuser", api_id=api_id, api_hash=api_hash, in_memory=True) as ext:
        print("\nYour Extended SESSION is saved in your telegram saved messages.")
        _session = ext.export_session_string()
        ext_session = extended_session(_session)
        ext.send_message(
            "me",
            f"#EXTENDED_SESSION \n\n`{ext_session}`",
        )



def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


def extendedbot(text):
    res = ''.join(
        map(
            random.choice,
            zip(text.lower(), text.upper()),
        )
    )
    return res.strip()


def extended_session(session):
    pyro_format = {
        351: ">B?256sI?",
        356: ">B?256sQ?",
        362: ">BI?256sQ?",
    }

    ipv4_dc = {
        1: "149.154.175.53",
        2: "149.154.167.51",
        3: "149.154.175.100",
        4: "149.154.167.91",
        5: "91.108.56.130",
    }

    error_msg = "Error in generating session! Report it in extended Chats"

    # converting session
    if len(session) in pyro_format.keys():
        if len(session) in [351, 356]:
            dc_id, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )
        else:
            dc_id, _, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )

        new_session = CURRENT_VERSION + StringSession.encode(
            struct.pack(
                _STRUCT_PREFORMAT.format(4),
                dc_id,
                ipaddress.ip_address(ipv4_dc[dc_id]).packed,
                443,
                auth_key
            )
        )
        return f"=={extendedbot('extd')}{new_session}{extendedbot('bot')}=="
    else:
        return error_msg


main()


#patched by hellbot extended team !!!
