class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        max_length = 0
        last_seen = {}
        while r<len(s):
            c = s[r]
            if c in last_seen:   # checking if already in hashmap
                l = max(l, last_seen[c]+1)
                #  left pointer changed to greater index between 
                #(current left) and (character next to old version
                # of newly found character already in last_seen) 
                # in abcabcbb if current substring is "cab", 
                # and r advances to c(5) next to b(4), 
                # l is shifted from c to a(2 to 3)
                # old l,r = 2,4
                # new l,r = 3,5
            last_seen[c] = r #change hashmap value of that character to character at right pointer
            max_length = max(max_length, r - l + 1) 
            # length of new substring, 
            # (difference of left and right + 1)
            r += 1   #advancing r 
        return max_length