# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import regex as re
def count_numbers(text):
    """
        counts whole number and decimals i.e -ve and +ve whole numbers decimals
        TODO update doc strings
    """
    file = open(text,"r")
    new_text = file.read()
    number = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))($|[.,]$)')
    x = new_text.split()
    nums = []
    count = 0
    for i in x:
        if number.match(i):
            nums.append(i)
            count += 1
    return  count



def count_fraction():
    """
        counts fractional numbers i.e both negative an positive
        TODO update doc strings
    """
    pass #TODO update the fucntion to pass test

print(count_numbers("article.txt"))
