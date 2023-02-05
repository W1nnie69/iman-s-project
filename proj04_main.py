from sys import exit
import time
import module as md
import data as d



 

print("")

d.fulldatatable()

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
        row = md.read_csv_row(6)
        # output1 = ', '.join(map(str, row))

        colrow = d.printcolumnname()
        # output2 = ' '.join(colrow)

        format_string = "{:<16} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}"

        print("")
        print(format_string.format(colrow[0], colrow[1], colrow[2], colrow[3], colrow[4], colrow[5], colrow[6], colrow[7], colrow[8], colrow[9], colrow[10], colrow[11], colrow[12], colrow[13]))
        print(format_string.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))

        
    

        print("")
        input("Press Enter to Continue")
        print("")
        
        d.fulldatatable()

        print("")
        print(" -------------------------------------------------------------------------------------------------------------------")
        print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
        print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
        print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
        print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
        print("| 5)Quit                                                                                                            |")
        print(" -------------------------------------------------------------------------------------------------------------------")

        option1 = input("Please enter which an option:" ) 
        
        
            

    elif option1 == "2":
        

        print("1) Diesel")
        print("2) Diesel-Electric")
        print("3) Electric")
        print("4) Petrol")
        print("5) Petrol-CNG")
        print("6) Petrol-Electric")
        print("7) Petrol-Electric (Plug-In)")
        print("")

    
        x = md.mean_value_of_selected_fuel_type()
        
        y = tuple(map(int, x))

        a, b = y

        print("")

        input("Press Enter to Continue")
        
        print("")

        md.valuesabovemean(a, b)

        print("")
        input("Press Enter to Continue")
        print("")

        d.fulldatatable()
        
        print("")
        print(" -------------------------------------------------------------------------------------------------------------------")
        print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
        print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
        print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
        print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
        print("| 5)Quit                                                                                                            |")
        print(" -------------------------------------------------------------------------------------------------------------------")

        option1 = input("Please enter which an option:" )
        

    
        


    elif option1 == "3":
        
        print("1) Diesel")
        print("2) Diesel-Electric")
        print("3) Electric")
        print("4) Petrol")
        print("5) Petrol-CNG")
        print("6) Petrol-Electric")
        print("7) Petrol-Electric (Plug-In)")
        print("")

        userinput = input("Please choose a fuel type: ")
        print("")

        try:
            md.display_vehicle_population(userinput)

        except ValueError as e:
            print(e)
            print("")



        input("Press enter to continue")

        








        print("")

        d.fulldatatable()

        print("")
        print(" -------------------------------------------------------------------------------------------------------------------")
        print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
        print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
        print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
        print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
        print("| 5)Quit                                                                                                            |")
        print(" -------------------------------------------------------------------------------------------------------------------")

        option1 = input("Please enter which an option:" )
        





    
    elif option1 == "4":
        print("")
        print(" -------------------------------------------------------------------")
        print("|A) Line graph of Petrol-Electric and Petrol-CNG vehicle population |")
        print("|B) Bar graph of Petrol-Electric and Diesel population              |")
        print("|C) Go back to main menu                                            |")
        print(" -------------------------------------------------------------------")
        option2 = input("Select option A, B or C:" )


        if option2 == "A":

            md.optionA()

            print(" -------------------------------------------------------------------")
            print("|A) Line graph of Petrol-Electric and Petrol-CNG vehicle population |")
            print("|B) Bar graph of Petrol-Electric and Diesel population              |")
            print("|C) Go back to main menu                                            |")
            print(" -------------------------------------------------------------------")
            option2 = input("Select option A, B or C:" )
            
            
        
        if option2 == "B":

            md.optionB()

            print(" -------------------------------------------------------------------")
            print("|A) Line graph of Petrol-Electric and Petrol-CNG vehicle population |")
            print("|B) Bar graph of Petrol-Electric and Diesel population              |")
            print("|C) Go back to main menu                                            |")
            print(" -------------------------------------------------------------------")
            option2 = input("Select option A, B or C:" )

            
        if option2 == "C":
            print("")

            d.fulldatatable()

            print("")
            print(" -------------------------------------------------------------------------------------------------------------------")
            print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
            print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
            print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
            print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
            print("| 5)Quit                                                                                                            |")
            print(" -------------------------------------------------------------------------------------------------------------------")

            option1 = input("Please enter which an option:" ) 
            

        else:
            print("You have entered an invalid option. Please try again")
            time.sleep(2)

            print(" -------------------------------------------------------------------")
            print("|A) Line graph of Petrol-Electric and Petrol-CNG vehicle population |")
            print("|B) Bar graph of Petrol-Electric and Diesel population              |")
            print("|C) Go back to main menu                                            |")
            print(" -------------------------------------------------------------------")
            option2 = input("Select option A, B or C:" )
        




    elif option1 == "5":
        exit()




    else:
        print("You have entered an invalid option. Please try again")
        time.sleep(1)
        print("")

        d.fulldatatable()

        print("")
        print(" -------------------------------------------------------------------------------------------------------------------")
        print("| 1)Vehicle Population of Petrol-ELectric fuel type from 2006 - 2018                                                |")                      
        print("| 2)Mean of selected vehicle fuel type from 2008-2012 | Years and vehicle population which exceeded the mean        |")
        print("| 3)Fuel type of vehicle and year which has decreased by at least 5%                                                |")
        print("| 4)Line plot of Petrol-Electric and Petrol-CNG for each year and bar chart of Petrol-Electric and Diesel           |")
        print("| 5)Quit                                                                                                            |")
        print(" -------------------------------------------------------------------------------------------------------------------")

        option1 = input("Please enter which an option:" )





        
        
                
                
        
            

            
            
            


                







   