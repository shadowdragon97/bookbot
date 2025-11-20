
def get_book_text(path):
    with open(path) as f:
        file_content = f.read()

    return file_content

def count_words(path):
    text = get_book_text(path)
    words_list = text.split()
    list_lenght = len(words_list)
    return list_lenght

def count_char(path):
    text = get_book_text(path).lower()
    chr_dict = {}

    for chr in text:
        if chr in chr_dict:
            chr_dict[chr] = chr_dict[chr] + 1
        else:
            chr_dict[chr] = 1

    return chr_dict

def sort_on(items):
    return items["num"]

def sort_char(path):
    char_dict = count_char(path)
    char_list = []
    for k,v in char_dict.items():
        char_list.append({"char": k, "num": v})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
