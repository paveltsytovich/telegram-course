from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

bot_token = '1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4'

webhook_host = 'challenge.teachwizard.ru' 
webhook_path = '/api/'
webhook_url = f"{webhook_host}{webhook_path}"

webapp_host = 'localhost'
webapp_port = 80

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

async def on_startup(dp):
    await bot.set_webhook(webhook_url)

async def on_shutdown(dp):
    logging.warning('Shutting down..')

    await bot.delete_webhook()
   
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=webhook_path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=webhook_host,
        port=webapp_port,
    )
