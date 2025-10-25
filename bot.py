import discord
import os
from discord.ext import commands
from discord import Embed

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!роли ', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'✅ Организатор ролей запущен!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!роли помощь"))

@bot.command()
async def помощь(ctx):
    embed = Embed(title="🛠️ Помощь по командам", color=0x00FFFF)
    commands_list = [
        ("🎯 `!роли создать_структуру`", "Создает полную структуру ролей"),
        ("👑 `!роли выдать_статус @участник модератор`", "Выдает роль"),
        ("📊 `!роли показать_структуру`", "Показывает структуру")
    ]
    for cmd, desc in commands_list:
        embed.add_field(name=cmd, value=desc, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def создать_структуру(ctx):
    structure = {
        '👑 Основатель': 0xFFD700,
        '🤖 Боты сервера': 0x7289DA, 
        '🛡️ Модераторы': 0x00FF00,
        '💎 Абсолютные': 0xFF69B4,
        '✨ Мифические': 0x9932CC
    }
    
    for role_name, color in structure.items():
        existing_role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not existing_role:
            await ctx.guild.create_role(name=role_name, color=discord.Color(color), hoist=True)
    
    await ctx.send("✅ Структура ролей создана!")

token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
