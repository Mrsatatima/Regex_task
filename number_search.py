# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import re

def count_numbers(text):
    pattern = r"^[-]?((\d+(\.\d+)?)|(\.?,?\d+))($|[.,]$)"

    with open(text, "r") as f:
        text = f.read().split()
        regex = re.compile(pattern)
        searched_matches = []
        for item in text:
            if regex.match(item):
                searched_matches.append(item)
                
        count = len(searched_matches)
        return count
    return
    pass #TODO update the fucntion to pass test



def count_fraction(text):
    frac_pattern = r'^[-]?((\d+\\tinyfrac)|(\\frac)){\d+}{\d+}$'

    with open(text, "r") as f:
        read_text = f.read().split()
        regex = re.compile(frac_pattern)
        search_fraction = []
        for item in text:
            if regex.match(item):
                search_fraction.append(item)
        
        count = len(search_fraction)
        return count
    return
    pass #TODO update the fucntion to pass test


## Use this for your debugging purposes (all print statements should go here)
if __name__ == "__main__":
    print(count_numbers("article.txt"))
    print(count_fraction("article.txt"))
    
    # Replace pass with your debugging code if any
    pass
