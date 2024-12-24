arr = [1,2,3,4,5,6,7,8]

# ----------------- 0 (1) 

# access 
arr[0]

# rm from the last pos
popped = arr.pop()


# append on last

arr.append(10)

# ----------------- 0 (n)

# rm from the any pos except last due to rearrange
index_popped = arr.pop(1)

# insert el any pos except last
arr.insert(0,1)

# extend method is linear
#slice also ...
arr[1:2]