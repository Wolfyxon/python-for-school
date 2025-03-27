def bubble_sort(nums: list[float]) -> list[float]:
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

def select_sort_min(nums: list[float]) -> list[float]:
    ln = len(nums)

    for i in range(ln):
        min_i = i

        for j in range(i + 1, ln):
            if nums[j] < nums[min_i]:
                min_i = j
        
        nums[i], nums[min_i] = nums[min_i], nums[i]

    return nums

def select_sort_max(nums: list[float]) -> list[float]:
    ln = len(nums)

    for i in range(ln):
        max_i = i

        for j in range(i + 1, ln):
            if nums[j] > nums[max_i]:
                max_i = j
        
        nums[i], nums[max_i] = nums[max_i], nums[i]

    return nums



print(bubble_sort([2, 5, 3, 1]))
print(select_sort_min([1, 9, 5, 3, 0, 1]))
print(select_sort_max([1, 6, 3, 3, 2, 9]))