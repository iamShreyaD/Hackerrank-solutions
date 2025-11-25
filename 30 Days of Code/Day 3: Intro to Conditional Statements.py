Task
Given an integer,N , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of  to , print Not Weird
If N is even and in the inclusive range of  to , print Weird
If N is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    if (N%2 != 0):
        print("Weird")
        
    elif (N%2 == 0) and (2 <= N <= 5):
        print("Not Weird")
             
    elif (N%2 == 0) and (6 <= N <= 20):
        print("Weird")
        
    elif (N%2 == 0) and (N > 20):
        print("Not Weird")
