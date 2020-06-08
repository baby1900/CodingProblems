"""
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome

For example, given the list ["code", "edoc", "da", "d"], return[(0,1), (1,0), (2,3)]
"""
def is_pali(word):
    return word == word[::-1]


def genreate_pali(wordarr):
    word_dict = {}
    for i, word in enumerate(wordarr):
        word_dict[word] = i

    result = []

    for index, word in enumerate(wordarr):
        for char_index in range(len(word)):
            currprefix = word[:char_index]
            currsurfix = word[char_index:]
            reversed_surfix = currsurfix[::-1]
            reversed_prefix = currprefix[::-1]
            if is_pali(reversed_surfix + word) and reversed_surfix in word_dict:
                if index != word_dict[reversed_surfix]:
                    result.append((word_dict[reversed_surfix], index))
            if is_pali(word + reversed_prefix) and reversed_prefix in word_dict:
                if index != word_dict[reversed_prefix]:
                    result.append((index, word_dict[reversed_prefix]))
            if currprefix == "" and is_pali(word):
                if currprefix in word_dict:
                    result.append((word_dict[currprefix], index))
    return result

