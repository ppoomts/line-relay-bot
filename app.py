import os
import discord
import requests


TOKEN = os.getenv("DISCORD_TOKEN")
AIO_USERNAME = os.getenv("AIO_USERNAME")
AIO_KEY = os.getenv("AIO_KEY")
FEED_NAME = os.getenv("FEED_NAME")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def send_to_adafruit(value):
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data"
    headers = {
        "X-AIO-Key": AIO_KEY,
        "Content-Type": "application/json"
    }
    data = {"value": value}
    r = requests.post(url, json=data, headers=headers)
    print("Status:", r.status_code)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!on":
        send_to_adafruit("ON")
        await message.channel.send("รีเลย์เปิดแล้ว ✅")

    elif message.content == "!off":
        send_to_adafruit("OFF")
        await message.channel.send("รีเลย์ปิดแล้ว ❌")

client.run(TOKEN)


