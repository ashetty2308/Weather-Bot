import discord
import requests, json


client = discord.Client()


@client.event
async def on_ready():
    print("{0.user}".format(client))

@client.event
async def on_message(message):

    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message}: ({channel})')

    city = user_message[1:]

    if message.author == client.user:
        return
    elif message.author != client.user:
        api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7e3eac24249fda8fc39ac0f291163bb2&units=imperial"
        response = requests.get(api_url)
        final_resp = response.json()
        await message.channel.send(final_resp)
        return


client.run(TOKEN)
