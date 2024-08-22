#!/usr/bin/python3
'''0x04. UTF-8 Validation Project'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding'''

    idx = 0
    while idx < len(data):
        if data[idx] & 192 <= 128:
            idx += 1
            continue
        elif (data[idx] & 224 == 192 and idx+1 < len(data)
              and data[idx+1] & 192 == 128):
            idx += 2
            continue
        elif (data[idx] & 240 == 224 and idx+2 < len(data)
              and data[idx+1] & 192 == 128
              and data[idx+2] & 192 == 128):
            idx += 3
            continue
        elif (data[idx] & 248 == 240 and idx+3 < len(data)
              and data[idx+1] & 192 == 128 and
              data[idx+2] & 192 == 128 and data[idx+3] & 192 == 128):
            idx += 4
            continue
        else:
            return False
    return True