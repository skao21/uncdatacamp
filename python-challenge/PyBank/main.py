#!/usr/bin/python3

import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # create a list cotainer
    rows = [ i for i in csvreader ]

    # Calculate total profit and loss, add total months involved
    profitLoss = [ float(i[1]) for i in rows ]

    totMonths = len(profitLoss)

    totalPL = sum(profitLoss)

    # Build a list to contain the P&L difference for each month
    diffs = [ profitLoss[i] - profitLoss[i-1] if i != 0 else 0 for i in range(len(profitLoss)) ]

    # Calculate the average P&L difference
    avgChanges = round(sum(diffs) / (len(diffs) - 1 ),2)

    # find out the greatest Profit in price and in month
    greatestInc = max(diffs)

    gIncMonth = rows[diffs.index(greatestInc)][0]

    # find out the greatest loss in price and in month
    greatestDec = min(diffs)
    
    gDecMonth = rows[diffs.index(greatestDec)][0]
    
     # create output file
    outpath = os.path.join('.', 'Resources', 'pybank_result.txt')

    with open(outpath, 'w') as text:
        line = f"Financial Analysis\n----------------------------\nThe total number of months:\t\t\t {totMonths}\n"
        line += f'The net total amount of "Profit/Losses": \t${totalPL}\n'
        line += f'"Average Change: \t\t\t\t${avgChanges}\n'
        line += f"The greatest increase in profits: \t\t{gIncMonth} (${greatestInc})\n"
        line += f"The greatest decrease in losses: \t\t{gDecMonth} (${greatestDec})\n"
        text.write(line)

    print(line)