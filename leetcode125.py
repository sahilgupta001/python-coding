class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
#         ab iss program ko bhot hi dhyaan se samajhio
# mushkil 1% bhi ni hai
# kia bas yahi hai ki jo string hai usme se alphabets aur numbers ke alawa jo bhi special characters hai unko nikal ke ek naya string bana lo kyuki esa ques me kaha hai
# and uske next steo me fir hum naye bane hue string ko reverse karege
# fir uske baad hum straight and reverse string ko compare karege ki agar equal hai to matlab pallindrome hai varna ni


#ab dikkat tujhe ye lagegi ki isme sab shortcuts used hai python ke har step pe
# inhi shortcuts ke chakkar me python use ki jaati hai vese 
# ab shortcuts neeche ke comments se padh

        #iss line me hum string bana rahe hai naya ... single line me hi humne for loop laga dia jo har character ko iterate karega input ke and check karega ki vo isalnum(alphabet ya number ka inbuilt function hai ye) hai ya ni
    
#uske baad usko lowercase me convert karege using inbuild function lower()

# iss line me bas likhne ka treeka seekh
# logic to vahi nnormal for loop and if else hai

        string = ''.join([c.lower() for c in s if c.isalnum()])
#         ab neeche vaali line bane hue string ko reverse karegi
# hum reverse loop chalane ke lie start index end index and kitna kitna steo lena hai vo dete the
# but python me agar khali chordo start and end index ese format me jese neeche hai to fir vo automaticalli chalata hai reverse bas -1 dekh ke aur reverse kar deta hai 

# again ratne vaala kaam tha ye
        reverseString = string[::-1]
        if string == reverseString:
            return True
        return False