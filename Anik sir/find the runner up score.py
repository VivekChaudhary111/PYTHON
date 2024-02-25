if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    List=[]
    for i in arr:
        List.append(i)
    List.sort(reverse=True)
    for i in List:
        if i<List[0]:
            print(i)
            break
        else:
            continue