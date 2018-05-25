def swap(array,first,last):
    temp = array[first]
    array[first] = array[last]
    array[last] = temp;
def reverseList(L):
    first = 0
    last = len(L) -1
    while(first < last):
        swap(L,first,last)
        first = first + 1
        last = last -1
    return L

print(reverseList([1,2,3,4,5,6,7]))
