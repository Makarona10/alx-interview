#!/usr/bin/python3

'''0x03. Log Parsing Problem'''

import sys


lines = []
fileSize = 0
statusCodes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
while True:
    try:
        line = sys.stdin.readline()
        lines.append(line)
        fileSize += int(((line.split(' '))[-1]).strip())
        status = int((line.split(' '))[-2])
        if isinstance(status, int) or status in list(statusCodes.keys()):
            statusCodes[status] += 1
            if len(lines) % 10 == 0:
                print(f'File size: {fileSize}')
                for k, val in statusCodes.items():
                    if val > 0:
                        print(f'{k}: {val}')
    except KeyboardInterrupt:
        print(f'File size: {fileSize}')
        for k, val in statusCodes.items():
            if val > 0:
                print(f'{k}: {val}')
