from models import Personal, Information, Sites

import sqlite3


class DatabaseManager(Personal, Information, Sites):

    def __init__(self):
        db = sqlite3.connect('NewData.db')
        self.cur = db.cursor()

    def Personal(self):
        self.cur.execute('CREATE TABLE if not exists Personal(nameNum INT, name TEXT, address INT, country TEXT, region TEXT)')
        self._nameNum = input('Please enter nameNum: ', + self._nameNum.get),
        self._name = input('Please enter name: ', + self._name.get),
        self._address = input('Please enter address: ', + self._address.get),
        self._country = input('Please enter country: ', + self._country.get),
        self._region = input('Please enter region:', + self._region.get)

    def Information(self):
        self.cur.execute('CREATE TABLE if not exists Information(cuisinesNum INT, cuisines TEXT, categories TEXT,_has_menu TEXT)')
        self._cuisinesNum = input('Please enter cuisinesNum: ' + self._cuisinesNum.get),
        self._cuisines = input('Please enter cuisines: ', + self._cuisines.get),
        self._categories = input('Please enter categories: ', + self._categories.get),
        self._has_menu = input('Please enter has_menu: ', + self._has_menu.get)

    def Sites(self):
        self.cur.execute('CREATE TABLE if not exists Sites(website_url TEXT,resource_uri TEXT)')
        self._website_url = input('Please enter website_url: ', + self._website_url.get),
        self._resource_uri = input('Please enter resource_uri: ', + self._resource_uri.get)

        self.cur.execute('insert into Personal values(?,?,?,?,?)', (self._nameNum, self._name, self._address, self._country, self._region))
        self.cur.execute('INSERT INTO Information VALUES(?,?,?,?)', (self._cuisinesNum, self._cuisines, self._categories, self._has_menu))
        self.cur.execute('INSERT INTO Sites VALUES(?,?)', (self._website_url, self._resource_uri))

        self.cur.execute('select * from Personal')
        self.cur.execute('select * from Information')
        self.cur.execute('select * from Sites')
        self.db.commit()
        for row in self.cur:
            print(row)

        self.db.close()







