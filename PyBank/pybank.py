# IN dedication to Carlos's List Comprehensions and playing with dictionaries
# import os /csv , my hands are tied - no pandas
import os
import csv

# define path to file file_path="/Resources/budget_data.csv"
file_path=os.path.join("Resources","budget_data.csv")

# open file using csv open function, using csv reader to form csvreader object ....rows 
with open(file_path, 'r', encoding="utf-8") as csvfile:
    csvrow=csv.reader(csvfile, delimiter=",")
    header=(next(csvrow))
    # print(header) # debug print first row
    # create dictionary key =month , value =float of profits from csvreader object
    mydict = {r[0]:float(r[1]) for r in csvrow} 
    # print(mydict) #debug print dictionary


# creating reversed dictionary  key- change of profit from one month to another (original dates are sorted)
i_dict={}
for x,y in mydict.items():
    if x!=list(mydict.keys())[0]:  # skip first row in original as there is nothing to subtract
        i_dict[y-previous_month]=x
    previous_month=y               # little buffer for previous month value
#print(i_dict)    #debug print
# total months will be length of original dictionary keys , can just use 
total_month=len(mydict)
# print(total_month) #debug print
# finding max value for profit loss and corresponding date - create tuple from reversed change of profit dictionary
max_tuple=max(i_dict.items()) 
max_ch="${:,.2f}".format(max_tuple[0])
#print(max_tuple) # debug print
#print(max(mydict.values())) # debug  check 
# same for min profit tuple
min_tuple=min(i_dict.items())
min_ch="${:,.2f}".format(min_tuple[0])
# print(min_tuple) #debug print
#  suym of all profits - using sum function
total=sum(mydict.values())
formatted_total = "${:,.2f}".format(total)
# print(formatted_total) #debug print
# average change in profit calculation - sum of keys divided by length
average_change=sum(i_dict.keys()) / len(i_dict)
formatted_ac = "${:,.2f}".format(average_change)
# print(formatted_ac) #debug print
# Print Analysis - create list of strings with print content
prn_str="Financial Analysis \n"+"_"*40+"\n"
prn_str+=f"Total Months: {total_month}\n"
prn_str+=f"Total: {formatted_total}\n"
prn_str+=f"Average Change: {formatted_ac}\n"
prn_str+=f"Greatest Increase in Profits: {max_tuple[1]} ({max_ch})\n"
prn_str+=f"Greatest Decrease in Profits: {min_tuple[1]} ({min_ch})\n"
print(prn_str)
# file path to write
file_path2 = os.path.join('Resources', 'budget_data_results.text')
# Open File Using to "Write". and write print list
with open(file_path2, 'w') as txt_file:
     txt_file.write(prn_str)
print(f'\n File is created/(written over) at "{file_path2}" \n the end\n')