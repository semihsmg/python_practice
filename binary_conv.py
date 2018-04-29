# maksimum tekrar eden 1 sayisi
print(max(map(len, bin(int(input().strip()))[2:].split('0'))))
