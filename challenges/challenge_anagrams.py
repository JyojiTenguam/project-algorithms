def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left_half = merge_sort(string[:mid])
    right_half = merge_sort(string[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_string = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_string.append(left[i])
            i += 1
        else:
            sorted_string.append(right[j])
            j += 1

    sorted_string.extend(left[i:])
    sorted_string.extend(right[j:])

    return sorted_string


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        sorted_first = ''.join(merge_sort(first_string))
        sorted_second = ''.join(merge_sort(second_string))
        return (sorted_first, sorted_second, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first = ''.join(merge_sort(first_string))
    sorted_second = ''.join(merge_sort(second_string))

    return (sorted_first, sorted_second, sorted_first == sorted_second)
