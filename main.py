import discord, random
import sll
from discord.ext import commands
from config import settings, TOKEN

bot = commands.Bot(command_prefix='!')#префикс для команд

@bot.command()
async def bot_on(ctx):
    await ctx.send('Working-hard')

@bot.command()
async def cmd(text):
    await text.send('Мои команды:\n1. !EGE *предмет* *номер задания* - выдает url ссылку на сайт решу ЕГЭ\n2. !bot_on - выводит статус бота, если он работает')

@bot.command()
async def hello(hi):
    author = hi.message.author
    await hi.send(f'go in peace, {author.mention}!')

@bot.command()
async def EGE(_, subject, exercise_number):
    author = _.message.author
    exercise_number=str(exercise_number)
    url = 'https://'
    url2 = 'ege.sdamgia.ru/'
    ex_index = random.randint(0, (len(sll.all_tasks[subject][exercise_number])-1))
    url_fin = url + sll.get_url[subject] + url2 + 'test?theme=' + sll.all_tasks[subject][exercise_number][ex_index]
    await _.send("{1}! Вот твой URL: {0}".format(url_fin, author.mention))

@bot.command()
async def getnumurl(_, subject, exercise_number):
    author = _.message.author
    exercise_number=str(exercise_number)
    url = 'https://'
    url2 = 'ege.sdamgia.ru/problem?id='
    url_fin = url + sll.get_url[subject] + url2 + exercise_number
    await _.send("{1}! Вот твой URL: {0}".format(url_fin, author.mention))

bot.run(TOKEN)

'''TO-DO LIST:
0. ввод будет тип: "!geturl *предмет* *номер задания*" COMPLETED
1. прислать url к номерам ЕГЭ COMPLETED
2. ввод для отдельного задания !getnumurl *предмет* *номер задания* COMPLETED
3. сделать ссылку на вариант 
'''