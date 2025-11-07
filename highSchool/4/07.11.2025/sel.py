
def get_min_idx(tab: list, start: int = 0) -> int:
    min_idx = start

    for i in range(start, len(tab)):
        n = tab[i]

        if n < tab[min_idx]:
            min_idx = i 

    return min_idx

def sort(tab: list) -> list:
    for i in range(len(tab)):
        min_idx = get_min_idx(tab, i)
        
        tab[i], tab[min_idx] = tab[min_idx], tab[i]

    return tab
