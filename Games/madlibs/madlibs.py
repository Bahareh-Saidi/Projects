with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:  ##this means we already found the ending of the word which is > and if the start_of_word is -1 it means we dont's have anything for the start
        word = story[start_of_word : i+1]
        words.add(word)
        start_of_word = -1 ## reset the start_of_word

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)