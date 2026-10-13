import asyncio from aiogram import Bot, Dispatcher, types from aiogram.filters import CommandStart, CommandObject from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
----------------- НАСТРОЙКИ -----------------
BOT_TOKEN = "8991505130:AAHAtbgKCZwpjNhgUYLYO97eB4JKObr-_rg" ADMIN_CHAT_ID = 625541167
----------------------------------------------
bot = Bot(token=BOT_TOKEN) dp = Dispatcher()
@dp.message(CommandStart(deep_link=True)) async def handle_artist_link(message: types.Message, command: CommandObject): artist_username = command.args user = message.from_user user_mention = f"@{user.username}" if user.username else f"{user.first_name} (ID: {user.id})"
# 1. Отправляем уведомление ТЕБЕ в личные сообщения
admin_notification = (
    f"🔔 **Новый вероятный заказ!**\n\n"
    f"👤 **Заказчик:** {user_mention}\n"
    f"🎨m import Bot, Dispatcher, @{artist_username}"
)
try:
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_notification, parse_mode="Markdown")
except Exception as e:
    print(f"Ошибка отправки уведомления: {e}")

# 2. Кнопка и текст для заказчика
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f"💬 Написать художнику (@{artist_username})",
                url=f"https://t.me/{artist_username}"
            )
        ]
    ]
)

reply_text = (
    "Привет! Я бот-проводник, создан для того, чтобы отслеживать эффективность канала количеством заказов.\n\n"
    f"Вот юзер художника, который тебя интересует: **@{artist_username}**\n"
    "Можешь смело писать ему!"
)
await message.answer(text=reply_text, reply_markup=keyboard, parse_mode="Markdown")
@dp.message(CommandStart()) async def handle_simple_start(message: types.Message): await message.answer( "Привет! Я бот-проводник канала с художниками. " "Чтобы связаться с конкретным художником, перейди по ссылке под его работой в канале." )
async def main(): print("Бот успешно запущен!") await dp.start_polling(bot)
if name == "main": asyncio.run(main())
