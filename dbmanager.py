import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()


async def add_likes(user_id, num_likes):

    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        likes_table = await connection.fetchrow(f'SELECT likes FROM clout_data WHERE user_id={user_id};')

        # Create new user if doesn't exist
        if not likes_table:
            await connection.execute(f'INSERT INTO clout_data VALUES ({user_id}, {num_likes}, 0, 0, 0);')

        else:
            likes = likes_table['likes']
            updated_likes = likes + num_likes
            await connection.execute(f'UPDATE clout_data SET likes={updated_likes} WHERE user_id={user_id};')

    finally:
        await connection.close()


async def add_dislikes(user_id, num_dislikes):
    
    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        dislikes_table = await connection.fetchrow(f'SELECT dislikes FROM clout_data WHERE user_id={user_id};')

        # Create new user if doesn't exist
        if not dislikes_table:
            await connection.execute(f'INSERT INTO clout_data VALUES ({user_id}, 0, {num_dislikes}, 0, 0);')

        else:
            dislikes = dislikes_table['dislikes']
            updated_dislikes = dislikes + num_dislikes
            await connection.execute(f'UPDATE clout_data SET dislikes={updated_dislikes} WHERE user_id={user_id};')

    finally:
        await connection.close()


async def add_kills(user_id, num_kills):
    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        kills_table = await connection.fetchrow(f'SELECT kills FROM clout_data WHERE user_id={user_id};')

        # Create new user if doesn't exist
        if not kills_table:
            await connection.execute(f'INSERT INTO clout_data VALUES ({user_id}, 0, 0, {num_kills}, 0);')

        else:
            kills = kills_table['kills']
            updated_kills = kills + num_kills
            await connection.execute(f'UPDATE clout_data SET kills={updated_kills} WHERE user_id={user_id};')

    finally:
        await connection.close()


async def add_sniped(user_id, num_sniped):
    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        sniped_table = await connection.fetchrow(f'SELECT sniped FROM clout_data WHERE user_id={user_id};')

        # Create new user if doesn't exist
        if not sniped_table:
            await connection.execute(f'INSERT INTO clout_data VALUES ({user_id}, 0, 0, 0, {num_sniped});')

        else:
            sniped = sniped_table['sniped']
            updated_sniped = sniped + num_sniped
            await connection.execute(f'UPDATE clout_data SET sniped={updated_sniped} WHERE user_id={user_id};')

    finally:
        await connection.close()


async def fetch_all_db_data():
    # Connect to Database
    connection = await asyncpg.connect(
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    try:
        db_table = await connection.fetch(f'SELECT * FROM clout_data;')
        return db_table
    
    finally:
        await connection.close()
