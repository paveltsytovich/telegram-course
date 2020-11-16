from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
bot_token = '1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4'
 
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    simple_button = KeyboardButton('Добро пожаловать 🚪 ')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(simple_button)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup = kb)
    
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)