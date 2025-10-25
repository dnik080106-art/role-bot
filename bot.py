import discord
import os
from discord.ext import commands
from discord import Embed

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='ipomn ', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("[+] Бот запущен успешно!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ipomn nowoms"))

@bot.command()
async def nowoms(ctx):
    embed = Embed(title="🔄 Помощь по командам", color=0x00FFFF)
    command_list = [
        ("ipomn создать_структуру", "Создает полную структуру ролей"),
        ("ipomn выдать_статус @участник модератор", "Выдает роль"),
        ("ipomn показать_структуру", "Показывает структуру")
    ]
    for cmd, desc in command_list:
        embed.add_field(name=cmd, value=desc, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def создать_структуру(ctx):
    guild = ctx.guild
    
    # Создаем роли если их нет
    roles_to_create = [
        {"name": "Модератор", "color": discord.Color.blue()},
        {"name": "Администратор", "color": discord.Color.red()},
        {"name": "Участник", "color": discord.Color.green()}
    ]
    
    created_roles = []
    for role_data in roles_to_create:
        existing_role = discord.utils.get(guild.roles, name=role_data["name"])
        if not existing_role:
            role = await guild.create_role(name=role_data["name"], color=role_data["color"])
            created_roles.append(role.name)
        else:
            created_roles.append(f"{role_data["name"]} (уже существует)")
    
    await ctx.send(f"✅ Структура ролей создана!\nСозданные роли: {', '.join(created_roles)}")

@bot.command()
@commands.has_permissions(administrator=True)
async def выдать_статус(ctx, member: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await member.add_roles(role)
        await ctx.send(f"✅ Роль {role_name} выдана участнику {member.mention}")
    else:
        await ctx.send(f"❌ Роль {role_name} не найдена")

@bot.command

