def BS(a_list, item):
    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return '{item} was not found in the list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return '{item} found'.format(item=item)
        else:
            if a_list[i] < item:
                return BS(a_list[i+1:], item)
            else:
                return BS(a_list[:i], item)
    

def SqSum(L):
    if(len(L) == 1):
        return L[0] * L[0]
    else:
        x = 0
        return L[0] **2 + SqSum(L[1:])


print(BS([1,3,5,7,9,11,13],11))
        
