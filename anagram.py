import sys
import numpy as np

path = 'wordlist2.txt'

def unique(arr):
    unique_arr = []
    for x in arr:
        if x not in unique_arr:
            unique_arr.append(x)
    
    for y in unique_arr:
        print(y)

final_array = []

def isAnagram(word1, word2):
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())

    return sorted_word1 == sorted_word2
    
#ajuntar por cantidad de letras

with open(path, 'r') as f:
    data = f.readlines()

    for word in data:
        
        temp_array = []
        temp_array.append(word)

        word_length = len(word)

        same_length_words = []

        for word2 in data:
            if len(word2) == len(word):
                same_length_words.append(word2)

        for word3 in same_length_words:  
            checker = False
                
            if isAnagram(word, word3):
                temp_array.append(word3)
                
        temp_array.pop(0)

        final_array.append(temp_array)

unique(final_array)

print(isAnagram("claimed", "decimal"))