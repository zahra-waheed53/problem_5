# Write a program that will calculate the average word length of a text entered by the user as input (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens

text = input("""Enter text:  """)
words = text.split()
average = sum(len(word) for word in words) / len(words)
print(average)