class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]   #empty stack
        closeToOpen = {")":"(", "}":"{","]":"["}  
        #hashmap to map all the closing brackets to their opening counterparts

        for ch in s:     #loop through every character of given string
            if ch in closeToOpen:  # check if ch exists as a key in hashmap (closing ones)
                if stack and stack[-1] == closeToOpen[ch]:   
                #if stack is not empty and last item in the stack exists as a value (opening ones) to the character key in the hashmap,
                    stack.pop()  # remove that item from the stack.
                else:  #either stack empty, or last item in stack doesnt exist as a value in the hashmap
                    return False   # work is not done yet, return invalid
            else:
                stack.append(ch)  # append as many opening brackets as typed
        
        if stack:
            return False  # work is not done yet
        else: 
            return True   # stack empty, work done