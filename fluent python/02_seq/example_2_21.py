
Test = """
>>> import array
>>> numbers = array.array('h', [-2, -1, 0, 1, 2,])
>>> number
array('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview(numbers)
>>> len(memv)
5
>>> memv[-1]
2
>>> memv[-2]
1
>>> memv[0]
-2
>>> memv_oct = memv.cast('B')
>>> memv_oct
<memory at 0x7f87e64ebdc8>
>>> len(memv_oct)
10
>>> memv_oct.tolist()
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
>>> memv_oct[5] = 4
>>> numbers
array('h', [-2, -1, 1024, 1, 2])
"""