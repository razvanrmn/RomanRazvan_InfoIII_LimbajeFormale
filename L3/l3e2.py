import itertools
import random

class FiniteStateMachine:
    def __init__(self):
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2', 'c': 'q1', 'd': 'q1'},
            'q2': {'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q2'},
            'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'},
        }
        self.start_state = 'q0'
        self.final_state = 'q3'

    def is_accepted(self, word):
        current_state = self.start_state

        for letter in word:
            if letter not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][letter]

        return current_state == self.final_state

E = ["a", "b", "c", "d"]
words = [''.join(permutation) for permutation in itertools.permutations(E, 3)]

fsm = FiniteStateMachine()

print("The generated words are:")
print(words)
for _ in range(3):
    word_to_check = random.choice(words)
    if len(word_to_check) * 2 <= 6 and fsm.is_accepted(word_to_check):
        print(f"The word '{word_to_check}' is accepted")
    else:
        print(f"The word '{word_to_check}' is rejected")
