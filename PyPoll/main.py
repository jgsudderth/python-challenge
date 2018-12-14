##The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.





import os
import csv


# Import file <standard code to find where the file is
csv_path = os.path.join("..", "Resources", "election_data.csv")

#First thing to do is create an empty dictionary to store all the poll data
poll_data = {}

#if you want to sum something you first have to set its value to 0, just like creating an empty dictionary
total_votes = 0

#gets data file 
#standard code is always
#with open(csv_path, 'r') <just means read it instead of write it as f: <just means as file could be anything
#       reader = csv.reader(f)
with open(csv_path, 'r') as f:
    reader = csv.reader(f)

    #skips header line <standard coding is next(reader, None)
    next(reader, None)

    for row in reader:
        #add 1 to the total votes
        total_votes += 1
        #start if statement to start couting votes per candidate
        if row[2] in poll_data.keys():
            poll_data[row[2]] = poll_data[row[2]] + 1
        else:
            poll_data[row[2]] = 1
 
#create empty list for candidates and their vote count
candidates = []
num_votes = []

#takes dictionary keys and values and puts them into lists

for k, v in poll_data.items():
    candidates.append(k)
    num_votes.append(v)

# make an empty list for the vote percent

vote_percent = []
#iterate through number of votes and find the percentage (rounded to 2) and 
for num in num_votes:
    vote_percent.append(round(num/total_votes*100, 1))

# prepare info for output by zipping into a tuple 
output_data = list(zip(candidates, num_votes, vote_percent))

#create empty winner list
winner_list = []

for candidate in output_data:
    if max(num_votes) == candidate[1]:
        winner_list.append(candidate[0])

# determine winner (value is at index 0)
winner = winner_list[0]

# print to text file
with open('Output.txt', 'w') as text_file:
    text_file.write('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for x in output_data:
        text_file.write(x[0] + ": " + str(x[2]) +'%  (' + str(x[1]) + ')\n')
    text_file.write('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open('Output.txt', 'r') as readfile:
    print(readfile.read())

    ##this was super challenging, thanks for the help with outputting the information to a text file,
    ##i had to find a stack overflow thread about how to do it.
    