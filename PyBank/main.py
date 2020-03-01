import csv

budgetdata = "budget_data.csv"
month_counter = 0
total_PL = 0
greatest_inc = 0
greatest_dec = 0
with open (budgetdata, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        month_counter += 1
        total_PL += int(row[1])
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_m = row[0]
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_m = row[0]

print(f"""Financial Analysis
-------------------------------------   
Total months: {month_counter}
Total: ${total_PL}
Average change: ${round(total_PL/month_counter,2)}
Greatest Increase in Profits: {greatest_dec_m} (${greatest_dec})
Greatest Decrease in Profits: {greatest_inc_m} (${greatest_inc})
""")
output_file = open("Financial_Analysis.txt", "w+")
output_file.write (f"""Financial Analysis
-------------------------------------   
Total months: {month_counter}
Total: ${total_PL}
Average change: ${round(total_PL/month_counter,2)}
Greatest Increase in Profits: {greatest_dec_m} (${greatest_dec})
Greatest Decrease in Profits: {greatest_inc_m} (${greatest_inc})
""")