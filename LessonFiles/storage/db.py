import sqlite3
import hashlib
import os

class Database(object):
    def __init__(self):
        self.path = 'app/storage/'

        if not os.path.exists(os.path.join(self.path, 'db.sqlite')):
            conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
            cur = conn.cursor()


            sql0 = '''
            CREATE TABLE tasks(id integer primary key, name text not null, date text not null)
            '''

            sql1 = '''
            CREATE TABLE users(id integer primary key, name text not null, password text not null)
            '''

            cur.execute(sql0)
            cur.execute(sql1)
    def db_connect(self):
            conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
            cur = conn.cursor()

            return conn

    def add_task(self, task: tuple):
        """ add a task """
        conn = self.db_connect()
        cur = conn.cursor()
        
        try:
            sql = 'INSERT INTO tasks(name, date) VALUES(?,?)'
            cur.execute(sql, task)
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def delete_task(self, name):
        """ delete a task """
        conn = self.db_connect()
        cur = conn.cursor()
        
        try:
            sql = '''DELETE FROM tasks
            WHERE name=?
            '''
            cur.execute(sql, [name])
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False


    def get_tasks(self):    
        """ show tasks """
        conn = self.db_connect()
        cur = conn.cursor()

        try:
            sql = 'SELECT * FROM tasks'
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()

            return data
        except Exception as e:
            print(e)
            return False
        

    def update_task(self, task: list):
        """ update a task """
        conn = self.db_connect()
        cur = conn.cursor()
        
        try:
            sql = '''UPDATE tasks
            SET name=?,
            date=?
            WHERE name=?
            '''
            task.append(task[0])
            cur.execute(sql, task)
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False
        
            
    def auth_user(self, user: tuple):
        """ verify users added """
        
        conn = self.db_connect()
        cur = conn.cursor()

        sql = 'SELECT * FROM users WHERE name=?'
        name, passw = user
        try:
            pwd = hashlib.sha256(passw.encode()).hexdigest()
            userx = (name, pwd)        
            cur.execute(sql, [name])
            conn.commit()
            
            dat = cur.fetchall()
            if len(dat) > 0:
                db_user = dat[0]
                if pwd == db_user[2]:
                    return True
                else:
                    return False
            else:
                return False
            
        except Exception as e:
            print(e)
            return []
    
    def add_user(self, user: tuple):
        """ Add new User to db

        """

        conn = self.db_connect()
        cur = conn.cursor()
        
        name, passw = user
        try:
            pwd = hashlib.sha256(passw.encode()).hexdigest()
            userx = (name, pwd)

            sql = 'INSERT INTO users(name, password) VALUES(?,?)'
            cur.execute(sql, userx)
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False
        
