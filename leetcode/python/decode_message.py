# -*- coding: utf-8 -*-

# @Time: 2023-02-01
# @File: %
# @Author: dreamhomes
# @Description: 

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for x in key:
            if x !=' ' and x not in new_key:
                new_key.append(x)
        mapping_dict =dict(zip(new_key,list(alpha[:len(new_key)])))
        for i in message:
            if i == ' ':
                print(' ', end='')
            else:
                print(mapping_dict[i],end='')
        print()





if __name__ == '__main__':
    a = Solution()
    a.decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv")

"""
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for x in key:
            if x !=' ' and x not in new_key:
                new_key.append(x)
        mapping_dict =dict(zip(new_key,list(alpha[:len(new_key)])))
        for i in message:
            if i == ' ':
                result += ' ' 
            else:
                result += mapping_dict[i]
        return result

"""
