if __name__ == "__main__":
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst1 += lst2
    lst1.sort()
    sum = 0
    #print(lst1)
    for i in range(len(lst2)):
        #print(lst1[i], lst1[-1*(i+1)])
        sum += lst1[i]*lst1[-1*(i+1)]
    print(sum)
