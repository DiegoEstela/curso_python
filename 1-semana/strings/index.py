cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_al_reves = cadena[::-1]
print(cadena_al_reves)

nombre_alumno = cadena_al_reves[0: 12]
print(nombre_alumno)

nota = cadena_al_reves.split(',')[1].strip()
print(nota)

materia = cadena_al_reves.split(',')[2].strip()
print(materia)

cadena_formateada = f"{nombre_alumno} se saco un: {nota} en: {materia}"

print(cadena_formateada)
