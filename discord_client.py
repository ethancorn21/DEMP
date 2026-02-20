#interacts with discord API to get/send messages

import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_message(message): 
    if message.author.id == client.user.id:                     #bot does not reply to self
        return

    if message.content.startswith("!start"):
        await start_chat(message)

async def start_chat(message):
    await message.reply("starting chat...", mention_author = True)

    user_1 = await client.fetch_user(int(os.getenv("USER_ID_MAIN")))
    user_2 = message.author

    global dm_channel_1
    global dm_channel_2
    dm_channel_1 = await user_1.create_dm()
    dm_channel_2 = await user_2.create_dm()

    await dm_channel_1.send(f"connected to {user_2}")
    await dm_channel_2.send(f"connected to {user_1}")


"""
    if message.content.type == discord.ChannelType.private:
        on_dm(message)

async def on_dm(message):
        if message.author.id == 
        message.content
"""
client.run(os.getenv("BOT_TOKEN"))

# get user id
# create dm channel
# send message to that channel (message_operations will handle this)