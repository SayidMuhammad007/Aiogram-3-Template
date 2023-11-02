from aiogram import Router, types
from aiogram.filters import CommandStart

from utils.db.functions import checkUser, newUser
from utils.extra_datas import make_title

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    check = await checkUser(user_id)
    print("**********************",check)
    if check == None:
        await newUser(user_id, full_name, message.from_user.username)
    await message.answer(f"Assalomu alaykum {make_title(full_name)}!")
