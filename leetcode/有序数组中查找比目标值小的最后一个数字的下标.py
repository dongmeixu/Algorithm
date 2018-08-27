def search(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if left == right and target != nums[left]:  # target未出现
            if nums[left] >= target:  # 此时如果target的值小于left,说明target应该插入到left-1的位置
                return left - 1
            else:  # 小于target，则说明当前元素就是比target小的最大下标的元素
                return left

        if nums[mid] >= target:
            right = mid - 1
        else:
            if nums[mid + 1] >= target:
                return mid
            else:
                left = mid + 1
    return -1


nums = [0, 1, 2, 2, 5, 6]
print(search(nums, 1))
