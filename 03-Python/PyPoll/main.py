#!/usr/bin/python3

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# for round function
import math

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

countVotes = lambda  cand, candVotes : candVotes[cand] + 1 if cand in candVotes.keys() else 1

#open CSV file 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # initialize data
    totalVotes = 0
    # extrace from csvreader to a list
    candidatesVotesList = [ row[2].lstrip().rstrip()  for row in csvreader]

    candidates = set(candidatesVotesList)

    # initialize vote counts as a dictionary
    voteCountPerCandidate = { i: candidatesVotesList.count(i) for i in candidates}

    # generate report line
    totalVotes = sum(voteCountPerCandidate.values())

    winnerVotes = max(voteCountPerCandidate.values())

    line = f"Election Results\n----------------------------\nTotal Votes: \
            {totalVotes}\n-------------------------\nCandidate list: \
            {candidates}\n-------------------------\n"

    winner = ''

    for candidate, voteCounts in voteCountPerCandidate.items():

        line += f"{candidate} :  {'{0:0.3f}'.format(voteCounts * 100 / totalVotes)}%\t({voteCounts})\n"

        if voteCounts == winnerVotes:

            winner = candidate

    line += f'-------------------------\nWinner: {winner}'

     # create output file
    outpath = os.path.join('.', 'Resources', 'pypoll_result.txt')

    # output 
    with open(outpath, 'w') as text:

        text.write(line)

    print(line)