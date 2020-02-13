def riemann(li, ls, elementos=1000):
    base = (ls-li)/elementos
    suma = 0

    for i in range (elementos):
        suma += base * (li + (i * base))**2

    return suma

if __name__ == "__main__":
    print(riemann(1, 10, 10))