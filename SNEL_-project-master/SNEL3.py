import random
import math
import string
import os


def get_file_content():
    num_chars = 18000
    result = ""
    for i in range(num_chars):
        n = random.randrange(32,127)
        result += chr(n)
    return(result)
    
def get_char_counts(result):
    counts = [0] * 127
    
    for c in result:
        n = ord(c)
        counts[n] += 1
        
    
    counts = counts[32:]
    print(counts)


def random_file_writer(num_chars):
    file_num = "0"

    for n in range(num_files):
        files =  open("file" + str(file_num) + '.txt', 'w' )

        file_num += str(1)

        for i in range(1):
            files.write(num_chars)
        
        

def chi_square(vals):
    
    x = 0

    

    expected = sum(vals)/ len(vals)
    for observed in vals :
        x += (observed - expected) ** 2 / (expected)
    return x 

def file_read():


    for n in num_files(): 
         file = open("file" + str(file_num) + '.txt', 'r')
         print(x)

            
        

''' you got it to at least add all the letters for each letter''' 


#lets do this
num_files = 2
threshold = 50

#file_names = os.listdir("C:\Users\dhamil1351\Documents\text_files")
#print(file_names[:10])


'''for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("files/"+ file_name)
    counts = get_char_counts(text)
    chi_square = chi_square(counts)


    if chi_square > threshold:
        print(file_name,chi_square)'''

    

    









get_file_content()
vals = [4,3]
get_char_counts(get_file_content())

print(chi_square(vals))
random_file_writer(get_file_content())

