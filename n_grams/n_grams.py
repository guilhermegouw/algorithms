import string

def n_grams(text: str) -> list:
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    n_grams_list = []
    for start in range(len(words)):
        words_slice = words[start:]
        for i in range(1, len(words_slice) + 1):
            item = " ".join(words_slice[0:i])
            n_grams_list.append(item)
    return n_grams_list
