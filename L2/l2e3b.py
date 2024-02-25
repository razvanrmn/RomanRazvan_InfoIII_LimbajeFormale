V = ["S", "X", "Y", "Z"]
T = ["0", "1", "2", "3", "4"]
P = {"S": "X", "X": ["0Y", "1Z"], "Y": ["2", "X"], "Z": ["3", "4", "X"]}

def generate_words(productions, max_length, current_words=["S"]):
    if max_length == 0:
        return []

    new_words = []
    for word in current_words:
        if len(word) <= max_length:
            for i, char in enumerate(word):
                if char in productions:
                    for production in productions[char]:
                        new_word = word[:i] + production + word[i+1:]
                        new_words.append(new_word)

    new_words = list(set(new_words))
    terminal_words = [word for word in new_words if all(char not in productions for char in word)]

    return terminal_words + generate_words(productions, max_length - 1, new_words)

max_length = int(input("Enter max length: "))
words = generate_words(P, max_length)
print(words)
