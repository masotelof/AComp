def riemann(li, ls, elementos=1000):
    base = (ls-li)/elementos
    inc = li
    suma = 0
    while inc<ls:
        suma += base * (inc)**2 
        inc += base
    return suma

if __name__ == "__main__":
    print(riemann(1, 10, 10))