class MealyMachine:
    def __init__(self):
        self.transitions = {
            ('Q1', 'X'): ('Q2', 'O1'),
            ('Q1', 'Y'): ('Q1', 'O1'),
            ('Q2', 'X'): ('Q1', 'O2'),
            ('Q2', 'Y'): ('Q2', 'O2')
        }
        self.current_state = 'Q1'

    def transition(self, input_symbol):
        if (self.current_state, input_symbol) in self.transitions:
            next_state, output = self.transitions[(self.current_state, input_symbol)]
            self.current_state = next_state
            return output
        else:
            return None

mealy_machine = MealyMachine()
inputs = ['X', 'Y', 'X', 'Y', 'X', 'Y']
for inp in inputs:
    output = mealy_machine.transition(inp)
    if output:
        print(f"Input: {inp}, Output: {output}")
    else:
        print(f"Invalid input: {inp}")
