list = [9,8,7,6,5,4,3,2,1]

def selectionsort(list):
    n = len(list)
    for i in range(0,n):
        mini_ind = i
        for j in range(i+1,n):
            if list[j]>=list[mini_ind]:
                mini_ind = j
        list[i],list[mini_ind]=list[mini_ind],list[i]

    return list

print(selectionsort(list))

