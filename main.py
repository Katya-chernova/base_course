import asyncio 
from aiogram import Bot, Dispatcher, F 
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command 
 
 
bot = Bot(token='7874921859:AAGmwYvEWyPyPwELdp5CLU7y8ZeLhtW-hdY') 
dp = Dispatcher() 
 
@dp.message(CommandStart()) 
async def cmd_starts(message: Message): 
    await message.answer('Привет!') 
    await message.reply('Как дела?') 
 
@dp.message(Command('help')) 
async def cmd_help(message: Message): 
    await message.answer('Вы нвжали на кнопку помощи')

@dp.message(F.text == 'У меня все хорошо') 
async def nice(message: Message): 
    await message.answer('Я очень рад') 
 
 
async def main(): 
    await dp.start_polling(bot) 
     
     
if __name__ == '__main__': 
    try: 
        asyncio.run(main()) 
    except KeyboardInterrupt: 
        print('Бот выключен')