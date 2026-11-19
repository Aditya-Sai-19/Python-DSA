# Right rotation by 1 place


# normally when you assign the rotation to nums again it changes the meory address of nums
nums = [5,-2,3,9,0,6,10,7]
print(id(nums))
n = len(nums)-1
nums = nums[n:] + nums[:n]
print(nums)
print(id(nums))
# if you want to do a inplace change that is change the value of nums in the same memeory address use slicing operator
nums = [5,-2,3,9,0,6,10,7]
print(id(nums))
n = len(nums)-1
nums[:] = nums[n:]+ nums[:n]
print(nums)
print(id(nums))


# Rotation by K places and do it inplace 

#BruteForce

nums = [5,-2,3,9,0,6,10,7]
n,k = len(nums)-1,3
rotations = k%n

for _ in range(0,rotations):
    e = nums.pop()
    nums.insert(0,e)

print(nums)

#Better

nums = [5,-2,3,9,0,6,10,7]
n,k = len(nums),3
k = k%n

nums[:] = nums[n-k:] + nums[:n-k]
print(nums)

#Optimal 
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
k = 3
k=k%n

def rotate(nums,left,right):
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1

rotate(nums,n-k,n-1)
rotate(nums,0,n-k-1)
rotate(nums,0,n-1)

print(nums)