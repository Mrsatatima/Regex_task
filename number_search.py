# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import re


def count_numbers(text):
    """
        counts whole number and decimals i.e -ve and +ve whole numbers decimals
        TODO update doc strings
    """
    count = 0
    pattern = re.compile(r'(\d+| \d+\.\d+)')
    with open('article.txt', 'r') as f:
        file = f.read()
        matches = pattern.finditer(file)
        for match in matches:
            #print(match)
            count += 1
    return count
    pass #TODO update the fucntion to pass test



def count_fraction(text):
    """
        counts fractional numbers i.e both negative an positive
        TODO update doc strings
    """
    count = 0
    pattern = re.compile(r'(\d+)?\\(tinyfrac|frac)+[0-9{}]+ (?!a)')
    with open('article.txt', 'r') as f:
        file = f.read()
        matches = pattern.finditer(file)
        for match in matches:
            print(match)
            count+=1

    return count
    pass #TODO update the fucntion to pass test


## Use this for your debugging purposes (all print statements should go here)
if __name__ == "__main__":
    count_numbers("article.txt")
    #count_fraction("article.txt")
    # Replace pass with your debugging code if any
    pass
