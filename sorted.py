#!/usr/bin/python3


def bubble_sort(nums):
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j > 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = []
    right = []
    for idx, num in enumerate(nums):
        if idx == mid:
            continue
        if num > nums[mid]:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [nums[mid]] + quick_sort(right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def shell_sort(nums):
    size = len(nums)
    grap = size // 2
    while grap > 0:
        for i in range(grap, size):
            j = i
            while j >= grap and nums[j] < nums[j - grap]:
                nums[j], nums[j - grap] = nums[j - grap], nums[j]
                j -= grap
        grap //= 2
    return nums


def adjust_heap(nums, i, size):
    left = i * 2 + 1
    right = i * 2 + 2
    max_index = i
    if left < size and nums[left] > nums[max_index]:
        max_index = left
    if right < size and nums[right] > nums[max_index]:
        max_index = right
    if max_index != i:
        nums[i], nums[max_index] = nums[max_index], nums[i]
        adjust_heap(nums, max_index, size)


def build_heap(nums, size):
    for i in range(size // 2, -1, -1):
        adjust_heap(nums, i, size)


def heap_sort(nums):
    size = len(nums)
    build_heap(nums, size)
    for i in range(size - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjust_heap(nums, 0, i)
    return nums


if __name__ == '__main__':
    unsort_nums = [4, -1, 51, 7, 3, 14, 23, 1, 5, -5, 4, 98, 134, -23]
    print(bubble_sort(unsort_nums))
    print(insertion_sort(unsort_nums))
    print(selection_sort(unsort_nums))
    print(quick_sort(unsort_nums))
    print(merge_sort(unsort_nums))
    print(shell_sort(unsort_nums))
    print(heap_sort(unsort_nums))
