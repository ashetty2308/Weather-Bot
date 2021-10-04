import discord
import requests, json

TOKEN = 'ODk0MjM5MTIzNzE4Njk3MDIw.YVnHFQ.OOeNeu-kcX5z0S_78FgKwm3ey6s'

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


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
        api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7e3eac24249fda8fc39ac0f291163bb2&units=imperial"
        response = requests.get(api_url)
        final_resp = response.json()

        temperature = final_resp['main']['temp']

        if user_message.__contains__('!'):

            temperature_display = 'Temperature: ' + str(temperature)

            if temperature >= 85:
                my_embed = discord.Embed(title='Weather in ' + city.title(), description=temperature_display,
                                         color=0x00ff00)
            elif temperature >= 65:
                my_embed = discord.Embed(title='Weather in ' + city.title(), description=temperature_display,
                                         color=0x00ff00)
            elif temperature > 45:
                my_embed = discord.Embed(title='Weather in ' + city.title(), description=temperature_display,
                                         color=0x00ff00)
            else:
                my_embed = discord.Embed(title='Weather in ' + city.title(), description=temperature_display,
                                         color=0x00ff00)

            await message.channel.send(embed=my_embed)

        elif not user_message.__contains__('!'):
            await message.channel.send("Try again! Please add the ! command before the city.")


client.run(TOKEN)
