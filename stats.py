def word_count(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count

def sort_characters(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():  # only include alphabet characters (no space, punctuation, numbers)
            char_list.append({'char': char, 'count': count})
    char_list.sort(key=lambda d: d['count'], reverse=True)
    return char_list

