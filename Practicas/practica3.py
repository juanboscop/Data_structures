def lista():
    gadgetsstr = ["bateria","portatil","ordenador central","altavoces","pantalla","maletin electrico","lente de camara"]
    gadgetsnum = [100,310.28,27.00,1000]
    gadgetsstr.sort()
    print(f"En orden ascendente = {gadgetsstr}")
    gadgetsstr.reverse()
    print(f"En orden descendente = {gadgetsstr}")
    gadgetsnum.sort()
    print(f"Numeros de pequeño a mayor  = {gadgetsnum}")
    gadgetsnum.reverse()
    print(f"Numeros de mayor a pequeño  = {gadgetsnum}")
lista()