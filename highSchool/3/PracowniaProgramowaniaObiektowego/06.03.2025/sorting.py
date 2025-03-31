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

def insertion_sort(nums: list[float]):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums


def merge_sort(nums: list[float]) -> list[float]:
    ln = len(nums)
    
    if ln <= 1:
        return nums
    
    half = ln // 2
    left = nums[:half]
    right = nums[half:]

    left_len = len(left)
    right_len = len(right)

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < left_len and j < right_len:
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < left_len:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < right_len:
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


print(bubble_sort([2, 5, 3, 1]))
print(select_sort_min([1, 9, 5, 3, 0, 1]))
print(select_sort_max([1, 6, 3, 3, 2, 9]))
print(insertion_sort([4, 2, 1, 3, 8, 1]))
print(merge_sort([4, 2, 1, 4, 5]))