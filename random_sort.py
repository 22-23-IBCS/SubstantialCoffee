import random



def randomize(a:[]):
    finalA = []
    
    indexes = []
    used = []
    for i in range(len(a)):
        indexes.append(i)

    for i in range(len(a)):
        index = random.choice(indexes)
        while index in used:
            index = random.choice(indexes)
        
        used.append(index)
        finalA.append(a[index])

    return finalA


def isSorted(a:[]):

    s = True

    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            s = False
            break

    return s
    

def random_sort(a:[]):

    
    while not isSorted(a):
        a = randomize(a)
    

    return a




def main():
    print(random_sort([1,7,9,2,4,3,2,6]))



if __name__ == "__main__":
    main()
