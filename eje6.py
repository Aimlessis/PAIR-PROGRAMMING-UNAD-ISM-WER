asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 70:
        repetir.append(asignatura)

print("Tienes que repetir:", repetir)
