def bubble_sort(list: list) -> list:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i + 1], list[i] = list[i], list[i + 1]
    return list