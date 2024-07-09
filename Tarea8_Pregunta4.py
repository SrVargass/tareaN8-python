def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n-1)
n=5
print("la sumatoria de",n,"es:",sumatoria(n)) #5+4+3+2+1 =15
