import discord
from datetime import datetime
id = 713590828056051774

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token=read_token()

client = discord.Client()
member = discord.member
@client.event
async def on_message(message):
    id = client.get_guild(713590828056051774)
    channels = ["comandos"]

    if str(message.channel) in channels:
        if message.content.find("!hola") != -1:
            text = str(message.author)
            print(text)
            text2=""
            carac = len(text)
            for i in range(carac-5):
                print(i)
                text2 += text[i]
            await message.channel.send(f"""Que tal {text2}""")
        elif message.content == "!user":
            await message.channel.send(f"""Usuarios en el server: {id.member_count} """)
        elif message.content == "!mytag":
            await message.channel.send(f"""id ;:v: {message.author}  """)
        elif message.content == "!fecha":
            now = datetime
            if now.hour() == 1 and now.minute() == 52:
                message = 'a'
                await message.channel.send(message)
            time=90
        else:
            time=1









client.run(token)