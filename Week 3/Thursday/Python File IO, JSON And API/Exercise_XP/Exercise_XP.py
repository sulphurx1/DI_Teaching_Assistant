from random import choice

def get_words_from_file():

    f = open('sowpods.txt')
    words = f.read()
    
    words_list = words.split("\n")

    return words_list
    

def get_random_sentence(length):

    words = get_words_from_file()

    random_sentence = []
    if length < 2:
        ValueError

    else: 
        for len in range(length):
            x = choice(words.lower())
            random_sentence.append(x)

    y = " ".join(random_sentence)

    return y



    


# get_words_from_file()
get_random_sentence(8)
