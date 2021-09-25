def mergeSort(L, ascending = True):
    result = []  
    
    if len(L) <= 1:
        return L  
   
    #diviser la liste en deux  
    mid = len(L) // 2
    #liste gauche du début jusqu'au milieu 
    list1 = mergeSort(L[:mid])
#liste droite du milieu à la fin de la liste 
    list2 = mergeSort(L[mid:])

    #index, on commence à partir de 0 : 
    x, y = 0, 0
    while x < len(list1) and y < len(list2):
        if list1[x] > list2[y]: # < for descending
            result.append(list2[y])
            y = y + 1

        else:
            result.append(list1[x])
            x = x + 1

    result = result + list1[x:]

    result = result + list2[y:]
    if ascending == True :
        return result
    else:
        result.reverse()
        return result

list=[3,2,4,1,5,9,7, 4.5, 6, 5+4]
print(list)
print(mergeSort(list, True) )# sort in ascending order
