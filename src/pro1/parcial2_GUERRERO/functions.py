def is_mutant(dna):
    # recibe las otras funciones para no tener que llamar a todas en el main
    is_mutant = False
    # count_times se va a ir sumando si se cumplen is_row, is_col y is_diag (diagonal y diagonal inversa)
    count_times = 0
    # Meter los strings de dna en una matriz para mejor comparacion
    compare_dna = [[dna[i][j] for j in range(6)] for i in range(6)]
    print("--------- MATRIZ DNA ---------")
    for row in compare_dna:
        print(" ".join(row))

    # Verificar filas
    is_row = check_row(compare_dna)
    if is_row >= 1:
        if is_row >= 2:
            print("MUTANTE POR FILAS")
        count_times += is_row

    # Verificar columnas
    is_col = check_col(compare_dna)
    if is_col >= 1:
        if is_col >= 2:
            print("MUTANTE POR COLUMNAS")
        count_times += is_col

    # Verificar diagonales
    is_diag = check_diag(compare_dna)
    if is_diag >= 1:
        if is_diag >= 2:
            print("MUTANTE POR DIAGONALES")
        count_times += is_diag

    # Determinar si es mutante segun cantidad de secuencias acertadas
    if count_times >= 2:
        is_mutant = True
    return is_mutant


# Checkear filas
def check_row(compare_dna):
    count_times = 0
    for i in range(6):
        count = 0
        j = 0
        while j < 5:
            count = count + 1 if compare_dna[i][j] == compare_dna[i][j + 1] else 0
            if count >= 3:
                count_times += 1
                break
            j += 1
    return count_times


# Checkear columnas
def check_col(compare_dna):
    count_times = 0
    for j in range(6):
        count = 0
        i = 0
        while i < 5:
            count = count + 1 if compare_dna[i][j] == compare_dna[i + 1][j] else 0
            if count >= 3:
                count_times += 1
                break
            i += 1
    return count_times


# Checkear diagonal y tambien diagonal inversa
def check_diag(compare_dna):
    count_times = -1
    for i in range(5):
        for j in range(5):
            count = 0
            actual_position = compare_dna[i][j]
            new_row = i + 1
            new_col = j + 1
            while (
                new_row < 6
                and new_col < 6
                and actual_position == compare_dna[new_row][new_col]
            ):
                if count >= 3:
                    count_times += 1
                    count = 0
                count += 1
                new_row += 1
                new_col += 1
    # Diagonal inversa
    for i in range(len(compare_dna) - 1):
        for j in range(len(compare_dna[0]) - 1):
            count = 0
            # declaro variables para empezar a contar desde [0][5]
            newRow = i + 1
            finalCol = (len(compare_dna[0]) - 1) - j
            actualPosition = compare_dna[i][finalCol]
            checkDiagonal = finalCol - 1
            while (
                newRow < len(compare_dna)
                and checkDiagonal > -1
                and actualPosition == compare_dna[newRow][checkDiagonal]
            ):
                count += 1
                if count >= 3:
                    count_times += 1
                    count = 0
                newRow += 1
                checkDiagonal -= 1
    return count_times
