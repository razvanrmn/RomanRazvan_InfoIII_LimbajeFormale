class NFA:
    def __init__(self):
        self.states = {'S0', 'S1', 'S2', 'S3'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'S0': {'a': {'S2'}, 'b': {'S3'}},
            'S1': {'a': set(), 'b': set()},
            'S2': {'a': {'S1', 'S2'}, 'b': {'S2'}},
            'S3': {'a': {'S3'}, 'b': {'S1'}}
        } 
        self.initial_state = 'S0'
        self.accept_states = {'S1'}

    def is_accepted(self, string):
        current_states = {self.initial_state}

        for char in string:
            next_states = set()
            for state in current_states:
                next_states |= self.transitions[state].get(char, set())
            current_states = next_states

        return bool(current_states & self.accept_states)


if __name__ == "__main__":
    nfa = NFA()

    strings = ["ab", "aab", "bb", "bba", "ba", "a", "b"]
    for string in strings:
        if nfa.is_accepted(string):
            print(f"String '{string}' is accepted by the NFA.")
        else:
            print(f"String '{string}' is not accepted by the NFA.")
