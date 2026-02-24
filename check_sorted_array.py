nums = [1,2,3,4,5,6,7,8,9,10]

def sortedarray(nums):
    n = len(nums)
    check = True
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            check =False
    return check
        
print(sortedarray(nums))
