#coding=utf-8
#循环
i = 2
while (i < 100):
      j = 2
      while (j <= (i / j)):
            if not (i % j): break
            j = j + 1
      if (j > i / j): print i, " 是素数"
      i = i + 1

print "Good bye!"


for letter in "python":
      if(letter=='h'):
            print letter;
            pass
      else:
            print "****"+letter;
            pass
      pass
pass


for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"
a=1;
b=2;
print a,b;
a=34;
print a;

number = [1,3,5,6,7,8]
print max(number);
print min(number);
print max(1,2,3,4,5,6,8)
print round(1213.5,2)
#print random.choice(range(10))
#print random();
print range(1,10)
print 'h' in 'python'
print r'\n'
print R'\n'
