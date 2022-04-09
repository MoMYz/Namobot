from json import load
import discord
import discord, random
import asyncio
from discord.utils import get
from pydoc import cli
from ast import alias
from youtube_dl import YoutubeDL
#from music_cog import music_cog
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

#client.add_cog(music_cog(client))

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Namolnwza007 | !command"))

@client.command()
async def botdev(context):
    
    myEmbed = discord.Embed(title='Bot developer:', description='<@462935839379292160>',color=0x66CD00)
    myEmbed.add_field(name="Bot version:", value="V.3.0.1", inline=False)
    myEmbed.set_author(name="Namo")
    myEmbed.add_field(name="Date released:", value="26 March 2022", inline=False)
    
    await context.message.channel.send(embed=myEmbed)

@client.command()
async def twitch(context):
    await context.send("https://www.twitch.tv/momyzch")
    
    await client.process_commands(message)

@client.command()
async def ig(context):
    await context.send("https://www.instagram.com/namo_pun/")
    
    await client.process_commands(message)

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
    choices = ("คุณต่อย <@" + str(player1.id) + ">ปากแตก แล้วกระทืบซ้ำ \U0001F3C6","คุณโดน <@" + str(player1.id) + ">ซัดหน้า ฟันหลุด 2 ซี่ \U0001F915", "คุณโดน <@" + str(player1.id) + ">เตะก้านคอ \U0001F915", "คุณเตะก้านคอ <@" + str(player1.id) + ">\U0001F3C6", 'น็อคคู่ \U0001F915')
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
    
    myEmbed = discord.Embed(title='Bot command \U0001F916:', description='All avaliable command',color=0x66CD00)
    myEmbed.add_field(name='!botdev', value='Bot developer', inline=False)
    myEmbed.add_field(name='!twitch', value='My twitch', inline=False)
    myEmbed.add_field(name='!ig', value='My instagram', inline=False)
    myEmbed.add_field(name='!kuy', value='ด่าบอท', inline=False)
    myEmbed.add_field(name='!ต่อยกับ (mention someone)', value='ต่อยกับใครก็ได้', inline=False)
    myEmbed.add_field(name='!ความเหลี่ยม', value='เช็คความเหลี่ยมของคุณ', inline=False)
    myEmbed.add_field(name='!randomnumber10', value='Random number 1-10', inline=False)
    myEmbed.add_field(name='!randomnumber100', value='Random number 1-100', inline=False)

    await context.message.channel.send(embed=myEmbed)

@client.command()
async def song(context):

    aEmbed = discord.Embed(title='Song command \U0001F3B6:', description='All avaliable song command',color=0x66CD00)
    aEmbed.add_field(name='!play or !p <song name>', value='play song', inline=False)
    aEmbed.add_field(name='!pause', value='pause current song', inline=False)
    aEmbed.add_field(name='!resume', value='resume current song', inline=False)
    aEmbed.add_field(name='!skip', value='skip current song', inline=False)
    aEmbed.add_field(name='!queue or !q', value='all song in queue', inline=False)
    aEmbed.add_field(name='!leave', value='kick bot from voice chat', inline=False)
    
    await context.message.channel.send(embed=aEmbed)

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
        await message.channel.send(f"\U0001F449 {message.author.mention}")               

    if message.content == 'ใครหล่อที่สุด':
        print(message.channel)
        await message.channel.send("<@462935839379292160>")

    if message.content == 'ใครเหลี่ยมที่สุด':
        print(message.channel)
        await message.channel.send("<@860033778072551444>")

    if message.content == 'นะโม':
        print(message.channel)
        await message.channel.send('นะโม ตัสสะ ภะคะวะโต อะระหะโต สัมมาสัมพุทธัสสะ \U0001F64F')

    if message.content == 'กวิสรา':
        print(message.channel)
        await message.channel.send('กวิสราเป็นนางฟ้าที่สวยเเละน่ารักที่สุดในจักรวาลนี้เเละจักรวาลหน้า \U0001F607')

    if message.content == 'สิริกาญจน์':
        print(message.channel)
        await message.channel.send('โสด น่ารัก เลี้ยงหมาเก่ง \U0001F415') 

    if message.content == 'ภทรวรรณ':
        print(message.channel)
        await message.channel.send('ภทรวรรณสวยที่สุดในโลก \U0001F60F')
    
    if message.content == 'ไข่มุก':
        print(message.channel)
        await message.channel.send('โฮ่งๆ  //กัดโซฟาอยู่ \U0001F415')

    if message.content == 'ธนวิน':
        print(message.channel)
        await message.channel.send('ทำไมธนวินเท่จัง')

    if message.content == 'โง่':
        print(message.channel)
        await message.channel.send('ไปนอนไอ้เด็กเหี้ย')

    if message.content == 'เกินปุยมุ้ย':
        print(message.channel)
        await message.channel.send('เกินอะไร เดี๋ยวตบปาก')

    if message.content == 'ฝันดี':
        print(message.channel)
        await message.channel.send('ฝันดีครับ \U0001F319')
        
    if message.content == '555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == '5555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == '55555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == '555555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == '5555555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == '55555555':
        print(message.channel)
        await message.channel.send('ขำมากมั้ง')

    if message.content == 'gg':
        print(message.channel)
        choicesss = ("ez", "wp")
        ans4 = random.choice(choicesss)
        await message.channel.send(ans4)

    if message.content == 'ใครจะได้แชมป์พรีเมียร์ลีก':
        print(message.channel)
        choice1 = ("ลิเวอร์พูล \U0001F534", "ไม่ใช่แมนยู \U0000274C", "ไม่ใช่แมนซิตี้ \U0001F535")
        ans7 = random.choice(choice1)
        await message.channel.send(ans7)

    if message.content == 'ขอบคุณ':
        print(message.channel)
        choicessss = ("ยินดีครับ", "ยินดีครับ แต่ทีหลังไม่ต้อง")
        ans6 = random.choice(choicessss)
        await message.channel.send(ans6)      

    await client.process_commands(message)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

client.run(os.environ['token'])
