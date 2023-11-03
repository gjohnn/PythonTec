# | GUERRERO, JUAN | PROGAMACION I | COMISION A |
# LOS IF Y ALGUNOS FOR LOS PASÉ A TERNARIOS UNA VEZ QUE FUNCIONARON PARA OPTIMIZAR CÓDIGO

from functions import is_mutant

exit_app = "s"
while exit_app != "n":
    option = 0
    while option < 1 or option > 5:
        # Menú
        print(" ------------ MENU ---------------- ")
        print("1) NUEVO MUTANTE")
        print("2) DEMO DE FILA ")
        print("3) DEMO DE COLUMNA ")
        print("4) DEMO DE DIAGONAL ")
        print("5) DEMO DE NO MUTANTE ")
        option = int(input("Ingrese opción: "))
        print(" ---------------------------------- ")
    # if para hacer lo que desea el usuario
    if option == 1:
        # CREAR PROPIO MUTANTE
        dna = []
        for i in range(6):
            wordADN = ""
            letter_position = 1
            while len(wordADN) < 6:
                letterADN = input(
                    f"Ingrese letra {letter_position} ADN {i+1} (A, T, C, G): "
                ).upper()
                if letterADN in ["A", "T", "C", "G"]:
                    wordADN += letterADN
                    letter_position += 1
                else:
                    print("Por favor, ingrese una letra válida (A, T, C, G).")
            dna.append(wordADN)
            print(dna)

        is_mutants = "Es mutante." if is_mutant(dna) else "No es mutante."
        print(is_mutants)
    elif option == 2:
        # Filas de T
        dna_row = [
            "ATTCGA",
            "CCTTTT",
            "ACTTTT",
            "AGAACG",
            "TCCTAA",
            "TCACTG",
        ]
        is_mutants = "Es mutante." if is_mutant(dna_row) else "No es mutante."
        print(is_mutants)
    elif option == 3:
        dna_col = [
            # Columnas de A y T
            "ATATGA",
            "AAATTC",
            "TTATTT",
            "AGATGG",
            "CCGCTA",
            "TCTCTG",
        ]
        is_mutants = "Es mutante." if is_mutant(dna_col) else "No es mutante."
        print(is_mutants)
    elif option == 4:
        dna_diag = [
            # diagonal de A y de T
            "TAGAGA",
            "CTATGC",
            "TATCAT",
            "AGATGG",
            "CCCXTG",
            "TCACTT",
        ]
        is_mutants = "Es mutante." if is_mutant(dna_diag) else "No es mutante."
        print(is_mutants)
    elif option == 5:
        dna_not = ["ATGCGA", "CAGTGC", "TTGTGT", "AGAAGG", "CGACTA", "TCACTG"]
        is_mutants = "Es mutante." if is_mutant(dna_not) else "No es mutante."
        print(is_mutants)
    exit_app = input("Desea continuar? (s/n): ")
