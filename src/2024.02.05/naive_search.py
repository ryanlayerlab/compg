def naive_search(T, P):
    occurrences = []
    o = []
    len_P = len(P)
    len_T = len(T)

    P_i = 0
    T_i = 0

    for T_i in range(len_T - len_P + 1):
        match = True
        for P_i in range(len_P):
            if P[P_i] != T[T_i + P_i]:
                match = False
                break
        if match:
            o.append(T_i)

    return o

def naive_search_backward(T, P):
    occurrences = []
    len_P = len(P)
    len_T = len(T)

    P_i = len(P) - 1
    T_i = len(P) - 1

    while T_i < len_T:
        t = 0
        while P_i >= 0:
            if P[P_i] != T[T_i]:
                break
            P_i -= 1
            T_i -= 1
            t += 1
        if P_i < 0:
            occurrences.append(T_i + 1)
        T_i += t + 1
        P_i = len_P - 1

    return occurrences

def get_bct(P):
    return None

def naive_search_bct(T, P):
    return None

def get_shift_match_table(P):
    m = len(P)
    shift_match_table = {}

    for shift in range(m - 1, 0, -1):
        p_1 = m - 1
        p_2 = m - shift - 1

        while p_2 >= 0:
            if P[p_2] == P[p_1]:
                p_1 -= 1
                p_2 -= 1
                if p_2 < 0:
                    shift_match_table[shift] = m - shift
                    break
            else:
                shift_match_table[shift] = m - shift - p_2 - 1
                break
    shift_match_table[m] = 0
    return shift_match_table

def get_gst(P):
    m = len(P)

    good_suffix_table = {}
    good_suffix_table[0] = 1

    shift_match_table = get_shift_match_table(P)

    for i in range(1, m + 1):
        good_suffix_table[i] = i + m

    for i in range(m, 0, -1):
        if shift_match_table[i] > 0:
            good_suffix_table[shift_match_table[i]] = i + shift_match_table[i]

    for i in range(m, 0, -1):
        if shift_match_table[i] + i == m:
            for j in range(shift_match_table[i] + 1, m+1):
                good_suffix_table[j] = min(good_suffix_table[j], j + i)
    return good_suffix_table

def naive_search_bct_gst(T, P):
    return None

def naive_search_gst(T, P):
    return None


