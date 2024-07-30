def mergeAlternatively(word1, word2):
  #Firstly taking the list with fixed length which is length of the whole string
  length = len(word1)+len(word2)
  arr = [None]*length
  str = ""

  #Then assigning the extra length of the string to the end of the List by taking minimum length of the both strings
  if len(word1)<len(word2):
    min_length = len(word1)
    for i in range(2*min_length, len(arr)):
      arr[i] = word2[i-min_length]
  else:
    min_length = len(word2)
    for i in range(2*min_length, len(arr)):
      arr[i] = word1[i-min_length]
  # There it will trake the minimum length of the string and then it will be used to fill the remaining elements to List

  #Here we will arrenge the letters alternatively into the List
  for i in range(min_length):
    arr[i*2] = word1[i]
    arr[i*2+1] = word2[i]

  #Here we are adding the letters to the empty string and then we will return that string
  for i in arr:
    res+=i
  return res



# Another Optimized Approach
i, j = 0, 0
arr = []
length = len(word1)-len(word2)
# We will itereate to the min length of the both strings
while i<len(word1) and j<len(word2):
  arr.append(word1[i])
  arr.append(word2[j])
  i+=1
  j+=1
# Here we will comapre that if length less than zero it means the length of word1 is less than word2
# Then we will append the remaining values to the List 
if length<0:
  arr.append(word2[j:]
else:
  arr.append(word1[i:]
             
return "".join(arr)


#Problem Link : https://leetcode.com/problems/merge-strings-alternately/description/
