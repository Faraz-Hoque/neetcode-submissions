class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointer solution
        #Declaring a variable to store input
        newStr = ""

        #Ignoring non-alphanumeric characters
        for ch in s:    #Iterate through all characters of the string input
            if ("a"<=ch<="z"
             or "A"<=ch<="Z"
             or "0"<=ch<="9"):
                newStr += ch.lower() # Add the elligible characters to the new string variable

        #Setting the two pointers
        l,r = 0, len(newStr)-1

        #They progressively match each characters from both ends
        while l<r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True
