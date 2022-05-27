def main():
    t = int(input())

    for i in range(t):
        a, b = map(int, input().split())
        print(f'#{i+1} {(a+b)%24}')


main()






"""
3
1 9
7 17
23 23
"""