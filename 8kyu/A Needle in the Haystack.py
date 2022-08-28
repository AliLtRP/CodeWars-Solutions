def find_needle(haystack):
    word = 'needle'
    if word in haystack:
        b = haystack.index(word)
    return f"found the needle at position {b}"
