# Was done without step by step instructions.
my_word_list = ['Shabbos', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def count_len_word_with_loop(word_list):
    words_len = []
    for word in word_list:
        words_len.append(len(word))
    return words_len

print(count_len_word_with_loop(my_word_list))

def count_len_word(word):
    return len(word)

len_words = map(count_len_word, my_word_list)
print(list(len_words))



