class PushdownAutomaton:
    def __init__(self):
        self.stack = []
        self.transitions = {
            ('q0', '0', ''): ('q0', '0'),
            ('q0', '0', '0'): ('q0', '0'),   
            ('q0', '1', '0'): ('q1', ''),   
            ('q1', '1', '0'): ('q1', ''),   
            ('q1', '', ''): ('q_accept', '') 
        }
        self.initial_state = 'q0'
        self.accept_state = 'q_accept'

    def process_input(self, input_string):
        current_state = self.initial_state
        
        for symbol in input_string:
            if (current_state, symbol, self.stack[-1] if self.stack else '') in self.transitions:
                current_state, stack_top = self.transitions[(current_state, symbol, self.stack[-1] if self.stack else '')]
                if stack_top:
                    self.stack.append(stack_top)
                else:
                    if self.stack:
                        self.stack.pop()
            else:
                return False
        
        return current_state == self.accept_state and not self.stack


def test_pda(input_string):
    pda = PushdownAutomaton()
    result = pda.process_input(input_string)
    if result:
        print(f'String "{input_string}" is accepted by the PDA.')
    else:
        print(f'String "{input_string}" is rejected by the PDA.')

test_pda("0011")
test_pda("0101") 
test_pda("000111")
test_pda("010101") 
