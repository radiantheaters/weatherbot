import requests, json
import discord
from discord.ext import commands

token = "ODA3ODExNDgzNjM0ODkyODIw.YB9bEg.ExQIMMgAoJYiI8IqJAD9xY7JW8I"
bot = commands.Bot(command_prefix="w!")

#openweathermap data
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "d8ba273b04593acbd5b7516222b743ab"
#openweathermap data

@bot.event
async def on_ready():
    print("WeatherBot - bot is ready")

@bot.command(aliases=["weather", "w", "getweather"])
async def get_weather(ctx, *, city_loc):
    LOCATION = city_loc
    URL = BASE_URL + "q=" + LOCATION + "&appid=" + API_KEY

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        report = data['weather'][0]['main']
        report_description = data['weather'][0]['description']
        print(report + "\n" + report_description)
        embed = discord.Embed(title="Weather Report", description="Weather Report: " + report + " - " + report_description + "\n\n" + LOCATION)
        await ctx.send(embed = embed)
    else:
        embed2 = discord.Embed(title="Weather Report Error", description="Weather Report Error: Failed to get data - Make sure you have made no spelling errors" + "\n\n" + LOCATION)
        await ctx.send(embed = embed2)

bot.run(token)