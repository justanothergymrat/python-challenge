##############
##    imports
##############
import os
import csv

##############
##   variables
##############
# * directory set outside of git folder to avoid uploading anything large and having to spend
#   hours with seth again.

#toggle for data files
election_data_1 = os.path.join("..","..","resources","election_data_1.csv")
election_data_2 = os.path.join("..","..","resources","election_data_2.csv")

election_output_txt = os.path.join("..","..","resources","pypoll.txt")

election_result = []
election_data_1_voter = []
election_data_1_county = []
election_data_1_candidate = []

candidate_list = {}
total_votes = 0
winner = ""

with open(election_data_1, 'r', newline="") as csv_infile:
    csvreader = csv.reader(csv_infile, delimiter=",")

##############
##       read
##############
# extract values to play with
    for row in csvreader:
        if row[0] != "Voter ID":
            election_data_1_voter.append(row[0])
            election_data_1_county.append(row[1])
            election_data_1_candidate.append(row[2])

##############
##    do stuff
##############

#find uniques
# election_data_1_voter_set = set(election_data_1_voter)
election_data_1_county_set = set(election_data_1_county)
election_data_1_candidate_set = set(election_data_1_candidate)



#create buckets
# for item in election_data_1_candidate_set:
#     candidate_list[item] = 0

# print(candidate_list)

# #add to buckets
# for item in election_data_1_candidate:
#     candidate_list[item] = candidate_list[item] + 1

# print(candidate_list)



# but wait...
# 
# putting 2 for-loops together
for item in election_data_1_candidate:
    if item in candidate_list:
        candidate_list[item] += 1
    else:
        candidate_list[item] = 1
        
##############
##       maths
##############

total_votes = len(election_data_1_voter)  

winner = max(candidate_list.keys(), key=(lambda k: candidate_list[k]))

##############
##      output
##############

electionResult = zip(election_data_1_voter, election_data_1_county, election_data_1_candidate)

#to terminal
print("\nElection Results",
"\n-------------------------",
"\nTotal Votes: " + str(total_votes),
"\n-------------------------\n")
for item in candidate_list:
    print(item + ": " + (str("{0:.01f}%".format(candidate_list[item]/total_votes*100))) + "  (" + str(candidate_list[item]) + ")")

print("\n-------------------------\n",
    "Winner:  " + winner,
    "\n-------------------------\n"
    )

# prep for output

#using text files cause i just learnt how to in pybank
print("\nElection results exported to .txt file!\n")
with open(election_output_txt,'w') as text_file:
    print(f"Election Results\n",
"\n-------------------------",
"\nTotal Votes: " + str(total_votes),
"\n-------------------------\n",
file = text_file)
    for item in candidate_list:
        print(f"" + item + ": " + (str("{0:.01f}%".format(candidate_list[item]/total_votes*100))) +
        "  (" + str(candidate_list[item]) + ")", file = text_file)
        
    print(f"\n-------------------------\n",
        "Winner:  " + winner,
        "\n-------------------------\n",
        file = text_file)

#we dont need a copy of the csv in txt form...
    # print(f" -----------------\n",
    # "Data to follow:\n",
    # "-----------------\n",
    # file = text_file)
    # for item in electionResult:
    #     text_file.write(str(item)+"\n")