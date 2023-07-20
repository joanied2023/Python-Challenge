#This is main.py for PyBank exercise by Joan Denoncour

#import libraries
import os
import csv

#path to collect data from resources folder
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#specify the file path with txt file to write to
output_path = os.path.join(".","Analysis", "PyBankAnalysis.txt")

#read file using CSV module
#open up file
with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #internal command to tell you csvreader exists and we will call it
    print(csvreader)

    #read header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # since we are essentially counting the number of rows in the ws; answer should be 86
    # set counter at 0
    TotalMonthsCount = 0
    TotalMonths = []
    
    #assign values to variables with descr. names
    #Month_Year = str(budget_data[0])
   # PL_amt = int(budget_data[1])

    #set P&L adder to 0
    sum_PL = 0
    
    #create list to hold the PL changes from row to row (we will access this to calculate average change)

    PL_Changes_List = []
    PreviousRow = 0

    #read each row of data after the header
    for row in csvreader:

        #1 Calculate total months
        TotalMonths.append(row[0])
        TotalMonthsCount +=1

        #2 - calculate total profits/losses in period; essentially summing
        sum_PL += int(row[1])

        #3 - calculate net changes in P/L over period, and then average of changes.

        #Current Row = data in column 2
        CurrentRow = int(row[1])
        #PL Change is this row minus last row
        PLChange = CurrentRow - int(PreviousRow)
        #put this number in our list
        PL_Changes_List.append(PLChange)
        #make old row the current row
        PreviousRow = CurrentRow
       
    
    #3 - Remove first value in list; calculate average of changes
    PL_Changes_List.pop(0)
    TotalChanges = sum(PL_Changes_List)
    Average = TotalChanges/len(PL_Changes_List)
        
    #4 calculate greatest increase in profits (date and amount) over period
    greatest_increase = int(max(PL_Changes_List))
      
    #5 calculate greatest decrease in profits (date and amount) over period    
    greatest_decrease = int(min(PL_Changes_List))  

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(TotalMonthsCount))
print("Total: $" + str(sum_PL))
print("Average Change: $" + str(round((Average),2)))
print("Greatest Increase in Profits: $" + str(greatest_increase))
print("Greatest Decrease in Profits: $" + str(greatest_decrease))

def write_to_file(filename, lines):
    with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")

write_to_file("PyBankAnalysis.txt",["Financial Analysis","----------------------------",
                                    "Total Months: " + str(TotalMonthsCount),"Total: $" + str(sum_PL),
                                    "Average Change: $" + str(round((Average),2)),
                                    "Greatest Increase in Profits: $" + str(greatest_increase),
                                    "Greatest Decrease in Profits: $" + str(greatest_decrease)])