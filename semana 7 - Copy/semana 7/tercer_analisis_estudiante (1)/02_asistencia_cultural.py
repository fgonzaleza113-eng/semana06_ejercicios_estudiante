"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# TODO: Calcule el promedio y su porcentaje de ocupación.
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
asistencias = [120, 100, 240, 240, 200]
capacidad = 300

total = 0
bloques_superan = 0

for asistencia in asistencias:
    total += asistencia

    if asistencia > capacidad * 0.70:
        bloques_superan += 1

promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100

if porcentaje > 80:
    clasificacion = "alta"
elif porcentaje >= 50:
    clasificacion = "media"
else:
    clasificacion = "baja"

print("ASISTENCIA CULTURAL")
print("-------------------")
print(f"Total: {total}")
print(f"Promedio: {promedio}")
print(f"Ocupación: {porcentaje:.1f}%")
print(f"Bloques que superan el 70%: {bloques_superan}")
print(f"Clasificación: {clasificacion}")