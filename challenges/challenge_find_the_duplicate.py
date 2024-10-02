def is_valid_input(nums):
    return nums is not None and not isinstance(nums, str)


def all_integers(nums):
    return all(isinstance(num, int) for num in nums)


def no_negatives(nums):
    return all(num >= 1 for num in nums)


def find_duplicate_in_sorted(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
    return False


def find_duplicate(nums):
    if not is_valid_input(nums):
        return False

    if not all_integers(nums):
        return False

    if len(nums) < 2:
        return False

    if not no_negatives(nums):
        return False

    return find_duplicate_in_sorted(nums)
