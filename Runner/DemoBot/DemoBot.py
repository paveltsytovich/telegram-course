# (c) TICSIA
#
# demo bot class implementation

import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from  . import config

class DemoBot:
   
    def __init__(self):
        self.__bot = Bot(config.bot_id)
        
    async def __main(self):      
        try:
            disp = Dispatcher(bot=self.__bot)
            disp.register_message_handler(self.start_handler,commands = {"start","restart"})
            await disp.start_polling()
        finally:
            await self.__bot.close()
                    
    async def start_handler(self,event):
        await event.answer(f"Hello {event.from_user.get_mention(as_html=True)} :-)",parse_mode = types.ParseMode.HTML)
  
    def run(self):
        print('Bot run in polling mode. Please CTRL-Break for exit...')        
        asyncio.run(self.__main())    