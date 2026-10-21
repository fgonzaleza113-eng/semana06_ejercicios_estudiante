
#capacidad = 700
grupos_aceptados = []
grupos_rechazados = []
ocupacion = 0

entrada = input("Ingrese la cantidad de personas del grupo o 'fin' para terminar: ")

while entrada.lower() != "fin":
    try:
        grupo = int(entrada)

        if grupo <= 0:
            print("Entrada inválida: ingrese un número entero mayor que cero.")

        else:
            if ocupacion + grupo <= capacidad:
                grupos_aceptados.append(grupo)
                ocupacion = ocupacion + grupo
                print(f"Grupo aceptado: ingresan {grupo} personas.")
            else:
                grupos_rechazados.append(grupo)
                print(f"Grupo rechazado: no hay espacio para {grupo} personas.")

            print(f"Ocupación actual: {ocupacion}")
            print(f"Espacios disponibles: {capacidad - ocupacion}")

    except ValueError:
        print("Entrada inválida: ingrese un número entero o la palabra 'fin'.")

    entrada = input("Ingrese la cantidad de personas del grupo o 'fin' para terminar: ")

total_admitido = 0

for grupo in grupos_aceptados:
    total_admitido = total_admitido + grupo

print("\nREPORTE FINAL")
print("Grupos aceptados:", len(grupos_aceptados))
print("Grupos rechazados:", len(grupos_rechazados))
print("Personas admitidas:", total_admitido)
print("Capacidad máxima:", capacidad)
print("Espacios disponibles:", capacidad - total_admitido)

if total_admitido > 0:
    porcentaje = (total_admitido / capacidad) * 100
    print(f"Porcentaje de ocupación: {porcentaje:.2f}%")

    grupo_menor = min(grupos_aceptados)
    grupo_mayor = max(grupos_aceptados)

    print("Grupo aceptado más pequeño:", grupo_menor)
    print("Grupo aceptado más grande:", grupo_mayor)
else:
    print("Porcentaje de ocupación: 0.00%")
    print("No hubo grupos aceptados.")

if total_admitido == capacidad:
    print("Estado final: capacidad completa.")
elif total_admitido == 0:
    print("Estado final: sin ocupación.")
else:
    print("Estado final: capacidad disponible.") Desarrolle su solución a partir de esta línea.
