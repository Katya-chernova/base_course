import asyncio 
from app.handlers import router

from aiogram import Bot, Dispatcher, F 

async def main(): 
    bot = Bot(token='7874921859:AAGmwYvEWyPyPwELdp5CLU7y8ZeLhtW-hdY') 
    dp = Dispatcher() 
    dp.include_router(router)
    await dp.start_polling(bot) 
     
     
if __name__ == '__main__': 
    try: 
        asyncio.run(main()) 
    except KeyboardInterrupt: 
        print('Бот выключен')