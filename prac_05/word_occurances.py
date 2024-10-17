"""
20 minutes
14 minutes
"""
word_to_occurrences = {}
text = input("Enter text: ")
words = text.split()
for word in words:
    occurrences = word_to_occurrences.get(word, 0)
    word_to_occurrences[word] = occurrences + 1
words = list(word_to_occurrences.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_occurrences[word]}")
