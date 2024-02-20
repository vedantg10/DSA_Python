def linear(i,n):
    if i>n:
        return
    print (i)
    return linear(i+1,n)



if __name__ == "__main__":
    n = int(input ("What is the n value: "))
    linear(1,n)