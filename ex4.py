paragraph = """ Python is fun to learn. Learning Phython helps you solve problems and practice logical thinking. Phyton is powerful! """

words = paragraph.lower().replace(".","").replace("!", "").split()

unique_words = set(words)

print("Unique words in the paragraph: ")
print(unique_words)
print(len(unique_words))
