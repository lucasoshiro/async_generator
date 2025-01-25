#!/usr/bin/env python3

from threading import Thread

def async_lines(path):
    return_value = []

    def callback():
        print('reading file', path)
        with open(path) as f: return_value.append([*f])
        print('file read', path)

    thread = Thread(target=callback)
    thread.start()

    return (
        thread.join() or return_value[0]
        for _ in [None]
    )

async_lines1 = async_lines('long1.txt')
async_lines2 = async_lines('long2.txt')

result = (
    int(lines1[-2]) + int(lines2[-2])
    for lines1 in async_lines1
    for lines2 in async_lines2
)

print(next(result))

