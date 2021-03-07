# Activity 5 - Reading and Writing CSV Files

## Objectives
* Demonstrate basic knowledge of Python and writing to and reading from CSV files.

## Directions
1. Review the mpg python program introduced at the beginning of this class to determine miles per gallon posted with this Assignment on Canvas.
2. **Modify the program to allow the user to enter multiple trips** (miles driven and gallons of gas used), calculating the mpg for each trip. (Add a repetition structure)
3. **If the user does not enter numeric values, the program must recover** and allow the user to correct the value input. Implement a
  a. Python function to read a numeric value and allow the user to correct the value if it is not numeric.
  b. The function should receive a string as a parameter that contains the prompt to display to the user.
  c. The program should not crash due to an invalid value.
4. Modify the program to **store the data for each calculation, or trip, in a two-dimensional list**. After each trip is added to the list, print out all elements of the list.
  a. The list increases in size as you run it since you are appending all “calculation runs” to the list.
  b. For each calculation, add these values to the list: miles driven, gallons of gas used, and calculated value of MPG.
5. Modify the program to **save the data in the list to a file named trips.csv** when the user chooses to exit the program.
  a. Add a Python **function** to write the list to a csv file
  b. The movie list program is a useful reference program for completing this task.
  c. Verify the file is created correctly by opening the csv file with a spreadsheet program like Excel and viewing the contents.
6. Modify the program to ask the user if they would like to **read trips from a csv file before entering new trip data**.
  a. If they do, prompt the user for the filename.
  b. Open the file and read the contents into the list of trips.
  c. After reading the file, the program should function as described above.
  d. Use a Python function to read the list from a csv file and to validate the user’s trip inputs as numeric.
  e. Add exception handling to recover if the file does not open successfully.
7. Upload the Python file and the csv file your program created to **GitHub** for Activity 5.
8. Include the following comments at the top of your python file:
  a. Your name
  b. The course name and date
  c. A short description of the code in the file (i.e. purpose of the program)
9. Your file contents should look like below:
```Python
Sample csv file contents if 3 trips entered (format: miles, gallons, mpg)
100.0,10.0,10.0
300.0,3.0,100.0
150.0,30.0,5.0
```

## Example Runs
In the command line, the program should look like the screenshot below.
![Run1-BadFilename](https://github.com/uno-isqa-3900/activity5/blob/main/images/run1-BadFilename.png)
![Run2-GoodFilenameGoodInputs](https://github.com/uno-isqa-3900/activity5/blob/main/images/run2-GoodFilenameGoodInputs.png)
![Run1-GoodFilenameBadInputs](https://github.com/uno-isqa-3900/activity5/blob/main/images/run3-GoodFilenameBadInputs.png)

