A = ['a','b','c']
B = ['x', 'y', 'z']
C = [1,2,3]

def concatenate(s1, s2):
    return s1 + s2

def inverse(s):
    return s[::-1]

def substitution(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

def main():
    
    print('Concatenation: ',concatenate(A[0],B[2]))
    print('Inverse: ', inverse(A[0] + B[0] + str(C[0])))
    print('Substitution: ',substitution('abracadabra', 'a', 'z'))
    print('Lenght: ', 'aaaaaaaaaa')


if __name__ == "__main__":
    main()

