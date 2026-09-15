document = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
...             '130 hampsters from the cancer labs down the hall, and',
...             'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
...             'said the source on a recent Geraldo interview.']

def tokenize(lines):
    words = []

    
    for line in lines:

        start = 0
        
        while start < len(line):
            print(line[start])
            start = start+1

    return words


#print(tokenize(document))