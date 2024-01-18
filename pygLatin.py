#Lauren A 1588217949 11/20/23

print('******Welcome to Pyglatin Translator******\n')

def translate(i_phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    clusters = ['st', 'sm', 'gl', 'tr', 'fl', 'sl', 'th', 'sh', 'br', 'bl']
    special_cluster = ['str']
    
    if i_phrase.isalpha() == True:
        #iterates through all possible vowels (not including y)
        for x in range(len(vowels)):
            if i_phrase[0].lower() in vowels[x]:
                i_phrase = i_phrase + 'yay'
                return i_phrase
            
        #iterates through all possible clusters of consonant sounds
        for i in range(len(clusters)):
            if i_phrase[0:3].lower() in special_cluster[0]:
                i_phrase = i_phrase[3:] + i_phrase[0:3] + 'ay'
                return i_phrase
            elif i_phrase[0:2].lower() in clusters[i]:
                i_phrase = i_phrase[2:] + i_phrase[0:2] + 'ay'
                return i_phrase
            
        if 'ay' not in i_phrase[:-2].lower():
            i_phrase = i_phrase[1:] + i_phrase[0] + 'ay'
            return i_phrase
        

def piglatin(phrase):
    
        phrase = phrase.split()
        for i in range(len(phrase)):
            if phrase[i].isalpha() == True:
                for i in range(len(phrase)):
                    phrase[i] = translate(phrase[i])
                phrase = ' '.join(phrase)
                return phrase
            else:
                return 'Invalid syntax, must be a word.'


def main():
    #prompt only appears to begin the program and is not seen again
    phrase = input('Enter a word you would like to translate: ')
    
    while True:
        #prints what the function returns
        print(piglatin(phrase))
        print('\n')
        #this is the prompt that will continuously appear until the loop breaks
        phrase = input('Enter a word or q to quit: ')
        print('\n')
        
        if phrase.lower() == 'q':
            #entire program will be over when user enters 'q' or 'Q'
            break



#begins program
main()