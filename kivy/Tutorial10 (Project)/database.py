import pandas as pd
from pandas import DataFrame
import os
class Data:
    fields = ["description", "date", "priority"]
    fieldsNumber = len(fields)
    uniqueKey = "description"
    content = []
    def __init__(self, *args):
        for value in args:
            self.content.append(value)

    def getField(self, n):
        return self.content[n]
    def getLastField(self):
        return self.content[self.fieldsNumber-1]


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.dataType = Data
        self.uniqueKey = Data.uniqueKey
        if os.path.exists(filename):
            self.load()
        else:
            self.db = DataFrame()

    def addItem(self, item):
        if isinstance(item, self.dataType):
            if self.db.empty:
                self.db = DataFrame([item.content], columns = self.dataType.fields)
                print(self.db)
            else:
                self.db.append(item.content)
    
    def removeItem(self, key):
        index = self.db[self.db[self.uniqueKey]==key].index
        self.db.drop(index, inplace = True)
    
    def saveItem(self, item):
        if item is not None:
            with open(self.filename, "a") as f:
                field = None
                while field != item.getLastField():
                    field = item.getField()
                    f.write(f"{field},")
                f.write(f"{item.getLastField()}\n")
    
    def save(self):
        open(self.filename, "w+").close()
        self.db.to_csv(self.filename, index = None, header = True)

    def load(self):
        self.db = pd.read_csv(self.filename)

db = Database("test.csv")
db.addItem(Data("Test Desc.", "02.11.2019", "1"))
db.removeItem("Test Desc.")
db.save()
