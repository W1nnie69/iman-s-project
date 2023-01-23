import csv
import matplotlib as plt
from data import opencsvAsDict, read_csv_row

# def read_csv_row(row_number):                                     #This function ables you to specify which row from the csv you wanna output
#     with open('annualmvpop_dataset.csv', 'r') as f:               #Opens the csv                       
#         reader = csv.reader(f, delimiter=",")                     #Reads the csv, data of csv = "reader"
#         for i, row in enumerate(reader):                          #Emuerates the data and returns an iterator that produces tuples containing 
#             if i == row_number:
#                 return row                                        #the index and the value of each element of the object.




def mean_value_of_selected_fuel_type():
    userinput = input("Select a fuel type:" )
    

    rowprint = read_csv_row(int(userinput))                         #prints the fuel row, showing the values
    rowprintsliced = rowprint[3:8]                                  #picks values from 2008 to 2012
    fuelname = read_csv_row(int(userinput))        
    rowprintname = fuelname[:1]                                     #picks the fuel name only
    rowprintappend = tuple(rowprintname) + tuple(rowprintsliced)    #append fuel name and the values together, making a new tuple
    output = ', '.join(map(str, rowprintappend))                    #removes the brackets

    row = read_csv_row(int(userinput)) 
    slicing = row[3:8]                                              #picks values from 2008 to 2012
    sliced = tuple(map(int, slicing))

    total = sum(sliced)

    meanvalue = total / len(sliced)

    

    print("Showing data from 2008 to 2012")
    print("")
    print(output)
    print("")
    print("mean: ", meanvalue)

    return meanvalue





def valuesabovemean(meanvaluefrommenu): #This function finds values greater than the mean population shown in the menu
       
    data = opencsvAsDict()                                                          

    
    years = ['2008', '2009', '2010', '2011', '2012']               # Specify the years of population it will use/search

    valuelist = []                                                 #initialize a list called "valuelist"
    


    for row in data:                                                   #|
        fuel_type = row['Fuel Type']                                   #|
        for year in years:                                             #|
            if year in row:                                            #|----- Goes through the Dict and finds values that are more than the mean value
                value = row[year]                                      #|
                if int(value) > meanvaluefrommenu:                     #|
                                                                        #|
                    valuelist.append((fuel_type, year, value))         #|
            

    format_string = "{:<27} {:<10} {:<10}"

    # Print the header
    print(format_string.format("Fuel Type", "Year", "Population"))

    # Print the values
    for item in valuelist:

        print(format_string.format(item[0], item[1], item[2]))


def optionA():
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



def optionB():
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