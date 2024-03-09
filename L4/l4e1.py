def deterministic_automaton(input_sequence):
    current_state = 'A'

    for symbol in input_sequence:
        if current_state == 'A':
            if symbol == '0':
                current_state = 'B'
        elif current_state == 'B':
            if symbol == '1':
                current_state = 'B'
            elif symbol == '0':
                current_state = 'A'

    return current_state

input_sequences = ["010", "110", "1001"]

for sequence in input_sequences:
    final_state = deterministic_automaton(sequence)
    print(f"Final state for input sequence '{sequence}': {final_state}")
