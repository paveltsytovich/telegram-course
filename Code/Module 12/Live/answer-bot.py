from aiogram import Bot, Dispatcher, executor, types
bot_token = '1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4'
 
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(regexp="Картинка")
async def text(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer_photo(types.InputFile('python.jpg'))
    
@dp.message_handler(regexp="Звук")
async def audio(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer_audio(types.InputFile('sample.mp3'))
   
@dp.message_handler(regexp="Сообщение")
async def voice(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer_voice(types.InputFile('sample.mp3'))
     
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    