import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--A',
                        type=str,
                        required=True,
                        help='Sequence A')
    parser.add_argument('--B',
                        type=str,
                        required=True,
                        help='Sequence B')
    parser.add_argument('--gap',
                        type=int,
                        default=-2,
                        help='Gap penalty (default: -2)')
    parser.add_argument('--miss',
                        type=int,
                        default=-1,
                        help='Mismatch penalty (default: -1)')
    parser.add_argument('--match',
                        type=int,
                        default=1,
                        help='Match score (default: 1)')
    return parser.parse_args()


def sw_fill_matrix(A, B, gap, miss, match):
    H = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            H[i][j] = max( H[i-1][j-1] + (match if A[i-1] == B[j-1] else miss),
                           H[i-1][j] + gap,
                           H[i][j-1] + gap,
                           0)
    return H

def sw_traceback(H, A, B, gap, miss, match):
    i = None
    j = None
    max_score = 0
    for _i in range(len(A) + 1):
        for _j in range(len(B) + 1):
            if H[_i][_j] > max_score:
                max_score = H[_i][_j]
                i = _i
                j = _j

    score = H[i][j]
    align_A = []
    align_B = []
    while H[i][j] > 0:
        if H[i][j] == H[i-1][j-1] + (match if A[i-1] == B[j-1] else miss):
            align_A.append(A[i-1])
            align_B.append(B[j-1])
            i -= 1
            j -= 1
        elif H[i][j] == H[i-1][j] + gap:
            align_A.append(A[i-1])
            align_B.append('-')
            i -= 1
        elif H[i][j] == H[i][j-1] + gap:
            align_A.append('-')
            align_B.append(B[j-1])
            j -= 1
        else:
            break
    return ''.join(align_A[::-1]), ''.join(align_B[::-1]), score

def sw(A, B, gap, miss, match):
    H = sw_fill_matrix(A, B, gap, miss, match)
    A, B, score = sw_traceback(H, A, B, gap, miss, match)
    match = ['|' if A[i] == B[i] else ' ' for i in range(len(A))]
    return score, A, B, ''.join(match)

def main():
    args = get_args()

    score, align_A, align_B, match = sw(args.A,
                                        args.B,
                                        args.gap,
                                        args.miss,
                                        args.match)
    print(score)
    print(align_A)
    print(match)
    print(align_B)


if __name__ == '__main__':
    main()
