import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import botid

async def start_handler(event):
    await event.answer(f"Hello {event.from_user.get_mention(as_html=True)} :-)",parse_mode = types.ParseMode.HTML)
    
async def main():
    bot = Bot(botid.bot_id)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler,commands = {"start","restart"})
        await disp.start_polling()
    finally:
        await bot.close()
        
asyncio.run(main())