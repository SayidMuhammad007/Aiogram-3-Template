from datetime import datetime

from utils.db.mysql import User, async_session
from sqlalchemy import select, insert

async def checkUser(tg_id):
    async with async_session() as session:
        result = await session.scalars(select(User).where(User.tg_id == tg_id))
        user = result.first()
        return user

async def newUser(tg_id, fullname, username):
    async with async_session() as session:
        try:
            await session.execute(
                insert(User).values(
                    tg_id=tg_id,
                    fullname=fullname,
                    username=username,
                    date=datetime.now().date(),
                    last_active_day=datetime.now().date()
                )
            )
            await session.commit()
            result = True
        except:
            result = False
        return result