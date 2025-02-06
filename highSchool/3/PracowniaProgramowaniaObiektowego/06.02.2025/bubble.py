
str_nums = input("Podaj liczby: ").split(" ")
nums = []

for i in str_nums:
    try:
        nums.append(float(i))
    except ValueError:
        print(f"'{i}' nie jest prawidłową liczbą")

    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(nums) - 1):
            current = nums[i]
            next = nums[i + 1]

            if current > next:
                nums[i] = next
                nums[i + 1] = current

                sorted = false

    print("Posortowano:")
    print(nums)
            