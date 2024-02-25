V = ["S", "A", "B"]
T = ["a", "b"]
P = {"S": "AB", "A": "aA", "B": "bB"}

def generate_words(productions, max_length, current_words=["S"]):
    if max_length == 0:
        return set(current_words)

    new_words = []
    for word in current_words:
        for i, char in enumerate(word):
            if char in productions:
                for replacement in productions[char]:
                    new_word = word[:i] + replacement + word[i+1:]
                    new_words.append(new_word)

    current_words.extend(new_words)
    current_words = list(set(current_words))

    return generate_words(productions, max_length - 1, current_words)

max_length = int(input("Enter max length: "))
words = generate_words(P, max_length)
print(words)
