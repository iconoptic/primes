import multiprocessing 

primes = [2,3,5,7,11,13,17,19,23,29,31,37]
def isPrime(num): 
    for i in range(len(primes)): 
        if num % primes[i] == 0:
            return -1
        elif i == len(primes)-1:
            return num 

lim = int(input("Find primes from 0 to...? ")) 
print("Working...")

if __name__ == '__main__':
    cand = []
    p = multiprocessing.Pool() 
    for i in range(39, lim+1, 24):
        for j in range(i,i+24,2):
            cand.append(j)
        result = p.map(isPrime, cand)
        for r in result:
            if r > 0: 
                primes.append(r) 
        cand.clear() 
        result.clear()

    print(primes)
