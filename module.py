import csv
import matplotlib.pyplot as plt
from data import opencsvAsDict, read_csv_row



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

    return meanvalue, userinput
    




def valuesabovemean(meanvaluefrommenu, fuelnumber): #This function finds values greater than the mean population shown in the menu
    
    x = str(fuelnumber)

    data = opencsvAsDict()                                                          

    
    years = ['2008', '2009', '2010', '2011', '2012']               # Specify the years of population it will use/search

    valuelist = []                                                  #initialize a list called "valuelist"

    fueldict = {
        "1": "Diesel",
        "2": "Diesel-Electric",
        "3": "Electric",
        "4": "Petrol",
        "5": "Petrol-CNG",
        "6": "Petrol-Electric",
        "7": "Petrol-Electric (Plug-In)"
}


    if x in fueldict:
        fuel = fueldict[x] 
   


    
    for row in data:
        if row["Fuel Type"] == fuel:
            for year in years:
                if year in row:
                    value = row[year]                                           #|
                    if int(value) > meanvaluefrommenu:                          #|
                        valuelist.append((fuel, year, value))
                    
                                                                                    #|
            

    

    format_string = "{:<27} {:<10} {:<10}"


    if not valuelist:
        print("There are no values above the mean")

    else:
        # Print the header
        print(format_string.format("Fuel Type", "Year", "Population"))

    # Print the values
        for item in valuelist:

            print(format_string.format(item[0], item[1], item[2]))





def display_vehicle_population(selected_vehicle_type):

    fueldict = {
        "1": "Diesel",
        "2": "Diesel-Electric",
        "3": "Electric",
        "4": "Petrol",
        "5": "Petrol-CNG",
        "6": "Petrol-Electric",
        "7": "Petrol-Electric (Plug-In)"
}
    x = str(selected_vehicle_type)

    if x in fueldict:
        fuel = fueldict[x]
    

#     # Filter the data to get only the selected vehicle type
    data = opencsvAsDict()



    year_population = {}
    for d in data:
        if d["Fuel Type"] == fuel:
            for year, population in d.items():
                if year == "Fuel Type":
                    continue
                population = int(population)
                if population == 0:
                    raise ValueError("population cannot be zero")
                if year not in year_population:
                    year_population[year] = population
                else:
                    year_population[year] += population

    for year, population in year_population.items():
        previous_year = str(int(year) - 1)
        if previous_year in year_population:
            change = (population - year_population[previous_year]) / year_population[previous_year] * 100
            if change < -5:
                print(f"In {year}, the population of {fuel} vehicles decreased by {abs(change):.2f}% compared to {previous_year}")
            break

    if change > -5:
        print("There are no percentage decrease above 5%")





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