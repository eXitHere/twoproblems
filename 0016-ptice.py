if __name__ == "__main__":
    pettern = ["ABC", "BABC", "CCAABB"]
    n = int(input())
    inp = input()
    count = [0,0,0]
    for i in range(len(inp)):
        for j in range(3):
            if inp[i] == pettern[j][i%len(pettern[j])]:
                #print(j, pettern[j][i%len(pettern[j])])
                count[j] += 1
    print(max(count))
    if max(count) == count[0]:
        print("Adrian")
    if max(count) == count[1]:
        print("Bruno")
    if max(count) == count[2]:
        print("Goran")

