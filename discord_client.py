#interacts with discord API to get/send messages
import discord
import os
from dotenv import load_dotenv
from message_operations import encapsulated_message

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_message(message): 
    if message.author.id == client.user.id:      #bot does not reply to self
        return

    if message.content.startswith("!start"):
        await start_chat(message)
    if message.channel.type == discord.ChannelType.private:
        await send_chat(message)

async def start_chat(message):
    await message.reply("starting chat...", mention_author = True)

    global user_1
    global user_2
    user_1 = await client.fetch_user(int(os.getenv("USER_ID_MAIN")))
    user_2 = message.author

    global dm_channel_1
    global dm_channel_2
    dm_channel_1 = await user_1.create_dm()
    dm_channel_2 = await user_2.create_dm()

    await dm_channel_1.send(f"relaying to {user_2}")
    await dm_channel_2.send(f"relaying to {user_1}")
    print("connected...")

async def send_chat(message):
    try:
        if message.author == user_2:
            await dm_channel_1.send(encapsulated_message(message))
            print(f"{message.author} {message.created_at} : {message.content}")
        else:
            await dm_channel_2.send(encapsulated_message(message))
            print(f"{message.author} {message.created_at} : {message.content}")
    except NameError:
        print("Please initiate in server first")
        await message.channel.send("Please initiate in server first")

    
client.run(os.getenv("BOT_TOKEN"))