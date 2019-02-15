import random
import math
import string
import os

def random_file_writer(num_chars):
    file_num = "0"
    for n in range(num_files):
        files =  open("file" + str(file_num) + '.txt', 'w' )
        file_num += str(1)
        for i in range(1):
            files.write(num_chars)

def get_file_name(num):
    num_str = hex(num)
    num_str = num_str[2:]

    return "file_" + num_str.upper().zfill(4) + ".txt"



def get_file_content():
    # open file_name, read it, return the contents

    
    file_name = open('text_files/file_0000.txt', 'r')

    return file_name.read()
     
    
def get_char_counts(result):
    counts = [0] * 127
    for c in result:
        n = ord(c)
        counts[n] += 1
    counts = counts[32:]
    print (counts)

   
def chi_square(vals):
    x = 0
    expected = sum(vals)/ len(vals)
    for observed in vals :
        x += (observed - expected) ** 2 / (expected)
    return x 


def file_read():
    for n in range(18000): 
         file = open("file" + str(get_hex(n)) + '.txt', 'r')
         print(x)


    

#write get hex function

  
''' you got it to at least add all the letters for each letter''' 


#lets do this
'''
num_files = 1
threshold = 50


for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("files/"+ file_name)
    counts = get_char_counts(text)
    chi_square = chi_square(counts)


    if chi_square > threshold:
        print(file_name,chi_square)
'''

print( get_file_name(0) ) # file_0000.txt
print( get_file_name(9) ) # file_0009.txt
print( get_file_name(10) ) #file_000A.txt
print( get_file_name(2342) )
print( get_file_name(17999) )
print( get_char_counts(get_file_content()) )



