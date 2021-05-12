
def hanoi(n, from_pos, to_pos, aux_pos) :
    if n == 1 :
        print(from_pos, "->", to_pos)

        return

    # 원반 n-1 개를 aux_pos 로 이동 
    hanoi(n - 1, from_pos, aux_pos, to_pos)

    print(from_pos, "->", to_pos)

    # 원반 n-1 개를 to_pos 로 이동
    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(3, 1, 3, 2)