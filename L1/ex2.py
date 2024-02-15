A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k']
C = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']

def concatenate(s1, s2):
    return s2 + s1

def repeat(s, n):
    return s * n

def reverse(s):
    return s[::-1]

def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)

def main():

    print("Concat:", concatenate(str(A[0]), C[2]))
    print("Repeat:", repeat(B[4], 3))
    print("Reverse:", reverse(C[6]))
    print("Extract:", extract(C[8], 1, 3))
    print("Replace:", replace(C[5], 'y', 'z'))

if __name__ == "__main__":
    main()
