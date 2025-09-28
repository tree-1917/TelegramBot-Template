from aiogram import Bot, Dispatcher, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

TOKEN = "TOKEN" 

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# Create reply keyboard
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# /start command handler
@router.message(F.text.in_(["/start", "/help"]))
async def start(message: Message):
    await message.answer("Hello! How are you?", reply_markup=keyboard)

# Handle user reply
@router.message()
async def handle_reply(message: Message):
    if message.text == "Button 1":
        await message.answer("You pressed Button 1!")
    elif message.text == "Button 2":
        await message.answer("You pressed Button 2!")
    else:
        await message.answer(f"You said: {message.text}")

# Register router
dp.include_router(router)

# Run bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
