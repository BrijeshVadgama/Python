# 8. WAP to remove all the duplicate words from the list using dictionary.

word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "orange"]

word_dict = {}

# Populate the dictionary with unique words
for word in word_list:
    word_dict[word] = True

unique_words = list(word_dict.keys())

print("List with duplicate words removed:")
print(unique_words)
