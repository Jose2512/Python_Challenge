import csv
# Set a variable for the file to be read
budgetdata = "budget_data.csv"
# Variable to count the months 
month_counter = 0
#Variable to sum all PL 
total_PL = 0
#list for profits and months
profit = []
months = []
with open (budgetdata, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Pass the headers row
    csv_header = next(csvfile)
    for row in csvreader:
        # adding 1 number to the counter for each month
        month_counter += 1
        # adding the profit value to the variable. Since losses have "-" a sum will work
        total_PL += int(row[1])
        # Add the P&L value to a list and the months to another list
        profit.append(int(row[1]))
        months.append(row[0])

# Search for the highest number in the list and return its index
index_increase = profit.index(max(profit))
# Search for the lowest number in the list and return its index
index_decrease = profit.index(min(profit))
# The index is used to find value of profit and month in the lists

fin_analysis = f"""Financial Analysis
-------------------------------------   
Total months: {month_counter}
Total: ${total_PL:,}
Average change: ${round(total_PL/month_counter,2):,}
Greatest Increase in Profits: {months[index_increase]} (${profit[index_increase]:,})
Greatest Decrease in Profits: {months[index_decrease]} (${profit[index_decrease]:,})
"""
print(fin_analysis)
# Crate file and write the financial analysis 
output_file = open("Financial_Analysis.txt", "w+")
output_file.write (fin_analysis)