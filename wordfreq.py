# document = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
# ...             '130 hampsters from the cancer labs down the hall, and',
# ...             'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
# ...             'said the source on a recent Geraldo interview.']

def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        current_word_in_making = []
        while start < len(line):
            char = line[start]
            if char.isspace() == False:
                if char.isdigit():
                    print(f"{char} is a digit")
                    current_word_in_making.append(char)
                    if  start == len(line)-1 or line[start+1].isdigit() != True: #om det är slutet av line eller om nästa karaktär inte är samma som den just nu
                        new_word = "".join(current_word_in_making) #samma kod gör till funktion om man vill
                        words.append(new_word)
                        current_word_in_making = []
                    
                elif char.isalpha():
                    print(f"{char} is a letter")
                    current_word_in_making.append(char)
                    if  start == len(line)-1 or line[start+1].isalpha() != True: #om det är slutet av line eller om nästa karaktär inte är samma som den just nu
                        new_word = "".join(current_word_in_making) #samma kod gör till funktion om man vill
                        new_word = new_word.lower()
                        words.append(new_word)
                        current_word_in_making = []

                else:
                    print(f"{char} is a symbol")
                    current_word_in_making.append(char) 
                    #isalpha kommer inte att fungera ska ändra 
                    #spelar inte roll eftersom det är bara EN symbol! :(
                    new_word = "".join(current_word_in_making) #samma kod gör till funktion om man vill
                    words.append(new_word)
                    current_word_in_making = []
            start = start + 1
                
    return words

def countWords(words, stop_words):
    counted_words = {}
    for word in words:
        if word in stop_words:
            continue
        elif word in counted_words:
            counted_words[word] += 1

        else:
            counted_words.update({word: 1})
            
    return counted_words



test_strings = {"testar strings i en array: ": ["apple", "pie"],
                "testar om den tar bort whitespace: ": ['  \n  sweet  apple  tart.23']
                }

def split_func(string, **kwargs): #igga
    x = kwargs.get("c")
    return string.split()

def test(dict, function): #test funktion för att testa flera olika strings etc med olika funktioner
    for type, test_string in dict.items():
        print(type)
        print(function(test_string))


test(test_strings, tokenize)

#print(tokenize(document))