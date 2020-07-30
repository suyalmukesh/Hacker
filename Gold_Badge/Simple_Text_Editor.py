########################################################
##  Wow , the last assignment to get Gold Badge in HR ##
##  Not so tough as Medium level                      ##
##  All tests passed like charm                       ##
##  Dated : 25/07/2020                                ##
########################################################
import os
import sys
stack = []
st = ""
for i in range(int(input())):
    s = input()
    if s[0] == '1':
        if stack:
            st = stack[-1]
            st = st.strip()
            st = st + s[2:]
            stack.append(st)
        else:
            stack.append(s[2:])
    elif s[0]  == '2':
        st = stack[-1]
        n = len(st)
        k = int(s[2:])
        st = st[:n-k]
        stack.append(st)
    elif s[0]  == '3':
        a = stack[-1]
        k = int(s[2:])
        print(a[k-1])
    elif s[0] == '4':
        stack.pop(-1)

# -------------- E N D --------------------------------- #
