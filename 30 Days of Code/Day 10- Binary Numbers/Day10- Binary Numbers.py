#!/bin/python3

import sys
n = int(input().strip())
max=0
count=0
while n>0:
    if n%2==1:
        count+=1
        if(count>max):
            max=count
    else:
        count=0
    n=n//2
    
        
print(max)