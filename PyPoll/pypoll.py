# import os /csv , my hands are tied - no pandas
import os
import csv

# define path to file file_path="/Resources/election_data.csv"
file_path=os.path.join("Resources","election_data.csv")

# open file using csv open function, using csv reader to form csvreader object ....rows 
with open(file_path, 'r', encoding="utf-8") as csvfile:
    csvrow=csv.reader(csvfile, delimiter=",")
    header=(next(csvrow))
    # print(header) # debug print first row
    candidate_counter = {}  # initial dictionary naming
    for row in csvrow:      # populating dictionary - unique name  and counter
        if row[2] not in candidate_counter:
            candidate_counter[row[2]] = 1
        else:
            candidate_counter[row[2]] += 1 
    # print(candidate_counter) # debug print

total_votes=sum(candidate_counter.values()) # total votes is a sum of values 
#print(total_votes) # debug print

candidate_counter1={}  # creating additional dic to add % of votes
for key in candidate_counter:
    percent=(candidate_counter[key])/total_votes*100
    candidate_counter1[key]=["{:.3f}".format(percent),candidate_counter[key]]
#print(candidate_counter)
# print(candidate_counter1) # debug print

max_key = max(candidate_counter1, key=candidate_counter1.get) # getting key for max votes
# max_key # debug print

# Print Analysis - create list of strings with print content
prn_str=" Election Results \n"
prn_str+="-"*40+"\n"
prn_str+=f" Total Votes: {total_votes}\n"
prn_str+="-"*40+"\n"
for key in candidate_counter:
    prn_str+=f" {key} :{candidate_counter1[key][0]}% ({candidate_counter1[key][1]})\n"
prn_str+="-"*40+"\n"
prn_str+=f" Winner: {max_key}\n"
prn_str+="-"*40+"\n"

print(prn_str)
# file path to write
file_path2 = os.path.join('Resources', 'polls_results.text')

# Open File Using to "Write". and write print list
with open(file_path2, 'w') as txt_file:
     txt_file.write(prn_str)
print(f'\n File is created/(written over) at {file_path2}" \n the end')