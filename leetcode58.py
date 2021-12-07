class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #ab firse inbuilt function ka use kia jo ki hai split()
        # ye ek sentence ke har word ko split kardeta hai words me, on the basis of spaces matlab for example
        # "this is me"agar ek sentence hai to list banegi ["this", "is", "me"]
        # "this, is, me" agar ye hai sentence to fir ["this,", "is,", "me"]
        # "this             is           me" to banegi ["this", "is", "me"]
        # "this,is,me" to banegi ["this,is,me"]
        # ab agar comma ke basis pe split karna ho to chota sa argument pass karna hota hai split function me jisko baad me dekhege
        
        s = list(s.split())
#         ab hme last word pick karna hai to -1 agar daaldo python me to vo last index pick karleta hai.. I know ki ye bakchodi hai but ab hai kya kare and fir len fucntion length bata deta hai
        return len(s[-1])
        