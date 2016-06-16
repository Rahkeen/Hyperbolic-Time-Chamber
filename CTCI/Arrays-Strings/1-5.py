def compress(original):
    if original == None or len(original) == 0:
        return original

    result = ''
    pointer = 1
    curr = original[0]
    result += curr
    count = 1
    while pointer < len(original):
        if original[pointer] == curr:
            count += 1
        else:
            curr = original[pointer]
            result += str(count) + curr
            count = 1

        pointer += 1

    result += str(count)
    return result if len(result) < len(original) else original

test_string_1 = 'aabcccccaaa'
print compress(test_string_1)
