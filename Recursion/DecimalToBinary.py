def decimalToBinary(n):
    return (n%2) +10 *decimalToBinary(n//2)