from number_search import*

def test_number_count():
    text = "article.txt"
    assert(count_numbers(text) == 162)

def test_fraction_count():
    text = "article.txt"
    assert(count_fraction(text) == 35)
