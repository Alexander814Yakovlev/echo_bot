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

@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)