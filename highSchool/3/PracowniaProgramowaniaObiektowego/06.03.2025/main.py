def bubble_sort(nums: list[float]):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

print(bubble_sort([2, 5, 3, 1]))