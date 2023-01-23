import csv


def fulldatatable():
    with open("annualmvpop_dataset.csv", "r") as f:
                csvfile = csv.reader(f)
                for line in csvfile:
                    print(line)
                

def opencsvAsDict():
    with open("annualmvpop_dataset.csv", "r") as f:                    #|
        csvdata = csv.DictReader(f, delimiter=",")
        data = [row for row in csvdata]
        return data


def read_csv_row(row_number):                                     #This function ables you to specify which row from the csv you wanna output
    with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
        reader = csv.reader(f, delimiter=",")                     #Reads the csv, data of csv = "reader"
        for i, row in enumerate(reader):                          #Emuerates the data and returns an iterator that produces tuples containing 
            if i == row_number:
                return row                                        #the index and the value of each element of the object.


def printcolumnname():                                     #This function ables you to specify which row from the csv you wanna output
    with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
        reader = csv.reader(f, delimiter=",")                     #Reads the csv, data of csv = "reader"
        for i, row in enumerate(reader):                          #Emuerates the data and returns an iterator that produces tuples containing 
            if i == 0:
                return row                                        #the index and the value of each element of the object.