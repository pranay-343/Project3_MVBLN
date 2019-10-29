from time import process_time

arr = []
def MVBLN(arr,i, k):
    #base case
    if (i<0 or k<0):
        return 0
    else:
        return max(max(MVBLN(arr,i-1,k), MVBLN(arr,i-1,k-1) + arr[i]),MVBLN(arr,i-2,k) + arr[i])

# Taking array input and atmost value of 1's from user
n = int(input("Enter number of elements in array : "))
k = int(input("Enter number of adjacent 1s : "))
for i in range(0, n):
    arr_ele = int(input("Enter array element : "))
    arr.append(arr_ele)

start_time = process_time()
ans = MVBLN(arr,n-1, k)
print(ans)
stop_time = process_time()
print("Elapsed time during the whole program in seconds:",stop_time-start_time)