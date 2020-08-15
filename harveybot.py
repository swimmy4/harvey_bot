import os
import discord
import random

client = discord.Client()

path = r"/Users/moreycn/Desktop/steves"
imgs = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "show me harvey" in message.content:
        d = random.choice(imgs)
        filepath = r"/Users/moreycn/Desktop/steves/" + d
        await message.channel.send(file=discord.File(filepath))



client.login(process.env.NzQ0MDkyOTcyNjM5MDU5OTY4.XzeMlQ.MbTw3RRL5f6hXAkYbUGr0xc9kkc)
