def count_words(words):
    word_set = set(words)
    word_counts = {}
    for word in word_set:
        word_counts[word] = words.count(word)
    return word_counts

words = ["apple", "banana", "cherry", "apple", "banana", "apple"]
word_counts = count_words(words)
print(f"The unique words and their frequency of occurrence are: {word_counts}")