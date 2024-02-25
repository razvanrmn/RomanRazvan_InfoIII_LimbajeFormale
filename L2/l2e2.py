V = ['S', 'A', 'B']
T = ['a', 'b']

def generate_strings(S, iterations):
    if iterations == 0:
        return ['']

    strings = []
    for symbol in S:
        if symbol == 'S':
            strings.extend([terminal + x + terminal for x in generate_strings(S, iterations - 1) for terminal in T])
            strings.extend(T)
        elif symbol == 'A':
            strings.extend([terminal + x + terminal for x in generate_strings(S, iterations - 1) for terminal in T])
            strings.extend(['a' * iterations, 'b' * iterations])
        elif symbol == 'B':
            strings.extend(['a' * iterations, 'b' * iterations])

    return strings

iterations = 3
generated_strings = generate_strings(['S'], iterations)
print("Generated strings:")
print(generated_strings)
