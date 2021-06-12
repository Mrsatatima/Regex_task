# update the fucntions to count number of number(whole, decimal and fractions)
#  in article.txt
# use regex to match numbers and fractions
import re

def count_numbers(text):
    pattern = r"(?:-?\\frac{\d+}{\d+}|-?\d+\\tinyfrac{\d+}{\d+}|[A-Z]+[0-9]+|[a-z][0-9]+|-?\d+\.? ?,?\d+|-?\d+)"

    with open(text, "r") as f:
        text = f.read()
        regex = re.compile(char)
        matched = regex.findall(text)
        searched_matches = []
        for i in range(len(matched)):
            if re.compile(r"(?:^[-]?\d+\.? ?,?\d+$|^[-]?\d+$)").search(matched[i]):
                searched_matches.append(matched[i])
        count = len(searched_matches)
        return count
    return



def count_fraction(text):
    frac_pattern = r"(?:-?\\frac{\d+}{\d+}|-?\d+\\tinyfrac{\d+}{\d+})"

    with open(text, "r") as f:
        read_text = f.read()
        regex = re.compile(pattern)
        matched = regex.findall(read_text)
        count = len(matched)
        return count
    return


## Use this for your debugging purposes (all print statements should go here)
if __name__ == "__main__":
    print(count_numbers("article.txt"))
    print(count_fraction("article.txt"))
    
    # Replace pass with your debugging code if any
    pass
