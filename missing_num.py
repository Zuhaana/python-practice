def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum
numbers = [1, 2, 3, 5]
n=5
print("Missing number is:", find_missing_number(numbers,n ))
