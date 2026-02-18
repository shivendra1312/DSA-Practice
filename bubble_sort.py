def bubble(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        isswapped = False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                isswapped = True
        if isswapped == False:
            break

nums =[2,5,6,8,9,4,3,2,4,3,2,1,0]

bubble(nums)

print(nums)
