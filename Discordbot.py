from multiprocessing import get_context
from secrets import choice
from unicodedata import name
import discord
import discord, random
from email import message
from re import M
from discord.ext import commands
from discord.utils import get

client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.command()
async def botdev(context):
    
    print('here')
    myEmbed = discord.Embed(title='Bot developer:', description='Pun Srimuangwong',color=0x66CD00)
    myEmbed.add_field(name="Bot version:", value="V.1.0.4", inline=False)
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
async def on_ready():
    general_channel = client.get_channel(598821748984774656)
    await general_channel.send("Namolnwza007 bot is now online \U0001F7E2")

@client.event
async def on_message(message):
    
    bot = f'<@!{client.user.id}>'
    if message.content == bot:
        choicess = (f"ว่าไงวัยรุ่น {message.author.mention}", f"ครับท่าน {message.author.mention}", f"Do {message.author.mention} need something?")
        ans3 = random.choice(choicess)
        await message.channel.send(ans3)        

    if message.content == 'ควาย':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('นน \U0001F403')               

    if message.content == 'นะโม':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('นะโม ตัสสะ ภะคะวะโต อะระหะโต สัมมาสัมพุทธัสสะ \U0001F64F')

    if message.content == 'ปัป':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('ชื่อกูเขียนอย่างนี้ไอสัส "ปั๊ป"')   

    if message.content == 'ปั๊ป':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('กะหรี่ปั๊')

    if message.content == 'นน':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('ไถนาอยู่ครับพรี่')

    if message.content == 'โง่':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('ไปนอนไอ้เด็กเหี้ย')

    if message.content == 'ตุลย์':
        general_channel = client.get_channel(598821748984774656)
        await general_channel.send('กูว่าแล้ว/กูคิดไว้แล้ว')

    await client.process_commands(message)

client.run('OTU2OTM3MTE1NDQ1MzgzMjc5.Yj3fIw.AsnEq7e5Id_7gc5tDyefZTRVJxw')
