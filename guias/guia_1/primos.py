lim = 15000
primos = [2,3]
n = 4
while len(primos)<lim:
    cnt = 0
    for p in primos:
        if n%p==0: 
            cnt += 1
            break
    if cnt == 0: primos.append(n) 
    n += 1

print(primos)