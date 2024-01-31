
def ns(P, T):
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

if __name__ == '__main__':
    #    012345678901234567890
    T = 'ACCTGTACCGTCAGGTAACCG'
    P = 'ACCG'
    # 6 and 17
    r = ns(P,T)
    print(r)
