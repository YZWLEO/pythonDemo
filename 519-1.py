#coding=utf-8
#循环
numbers = [1,2,3,4,11,22,33,88,99,1000];
print numbers
even = [];
odd = [];
while len(numbers)>0:
      num = numbers.pop();
      if(num%2==0):
            even.append(num);
      else:
            odd.append(num);

print even;
print odd;
print even+odd;
print set(even+odd)


count = 0;
while(count<=9):
      print "the count is:",count;
      count+=1;
print "gooods bye"



for str in "yanzhiwei":
      print str;
      pass
print "end for;"

import sys
print sys.getdefaultencoding();
print isinstance("中国",unicode)

