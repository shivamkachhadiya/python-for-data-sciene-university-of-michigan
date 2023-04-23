import numpy as np
import math
farenhit=np.array([0,-10,-5,-15,0])
celcius=(farenhit - 31)*(5/9)
print(celcius)

#boolean array
#matrix
A=np.array([[1,1],[0,1]])
B=np.array([[3,7],[8,2]])
print(A*B)
print(A@B)
print(A.shape)

array1=np.array([[1,2,3],[4,5,6]])
print(array1.dtype)
array2=np.array([[1.5,3.7,7.4],[7.8,3.9,3.7]])
print(array2.dtype)

array3=array1+array2
print(array3)
print(array3.dtype)

print(array3.sum())
print(array3.max())
print(array3.min())
print(array3.mean())

#b=np.arange(1,10,1).reshape(3,4)
#print(b)

from PIL import Image
from IPython.display import display

#display(im)

a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a[2,1])

ab=np.array([a[0,0],a[1,1],a[2,1]])
print(ab)

print(ab>5)

print(a[a>5])

a=np.array([0,1,2,3,4,5])
print(a[:3])
print(a[2:4])

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:2])
print(a[1:2])

sub_array=a[:2,1:3]
print("sub ARRRAY [0,0] value before change ",sub_array[0,0])
sub_array[0,0]=50
print("sub ARRRAY [0,0] value after change ",sub_array[0,0])
print("original arary index [0,1] vallue after change",a[0,1])
print(sub_array)


#text searching
import re
text="this is good day"
if re.search("good",text):
    print("wonderful")
else:
    print("offs not found :(")

text1="hi i am shivam computer student.hi this is spliyt"
print(re.split("hi",text1))
print(re.findall("hi",text1))

text="shivam is good. shivam is very smart. shivam can do the hard work."
print(re.search("shivam",text))

grads="ACAABCCAAACAA"
print(re.findall("B",grads))
print(re.findall("[AB]",grads))
print(re.findall("[A][B-C]",grads))
print(re.findall("[^A]",grads))

print(re.findall("A{2,10}",grads))



############################################    output    #############################
PS C:\Users\i\desktop> python num.py
[-17.22222222 -22.77777778 -20.         -25.55555556 -17.22222222]
[[3 7]
 [0 2]]
[[11  9]
 [ 8  2]]
(2, 2)
int32
float64
[[ 2.5  5.7 10.4]
 [11.8  8.9  9.7]]
float64
49.0
11.8
2.5
8.166666666666666
[[1 2]
 [3 4]
 [5 6]]
6
[1 4 6]
[False False  True]
[6]
[0 1 2]
[2 3]
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[1 2 3 4]
 [5 6 7 8]]
[[5 6 7 8]]
sub ARRRAY [0,0] value before change  2
sub ARRRAY [0,0] value after change  50
original arary index [0,1] vallue after change 50
[[50  3]
 [ 6  7]]
wonderful
['', ' i am s', 'vam computer student.', ' t', 's is spliyt']
['hi', 'hi', 'hi', 'hi']
<re.Match object; span=(0, 6), match='shivam'>
['B']
['A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A']
['AC', 'AB', 'AC']
['C', 'B', 'C', 'C', 'C']
['AA', 'AAA', 'AA']
PS C:\Users\i\desktop> 
