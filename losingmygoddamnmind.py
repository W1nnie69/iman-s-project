import csv
import time
import os





def read_csv_row(row_number):          #This function ables you to specify which row from the csv you wanna output
    with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
        reader = csv.reader(f, delimiter=",")     #Reads the csv, data of csv = "reader"
        for i, row in enumerate(reader):          #Emuerates the data and returns an iterator that produces tuples containing 
            if i == row_number:
                return row                #the index and the value of each element of the object.
        


def printcolumnname():                                 #column names as in "Fuel type" and the years
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

    return meanvalue





def menu():
    global option1 
    #os.system("cls")
    # time.sleep(0.5)
    # with open("annualmvpop_dataset.csv", "r") as f:
    #     csvfile = csv.reader(f)
    #     for line in csvfile:
    #         print(line)

    print("")
    print(" -------------------------------------------------------")
    print("| 1)Vehicle Population of fuel type from 2006 - 2018    |")                      
    print("| 2)Select fuel type to display                         |")
    print("| 3)Find which fuel type has decreased by at least 5%   |")
    print("| 4)Graphing shit                                       |")
    print(" -------------------------------------------------------")

    option1 = input("Please enter which an option:" ) 

    loop = True
    while loop == True:

        if option1 == "1":
            row = read_csv_row(6)
            output = ', '.join(map(str, row))
            print(output)


            time.sleep(1)
            menu()
                
    
        elif option1 == "2":
            # global foc
            # # os.system("cls")

            # print("1) Diesel")
            # print("2) Diesel-Electric")
            # print("3) Electric")
            # print("4) Petrol")
            # print("5) Petrol-CNG")
            # print("6) Petrol-Electric")
            # print("7) Petrol-Electric (Plug-In)")
            # print("")

        
            # x = gettingmeanvalueofselectedfueltype()
            
            # y = int(x)

            # print("")

            # input("Press Enter to Continue")
            
            # print("")

            # with open("annualmvpop_dataset.csv", "r") as f:  #This is the part that answers Q2 part B aka, finding other values that are higher than the mean above
            #     csvfile = csv.reader(f, delimiter=",")       
            #     next(csvfile)   
            #     for i, row in enumerate(csvfile):           
            #         slicing = row[3:8]
            #         cutdata =  tuple(map(int, slicing))     


            
            #         for value in cutdata:

            #             if value > y:
            #                 print(value)
                    

        
            # os.system("cls")
            with open("annualmvpop_dataset.csv", "r") as f:     #converts the raw csv to python dict
                csvdata = csv.DictReader(f, delimiter=",")
                data = [row for row in csvdata]
                
                fuel_type = 'Diesel'
                years = ['2006', '2007', '2008', '2009', '2010']

                for dictionary in data:
                    if dictionary.get("Fuel Type") == fuel_type:
                        for year in years:
                            if year in dictionary:
                                value = dictionary[year]
                                print(year, value)
                                
            break


menu()



        
        
                
                
        
            

            
            
            


                







   