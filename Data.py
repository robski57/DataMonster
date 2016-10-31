'''Data Monster is a Api storage program that pulls data from the data.gov FDA database\n
and displays all complaints from customers of different companies.'''

from database import DatabaseManager
from tkinter import *
import csv
db = DatabaseManager('monsterData.db')
db.setup_db()

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

        self._nameLabel = Label(self, text="Name")
        self._nameLabel.grid(row=0, column=4)
        self._nameStr = StringVar()
        self._nameEntry = Entry(self, textvariable=self._nameStr)
        self._nameEntry.grid(row=0, column=5)

        self._addressLabel = Label(self, text="Address")
        self._addressLabel.grid(row=1, column=0)
        self._addressStr = StringVar()
        self._addressEntry = Entry(self, textvariable=self._addressStr)
        self._addressEntry.grid(row=1, column=1)

        self._phoneLabel = Label(self, text="Phone")
        self._phoneLabel.grid(row=1, column=4)
        self._phoneStr = DoubleVar()
        self._phoneEntry = Entry(self, textvariable=self._phoneStr)
        self._phoneEntry.grid(row=1, column=5)

        self._postalCodeLabel = Label(self, text="Postal Code")
        self._postalCodeLabel.grid(row=2, column=4)
        self._postalCodeStr = DoubleVar()
        self._postalCodeEntry = Entry(self, textvariable=self._postalCodeStr)
        self._postalCodeEntry.grid(row=2, column=5)

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

        ''' self._totalLabel = Label(self, text="Total")
        self._totalLabel.grid(row=4, column=0)
        self._totalVar = DoubleVar()
        self._totalEntry = Entry(self, textvariable=self._totalVar)
        self._totalEntry.grid(row=4, column=1)'''

        # command button for compute and quit.
        self._button = Button(self, text="Total", command=self._total)
        self._button.grid(row=5, column=0, columnspan=2)

        #self._button = Button(self, text="API", command=self._locu_search)
        #self._button.grid(row=7, column=0, columnspan=5)



    def _total(self):
        NameNum = self._nameNumStr.get()
        Name = self._nameStr.get()
        Address = self._addressStr.get()
        PostalCode = self._postalCodeStr.get()
        Phone = self._phoneStr.get()
        Country = self._countryVar.get()
        Region = self._countryVar.get()

        print('NumberID' + NameNum)
        print('Name' + Name)
        print('Address' + Address)
        print('Postal' + PostalCode)
        print('Phone' + Phone)
        print('Country' + Country)
        print('Region' + Region)

        headers = ['NameNum','Name','Address','Region', 'Phone', 'PostalCode', 'Country']

        '''csv_file_name = 'Locu_Data_Push.csv'

        # newline avoid the extra blank row when you import the data
        with open(csv_file_name, 'w', newline='') as file:
            file_csv = csv.DictWriter(file, headers)
            file_csv.writeheader()
            file_csv.writerows(self)'''


def start_gui():
    MonsterGui().mainloop()


def quit():
    sys.exit()


def main():
    start_gui()


main()