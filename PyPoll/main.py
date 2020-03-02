import csv
# Declaring lists for candidates, votes and percentages
candidates = []
votes = []
percentages = []
# Set a variable for the file to be read
election_data = "election_data.csv"
# Setting a counter for the voters
voter_counter = 0
with open (election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     # Pass the headers row
    csv_header = next(csvfile)
    for row in csvreader:
        # adding 1 number to the counter for each row (voter)
        voter_counter += 1
        # If the name of the candidate (row[2]) already exist in the list of candidates, do nothing, else add it to the list
        if row[2] in candidates:
            pass
        else:
            candidates.append(row[2])
            # also creates a space with value 0 in the votes list for each candidate
            votes.append(0)
        # for each row, verifies the canddidate name and return its index value from the candidates list
        index = candidates.index(row[2])
        # add a value of 1 in the votes list in the index value determined for the candidate
        votes[index] +=1
    # for each candidate, it will calculate its percentage and add it to another list
    for x in range(len(candidates)):
        percentages.append(votes[x]/voter_counter)
    # find the index for the max number of votes of the candidates and with that index, find the winner in the candidates list
    winner = candidates[votes.index(max(votes))]
    # Joining the data with zip
    datos = zip(candidates, percentages, votes)

# formating the output in 3 parts
results_header = f"""Election Results
-----------------------------
Total votes : {voter_counter:,}
-----------------------------
"""
ind_result = [f"{info[0]}: {info[1]:.2%} ({info[2]:,})" for info in datos]
results_footer= f"""
-----------------------------
Winner : {winner}
-----------------------------
"""
# printing the 3 parts
print(results_header)
for result in ind_result:
    print(result)
print(results_footer)

# Creating the output file
output_file = open("Election results.txt", "w+")
#writing the 3 parts into the file
output_file.write (results_header)
for result in ind_result:
    output_file.write(result+"\n")
output_file.write (results_footer)
