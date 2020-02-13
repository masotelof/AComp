def seq(li, ls, elementos):
    dist = (ls-li)/elementos
    while li<ls:
        yield li
        li += dist

def riemann(li, ls, elementos=1000, funcion="x**2"):
    base = (ls-li)/elementos
    suma = 0

    for x in seq(li, ls, elementos):
        suma += base * eval(funcion)

    return suma

if __name__ == "__main__":
    print(riemann(-10, 10, funcion="x**3+x**2"))