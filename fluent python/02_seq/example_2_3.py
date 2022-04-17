
symbals = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbals if ord(s) > 127]
print(beyond_ascii)

beyond_ascii_2 = list(filter(lambda c : c > 127,map(ord,symbals)))
print(beyond_ascii_2)
