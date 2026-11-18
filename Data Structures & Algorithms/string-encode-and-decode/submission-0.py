class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #appending encoded string to result string
            #in format 4#code
            # length of string + delimiter + string itself
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        #result list, position in list so far
        res, i =[], 0

        #iterate character by character
        #each iteration of this loop reads one entire word
        while i< len(s):
            j = i
            #starting off, first position is gonna be an int
            #first, we find the delimiter
            # so another pointer j

            #finding length of the string
            #while j has still not reached delimiter #
            while s[j] != "#":
                j +=1 #increment j
            #now storing length of the string
            length = int(s[i:j])
            #how many ch we have to read after j
            #first ch is at j+1
            #slicing up until string length
            res.append(s[j+1 : j+1 + length])

            #setting i pointer to next word
            i = j+1 + length
        return res
