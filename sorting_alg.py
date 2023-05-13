import time

a = [4,1,6,5,65,1,7,9,9,35,33]


#one of the famous sorting algorithms is bubblesort algorithm in which adjacent items are compared.
def bubble_sort(array):
    #we need to go through the array as many times as the number of the items in the array
    for i in range(len(array)):
        #in each iteration, we look at adjacent elements 2 by 2 and swap if the first is larger than the latter. 
        for j in range(0, len(array) - i - 1):
            if array[j+1] < array[j]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)

start_t = time.time()
bubble_sort(a)
end_t = time.time()

run_t_bub = end_t - start_t
print(run_t_bub)  #it is 2.09808349609375e-05 seconds

a = [4,1,6,5,65,1,7,9,9,35,33]

def selection_sort(array):
    for i in range(len(array)):
        min_pos = i
        for j in range(i+1, len(array)):
            if array[min_pos] > array[j]:
                min_pos = j

    print(array)


start_t_2 = time.time()
selection_sort(a)
end_t_2 = time.time()    

run_t_sel = end_t_2 - start_t_2
print(run_t_sel)  #it is 7.867813110351562e-06 seconds
