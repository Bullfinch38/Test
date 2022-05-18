import sys


if __name__ == '__main__':
    interval = list(map(int, sys.argv[1:]))
    with open('steps.txt', 'r', encoding='utf-8') as f:
        array = [int(row.strip()) for row in f]

m = sorted(array)[len(array) // 2]
print(sum(abs(v - m) for v in array))
