#!/usr/bin/python3

'''0x03. Log Parsing Problem'''

from sys import stdin


if __name__ == '__main__':
    stdin = stdin
    lines = []
    fileSize = 0
    statusCodes = {'200': 0, '301': 0, '400': 0,
                   '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in stdin:
            lines.append(line)
            fileSize += int(((line.split())[-1]))
            try:
                fileSize += int(((line.split())[-1]))
                if (line.split())[-2] in list(statusCodes.keys()):
                    statusCodes[(line.split())[-2]] += 1
            except (IndexError, ValueError):
                pass

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
        raise
