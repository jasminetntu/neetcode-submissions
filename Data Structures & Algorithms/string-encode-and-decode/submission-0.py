class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each s in strs
        # take len(s) -> add to string
        # since s itself can contain nums, need way to separate len from nums in s
        # use any delimiter we choose -> first time we hit delimiter, len is done
        # have the word after delimiter
        # repeat
        # ['Hello', 'World'] -> 5-Hello5-World


        encoded_string = []

        for s in strs:
            encoded_string.append(str(len(s)))
            encoded_string.append('-')
            encoded_string.append(s)
        # print(encoded_string)
        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        p = 0
        num = []

        while p < len(s):
            if s[p].isdigit():
                num.append(s[p])
                p += 1
            elif s[p] == '-':
                length = int(''.join(num))
                decoded_strs.append(s[p + 1: p + 1 + length])
                p += 1 + length
                num = []

        return decoded_strs