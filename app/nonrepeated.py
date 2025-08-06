# nonrepeated.py

def first_non_repeated_char(s):
    from collections import Counter

    counts = Counter(s) 

    if all(count == 1 for count in counts.values()):
        return s[0]
    
    for char in s:
        if counts[char] == 1:
            return char

    return None

print(first_non_repeated_char("test"))