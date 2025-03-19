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

def sort_on_count(dict):
    return dict["count"]

def count_characters_sorted(dict_count_characters):
    sorted_char_count = []
    for key in dict_count_characters:
        sorted_char_count.append({"character": key, "count": dict_count_characters[key]})
    sorted_char_count.sort(reverse=True, key=sort_on_count)
    return sorted_char_count
