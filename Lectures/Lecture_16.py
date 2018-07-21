#selection sort
def selection_sort(L):
    """(list of numbers) -> None
    sort given list L
    """

    #after that, L[i] is in its correct pos.
    #the next iteration apply on list[i+1..end]
    
    for i in range(len(L)-1):
        #Find min in the list[i.. end]
        #If min not the first in sublist, do swap.
        current_min=L[i]
        index_min = i
        for j in range(i, len(L)):
            if L[j] < current_min:
                current_min = L[j]
                index_min = j
        if current_min != L[i]: 
            L[index_min] = L[i]
            L[i] = current_min
        
        
