from aiogram import Bot, Dispatcher, executor, types

with open('my_token.txt', 'r') as token:
    TOKEN: str = token.read()

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет\nМеня зовут Эхо-бот\nЯ буду повторять всё, что Вы мне напишете!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Я повторяю сообщения, которые вы присылаете)")

@dp.message_handler(content_types=['photo'])
async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)
    
@dp.message_handler(content_types=['sticker'])
async def send_sticker_echo(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)

@dp.message_handler(content_types=['video'])
async def send_video_echo(message: types.Message):
    await message.answer_video(message.video.file_id)

@dp.message_handler(content_types=['audio'])
async def send_audio_echo(meassage: types.Message):
    await meassage.answer_audio(meassage.audio.file_id)

@dp.message_handler(content_types=['document'])
async def send_document_echo(message: types.Message):
    await message.answer_document(message.document.file_id)

@dp.message_handler(content_types=['location'])
async def send_location_echo(message: types.Message):
    await message.answer_location(message.location.latitude, message.location.longitude)
    
@dp.message_handler(content_types=['contact'])
async def send_contact(message: types.Message):
    await message.answer_contact(message.contact.phone_number, message.contact.first_name)
    print(message.answer_contact)

@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer(f'Вы написали:\n{message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)