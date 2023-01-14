from random import randint
import logging
import pymysql.cursors


class MySQL:
    def __init__(self, host, port, user, password, db_name):
        self._connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    def check_user_register(self, tg_id) -> bool:
        select_query_user = f"SELECT * FROM `user` WHERE tg_id = '{tg_id}' AND banned != 1"
        try:
            with self._connection.cursor() as cursor:
                register = cursor.execute(select_query_user)
                if register == 0:
                    return False
                else:
                    return True
        except Exception as e:
            logging.error(f'[check_user_register] error text: {e}')

    def add_user(self, tg_id, username, code=None):
        select_query_user = f"INSERT INTO `user` (`tg_id`, `username`, `ref_code`, `ref_link`) VALUES (%s, %s, %s, %s)"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query_user, (tg_id, username, code, randint(0, 9999999999)))
                self._connection.commit()
        except Exception as e:
            logging.error(f'[add_user] error text: {e}')

    def get_ref_link(self, tg_id):
        select_query_user = f"SELECT * FROM `user` WHERE tg_id = '{tg_id}'"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query_user)
                data = cursor.fetchone()
                return data['ref_link']
        except Exception as e:
            logging.error(f'[get_ref_link] error text: {e}')

    def get_transitions(self, code):
        select_query_user = f"SELECT * FROM `user` WHERE `ref_code` = {code}"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query_user)
                data = cursor.fetchall()
                return len(data)
        except Exception as e:
            logging.error(f'[get_transitions] error text: {e}')