#Name: Siyu Pan
#Class: ISQA3900
#Desciption: Demonstrate basic knowledge of Python and writing to and reading from CSV files.


# read data from file
def readdata(filename):
    #Function to read data from csv file.
    try:
        data = open(filename)
        dataList = []
        for line in data.readlines():
            dataList.append(line.split(","))
        for i in range(len(dataList)):
            #One way to delete the \n
            # if "\n" in dataList[i][2]:
            #     dataList[i][2] = dataList[i][2][:-1]
            dataList[i][2] = dataList[i][2].replace("\n","")
        print("Trips:")
        printlist(dataList)
        print()
        data.close()
        return dataList
    except(FileNotFoundError):
        print("Trips not read from file - file not found: {}".format(filename))

# write data
def writedata(datalist):
    #Write the data into the csv file.
    data = open("trips.csv","w")
    for list in datalist:
        data.writelines(",".join(list)+"\n")
    data.close()

# create list
def createtriplist(total):
    #create trip data
    if total == None:
        total = []
    while True:
        Continue = input("Would you like to continue? y/n:")
        singletrip = []
        if Continue == "y":
            #enter the first attribute single trip data.
            while True:
                try:
                    #As the instruction, the function should be string format in the list
                    miles_driven= str(float(input("Enter miles driven:\t\t")))
                    singletrip.append(miles_driven)
                    break
                except:
                    print("Enter numeric values only. Try again.")
            # enter the second attribute single trip data.
            while True:
                try:
                    gallons_used = str(float(input("Enter gallons of gas used:\t")))
                    singletrip.append(gallons_used)
                    break
                except:
                    print("Enter numeric values only. Try again.")
            #Calculate the third data.
            mpg = round(eval(miles_driven)/eval(gallons_used),2)
            singletrip.append(str(mpg))
            total.append(singletrip)
            printlist(total)
            print()
        else:
            break
    return total

# print list
def printlist(trip):
    #file to print the current trip list.
        for i in range(len(trip)):
            print("{}.".format(i+1),end="")
            print("Miles: {:<10}".format(trip[i][0]),end="")
            print("Gallons of Gas: {:<10}".format(trip[i][1]),end="")
            print("Mpg: {:<10}".format(trip[i][2]))

#main function to do the job.
def main():
    # display a title
    print("The Miles Per Gallon program")
    print()
    totallist = list()
    userinput = input("Would you like to read trips from a file? y/n: ")
    if userinput == "y":
        totallist = readdata(input("Enter the csv filename containing trip data: "))
    totallist = createtriplist(totallist)
    writedata(totallist)
    print()
    print("Trips saved to file: trips.csv")


#Execute statement
main()