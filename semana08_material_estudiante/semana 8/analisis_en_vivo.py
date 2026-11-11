"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

# Comencemos aquí con la muestra y después construyamos nuestro contador.
print("\nMUESTRA DE DATOS")

for indice in range(3):
    registro = registros[indice]
    print(
        registro["codigo"], "-",
        registro["paciente_cedula"], "-",
        registro["paciente_nombre"], "-",
        registro["diagnostico"], "-",
        registro["medicamentos"]
    )
    # FASE 1: CONTAR MEDICAMENTOS

conteo_medicamento = {}
conteo_recetas = 0

for registro in registros:
    for medicamento in registro["medicamentos"]:
        if medicamento in conteo_medicamento:
            conteo_medicamento[medicamento] += 1
        else:
            conteo_medicamento[medicamento] = 1

    conteo_recetas += 1

print("\nCONTEO DE MEDICAMENTOS")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamento)
# CONTEO DE PACIENTES POR HOSPITAL

conteo_hospital = {}

for registro in registros:
    hospital = registro["hospital"]

    if hospital in conteo_hospital:
        conteo_hospital[hospital] += 1
    else:
        conteo_hospital[hospital] = 1

print("\nPACIENTES POR HOSPITAL")

for hospital, cantidad in conteo_hospital.items():
    print(hospital, ":", cantidad)
    print("Total de registros:", len(registros))
    