import numpy 
import csv
import time
import os


def fueloptionconvertion():
    global x
    fueldict = {
        "Diesel":'1',
        "Diesel-Electric":"2",
        "Electric":"3",
        "Petrol":"4",
        "Petrol-CNG":"5",
        "Petrol-Electric":"6",
        "Petrol-Electric(Plug-in)":"7"
    }
    x = fueldict.get(foc)
    print(x)





def read_csv_row(row_number):          #This function ables you to specify which row from the csv you wanna output
    with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
        reader = csv.reader(f, delimiter=",")     #Reads the csv, data of csv = "reader"
        for i, row in enumerate(reader):          #Emuerates the data and returns an iterator that produces tuples containing 
            if i == row_number:
                return row                #the index and the value of each element of the object.
        


def printcolumnname():
    with open('annualmvpop_dataset.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if i == 0:
                output = ', '.join(map(str, row))
                print(output)




def gettingmeanvalueofselectedfueltype():
    userinput = input("Select a fuel type:" )
    

    rowprint = read_csv_row(int(userinput))       #prints the fuel row, showing the values
    rowprintsliced = rowprint[3:8]                #picks values from 2008 to 2012
    fuelname = read_csv_row(int(userinput))        
    rowprintname = fuelname[:1]                   #picks the fuel name only
    rowprintappend = tuple(rowprintname) + tuple(rowprintsliced) #append fuel name and the values together, making a new tuple
    output = ', '.join(map(str, rowprintappend))       #removes the brackets


    row = read_csv_row(int(userinput)) 
    slicing = row[3:8]                            #picks values from 2008 to 2012
    sliced = tuple(map(int, slicing))

    total = sum(sliced)

    meanvalue = total / len(sliced)

    print("Showing data from 2008 to 2012")
    print("")
    print(output)
    print("")
    print("mean: ", meanvalue)





def menu():
    global option1 
    print(" -------------------------------------------------------")
    print("| 1)Full table                                          |")                      
    print("| 2)Select fuel type to display                         |")
    print("| 3)Find which fuel type has decreased by at least 5%   |")
    print("| 4)Graphing shit                                       |")
    print(" -------------------------------------------------------")

    option1 = input()

#menu()

option1 = "2" #temp code for testing

loop = True
while loop == True:

    if option1 == "1":
        with open("annualmvpop_dataset.csv", "r") as f:
            csvdata = csv.reader(f)
            for row in csvdata:
                print(row)

            time.sleep(1)
            menu()
                
    
    elif option1 == "2":
        global foc
        os.system("cls")

        print("1) Diesel")
        print("2) Diesel-Electric")
        print("3) Electric")
        print("4) Petrol")
        print("5) Petrol-CNG")
        print("6) Petrol-Electric")
        print("7) Petrol-Electric (Plug-In)")
        print("")

        
        gettingmeanvalueofselectedfueltype()
    


        #output = ', '.join(map(str, meanvalue))
        
        
        break
       

        
        
                
                
        
            

            
            
            


                







    #for row in csvdata:
        #print(row)
