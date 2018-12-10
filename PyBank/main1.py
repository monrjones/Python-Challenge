import os
import csv

totalMonths =0
totalAmount =0
firstAmount = 0
averageAmountChange = 0
greatIncreaseDate = 'increasing date'
greatIncreaseAmount = 0
greatDecreaseDate = 'decreasing date'
greatDecreaseAmount = 0
totalAmountChange = 0

bankCSV = os.path.join('Resources','budget_data.csv')

with open(bankCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        totalAmount = totalAmount +int(row[1])
        totalMonths = totalMonths +1
        amountIncrease = int(row[1]) - firstAmount
        totalAmountChange = totalAmountChange + amountIncrease
        firstAmount = int(row[1])

        if (amountIncrease> greatIncreaseAmount):
            greatIncreaseAmount = amountIncrease
            greatIncreaseDate = row[0]

        if(amountIncrease< greatDecreaseAmount):
            greatDecreaseAmount = amountIncrease
            greatDecreaseDate = row[0]


averageAmountChange = round(totalAmount/totalMonths)

#Print Results
print("  Financial Analysis  ")
print("----------------------")
print("Total Months: " + str(totalMonths))
print("Total Revenue: " + str(totalAmount))
print("Average Revenue Change: $ "+ str(averageAmountChange))
print("Greatest Increase in Revenue: " + str(greatDecreaseDate) + " " + str(greatDecreaseAmount))  
print("Greatest Decrease in Revenue: " + str(greatIncreaseDate) + " " + str(greatIncreaseAmount)) 


write_file = f"pybank_budget_results_summary.txt"
#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("  Financial Analysis  ")
filewriter.write("--------------------------\n")
filewriter.write("Total Months: " + str(totalMonths))
filewriter.write(("Total Revenue: " + str(totalAmount)))
filewriter.write("Average Revenue Change: $ "+ str(averageAmountChange))
filewriter.write("Greatest Increase in Revenue: " + str(greatDecreaseDate) + " " + str(greatDecreaseAmount))  
filewriter.write("Greatest Decrease in Revenue: " + str(greatIncreaseDate) + " " + str(greatIncreaseAmount)) 

#close file
filewriter.close()