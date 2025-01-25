#!/usr/bin/env python3

def not_async_lines(path):
    print('reading file', path)
    with open(path) as f: lines = [*f]
    print('file read', path)

    return lines

lines1 = not_async_lines('long1.txt')
lines2 = not_async_lines('long2.txt')

result = int(lines1[-2]) + int(lines2[-2])

print(result)
