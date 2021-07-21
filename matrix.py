import numpy as np
import random

def create_field(x = 5, y = 5):
    return np.zeros((y,x), dtype= int)

def rand_array(a, num = 6):
    i = j = n = 0
    x = a.shape[0]
    y = a.shape[1]
    row = random.sample(range(1, x*y), num)
    for i in range (x):
        for j in range(y):
            n += 1 
            if n in row:
                a[i,j] = 9

def modify (a):
    x = a.shape[0]
    y = a.shape[1]
    #insert row  
    row = np.zeros(y,dtype= int)
    a = np.insert(a,x,[row],axis = 0)
    a = np.insert(a,0,[row],axis = 0)
    # rotate
    a = np.rot90(a,1)
    #insert row
    x = a.shape[0]
    y = a.shape[1]
    row = np.zeros(y,dtype= int)
    a = np.insert(a,x,[row],axis = 0)
    a = np.insert(a,0,[row],axis = 0)
    a = np.rot90(a,3)
    x = a.shape[0]
    y = a.shape[1]
    i = j = 1
    n = 0
    for i in range (x-1):
        for j in range(y-1):
            if a[i,j] == 0:
                #find_neibor
                n = 0
                if a[i-1, j-1] == 9: n += 1
                if a[i-1, j  ] == 9: n += 1
                if a[i-1, j+1] == 9: n += 1
                if a[i,   j-1] == 9: n += 1
                if a[i,   j+1] == 9: n += 1
                if a[i+1, j-1] == 9: n += 1
                if a[i+1, j]   == 9: n += 1
                if a[i+1, j+1] == 9: n += 1
                a[i,j] = n

    #remove row
    a = np.delete(a, (x-1), axis = 0)
    a = np.delete(a, (y-1), axis = 1)
    a = np.delete(a, (0), axis = 0)
    a = np.delete(a, (0), axis = 1)

    return a

def main():
    my_arr = create_field(12,8)
    rand_array(my_arr, 10)
    my_arr = modify(my_arr)
    print (my_arr)



if __name__ == '__main__':
    main ()
