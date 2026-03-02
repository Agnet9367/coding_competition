import sys
import string

Test_line = sys.stdin.readline().rstrip() 

T = int(Test_line)
for i in range(T):
    numbers = sys.stdin.readline().rstrip() 
    splitted = numbers.split()
    num1 = int(splitted[0]); num2 = int(splitted[1])
    print(num1 + num2, num1 * num2)