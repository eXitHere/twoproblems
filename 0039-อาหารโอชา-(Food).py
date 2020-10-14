def permutation(x):
    if x == n:
        if str(List[0]) not in str(blackList):
            print(*List)
        return
    for i in range(0,n):
        if not check[i]:
            check[i] = True
            List[x] = i+1
            permutation(x+1)
            check[i] = False

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    blackList = input().split()
    check = [False]*n
    List = [i+1 for i in range(n)]
    permutation(0)
