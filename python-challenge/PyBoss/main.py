# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# for us state abbreviation
from us_state_abbr import us_state_abbrev as ab

# print(ab['Alabama'])

csvpath = os.path.join('.', 'Resources', 'employee_data.csv')
output_path = os.path.join(".", "Resources", "result.csv")


# Improved Reading using CSV module

with open(csvpath, newline='') as csvfile, open(output_path, 'w', newline='') as outfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize csv.writer
    csvwriter = csv.writer(outfile, delimiter=',')
    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Write the first row (column headers)
    # csvwriter.writerow(csv_header)
    csvwriter.writerow(['Emp ID', 'First Name'.ljust(20), 'Last Name', 'DOB', 'SSN', 'State'])

    # Read each row of data after the header AND write a new translated row
    for row in csvreader:
        mmddyyyy = row[2].split('-')[1] + '/' + row[2].split('-')[2] + \
            '/' + row[2].split('-')[0]
        csvwriter.writerow([row[0], row[1].split()[0].rjust(20), row[1].split()[1].rjust(20), mmddyyyy,  \
            "***-**-".rjust(20) + row[3][-4:], ab[row[4]].rjust(20) ])