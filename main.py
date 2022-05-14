import discord, asyncio, datetime, zipfile, os
from datetime import datetime
from discord_components import DiscordComponents

client = discord.Client()

@client.event
async def on_ready():
    DiscordComponents(client)
    print(f"Login: {client.user}/nInvite Link: https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")
    while True:
        await client.change_presence(activity=discord.Game(f"F SERVICE - KRㅣ데이터베이스 백업"), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(f"F SERVICE - KRㅣ데이터베이스 백업"), status=discord.Status.online)
        await asyncio.sleep(5)

@client.event
async def on_message(message):
    if message.author.bot or message.author.id != int():
        return
    if message.content == ".데이터백업":

            # 데이터 베이스 파일 압축하기
            os.chdir('경로')
            db_zip = zipfile.ZipFile('DB.zip', 'w')
        
            for folder, subfolders, files in os.walk('경로'):
                for file in files:
                    if file.endswith('.db'):
                        db_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file)))
            db_zip.close()
            os.chdir('경로')
            lc_zip = zipfile.ZipFile('LICENSE.zip', 'w')
            lc_zip.write('license.db')
            lc_zip.close()
            now_time = str(datetime.now())
            await message.reply(embed=discord.Embed(title='```⭐ 데이터베이스 백업이 시작되었습니다.```',description='```데이터 백업 시간 : ' + now_time + '```', color=0x70c0ff)) 
            await client.get_channel(int(972469774183432243)).send(embed=discord.Embed(title='```⭐ 데이터베이스 백업이 시작되었습니다.```',description='```백업 시작 시간 : ' + now_time + '```', color=0x70c0ff))
            await message.channel.send(file=discord.File("경로/DB.zip"))
            await message.channel.send(file=discord.File("경로/LICENSE.zip"))
            os.remove("경로/DB.zip")
            os.remove("경로/LICENSE.zip")
            finish_time = str(datetime.now())
            await client.get_channel(int()).send(embed=discord.Embed(title='```⭐ 데이터베이스 백업이 완료되었습니다.```',description='```백업 완료 시간 : ' + finish_time + '```', color=0x70c0ff))
        


client.run('')
