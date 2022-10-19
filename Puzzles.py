


def q1(a:[]):
    works = False
    for i in range(len(a)-1):
        if a[i] == 7 and a[i+1] == 7:
            works = True
            break
    return works

def q2(a:[]):
    first5Prime = [2,3,5,7,11]
    s = 0
    for i in range(len(a)):
        num = a[i]
        if num in first5Prime:
            continue
        if i > 0:
            if isPrime(a[i-1]):
                break
        s+=num

    return s

def isPrime(n :int):
    if n == 1:
        return False
    for i in range(2, int(n/2)):
        if n%i==0:
            return False

    return True

def isBetween(i:int, a:[]):
    less = False
    greater = True

    for i in range(1):
        pass 

def q3(a:[]):
    pass


def main():
    print(q3([1,5,6,2,99,56,3]))




if __name__ == "__main__":
    main()
