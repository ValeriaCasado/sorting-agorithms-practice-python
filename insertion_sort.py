"""
"In place" sorting algorithm. It doesn't requrie any additional memory space.

Passes, comparing to the element before it until all is complete.
"""

def insertion_sort(l: list[int]):

    def _insertion_sort(start_index, l):
        swaps = 0

        if start_index >= len(l)-1:
            return l
        
        for i in range(len(l)-2, start_index-1, -1):
            e1 = l[i]
            e2 = l[i+1]
            if e2 < e1:
                l[i] = e2
                l[i+1] = e1
                swaps += 1
        if swaps == 0:
            return l
        else:
            return _insertion_sort(start_index+1, l)

    return _insertion_sort(0, l)
        

