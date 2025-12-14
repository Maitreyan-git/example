def unique_substring_length(filename):
    with open(filename, 'r') as file:
        sequence = file.readline().strip()

    c_set = set()
    max_len = 0
    s = 0

    for end in range(len(sequence)):
        while sequence[end] in c_set:
            c_set.remove(sequence[s])
            s += 1
        c_set.add(sequence[end])
        max_len = max(max_len, end - s + 1)

    with open('Max_unique_sequence.txt', 'w') as output_file:
        output_file.write(str(max_len))


unique_substring_length('Process_sequence.txt')
