import discord
import random
import time
import asyncio
import datetime
TOKEN = ""
client = discord.Client()
count = 0

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = discord.Object(id='491008546733817856')
    while not client.is_closed:
        songs = open("songs.txt", "r")
        song = songs.readlines()
        date_now = datetime.datetime.now()
        c_date = datetime.datetime(2018, 12, 25) - date_now
        c_days = c_date.days
        c_hour = date_now.hour
        if c_hour == 0 :
            global count
            try: song[count]
            except NameError: song_state_a = None
            if song_state_a == None:
                count = 0
            msg = ("There are " + str(c_days) + " left until Christmas. Here's a Christmas song to get you into the spirit: " + song[count]).format(message)
            count += 1
            await client.send_message(channel, msg)
        time.sleep(1)

@client.event
async def on_message(message):
    if message.content.startswith('!christmas'):
        song_state_b = 1
        c_date = datetime.datetime(2018, 12, 25) - datetime.datetime.now()
        c_days = c_date.days
        songs = open("songs.txt", "r")
        song = songs.readlines()
        global count
        try: song[count]
        except NameError: song_state_b = None
        if song_state_b == None:
            count = 0
        msg = ("There are " + str(c_days) + " left until Christmas. Here's a Christmas song to get you into the spirit: " + song[count]).format(message)
        count += 1
        await client.send_message(message.channel,msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
