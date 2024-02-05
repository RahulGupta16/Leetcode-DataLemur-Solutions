
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

"""
Given an list of integers called input, and an integer target, return the index of the two numbers which sum up to the target. Do not use the same list element twice.

Clarifications:

Assume there aren't multiple valid solutions.
In case there is no valid solution, return [-1, -1].
Return the indexes in increasing order (i.e. [1,3], NOT [3,1]).
Example #1
Input: input = [1, 4, 6, 10], target = 10

Output: [1, 2]

Explanation: Because 4 + 6 == 10, we return the index of elements 4 and 6, which is [1, 2]

Example #2
Input: input = [1, 4, 6, 10], target = 11

Output: [0, 3]

Explanation: Because input[0] + input[3] == 11, we return [0, 3].

Example #3
**Input: **input = [1, 4, 6, 10], target = 2

Output: [-1, -1]

Explanation: There are no two elements we can pick that sum up to 2. Remember, you can't use the same element twice!
"""

def two_sum(input: list[int], target: int) -> list[int]:
	ans = []
	for i in range(len(input)):
	  for j in range(i+1,len(input)):
	    if(i==j):
	      continue
	    else:
	      if(input[i]+input[j]==target):
	        ans.append(i)
	        ans.append(j)
	if(len(ans)==0):
	  return [-1,-1]
	else:
	  return (ans)
	

"""
Before, you work on this question, make sure you've solved the easier warmup problem Factorial Formula, where you need to write a function to compute 
n factorial as follows:

n!=n∗(n−1)∗(n−2)∗.....2∗1.

Now that you know the factorial formula, let's write a function that returns the number of trailing zeroes in n!.

For example, for 
5
!
5!, we'd return 1, because 5!=5∗4∗3∗2∗1=120

5!=5∗4∗3∗2∗1=120 and 120 has exactly 1 trailing zero.

For 
10
!
10!, which evaluates to 
3628800
3628800 we'd return 2, becuase there are two trailing zeroes."""
      
def trailing_zeroes(n):
  num = 1
  c = 0
  counter=0
  if(n<=1):
    num = 1
  else:
    while(n!=1):
      num = num*n
      n=n-1
  num = str(num)[::-1]

  for i,j in enumerate(range(len(num))):
    if(i==c and num[j]=='0'):
      counter+=1
      c+=1
    else: 
      break
    
  return counter