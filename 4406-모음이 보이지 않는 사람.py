def main():
    t = int(input())
    vowels = 'aeiou'

    for i in range(t):
        text = input()
        
        for v in vowels:
            text = text.replace(v, "")

        print(f'#{i+1} {text}')


main()



"""
import re

def main():
    t = int(input())

    for i in range(t):
        text = str(input())
        text = re.sub('[aeiou]', '', text)
        print(f'#{i+1} {text}')


main()

"""


"""
3
congratulation
synthetic
fluid
"""