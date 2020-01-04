# Import csv
import os
import csv

# join path
election_csv = os.path.join("Resources", "election_data.csv")

<<<<<<< HEAD
# create lists 
=======
# create variables 
>>>>>>> 76723b7956f6e6a3a6fc9634e09d3432fbfa8e47
total_votes = 0
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
khan = 0
correy = 0
li = 0
otooley = 0
votes = [khan, correy, li, otooley]
<<<<<<< HEAD
=======

>>>>>>> 76723b7956f6e6a3a6fc9634e09d3432fbfa8e47
# Open Csv
with open(election_csv, newline="") as csvfile:
    
    # store data in csvreader variable 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header 
    header = next(csvreader)

    # Iterate through rows 
    for row in csvreader:

<<<<<<< HEAD
        # Append the total votes and candidates to their corresponding lists
        total_votes +=1
        

=======
        # count ID's and store in variable 
        total_votes +=1
        
        # Count the number of times each name appears and store it in variable 
>>>>>>> 76723b7956f6e6a3a6fc9634e09d3432fbfa8e47
        if row[2] == "Khan":
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li":
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

<<<<<<< HEAD
candidates_votes = dict(zip(candidates, votes))
winner = max(candidates_votes, key= candidates_votes.get)
        
=======
# create a dictionary to find the winner 
candidates_votes = dict(zip(candidates, votes))
winner = max(candidates_votes, key= candidates_votes.get)

# find voter percentage for each candidate        
>>>>>>> 76723b7956f6e6a3a6fc9634e09d3432fbfa8e47
khan_per = (khan/total_votes) * 100
correy_per = (correy/total_votes) * 100
li_per = (li/total_votes) * 100
otooley_per = (otooley/total_votes) * 100


#print results 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {(total_votes)}")
print("----------------------------")
print(f"Khan: {khan_per:.3f}% ({khan})")
print(f"Correy: {correy_per:.3f}% ({correy})")
print(f"Li: {li_per: .3f}% ({li})")
print(f"O'Tooley: {otooley_per: .3f}% ({otooley})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#output text file 
file = open("output.txt", "w")   
file.write("Election Results")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Votes: {(total_votes)}")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Khan: {khan_per:.3f}% ({khan})")
file.write("\n")
file.write(f"Correy: {correy_per:.3f}% ({correy})")
file.write("\n")
file.write(f"Li: {li_per: .3f}% ({li})")
file.write("\n")
file.write(f"O'Tooley: {otooley_per: .3f}% ({otooley})")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Winner: {winner}")
file.write("\n")
file.close()