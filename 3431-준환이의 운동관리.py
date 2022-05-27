def main():
    t = int(input())

    for i in range(t):
        l, u, x = map(int, input().split())
        if x > u:
            print(f'#{i+1} -1')
        elif l <= x <= u:
            print(f'#{i+1} 0')
        else:
            print(f'#{i+1} {l-x}')


main()


"""
3
300 400 240
300 400 350
300 400 480
"""