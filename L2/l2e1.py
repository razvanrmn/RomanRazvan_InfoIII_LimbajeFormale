from itertools import product

E = ['0', '1', '2']

def isPalindrome(s):
    return s == s[::-1]

for length in range(1, 6):
    for comb in product(E, repeat=length):
        if isPalindrome(comb):
            print(f"{length} characters: {''.join(comb)}")
