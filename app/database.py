from time import sleep
import psycopg2
from psycopg2.extras import RealDictCursor
from . import config


while True:
    try:
        conn = psycopg2.connect(database=config.settings.database_name, 
                                user=config.settings.database_user,
                                password=config.settings.database_password, 
                                host=config.settings.database_host_url, 
                                port=config.settings.database_port, 
                                cursor_factory=RealDictCursor
                                )
        courser = conn.cursor()
        print("Database connected successfully!")
        break

    except Exception as e:
        print(e)
        sleep(2)


