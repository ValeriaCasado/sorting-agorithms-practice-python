"""
Choose a low index and high index (0, N)

Sort everything between low and high according to pivot N
blah blah blah
"""

def quick_sort(l: list[int]):

    def _solve_partition(l, low, high):

        pivot = l[high]
        i = low

        
        for j in range(low, high):
            
            if l[j] < pivot:
                l[i], l[j] = l[j], l[i]
                i += 1
        
        l[i], l[high] = l[high], l[i]
        return i
        
    
    def _find_partitions(l, low, high):

        if low < high:
            p =  _solve_partition(l, low, high)

            _find_partitions(l, low, p-1)
            _find_partitions(l, p + 1, high)

    _find_partitions(l, 0, len(l) - 1)
