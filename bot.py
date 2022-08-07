
#導入 Discord.py
import discord
import random
#client 是我們與 Discord 連結的橋樑
client = discord.Client()
import os
arr = os.listdir('./sponge')
#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message :discord.Message):
    if message.author == client.user:
        return
    ctx = message.content
    pic_list = []
    for i in arr:
        if ctx in i:
            pic_list.append(i)
    try:
        a = random.choice(pic_list)
        print(a)
        await message.channel.send(file =discord.File('./sponge/'+ a))
    except:
        pass
client.run('MTAwNTgwNTE3NjEwMTI3MzY4MQ.GlznKL.FbGl-zXwMHGf1ypbVdSoo7NoJWGVQiFrpYyaCo') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
