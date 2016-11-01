'''Data Monster is a Api storage program that pulls data from the data.gov FDA database\n
and displays all complaints from customers of different companies.'''

from database import DatabaseManager
from tkinter import *

db = DatabaseManager()


class MonsterGui(Frame):

    def __init__(self):
        Frame.__init__(self)
        self._cityVar = None
        self.master.title("DataMonster App")
        self.grid()

        self._nameNumLabel = Label(self, text="NameNum")
        self._nameNumLabel.grid(row=0, column=0)
        self._nameNumStr = StringVar()
        self._nameNumEntry = Entry(self, textvariable=self._nameNumStr)
        self._nameNumEntry.grid(row=0, column=1)

        self._cuisinesNumLabel = Label(self, text="CuisinesNum")
        self._cuisinesNumLabel.grid(row=0, column=2)
        self._cuisinesNumStr = StringVar()
        self._cuisinesNumEntry = Entry(self, textvariable=self._cuisinesNumStr)
        self._cuisinesNumEntry.grid(row=0, column=3)

        self._cuisinesLabel = Label(self, text="Cuisines")
        self._cuisinesLabel.grid(row=1, column=2)
        self._cuisinesStr = StringVar()
        self._cuisinesEntry = Entry(self, textvariable=self._cuisinesStr)
        self._cuisinesEntry.grid(row=1, column=3)

        self._nameLabel = Label(self, text="Name")
        self._nameLabel.grid(row=1, column=0)
        self._nameStr = StringVar()
        self._nameEntry = Entry(self, textvariable=self._nameStr)
        self._nameEntry.grid(row=1, column=1)

        self._categoriesLabel = Label(self, text="Categories")
        self._categoriesLabel.grid(row=2, column=2)
        self._categoriesVar = StringVar()
        self._categoriesEntry = Entry(self, textvariable=self._categoriesVar)
        self._categoriesEntry.grid(row=2, column=3)

        self._has_menuLabel = Label(self, text="Has_menu")
        self._has_menuLabel.grid(row=3, column=2)
        self._has_menuVar = StringVar()
        self._has_menuEntry = Entry(self, textvariable=self._has_menuVar)
        self._has_menuEntry.grid(row=3, column=3)

        self._addressLabel = Label(self, text="Address")
        self._addressLabel.grid(row=5, column=0)
        self._addressStr = StringVar()
        self._addressEntry = Entry(self, textvariable=self._addressStr)
        self._addressEntry.grid(row=5, column=1)

        self._countryLabel = Label(self, text="County")
        self._countryLabel.grid(row=2, column=0)
        self._countryVar = StringVar()
        self._countryEntry = Entry(self, textvariable=self._countryVar)
        self._countryEntry.grid(row=2, column=1)

        self._regionLabel = Label(self, text="Region")
        self._regionLabel.grid(row=3, column=0)
        self._regionVar = StringVar()
        self._regionEntry = Entry(self, textvariable=self._regionVar)
        self._regionEntry.grid(row=3, column=1)

        self._website_urlLabel = Label(self, text="Website")
        self._website_urlLabel.grid(row=0, column=4)
        self._website_urlVar = StringVar()
        self._website_urlEntry = Entry(self, textvariable=self._website_urlVar)
        self._website_urlEntry.grid(row=0, column=5)

        self._resource_uriLabel = Label(self, text="Resource")
        self._resource_uriLabel.grid(row=1, column=4)
        self._resource_uriVar = StringVar()
        self._resource_uriEntry = Entry(self, textvariable=self._resource_uriVar)
        self._resource_uriEntry.grid(row=1, column=5)



        # command button for compute and quit.
        self._button = Button(self, text="Injection", command=self._Injection)
        self._button.grid(row=5, column=4, columnspan=4)

        #self._button = Button(self, text="API", command=self._locu_search)
        #self._button.grid(row=7, column=0, columnspan=5)



    def _Interjection(self):
        nameNum = self._nameNumStr.get()
        print('NameNum: ' + nameNum)
        Name = self._nameStr.get()
        print('Name: ' + Name)
        Address = self._addressStr.get()
        print('Address: ' + Address)
        Country = self._countryVar.get()
        print('Country: ' + Country)
        Region = self._countryVar.get()
        print('Region: ' + Region)
        Categories = self._categoriesVar.get()
        print('Categories:' + Categories)
        Has_menu = self._has_menuVar.get()
        print('Has_menu:' + Has_menu)
        CuisinesNum = self._cuisinesNumStr.get()
        print('CuisinesNum:' + CuisinesNum)
        Cuisines = self._cuisinesStr.get()
        print('Cuisines:' + Cuisines)
        Websites_url = self._websites_urlVar.get()
        print('Websites:' + Websites_url)
        Resource_uri = self._resource_uriVar.get()
        print('Resource:' + Resource_uri)





def start_gui():
    MonsterGui().mainloop()


def quit():
    sys.exit()


def main():
    start_gui().mainloop()


main()