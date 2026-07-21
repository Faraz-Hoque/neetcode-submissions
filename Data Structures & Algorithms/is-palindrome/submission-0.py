class Solution:
    def isPalindrome(self, s: str) -> bool:

        #My solution - Reversing the string and check
        #Declaring a variable to store input
        newStr = ""

        #Ignoring non-alphanumeric characters
        for ch in s:    #Iterate through all characters of the string input
            if ("a"<=ch<="z"
             or "A"<=ch<="Z"
             or "0"<=ch<="9"):
                newStr += ch.lower() # Add the elligible characters to the new string variable

        #Reverse the string
        reversed_s = ""
        #Join the elements of array into a new string
        for i in range(len(newStr)-1,-1,-1):  #(start,stop,step) in range function
            reversed_s += newStr[i]
        #Check if new string matches input string
        return newStr == reversed_s