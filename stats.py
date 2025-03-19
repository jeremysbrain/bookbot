def count_words(contents):
    return len(contents.split())

def count_characters(contents):
    char_count = {}
    for char in contents:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count