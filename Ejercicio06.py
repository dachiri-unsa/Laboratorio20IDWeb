def normalizar(lista,modo):
    nuevaLista = []
    if (len(lista) == 0):
        print("La lista no puede estar vacia.")
        return
    match modo:
        case "minmax":
            minimo = min(lista)
            maximo = max(lista)
            if (minimo == maximo):
                print("No se puede realizar minmax ya que toda la lista es igual.")
                return
            for num in lista:
                nuevaLista.append((num - minimo)/(maximo-minimo))
        case "zscode":
            media = sum(lista)/len(lista)
            sumatoria = 0
            for num in lista:
                sumatoria += (num-media)**2
            desviacion = (sumatoria/len(lista))**(1/2)
            if (desviacion == 0):
                print("No se puede calcular zscode ya que la desviacion es 0.")
                return
            for num in lista:
                nuevaLista.append((num-media)/desviacion)
        case "unit":
            sumaCuadrados = 0
            for num in lista:
                sumaCuadrados += num**2
            norma_vector = sumaCuadrados**(1/2)
            if (norma_vector == 0):
                print("No se puede realizar unit ya que la norma da 0.")
                return
            for num in lista:
                nuevaLista.append(num/norma_vector)
            return nuevaLista
        case _ :
            print("Modo ingresado no valido.")
            return
    return nuevaLista
while True:
    modoSeleccionado = input("Ingrese un modo (minmax, zscode, unit, salir) : ")
    if (modoSeleccionado.lower() == "salir"):
        print("Gracias por usar este programa.")
        break
    lista = [10,20,30]
    print(normalizar(lista,modoSeleccionado))
