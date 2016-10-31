from models import Personal, Information, Sites
#from Api import Apidata
import sqlite3


class DatabaseManager:

    def __init__(self, filename):
        self.conn = sqlite3.connect('monsterData.db')

    def setup_db(self):

        sql_script = '''
            CREATE TABLE Personal (
                NameNum INT PRIMARY KEY
                Name TEXT NOT NULL
                Address INT
                Phone INT
                Postal_code INT
                Country TEXT NOT NULL
                Region TEXT NOT NULL
                FOREIGN KEY (CuisinesNum) REFERENCES Information
                ):

            CREATE TABLE Information (
                CuisinesNum INT PRIMARY KEY
                Cuisines TEXT NOT NULL
                Categories TEXT NOT NULL
                Has_menu TEXT NOT NULL
                ):

            CREATE TABLE Sites (
                Website_url TEXT NOT NULL
                Resource_uri TEXT NOT NULL
               ):

            INSERT INTO Personal VALUES(?,?,?,?,?),(NameNum, Name, Address, Phone, Postal_code, Country, Region))
            INSERT INTO Information VALUES(?,?,?), (Cuisines, Categories, Has_menu))
            INSERT INTO Sites VALUES(?,?), (Website_url, Resource_uri))
                '''

        try:
            print('Creating tables...')
            self.conn.executescript(sql_script)
            print('Table successfully created')

        except sqlite3.OperationalError as oe:
            print('Error:', oe)

    def _get_personal(self, NameNum):

        try:
            cur =self.conn.cursor()
            query = 'SELECT * FROM Personal WHERE NameNum = ?'
            cur.execute(query, (NameNum, ))

            row = cur.fetchall()
            if row:
                NameNum, Name, Address, Phone, Postal_code, Country, Region = (row[0], row[1], row[2])
                return Personal(NameNum, Name, Phone, Postal_code, Country, Region)

        except sqlite3.OperationalError as oe:
            print('Sql execution error', oe)
        except sqlite3.Error as e:
            print('Connection error ', e)

    ''' def _get_Information(self, cuisines, categories, has_menu):

        try:
            cur = self.conn.cursor()
            query = (
                'SELECT Cuisines, categories, has_menu '
                'From Information '
                'JOIN '

            )'''




