n = int(input("Enter the Input: "))
"""
  *
 ***
*****
"""

# for i in range(1, n+1):
#     print(" "* (n-i),end="")
#     if (i==1):
#         print("*"* i,end="")
#     else:
#         print("*"*((i*2)-1),end="")
#     print("")

for i in range(1, n+1):
    print(" "* (n-i),end="")
    print("*"*((i*2)-1),end="")
    print("")