# practicePython\atcoder\at_coder_input_sample.py

import io
import sys

_INPUT = """\
2
1 2 3
aaa
"""

sys.stdin = io.StringIO(_INPUT)

print(int(input()))
print(list(map(int, input().split())))
print(list(input()))

# 出力
2
[1, 2, 3]
['a', 'a', 'a']

import io
import sys

_INPUT = """\
3
abcbdab
bdcaba
abc
abc
abc
bc
"""
sys.stdin = io.StringIO(_INPUT)

def longest_common_subsequence(S,T):
    '''
    example : from 'abcbdab' and 'bdcaba' find 4 (the length of 'bcab' because it is found as '*bc**ab' and 'b*cab*')   
    '''
    print(S,T)
    N=len(T)
    DP=[0]*(N+1)
    for x in S:
        #print('DP',DP,x)
        C=DP[:]
        for j, y in enumerate(T):
            DP[j+1]=(max(DP[j+1],DP[j]),C[j]+1)[x==y] # if found the same character, previous max + 1 character , otherwise fill by max(previous,current)
            #print('DP',DP,j,y)
    return DP[N]

for _ in range(int(input())):
    s=input()
    t=input()
    print(longest_common_subsequence(s,t))


_INPUT = """\
5
1 1 2 2 3
2
1 2
"""
sys.stdin = io.StringIO(_INPUT)

