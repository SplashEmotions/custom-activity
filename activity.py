from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import discord

Client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Установка активности!") # увед. о начале работы

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    activity = discord.Game("шо случиас") # суда название активности
    await bot.change_presence(activity=activity)
    print("Активность установлена") # уведомление о установлении активности

bot.run("discord_token") #суда ваш токен