for a in range(200, 300):
    a_del = [b for b in range(1, a) if a % b == 0]
    c = sum(a_del)
    c_del = [b for b in range(1, c) if c % b == 0]
    if a == sum(c_del) and c == sum(a_del):
        print(f'{a} and {c} is friend!')
