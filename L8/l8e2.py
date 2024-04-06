class IBANValidator:
    def __init__(self):
        self.valid_country_codes = [
            "AL", "AD", "AT", "AZ", "BH", "BY", "BE", "BA", "BR", "BG",
            "CR", "HR", "CY", "CZ", "DK", "DO", "TL", "EE", "FO", "FI",
            "FR", "GE", "DE", "GI", "GR", "GL", "GT", "HU", "IS", "IQ",
            "IE", "IL", "IT", "JO", "KZ", "XK", "KW", "LV", "LB", "LI",
            "LT", "LU", "MK", "MT", "MR", "MU", "MD", "MC", "ME", "NL",
            "NO", "PK", "PS", "PL", "PT", "QA", "RO", "SM", "SA", "RS",
            "SK", "SI", "ES", "SE", "CH", "TN", "TR", "UA", "AE", "GB",
            "VG"
        ]
        self.iban_length = {
            "AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BH": 22, "BY": 28,
            "BE": 16, "BA": 20, "BR": 29, "BG": 22, "CR": 21, "HR": 21,
            "CY": 28, "CZ": 24, "DK": 18, "DO": 28, "TL": 23, "EE": 20,
            "FO": 18, "FI": 18, "FR": 27, "GE": 22, "DE": 22, "GI": 23,
            "GR": 27, "GL": 18, "GT": 28, "HU": 28, "IS": 26, "IQ": 23,
            "IE": 22, "IL": 23, "IT": 27, "JO": 30, "KZ": 20, "XK": 20,
            "KW": 30, "LV": 21, "LB": 28, "LI": 21, "LT": 20, "LU": 20,
            "MK": 19, "MT": 31, "MR": 27, "MU": 30, "MD": 24, "MC": 27,
            "ME": 22, "NL": 18, "NO": 15, "PK": 24, "PS": 29, "PL": 28,
            "PT": 25, "QA": 29, "RO": 24, "SM": 27, "SA": 24, "RS": 22,
            "SK": 24, "SI": 19, "ES": 24, "SE": 24, "CH": 21, "TN": 24,
            "TR": 26, "UA": 29, "AE": 23, "GB": 22, "VG": 24
        }
        self.pda_transitions = {
            ('q0', 'A', ''): ('q1', 'A'),
            ('q1', 'A', 'A'): ('q1', 'A'),  
            ('q1', 'B', 'A'): ('q2', 'B'), 
            ('q2', 'B', 'B'): ('q2', 'B'), 
            ('q2', 'C', 'B'): ('q3', 'C'),  
            ('q3', 'C', ''): ('q4', ''),   
            ('q4', '', ''): ('q_accept', '')
        }
        self.initial_state = 'q0'
        self.accept_state = 'q_accept'

    def is_valid_iban(self, iban):
        iban = iban.replace(' ', '')
        country_code = iban[:2]
        
        if country_code not in self.valid_country_codes:
            return False
        
        if len(iban) != self.iban_length[country_code]:
            return False
        
        current_state = self.initial_state
        stack = []
        
        for char in iban:
            if (current_state, char, stack[-1] if stack else '') in self.pda_transitions:
                current_state, stack_top = self.pda_transitions[(current_state, char, stack[-1] if stack else '')]
                if stack_top:
                    stack.append(stack_top)
                else:
                    if stack:
                        stack.pop()
            else:
                return False
        
        return current_state == self.accept_state and not stack

def test_iban_validator(iban):
    validator = IBANValidator()
    result = validator.is_valid_iban(iban)
    if result:
        print(f'The IBAN code "{iban}" is valid.')
    else:
        print(f'The IBAN code "{iban}" is not valid.')

test_iban_validator("RO49 YYYY 1B31 0075 9384 0000")
test_iban_validator("GB29 NWBK 6016 1331 9268 19")
