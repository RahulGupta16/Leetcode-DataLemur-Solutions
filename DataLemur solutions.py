
"""Given an input list containing n distinct numbers in the range 0 to 

n, return the only number in the range that is missing from the list.

For example, given input = [0,1,3], return 2. Because the input list has 3 elements in it, we expect to see the numbers 0 to 3 in there, but 2 is missing.

Another example: given input = [4, 3, 2, 1], return 0. We return 0 becuase the input list has 4 elements in it, 

so we expect to see the numbers 0 to 4 in there, but 0 itself is missing!"""

def missing_int(input: list[int])-> int:
  
   c = list(range(0,len(input)+1))
   if(c==input):
     return input[-1]+1
   else:
     for i in c:
       if(i not in input):
         return i
         break

"""Given a list of integers, return the maximum product of any three numbers in the array.
For example, for A = [1, 3, 4, 5], you should return 60, since 

3∗4∗5=60

For B = [−4, −2, 3, 5] you should return 40 since −4∗−2∗5=40"""

def max_three(input):
	 ans = 0
	 if(min(input)<0):
	   for i in range(len(input)):
	     for j in range(0,i):
	       for k in range(0,j):
	         if(i!=j and i!=k):
	           x = input[i]*input[j]*input[k]
	           if(x>ans):
	             ans = x
	 else:
	   ans = input[-1]*input[-2]*input[-3]
	   
	 return ans
      