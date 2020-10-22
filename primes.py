import multiprocessing 

def isPrime(num):
    pf = open('primes.txt', 'r')
    primes = pf.read().splitlines()
    for i in primes:
        prime = int(i)
        if num % prime == 0:
            break
        elif primes.index(i) == len(primes)-1:
            pf = open('primes.txt','a+')
            pf.write(str(num) + '\n')
    pf.close()

def runP(i):
    while True:
        isPrime(i)
        i += 2 * cores

if __name__ == '__main__':
    pf = open('primes.txt', 'r')
    l = pf.read().splitlines()
    start = int(l.pop(len(l)-1))+2
    
    cores = multiprocessing.cpu_count()
    procs = []
    for i in range(cores):
        procs.append(start)
        start += 2

    with multiprocessing.Pool(processes=cores) as p:
            p.map(runP, procs)
