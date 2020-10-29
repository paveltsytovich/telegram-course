import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import botid
class DemoBot:
    def __init__(self):
        pass
    async def __main(self):
        bot = Bot(botid.bot_id)
        try:
            disp = Dispatcher(bot=bot)
            disp.register_message_handler(self.start_handler,commands = {"start","restart"})
            await disp.start_polling()
        finally:
            await bot.close()
                    
    async def start_handler(self,event):
        await event.answer(f"Hello {event.from_user.get_mention(as_html=True)} :-)",parse_mode = types.ParseMode.HTML)
    
def run_bot():
    bot = DemoBot()         
    asyncio.run(bot._DemoBot__main())
    
run_bot()