import discord
import requests
import os

TOKEN = "MTQ3MDk5MjYzNzEyMDIxNzE3MA.GUgsPL.BOqE3jOSjcN-hQvUjzTyI3ZFhT0sCO1tMULC0k"

AIO_USERNAME = "ppom_ts"
AIO_KEY = "aio_OOGC63arpHjJiBdG5dKVLgYdjPaY"
FEED_NAME = "fear"

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
    requests.post(url, json=data, headers=headers)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg == "!on":
        send_to_adafruit("ON")
        await message.channel.send("รีเลย์เปิดแล้ว ✅")

    elif msg == "!off":
        send_to_adafruit("OFF")
        await message.channel.send("รีเลย์ปิดแล้ว ❌")

client.run(TOKEN)
