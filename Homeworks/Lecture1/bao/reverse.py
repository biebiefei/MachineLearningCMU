#!/usr/bin/python

import sys

def reverseWords(input, output):
    f = open(input, "r+")
    lineAsString = f.readline()
    f.close()

    #Since the reverse method only works for lists, we first split the words in the input string by "\n", and then reverse the them..
    wordList = lineAsString.split("\\n")
    wordList = wordList[:-1] #Remember that there is an extra "\n" at the end of the input string, so we remove the last null string in the list
    wordList.reverse()
    outputString = "" #Initialize the output string as a null stirng
    for word in wordList:
        outputString = outputString + word + "\\n"

    f = open(output, "w+")
    f.write(outputString)
    f.close()

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    reverseWords(input, output)
