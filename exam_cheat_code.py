# We split the 20 questions into 5 blocks of 4.
# For each block we have 4 representative patterns of length 4.
# You can experiment with different patterns to improve performance.

REPRESENTATIVES_PER_BLOCK = [
    # Block 0 representatives (questions 0-3)
    [
        [0, 0, 0, 0],  # index 0
        [0, 0, 0, 1],  # index 1
        [1, 1, 1, 0],  # index 2
        [1, 1, 1, 1],  # index 3
    ],
    # Block 1 representatives (questions 4-7)
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ],
    # Block 2 representatives (questions 8-11)
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ],
    # Block 3 representatives (questions 12-15)
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ],
    # Block 4 representatives (questions 16-19)
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ],
]



def encode(solutions: list[int]) -> list[int]:
    code = [0] * 10
    # Don't change anything above this line
    # ==========================

    # Block-based encoding (see explanation above)
    code = []

    for block_index in range(5):
        start = block_index * 4
        end = start + 4
        block = solutions[start:end]

        best_rep_index = 0
        best_matches = -1

        for rep_index in range(4):
            rep = REPRESENTATIVES_PER_BLOCK[block_index][rep_index]
            matches = 0
            for i in range(4):
                if block[i] == rep[i]:
                    matches += 1

            if matches > best_matches:
                best_matches = matches
                best_rep_index = rep_index

        first_bit = (best_rep_index // 2) % 2
        second_bit = best_rep_index % 2

        code.append(first_bit)
        code.append(second_bit)

    # ==========================
    # Don't change anything below this line
    return code



def decode(message: list[int]) -> list[int]:    
    solutions = [0] * 20
    # Don't change anything above this line
    # ==========================

    # Block-based decoding (see explanation above)
    for block_index in range(5):
        bit_pos = block_index * 2
        b0 = message[bit_pos]
        b1 = message[bit_pos + 1]

        rep_index = b0 * 2 + b1
        rep = REPRESENTATIVES_PER_BLOCK[block_index][rep_index]

        start = block_index * 4
        for i in range(4):
            solutions[start + i] = rep[i]

    # ==========================
    # Don't change anything below this line
    return solutions


