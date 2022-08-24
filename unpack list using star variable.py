def drop_first_last(list1):
    
    first,*middle,last=list1 #*(variable name) store all elements of list except first and last elements 
    print ('first->',first)
    for i in middle:
        print('middle-> ',i)
    print('last->',last)
list2=[1,2,8,78,565,454,35,65,43,22]
drop_first_last(list2)

