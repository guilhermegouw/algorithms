def bubble_sort(lista: list) -> list:
    unsorted_until = len(lista) -1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
                sorted = False
        unsorted_until -= 1
    return lista