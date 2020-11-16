from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton,ContentType
    
bot_token = '1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4'
 
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['one'])
async def one_keyboard(message: types.Message):
    simple_button = KeyboardButton('Добро пожаловать 🚪 ')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(simple_button)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup = kb)


@dp.message_handler(commands=['complex'])
async def complex_keyboard(message : types.Message):
    button_text = KeyboardButton('Это просто текст')
    button_contact = KeyboardButton('Отправь свой контакт',request_contact= True)
    button_location = KeyboardButton('Отправь свое местонахождение',request_location=True)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(button_text)
    kb.add(button_location)
    kb.add(button_contact)
    await message.answer('Нажми кнопку',reply_markup = kb)
    
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    print(message)
    await message.answer(message.text)
    
@dp.message_handler(content_types = [ContentType.CONTACT,ContentType.LOCATION] )
async def get_contact(message : types.Message):
    print(message)
    await message.answer('Данные получены')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)