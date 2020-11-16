from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton,ContentType
    
bot_token = '1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4'
 
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda x: x.data == 'btn')
async def first_button_handler(callback_query : types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,'🌞')
    
@dp.message_handler(commands=['inline'])
async def funcname(message: types.Message):
    button = InlineKeyboardButton('🏃',callback_data = 'btn')
    kb = InlineKeyboardMarkup().add(button)
    await message.answer('Нажми на кнопку - получишь результат',reply_markup=kb)
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)