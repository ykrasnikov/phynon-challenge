
# Phynon Challenge
  <img src="https://github.com/ykrasnikov/phynon-challenge/blob/main/Images/anaconda.gif" align="right" width="200"/>



**_Python Homework_** 



Homework consists of 4 parts : **PyBank , PyPoll, PyBoss and PyParagraph** and mainly focusing on basic concepts:
 We practiced **_creating loop, open file to  read/wriet, operating with data structures ( variables, string ,tuple, list, dictionary etc )_**. Special attention was given to **_string comprehension_** applications.
Code was created using **Jupiter Notebook 6.0.3 /Python 3.8.3**

### Part 1. PyBank
<img src="/Images/pybank.png" align="right" width="400"/>

Python script for analyzing the financial records of a company. Provided data set contains 2 columns of financial data: `Date` and `Profit/Losses`.

[Main.Py ](/PyBank/main.py) 
 is a python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

and outputs it to [text file](/PyBank/Resources/budget_data_results.text) 


### Part 2. PyPoll

<img src="/Images/pypoll.png" align="right" width="400" />
In this challenge, we are tasked with helping a small, rural town to modernize its vote counting process. 

Poll dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

[Main.Py ](/PyPoll/main.py)
 is a python script that analyzes the records to calculate each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.

and outputs it to [text file](/PyPoll/Resources/polls_results.text) 

### Part 3. PyBoss 
<img src="/Images/pyboss.jpg" align="right" width="400" />
Python script converts employee records to the specified format. 

[Main.Py ](/PyBoss/main.py) reads CSV file, formats data as required :
  * The `Name` column should be split into separate `First Name` and `Last Name` columns.
  * The `DOB` data should be re-written into `MM/DD/YYYY` format.
  * The `SSN` data should be re-written such that the first five numbers are hidden from view.
  * The `State` data should be re-written as simple two-letter abbreviations.
and outputs it to [CSV file](/PyBoss/Resources/converted_employee_data.csv) 


### Part 4. PyParagraph
<img src="/Images/pyparagraph.png" align="right" width="400" />
 Python script automates the analysis of any paragraph using specified metrics. 

 [Main.Py ](/PyParagraph/main.py) reads a txt file with a paragraph, and assesses the passages for each of the following:
 * Approximate word count
 * Approximate sentence count
 * Approximate letter count (per word)
 * Average sentence length (in words)

And prints results on the screen.
