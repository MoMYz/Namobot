from json import load
import discord
import discord, random
import asyncio
from pydoc import cli
from ast import alias
from youtube_dl import YoutubeDL
from music_cog import music_cog
from multiprocessing import get_context
from secrets import choice
from unicodedata import name
from email import message
from re import M
from discord.ext import commands
from discord.utils import get

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
api_key = os.getenv('APIKEY')
api_sec = os.getenv('API_SECRET')

client = discord.Client()
client = commands.Bot(command_prefix='!')

client.remove_command("help")

client.add_cog(music_cog(client))

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Namolnwza007 | !command"))

@client.command()
async def botdev(context):
    
    print('here')
    myEmbed = discord.Embed(title='Bot developer:', description='Pun Srimuangwong',color=0x66CD00)
    myEmbed.add_field(name="Bot version:", value="V.3.0.1", inline=False)
    myEmbed.set_author(name="MoMYz")
    myEmbed.add_field(name="Date released:", value="26 March 2022", inline=False)
    
    await context.message.channel.send(embed=myEmbed)

@client.command()
async def namotwitch(context):
    print('here')
    await context.send("https://www.twitch.tv/momyzch")
    
    await client.process_commands(message)

@client.command()
async def namoig(context):
    print('here')
    await context.send("https://www.instagram.com/namo_pun/")
    
    await client.process_commands(message)

@client.command()
async def namoyt(context):
    print('here')
    await context.send("https://www.youtube.com/channel/UCWBSrFL8YQpzqYASxaWxtAQ")
    
    await client.process_commands(message)

@client.command()
async def kuy(context):
    await context.send(f"fuck you! \U0001F595 {context.author.mention}")

@client.command()
async def playlist(context):
    await context.send(f"{context.author.mention} https://open.spotify.com/playlist/2r8ETdblQPWw3917iuDIqQ?si=26e99fd0b88d4908")

@client.command()
async def ความเหลี่ยม(context):
    ans4 = random.randint(0,100)
    await context.send(f"คุณ {context.author.mention} มีความเหลี่ยม " + str(ans4) + "%")

@client.command()
async def ความเหลี่ยมของ(context, p5: discord.Member):
    player5 = p5
    ans = random.randint(0,100)
    await context.send('ความเหลี่ยมของ <@' + str(player5.id) + '>คือ' + str(ans) + '%')

@client.command()
async def ต่อยกับ(ctx, p1: discord.Member):
    player1 = p1
    choices = ("คุณต่อย <@" + str(player1.id) + ">ปากแตก \U0001F3C6","คุณโดน <@" + str(player1.id) + ">ต่อยปากแตก \U0001F915", "คุณโดน <@" + str(player1.id) + ">เตะก้านคอ \U0001F915", "คุณเตะก้านคอ <@" + str(player1.id) + ">\U0001F3C6", 'น็อคคู่ \U0001F915')
    ans = random.choice(choices)
    await ctx.send(ans)      

@client.command()
async def randomnumber10(context):
    ans2 = random.randint(1,10)
    await context.send(ans2)

@client.command()
async def randomnumber100(context):
    ans3 = random.randint(1,100)
    await context.send(ans3)

@client.command()
async def command(context):
    print('here')
    myEmbed = discord.Embed(title='Bot command:', description='All avaliable command',color=0x66CD00)
    myEmbed.add_field(name='!botdev', value='Bot developer', inline=False)
    myEmbed.add_field(name='!namotwitch', value='My twitch', inline=False)
    myEmbed.add_field(name='!namoig', value='My instagram', inline=False)
    myEmbed.add_field(name='!kuy', value='ด่าบอท', inline=False)
    myEmbed.add_field(name='!ต่อยกับ (mention someone)', value='ต่อยกับใครก็ได้', inline=False)
    myEmbed.add_field(name='!ความเหลี่ยม', value='เช็คความเหลี่ยมของคุณ', inline=False)
    myEmbed.add_field(name='!randomnumber10', value='Random number 1-10', inline=False)
    myEmbed.add_field(name='!randomnumber100', value='Random number 1-100', inline=False)

    await context.message.channel.send(embed=myEmbed)
    
@client.event
async def on_message(message):
    
    bot = f'<@!{client.user.id}>'
    if message.content == bot:
        choicess = (f"ว่าไงวัยรุ่น {message.author.mention}", f"ครับท่าน {message.author.mention}")
        ans3 = random.choice(choicess)
        print(message.channel)
        await message.channel.send(ans3)        

    if message.content == 'ควาย':
        print(message.channel)
        await message.channel.send(f" {message.author.mention}")               

    if message.content == 'นะโม':
        print(message.channel)
        await message.channel.send('นะโม ตัสสะ ภะคะวะโต อะระหะโต สัมมาสัมพุทธัสสะ \U0001F64F')

    if message.content == 'ปัป':
        print(message.channel)
        await message.channel.send('ชื่อกูเขียนอย่างนี้ไอสัส "ปั๊ป"')   

    if message.content == 'ปั๊ป':
        print(message.channel)
        await message.channel.send('กะหรี่ปั๊ป')

    if message.content == 'นน':
        print(message.channel)
        await message.channel.send('ไถนาอยู่ครับพรี่')

    if message.content == 'โง่':
        print(message.channel)
        await message.channel.send('ไปนอนไอ้เด็กเหี้ย')

    if message.content == 'ตุลย์':
        print(message.channel)
        await message.channel.send('กูว่าแล้ว/กูคิดไว้แล้ว')
    
    if message.content == 'หลวงปู่ทัช':
        print(message.channel)
        await message.channel.send('หลวงปู่ทัช > พระพุทธเจ้า > พระเยซู > อัลเลาะห์')

    if message.content == 'นีล':
        print(message.channel)
        await message.channel.send('ไถนาอยู่กับพี่นนครับ')

    if message.content == 'gg':
        print(message.channel)
        choicesss = ("ez", "wp")
        ans4 = random.choice(choicesss)
        await message.channel.send(ans4)

    if message.content == 'ขอบคุณ':
        print(message.channel)
        choicessss = ("ยินดีครับ", "ยินดีครับ แต่ทีหลังไม่ต้อง")
        ans6 = random.choice(choicessss)
        await message.channel.send(ans6)      

    await client.process_commands(message)

client.run(os.environ['token'])
