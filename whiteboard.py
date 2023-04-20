# DESCRIPTION:
# Given a string, return a string that :
# Moves the first letter of each word to the end of it, then adds “ay” to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it(‘Pig latin is cool’) : ‘igPay atinlay siay oolcay’
# pig_it(‘Hello world !’)     : ‘elloHay orldway !’





def pig_it(str):
    x = str.split()
    pig_words = []
    for i in x:
        if i.isalpha():
            pig_words.append(i[1:]+i[0]+'ay')
        else:
            pig_words.append(i)

    return (' '.join(pig_words))
    
print(pig_it('Hello World !'))








# string_of_words = 'what do you say'

# print(string_of_words.split())