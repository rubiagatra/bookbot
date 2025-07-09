def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(path):
    num_words = len(get_book_text(path).split()) 
    return num_words

def get_count_characters(path):
    count_characters = {}
    text = get_book_text(path).lower()
    for char in text:
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1
    return count_characters

def sort_on(items):
    return items["num"]

def sorted_list_dictionaries(path):
    character_list = []
    characters = get_count_characters(path)
    for key, value in characters.items():
        character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

