#!/usr/bin/python3

# for regular expression
import re

# This will allow us to create file paths across operating systems
import os

file = os.path.join('.', 'Resources', 'paragraph_1.txt')

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()
    
    # get char count, word count and sentence count
    charCount = len(re.findall("[A-z]", lines))

    wordCount = len(re.split(r"\s+", lines))

    sentenceCount = len(re.split("(?<=[.!?]) +", lines))

    # Generate report accordingly
    print("Approximate Word Count: ", wordCount)

    print("Approximate Sentence Count: ", sentenceCount)

    print("Average Letter Count: ", round(charCount / wordCount, 2))

    print("Average Sentence Length: ", round(wordCount / sentenceCount, 2))
    