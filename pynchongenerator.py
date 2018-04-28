import random
import sys

def process_line(line):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''
    linel = list(line)
    linel.insert(0, 'BEGIN')
    linel.append('END')

    tuplelist = list(zip(linel, linel[1::], linel[2::]))

    return tuplelist

def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    """with open(filename,'r') as file:
        lines = file.readlines()

        for x, line in enumerate(lines):
            lst = process_line(str(line))
            for tuples in lst:
                if tuples[0] in d:
                    d[tuples[0]].append(tuples[1])
                else: 
                    d[tuples[0]] = [tuples[1]]
    return d"""

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
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''
    """import random
    sentence = ""
    nextkey = 'BEGIN'
    while nextkey != 'END':
        nextkey = random.choice(d[nextkey])
        if nextkey != 'END':
            sentence = sentence + " " + nextkey"""
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

