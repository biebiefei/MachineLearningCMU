import sys

def doSomething(input, output):
    file1 = open(input, "r+")
    doc = file1.readlines()
    doc.reverse()
    f = open(output, "w+")
    f.writelines(doc)

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    doSomething(input, output)
