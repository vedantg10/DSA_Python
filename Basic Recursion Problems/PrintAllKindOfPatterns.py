def subsequence(index, output, s, summation, arr, n):
    if index>=n:
        if summation == s:
            print (output)
        return output
    output.append(arr[index])
    summation += arr[index]
    subsequence(index+1, output, s, summation, arr, n)
    output.pop()
    summation -= arr[index]
    subsequence(index+1, output, s, summation,  arr, n)

subsequence(0, [], 3, 0, [3,1,2], 3)