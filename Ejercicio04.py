while True:
    ingreso_mensual = float(input("Ingrese el ingreso mensual (0 para salir): "))
    if ingreso_mensual == 0:
        print("Saliendo...")
        break
    ingreso_anual = ingreso_mensual * 14
    imp_tramo1 = 0
    imp_tramo2 = 0
    imp_tramo3 = 0
    imp_tramo4 = 0
    if ingreso_anual > 20000:
        monto = 20000 - 0
        imp_tramo1 = monto * 0
    else:
        monto = ingreso_anual - 0
        imp_tramo1 = monto * 0
    if ingreso_anual > 20000:
        limite_superior = min(ingreso_anual, 50000)
        monto = limite_superior - 20000
        imp_tramo2 = monto * 0.10
    if ingreso_anual > 50000:
        limite_superior = min(ingreso_anual, 100000)
        monto = limite_superior - 50000
        imp_tramo3 = monto * 0.20
    if ingreso_anual > 100000:
        monto = ingreso_anual - 100000
        imp_tramo4 = monto * 0.30
    total_impuestos = imp_tramo1 + imp_tramo2 + imp_tramo3 + imp_tramo4
    tasa_efectiva = (total_impuestos / ingreso_anual) * 100
    print("\n--- Impuestos por tramo ---")
    print(f"Tramo [0 - 20000]: {imp_tramo1}")
    print(f"Tramo (20000 - 50000]: {imp_tramo2}")
    print(f"Tramo (50000 - 100000]: {imp_tramo3}")
    print(f"Tramo (>100000]: {imp_tramo4}")

    print("\nTotal impuestos:", total_impuestos)
    print("Tasa efectiva real:", tasa_efectiva)
