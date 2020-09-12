#!/usr/bin/env python3
import argparse
import sys
from gensim.summarization.summarizer import summarize

parser = argparse.ArgumentParser(description='Summarise a text file')
parser.add_argument('input', metavar='input', type=str, 
                    help='Name of the input .txt file')

args = parser.parse_args()

input_filename = args.input
output_filename = input_filename.replace('.txt', '')

def preprocess(s):
    s = s.replace('- ', '')
    s = s.replace('\t', ' ')
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

f = open(input_filename, "r")
input_text = f.read()

input_text = preprocess(input_text)

print("Summarizing...")

summary = summarize(input_text)

with open(f"{output_filename}_summary.txt", "wt") as out:
    out.write(summary)
    print(f"Summary complete in {output_filename}_summary.txt")