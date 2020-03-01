import csv
loope=0
candidates = []
votes = []
percentages = []
election_data = "election_data.csv"
voter_counter = 0
with open (election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        voter_counter += 1
        if row[2] in candidates:
            pass
        else:
            candidates.append(row[2])
            votes.append(0)
        index = candidates.index(row[2])
        votes[index] +=1
    for x in candidates:
        #percentages.append(round(votes[loope]/voter_counter*100,2))
        percentages.append(votes[loope]/voter_counter)
        loope += 1
    winner = candidates[votes.index(max(votes))]

print(f"""Election Results
-----------------------------
Total votes : {voter_counter:,}
-----------------------------""")
anotherlooper = 0
for candidate in candidates:
    print(f"{candidates[anotherlooper]}: {percentages[anotherlooper]:.2%} ({votes[anotherlooper]:,})")
    anotherlooper +=1
print(f"""-----------------------------
Winner : {winner}
-----------------------------
""")