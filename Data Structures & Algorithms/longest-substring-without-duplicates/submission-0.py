class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of max length
        # inc right until there is a duplicate char
        # if duplicate, then inc left until there are no more duplicates
        
        max_length = 1
        i = 0
        j = 1

        if len(s) == 0: # edge case
            return 0
        
        seen = set(s[i])
        while i < j and j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                # max_length = max(len(s[i:j + 1]), max_length)
                max_length = max(max_length, j - i + 1) # just use index to find length

                # print(i, j, max_length)
                j += 1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
                seen.add(s[j])
                j += 1
        
        return max_length
            
            


        