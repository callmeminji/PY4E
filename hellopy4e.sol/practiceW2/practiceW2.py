"""
Written by M.J.Hong

starting date 23.03.29
last update 23.03.29
""" 
#

p=2
q=3
r=p*q

print (r)

r=r-q

while 1<r<5: 
    print (r+1)
    r=r-1

if r<r-1:
    print ("positive")
if r>r-1:
    print ("negative")

#
x=10
y=0
z=3


while z>0:
    if x+y>5:
        print(x)
        x=x-y-1
        y=y+1
    else :
        print(x)
        x=x+y+10
        y=0
        z=z-1

#

x=5
y=4
z=x+y
while x+y>5:
      print(z)
      z=z-2

if x+y==5:
      print("the answer is 5")


