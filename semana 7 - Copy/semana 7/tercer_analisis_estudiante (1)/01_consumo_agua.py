"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
"""Caso 1: cambio del consumo diario de agua."""

consumo_litros = [120, 115, 108, 102, 96]

# Calcular el consumo total y el promedio diario.
total = sum(consumo_litros)
promedio = total / len(consumo_litros)

# Comparar el primer día con el último.
primer_dia = consumo_litros[0]
ultimo_dia = consumo_litros[-1]
ahorro = primer_dia - ultimo_dia

# Calcular el porcentaje de reducción.
reduccion = (ahorro / primer_dia) * 100

# Clasificar la reducción.
if reduccion > 15:
    clasificacion = "reducción alta"
elif reduccion > 0:
    clasificacion = "reducción moderada"
else:
    clasificacion = "sin reducción"

# Mostrar los resultados.
print("CONSUMO DIARIO DE AGUA")
print("----------------------")
print(f"Consumo total: {total} L")
print(f"Promedio diario: {promedio:.1f} L")
print(f"Ahorro entre el primer y último día: {ahorro} L")
print(f"Reducción: {reduccion:.1f}%")
print(f"Clasificación: {clasificacion}")

print("\nLos cinco consumos registrados son:")
for dia, litros in enumerate(consumo_litros, start=1):
    print(f"Día {dia}: {litros} L")