def dual_hamming_simplex_check(r):
    n = (1 << r) - 1
    H = [0] * r
    for col in range(1, n + 1):         
        mask = 1 << (col - 1)             
        for row in range(r):
            if (col >> row) & 1:         
                H[row] |= mask          

    print(f"r = {r}, n = {n}")
    print("Порождающая матрица H (строки в двоичном виде):")
    for row in H:
        print(f"{row:0{n}b}")            

    words = []          
    weights = []        
    for coeff in range(1, 1 << r):
        word = 0
        for row in range(r):
            if (coeff >> row) & 1:
                word ^= H[row]          
        words.append(word)
        weight = word.bit_count()
        weights.append(weight)

    print("\nНенулевые слова и их веса:")
    for i, (w, wt) in enumerate(zip(words, weights)):
        print(f"слово {i+1:2}: {w:0{n}b}  вес = {wt}")

    if all(w == weights[0] for w in weights):
        print(f"\nненулевые слова имеют одинаковый вес = {weights[0]}")
        expected = 1 << (r - 1)       
        if weights[0] == expected:
            print(f"вес совпадает с ожидаемым для симплексного кода: 2^{r-1} = {expected}")
        else:
            print(f"ожидаемый вес для симплексного кода: {expected}")
    else:
        print("\nвеса различаются. Дуальный код не является симплексным")


if __name__ == "__main__":
    for r in range(2, 6):
        dual_hamming_simplex_check(r)
