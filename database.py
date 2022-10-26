import pandas as pd
from openpyxl import load_workbook


def create_database():
    dct = {'Id': {0: "214632002"},
           'Name': {0: 'danielle'},
           'Skills': {0: ["cooking"]},
           'Hours': {0: "3"}
           }
    data = pd.DataFrame(dct)
    data.to_excel("volt_database.xlsx")


def read_from_database():
    data = pd.read_excel("volt_database.xlsx")
    print(data)


def write_to_database():
    df = pd.DataFrame({'Id': {0: "214632002"},
                       'Name': {0: 'aaa'},
                       'Skills': {0: ["baking"]},
                       'Hours': {0: "5"}
                       })
    data2 = pd.DataFrame(df)
    data1 = pd.read_excel("volt_database.xlsx")
    data1.append(data2)
    df3 = pd.concat([data1, data2])
    df3.to_excel("new_vol")




# read_from_database()
write_to_database()
