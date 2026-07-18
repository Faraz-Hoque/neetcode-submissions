class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #check if the strings are of the same length
            return False
        count = {}  #empty dict to store characters  (frequency map)
        for ch in s:  # iterating through the characters of s 
            count[ch] = count.get(ch,0) + 1  #setting each key "ch" of the dict "count" = the value of each ch key or 0 if no value
            # count.get(key,value) selects a key in the dict count
        for ch in t:
            count[ch] = count.get(ch,0) - 1  #Decrement the value of a ch key if it also exists in t
            
        #If count comes back to 0 after cancelling out similar key counts of s and t, it is an anagram
        for val in count.values():
            if val != 0:
                return False
        return True