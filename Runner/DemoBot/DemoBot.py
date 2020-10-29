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
        self.__handlers = {}
        self.__disp = Dispatcher(bot=self.__bot)
        
    async def __main(self):      
        try:            
            await self.__disp.start_polling()
        finally:
            await self.__bot.close()
                    
    async def __start_handler(self,event):
        handler = self.__handlers.get('onStart')
        if not handler is None:
            result = handler(event.text)
            await event.answer(result,parse_mode = types.ParseMode.HTML)
        else:
            await event.answer(f"Hello {event.from_user.get_mention(as_html=True)} :-)",parse_mode = types.ParseMode.HTML)
    async def __handler(self,event,regexp):
            result = self.__handlers['text'](event.text)
            await event.answer(result,parse_mode = types.ParseMode.HTML)
    def run(self):
        print('Bot run in polling mode. Please CTRL-Break for exit...')        
        asyncio.run(self.__main())  
        
    def register_start_handler(self,handler=None):
        self.__disp.register_message_handler(self.__start_handler,commands = {"start","restart"})
        self.__handlers['onStart'] = handler
        
    def register_text_handler(self,handler,regexp):
        self.__handlers["text"] = handler
        self.__disp.register_message_handler(self.__handler,regexp = regexp)