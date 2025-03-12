def bubble_sort(nums: list[float]) -> list[float]:
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

def select_sort(nums: list[float]) -> list[float]:
    ln = len(nums) - 1

    for i in range(ln):
        min_i = 0

        for j in range(i, ln):
            if nums[j] < nums[min_i]:
                min_i = j
        print(min_i)
        #nums[i], nums[min_i + 1] = nums[min_i + 1], nums[i]

    return nums


print(bubble_sort([2, 5, 3, 1]))
print(select_sort([1, 9, 5, 3, 0, 1]))
