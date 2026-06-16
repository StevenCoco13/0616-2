import discord

import nest_asyncio

from discord.ext import commands
import google.generativeai as genai
from google.colab import userdata

# 創建一個機器人的實例，指定指令的前綴符號

intents = discord.Intents.default()

intents.members = True

intents.message_content = True # 啟用 message_content 權限

bot = commands.Bot(command_prefix='!', intents=intents)
api_keys = userdata.get('GEMINI_KEY')
genai.configure(api_key=api_keys)

# 初始化時就定義好它是誰
ai_persona = "你是一個年輕很潮的dancer,回復的時候往往會加入一些年輕人的用語"
model = genai.GenerativeModel(
#model_name='gemini-2.5-flash',
model_name='gemini-3.1-flash-lite-preview',
system_instruction=ai_persona
)
chat = model.start_chat(history=[])

# 當機器人成功連線時觸發的事件

@bot.event

async def on_ready():

  print(f'我們已經登入為 {bot.user}')


# 機器人回應 ping 指令

@bot.command()

async def ping(ctx):

  await ctx.send('Pong!')


# 機器人回應回傳訊息的指令

@bot.command()

async def echo(ctx, *, message):

    await ctx.send(message)



# 機器人回應回傳訊息的指令

@bot.command()

async def say(ctx, a, b):
    response = chat.send_message(f"請將我輸入的{a} {b}兩個數字做各種神奇的運算")
    await ctx.send(f"阿吉:{response.text}")





#回應特定訊息 讓機器人在用戶說出特定訊息時觸發回應：

@bot.event

async def on_message(message):

    if message.author == bot.user:

        return

    #如果將收到的訊息轉成小寫後存在hello的字串

    if 'hello' in message.content.lower():

        #向訊息發送者打招呼

        await message.channel.send('Hi ' + str(message.author) + ' !')

    await bot.process_commands(message)




@bot.command()
async def start(ctx, a):
    response = chat.send_message(f"請將我輸入的{a}種類設計為一個海龜湯遊戲,你盡可能只回答是或不是")
    await ctx.send(f"阿吉:{response.text}")

@bot.command()
async def guess(ctx, a):
    response = chat.send_message(a)
    await ctx.send(f"阿吉:{response.text}")













# 使用你的機器人 Token 啟動

nest_asyncio.apply()

bot.run('MTQ5ODYzNjc4OTU4MDE2OTI0Ng.GHB9um.80pdMhk5YagI8D9lppIcjAN1Zc1Rl706ryQdh0')
