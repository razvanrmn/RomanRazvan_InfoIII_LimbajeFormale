class MooreMachine:
    def __init__(self):
        self.transitions = {
            ('S1', 'A'): ('S1', 'O1'),
            ('S1', 'B'): ('S2', 'O2'),
            ('S2', 'A'): ('S1', 'O1'),
            ('S2', 'B'): ('S2', 'O2')
        }
        self.current_state = 'S1'

    def transition(self, input_symbol):
        if (self.current_state, input_symbol) in self.transitions:
            next_state, output = self.transitions[(self.current_state, input_symbol)]
            self.current_state = next_state
            return output
        else:
            return None

moore_machine = MooreMachine()
inputs = ['A', 'B', 'A', 'B', 'B', 'A']
for inp in inputs:
    output = moore_machine.transition(inp)
    if output:
        print(f"Input: {inp}, Output: {output}")
    else:
        print(f"Invalid input: {inp}")
