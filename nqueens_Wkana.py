def print_queens(queens):
    longitud = len(queens)
    for fila in queens:
        for columna in range(longitud):
            if columna == 0:
                if columna == fila:
                    print(f"|q|", end="")
                else:
                    print(f"| |", end="")
            else:
                if columna == fila:
                    print(f"q|", end="")
                else:
                    print(f" |", end="")
        print()
    print()
    print("--"*longitud, end="")
    print("-")
    print()

def is_valid(row, col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True

def place_queens(row, queens, n): # funcion recursiva para poner las reinas
    if row == n: # caso base
        #print(queens)
        print_queens(queens)
        return 1
    else:
        total_solucions = 0 # contador de soluciones
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                total_solucions += place_queens(row + 1, queens, n)
        return total_solucions


def n_queens(n): # funcion para llamar, general
    queens = [' ']*n # generar la estructura donde se ponen las reinas,
                     # el indice es la fila y el valor es la columna
    row = 0
    return place_queens(row, queens, n)

print(n_queens(5)) 