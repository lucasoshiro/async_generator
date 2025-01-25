#!/usr/bin/env python3

with open('long1.txt', 'w') as f:
    print(*range(50000000), sep='\n', file=f)

with open('long2.txt', 'w') as f:
    print(*range(0, 100000000, 2), sep='\n', file=f)
