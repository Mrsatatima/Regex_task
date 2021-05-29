# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import re
frac_pattern = r'(-?\d+\\tinyfrac{\d+}{\d+}[^A-Za-z]|-?\\frac{\d+}{\d+}[^A-Za-z])'
number_pattern = r"([^\na-zA-Z{./\\}]\d+ |\d+\.\d+|\d+[^\n/:\\)-}])"
numbers = []
fractions = []


def count_numbers(text):
    """
        counts whole number and decimals i.e -ve and +ve whole numbers decimals
        TODO update doc strings
    """

    with open(text, "r") as f:
        article = f.read()
    pattern = re.compile(number_pattern)
    match = pattern.finditer(article)
    for x in match:
        print(x.group(0))
        numbers.append(x.group(0))
    print(numbers)
    return len(numbers)


def count_fraction(text):
    """
        counts fractional numbers i.e both negative an positive
        TODO update doc strings
    """

    with open(text, "r") as f:
        article = f.read()

    pattern = re.compile(frac_pattern)
    match = pattern.finditer(article)
    for x in match:
        print(x.group(0))
        fractions.append(x.group(0))
    print(fractions)
    return len(fractions)


# Use this for your debugging purposes (all print statements should go here)
if __name__ == "__main__":

    # Replace pass with your debugging code if any
    pass
