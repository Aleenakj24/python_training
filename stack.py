# st=[]
# st.append(1)
# st.append(2)
# print(st)
# st.pop()
# print(st[-1])#peek

from collections import deque
st=deque()
st.append(0)
st.append(1)
st.popleft()
print(st)