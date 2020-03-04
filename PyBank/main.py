import csv
# Set a variable for the file to be read
budgetdata = "budget_data.csv"
# Variable to count the months 
month_counter = 1
#Variable to sum all PL 
total_PL = 0
#list for profits and months and change
profit = []
months = []
changePL = []

with open (budgetdata, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Pass the headers row
    csv_header = next(csvfile)
    # Extract the data in the first row since 1 month will not have PL change
    csv_first = next(csvreader)
    # Adding it to its respective list
    profit.append(int(csv_first[1]))
    months.append(csv_first[0])
    # Setting the first value for the change calculation
    prev_value = int(csv_first[1])
    for row in csvreader:
        # adding 1 number to the counter for each month
        month_counter += 1
        # Add the P&L value to a list and the months to another list
        profit.append(int(row[1]))
        months.append(row[0])
        # Take this month profit and calculate the month's change
        current_m_value = int(row[1])
        changeinpl = current_m_value - prev_value
        # Add the value to the changePL list
        changePL.append(changeinpl)
        # Replace prev_value with current one
        prev_value = current_m_value
# Sum all profits
total_PL = sum(profit)
# calculate the average change
average_change = sum(changePL)/len(changePL)
# Search for the highest number in the list and return its index
index_increase = changePL.index(max(changePL))
# Search for the lowest number in the list and return its index
index_decrease = changePL.index(min(changePL))
# The index is used to find value of profit and month in the lists

# deshacerte del ultimo valor

fin_analysis = f"""Financial Analysis
-------------------------------------   
Total months: {month_counter}
Total: ${total_PL:,}
Averge change: ${round(average_change,2):,}
Greatest Increase in Profits: {months[index_increase+1]} (${changePL[index_increase]:,})
Greatest Decrease in Profits: {months[index_decrease+1]} (${changePL[index_decrease]:,})
"""
print(fin_analysis)
# Create file and write the financial analysis 
output_file = open("Financial_Analysis.txt", "w+")
output_file.write (fin_analysis)

#Average change: ${round(total_PL/month_counter,2):,}