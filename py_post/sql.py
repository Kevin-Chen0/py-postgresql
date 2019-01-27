# -*- coding: utf-8 -*-

import psycopg2


class Session:

    def __init__(self, db, usr, pwd):
        conn_str = f"dbname={db} user={usr} password={pwd}"
        self.conn_str = conn_str

    def to_sql(self, query):
        conn = psycopg2.connect(self.conn_str)

        """ create table in the PostgreSQL database"""
        # conn = None
        try:
            # read the connection parameters
            # params = config()
            # connect to the PostgreSQL server
            # conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # to PostgresSQL
            cur.execute(query)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        except (Exception, psycopg2.ProgrammingError) as error:
            print(error)
            conn.rollback()
        except (Exception, psycopg2.InterfaceError) as error:
            print(error)
            conn = psycopg2.connect(self.conn_str)
            cur = conn.cursor()
        finally:
            if conn is not None:
                conn.close()
