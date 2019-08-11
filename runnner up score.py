if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    max1=max(arr)
    for i in range(n):
        if arr[i]==max1:
            arr[i]=-100
    print(max(arr))
    
