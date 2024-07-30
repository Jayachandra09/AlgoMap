def romanToInt(s):
  dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  c = dic[s[0]]
  for i in range(1, length(s)):
    if dic[s[i-1]]>=dic[s[i]]:
      c = c+dic[s[i]]
    elif dic[s[i-1]]<=dic[s[i]]:
      c = c+dic[s[i]]-2*dic[s[i-1]]
  return c


#another approach
  dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  summ = 0
  n = len(s)
  i = 0

while i<n:
  if i<n-1 and dic[s[i]]<dic[s[i+1]]:
    summ += (dic[s[i+1]]-dic[s[i]])
    i+=2
  else:
    summ+=dic[s[i]]
    i+=1
return summ


#Problem Link : https://leetcode.com/problems/roman-to-integer/description/
