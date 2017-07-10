# encoding:utf-8


def bubble_sort(lst):
    length = len(lst)
    for i in range(0, length-1):
        for j in range(i+1,length):
            print  i, j
            if lst[i] > lst[j]:
#
                lst[i], lst[j] = lst[j], lst[i]
    return lst


l = [6,7,8,69,'a',44,5,6,7,3,1]



print bubble_sort(l)