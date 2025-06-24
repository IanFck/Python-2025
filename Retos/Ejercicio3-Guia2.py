#Guia N°2
#Ejercicio 3 - Pia Rojas y Ian Fack

Vendedores = {
    "Juan": [500000, 400000, 300000, 200000, 200000],
    "Alvaro": [300000, 250000, 200000, 150000, 150000],
    "Pedro": [200000, 100000, 80000, 70000, 60000],
}

sueldo_base = 529000

print("REPORTE DE VENTAS Y SUELDOS\n")

for nombre, ventas in Vendedores.items():
    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / 5

    if total_ventas > 1500000:
        bono = sueldo_base * 0.20
    elif total_ventas > 1000000:
        bono = sueldo_base * 0.10
    elif total_ventas > 500000:
        bono = sueldo_base * 0.05
    else:
        bono = 0

    sueldo_total = sueldo_base + bono

    print(f"Vendedor: {nombre}")
    print(f"Ventas totales: {total_ventas:,.0f}")
    print(f"Promedio ventas diarias: {promedio_ventas:,.0f}")
    print(f"Bono: {bono:,.0f}")
    print(f"Sueldo total a pagar : {sueldo_total:,.0f}\n")



