from aiogram import Router, types
from aiogram.filters import CommandStart
from utils.extra_datas import make_title

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu alaykum {make_title(full_name)}!")
