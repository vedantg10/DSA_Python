def subsequence(index, output, arr, n):
    if index>=n:
        return [output[:]]
    print(index)
    output.append(arr[index])
    result = subsequence(index+1, output, arr, n)
    output.pop()
    result += subsequence(index+1, output, arr, n)
    return result

print(subsequence(0, [], [3,1,2], 3))