from aiogram import types
from loader import dp
import json


@dp.message_handler()
async def jsonify(message: types.Message):
     await message.answer(f"<code>{json.dumps(message.to_python(), indent=4)}</code>")
     