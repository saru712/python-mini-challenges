# --------------
#Code starts here

#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
palindrome(123)     
        
#Code ends here        


# --------------
#Code starts here

#Function to find anagram of one word in another

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)

#Code ends here


# --------------
#Code starts here
# python program to check if x is a perfect square 
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def check_fib(num): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (check_fib(i) == True): 
         print (i,"is a Fibonacci Number")
     else: 
         print (i,"is a not Fibonacci Number ")



# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)
compress('ssggtts')
#Code ends here


# --------------
#Code starts here

#Function to check existence of k distinct characters in string
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k
k_distinct('banana',4)
k_distinct('Messoptamia',8)
#Code ends here


