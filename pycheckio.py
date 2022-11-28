#Most frequent

"""
first_list = ['a', 'a', 'bi', 'bi', 'bi']

def most_frequent(x): 
    counter = 0
    num = x[0]
    for c in x: 
        freq = x.count(c)
        if freq > counter:
            counter = freq
            num = c
    return num 
            
print(most_frequent(first_list))
"""


#Easy unpack

"""
first_tuple = (6, 2, 9, 4, 3, 9)

def easy_unpack(x):
    x = list(x)
    d = []
    a = x.pop(0)
    d.append(a)
    b = x.pop(1)
    d.append(b)
    c = x.pop(-2)
    d.append(c)    
    return tuple(d) 

print(easy_unpack(first_tuple))
"""


# Split pairs

"""
The example that helped me to solve:

# How many elements each 
# list should have 
n = 4
   
# using list comprehension 
x = [l[i:i + n] for i in range(0, len(l), n)] 
print(x)

Output:
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]
"""


#separate with two 

"""
four_string = 'abcd'
three_string = 'abc'
five_string = 'abcde'

def test_func(x):
    x = [x[i: i + 2].ljust(2, '_') for i in range(0, len(x), 2)]
    return x

print(test_func(three_string))
"""


#Nearest value

"""
set_val = {4, 7, 10, 11, 12, 17}
val = 9


def nearest_value(values, one):
    values = sorted(list(values))
    if values[0] < 0:
        diff = lambda values : values - one
    else:
        diff = lambda values : abs(values - one)
    result = min(values, key = diff)
    return result


print(
    #list(set_val)
    nearest_value(set_val, val)
)
"""


#Non-unique Elements

"""
listik = [1, 2, 3, 4, 5]
listik_2 = [1, 2, 3, 1, 3]

def non_unique(data: list) -> list:
    c = [i for i in data if data.count(i) > 1] 
    return c 


print(
    non_unique(listik)
)
"""

"""
#Right to left

seq_str = ("aright", "right", "left", "stop")

def right_left(phrases: tuple) -> str:
    new_list = []
    for i in list(phrases):
        i = i.replace('right', 'left')
        new_list.append(i)
    return ', '.join(map(str, new_list))
            
print(
    right_left(seq_str)
)
"""


#Days Between

"""
from datetime import datetime

f_date = (2004, 1, 10)
s_date = (2008, 6, 15)

def days_diff(a:tuple[int, int, int], b:tuple[int, int, int]) -> int:
    first_date = datetime(*a)
    second_date = datetime(*b)
    result = second_date - first_date
    return abs(result.days)
    

print(
    days_diff(f_date, s_date)
)
"""


#Count Digits

"""
string = "who is 1st here"

def count_digits(text: str) -> int:
    text_dict = text.split()
    digits_count = 0
    for i in text_dict:
        for c in i:
            if c.isdigit() == True:
                digits_count += 1
    return digits_count

print(
    count_digits(string)
)
"""


#Duplicate Zeros

"""
donuts = [1, 0, 2, 0]

def donuts_duplicator(donuts):
    duplicated_list = []
    for i in donuts:
        if i == 0:
            duplicated_list.append(i)
            duplicated_list.append(i)
        else:
            duplicated_list.append(i)
    return duplicated_list

print(
    donuts_duplicator(donuts)
)
"""


#First Word. Get first word from the string

from detect_delimiter import detect
import string 
#choose string
string_1 = " greetings, friends "
string_2 = "... and so on ..."
string_3 = "don't touch it"
string_4 = "Hello.World"

def first_word(text:str) -> str:
    new_list = []
    delimiter = detect(text, whitelist = [string.punctuation, string.whitespace])
    splited_text = text.split(delimiter)
    for i in splited_text:
        if (len(i) > 0) and (i[0].isalpha() == True):
            for c in i[::-1]:
                if c in string.punctuation:
                    i = i.strip(c)
            new_list.append(i)
    return new_list[0], delimiter


print(
    first_word(string_4)
)





