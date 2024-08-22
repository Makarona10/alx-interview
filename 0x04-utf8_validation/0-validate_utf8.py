#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """

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
