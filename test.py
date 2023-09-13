
import os
import asyncpg
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def aa():
    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        likes_table = await connection.execute(f'DELETE FROM a WHERE user_id=4;')
        print(likes_table)

    finally:
        await connection.close()

asyncio.run(aa())