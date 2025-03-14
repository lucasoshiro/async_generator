#!/usr/bin/env python3

from threading import Thread

def async_generator(callback):
    return_value = []

    thread = Thread(target=lambda: return_value.append(callback()))
    thread.start()

    yield thread.join() or return_value[0]

def async_lines(path):
    def read_lines():
        print('reading file', path)
        with open(path) as f: return_value = [*f]
        print('file read', path)

        return return_value

    return async_generator(read_lines)

async_lines1 = async_lines('long1.txt')
async_lines2 = async_lines('long2.txt')

result = (
    int(lines1[-2]) + int(lines2[-2])
    for lines1 in async_lines1
    for lines2 in async_lines2
)

print(next(result))

