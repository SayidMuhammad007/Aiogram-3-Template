from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker


from data.config import SQL_ALCHEMY_URL

engine = create_async_engine(SQL_ALCHEMY_URL, echo=True)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger)
    fullname = Column(String(255))
    username = Column(String(255))
    date = Column(Date)
    last_active_day = Column(Date)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    import asyncio
    asyncio.run(async_main())