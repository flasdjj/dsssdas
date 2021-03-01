import discord
import random
client = discord.Client()
token = 'NzA3MTQxODQ3NjY3MTc5NjIz.XrEfKg.yy86-58MmsyEecq_LLUZDJaZylI'

@client.event
async def on_ready():
    print('Client is Ready')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('게임활동'))

@client.event
async def on_message(message):
    if message.content == "관리자출근":
        embed = discord.Embed(colour=0xFF8000, timestamp=message.created_at)
        embed.add_field(name="`관리자 출근안내.`", value="```관리자가 출근하였습니다.```", inline=True)
        embed.set_footer(text=f"{message.author}, 출근완료", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
        await message.channel.send(embed=embed)

    if message.content == "관리자퇴근":
        embed = discord.Embed(colour=0xFF4000, timestamp=message.created_at)
        embed.add_field(name="`관리자 퇴근안내.`", value="```관리자가 퇴근하였습니다.```", inline=True)
        embed.set_footer(text=f"{message.author}, 퇴근완료", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
        await message.channel.send(embed=embed)
       
    if message.content.startswith("신세계도움말"):
        embed=discord.Embed(title="✅신세계 도움말", description="명령어안내", color=0x00ff56)
        embed.set_author(name="신세계 RP", url="https://discord.gg/Tt7sN6BgGd")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
        embed.add_field(name="`!서버온`", value="서버온공지 명령어입니다.", inline=True)
        embed.add_field(name="`!서버오프`", value="서버오프공지 명령어입니다.", inline=True)
        embed.add_field(name="`신세계 인증 @멘션`", value="인증 명령어입니다.", inline=True)
        embed.add_field(name="`신세계 뉴비지원금 @멘션`", value="지원금 완료 명령어입니다.", inline=True)
        embed.set_footer(text="신세계 도움말이였습니다.")
        embed.set_footer(text=f"{message.author}, ㅣ신세계:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
        await message.channel.send(embed=embed) 
        
    if message.content == '!서버온': 
       embed = discord.Embed(title = '🟢 신세계:RP', description = '```🌐 신세계 서버 상태 : ON```', color = discord.Color.green())
       embed.add_field(name = "```🎮접속방법```", value = "```🔵 F8 > connect.준비중```", inline=False)
       embed.set_footer(text=f"{message.author}, ㅣ신세계:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
       await message.channel.send(embed=embed, content = '@everyone') 

    if message.content == '!서버오프': 
       embed = discord.Embed(title = '🔴 신세계:RP', description = '```🌐 신세계 서버 상태 : OFF```', color = discord.Color.red())
       embed.add_field(name = "```🌍리붓중```", value = "```🚨 서버접속을 금지합니다.```", inline=False)
       embed.set_footer(text=f"{message.author}, ㅣ신세계:RPㅣby 시 호 ♰#0096", icon_url=message.author.avatar_url)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/767351094283337758/802942987688345661/124222.png")
       await message.channel.send(embed=embed, content = '@everyone')   

client.run(token)