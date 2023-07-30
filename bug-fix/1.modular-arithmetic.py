def help_bobby(size):  
    array=[[[0]*size]*size] #2 array = 
    # print('arr---',array)
    for i in array:print(i)
    row=0
    # len(i)
    for column in range(size):
        # print(column, row, size)
        # print(array[column][row])
        print(array)
        print(column)
        # array[column][row]=1
        # array[column][row]=0
        # row+=1
    for i in array:print(i)
    # print(array)
    return array


help_bobby(3)