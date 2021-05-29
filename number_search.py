# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import re


capture_numbers = r'([^a-zA-Z{./\\}]\d+ |\d+\.\d+| \d+[^/:\\)-}])'

capture_fractions = r'(-?\\frac{\d+}{\d+}[^A-Za-z]|-?\d+\\tinyfrac{\d+}{\d+}[^A-Za-z])'

captured_numbers = []
captured_fractions = []



def count_numbers(text):

    with open(text, 'r') as file:
        article = file.read()
        capture_pattern = re.compile(capture_numbers)
        match = capture_pattern.finditer(article)

        for num in match:
            captured_numbers.append(num.group(0))
        return len(captured_numbers)


def count_fraction(text):

    with open(text, 'r') as file:
        article = file.read()
        capture_pattern = re.compile(capture_fractions)
        match = capture_pattern.finditer(article)

        for frac in match:
            captured_fractions.append(frac.group(0))
        return len(captured_fractions)
        

    """
        counts fractional numbers i.e both negative an positive
        TODO update doc strings
    """

## Use this for your debugging purposes (all print statements should go here)
if __name__ == "__main__":
    
    # Replace pass with your debugging code if any
    pass
