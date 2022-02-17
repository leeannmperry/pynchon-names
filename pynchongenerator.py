import random
import sys

def process_line(line):
    linel = list(line)
    linel.insert(0, 'BEGIN')
    linel.append('END')

    tuplelist = list(zip(linel, linel[1::], linel[2::]))

    return tuplelist

def process_textfile(filename):
    d = {}

    with open(filename,'r') as file:
        lines = file.readlines()
        for x, line in enumerate(lines):
            lst = process_line(str(line))
            for tuples in lst:
                tuplesS = str(tuples[0] + " " + tuples[1])
                if tuplesS in d:
                    d[tuplesS].append(tuples[2])
                else: 
                    d[tuplesS] = [tuples[2]]
    return d

def generate_line(d):
    import random
    nextkey = random.choice(list(k for k, v in d.items() if 'begin' in k.lower()))
    sentence = list(nextkey)[-1]
    nextword = []

    while nextword != 'END':
        nextword = random.choice(d[nextkey])
        nextkey = list(nextkey)[-1] + " " + nextword
        sentence = sentence + " " + nextword
    print(sentence)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: Run as python pynchongenerator.py <filename>')
        exit()

d = process_textfile(sys.argv[1])
generate_line(d)

