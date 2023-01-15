import csv
import time
from sys import exit
import matplotlib.pyplot as plt





def read_csv_row(row_number):                                     #This function ables you to specify which row from the csv you wanna output
    with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
        reader = csv.reader(f, delimiter=",")                     #Reads the csv, data of csv = "reader"
        for i, row in enumerate(reader):                          #Emuerates the data and returns an iterator that produces tuples containing 
            if i == row_number:
                return row                                        #the index and the value of each element of the object.
        


# def print_column_name():                                 #column names as in "Fuel type" and the years
#     with open('annualmvpop_dataset.csv', 'r') as f:
#         reader = csv.reader(f, delimiter=',')
#         for i, row in enumerate(reader):
#             if i == 0:
#                 output = ', '.join(map(str, row))
#                 print(output)




def mean_value_of_selected_fuel_type():
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
 #converts the raw csv to python dict



def valuesabovemean(meanvaluefrommenu):
    with open("annualmvpop_dataset.csv", "r") as f:    
        csvdata = csv.DictReader(f, delimiter=",")
        data = [row for row in csvdata]

        # fuel_type = 'Diesel'
        years = ['2008', '2009', '2010', '2011', '2012']

        valuelist = []
        
        # print(data)

        # for dictionary in data:
        #     if dictionary.get("Fuel Type") == fuel_type:
        # data = sorted(data, key=lambda x: x['year'])

        for row in data:
            fuel_type = row['Fuel Type']
            for year in years:
                if year in row:
                    value = row[year]
                    if int(value) > meanvaluefrommenu:

                        valuelist.append((fuel_type, year, value))      
                

        format_string = "{:<27} {:<10} {:<10}"

        # Print the header
        print(format_string.format("Fuel Type", "Year", "Population"))

        # Print the values
        for item in valuelist:

            print(format_string.format(item[0], item[1], item[2]))
        




def menu():
    global option1 
    #os.system("cls")
    # time.sleep(0.5)
    print("")
    with open("annualmvpop_dataset.csv", "r") as f:
        csvfile = csv.reader(f)
        for line in csvfile:
            print(line)

    print("")
    print(" -------------------------------------------------------------------------------------------------------------------")
    print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
    print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
    print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
    print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
    print("| 5)Quit                                                                                                            |")
    print(" -------------------------------------------------------------------------------------------------------------------")

    option1 = input("Please enter which an option:" ) 

    loop = True
    while loop == True:

        if option1 == "1":
            row = read_csv_row(6)
            output = ', '.join(map(str, row))
            print(output)

            print("")
            input("Press Enter to Continue")
            
            menu()
                
    
        elif option1 == "2":
            # os.system("cls")

            print("1) Diesel")
            print("2) Diesel-Electric")
            print("3) Electric")
            print("4) Petrol")
            print("5) Petrol-CNG")
            print("6) Petrol-Electric")
            print("7) Petrol-Electric (Plug-In)")
            print("")

        
            x = mean_value_of_selected_fuel_type()
            
            y = int(x)

            print("")

            input("Press Enter to Continue")
            
            print("")

            valuesabovemean(y)

            print("")
            input("Press Enter to Continue")

            menu()
            

        
            # os.system("cls")


        elif option1 == "3":
            print("still in testing")
            break






        
        elif option1 == "4":
            print(" -----------------------------------------------------")
            print("|A) Petrol-Electric and Petrol-CNG vehicle population |")
            print("|B) Petrol-Electric and Diesel population             |")
            print(" -----------------------------------------------------")
            option2 = input("Select option A or B:" )


            if option2 == "A":

                years = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
                petrol_electric_population = []
                petrol_cng_population = []

                row1 = read_csv_row(6)
                rowsliced1 = row1[1:]
                convertrow1 = tuple(map(int, rowsliced1))

                row2 = read_csv_row(5)
                rowsliced2 = row2[1:]
                convertrow2 = tuple(map(int, rowsliced2))


                petrol_electric_population = list(convertrow1)
                petrol_cng_population = list(convertrow2)


                print(petrol_electric_population)
                print(petrol_cng_population)


                plt.plot(years, petrol_electric_population, label='Petrol-Electric')
                plt.plot(years, petrol_cng_population, label='Petrol-CNG')


                plt.xlabel('Year')
                plt.ylabel('Population')
                plt.title('Difference between Petrol-Electric and Petrol-CNG vehicle population')
                plt.legend()
                plt.show()


                print("")
                input("Press Enter to Continue")

                menu()
            
            if option2 == "B":

                years = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
                petrol_electric_population = []
                diesel_population = []

                row1 = read_csv_row(6)
                rowsliced1 = row1[1:]
                convertrow1 = tuple(map(int, rowsliced1))

                row2 = read_csv_row(1)
                rowsliced2 = row2[1:]
                convertrow2 = tuple(map(int, rowsliced2))


                petrol_electric_population = list(convertrow1)
                diesel_population = list(convertrow2)


                print(petrol_electric_population)
                print(diesel_population)


                plt.bar(years, petrol_electric_population, label='Petrol-Electric')
                plt.bar(years, diesel_population, label='Diesel')


                plt.xlabel('Year')
                plt.ylabel('Population')
                plt.title('Difference between Petrol-Electric and Diesel vehicle population')
                plt.legend()
                plt.show()
                
                print("")
                input("Press Enter to Continue")

                menu()

            

        elif option1 == "5":
            exit()


menu()



        
        
                
                
        
            

            
            
            


                







   