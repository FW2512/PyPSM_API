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
        cursor = conn.cursor()
        print("Database connected successfully!")
        break

    except Exception as e:
        print(e)
        sleep(2)

user_table = """CREATE TABLE IF NOT EXISTS public.users
                (
                    user_id serial NOT NULL UNIQUE,
                    user_name character varying NOT NULL UNIQUE,
                    email_address character varying NOT NULL UNIQUE,
                    password character varying NOT NULL,
                    created_date timestamp with time zone NOT NULL DEFAULT NOW(),
                    PRIMARY KEY (user_id)
                );"""
cursor.execute(user_table)

machine_info_table = """CREATE TABLE IF NOT EXISTS public.machine_info
                (
                    user_id integer NOT NULL UNIQUE,
                    machine_name character varying DEFAULT NULL ,
                    platform character varying DEFAULT NULL ,
                    platform_version character varying DEFAULT NULL ,
                    cpu_info character varying DEFAULT NULL ,
                    battery_info character varying DEFAULT NULL ,
                    ram_info character varying DEFAULT NULL ,
                    PRIMARY KEY (user_id),
                    CONSTRAINT user_id FOREIGN KEY (user_id)
                        REFERENCES public.users (user_id) MATCH SIMPLE
                        ON UPDATE NO ACTION
                        ON DELETE CASCADE
                        NOT VALID
                );"""
cursor.execute(machine_info_table)

machine_status_table = """CREATE TABLE IF NOT EXISTS public.machine_status
(
    user_id integer NOT NULL UNIQUE,
    online boolean DEFAULT NULL,
    shutdown boolean DEFAULT NULL,
    PRIMARY KEY (user_id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);"""
cursor.execute(machine_status_table)

conn.commit()