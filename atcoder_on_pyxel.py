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


###

# -*- coding: utf-8 -*-
import pyxel
import sys
print(sys.executable) # check which pything is running

# constant variables (rare to change)
screen_width=160
screen_height=120
my_disp_scale=2
my_fps=60

# for this app
from time import gmtime, strftime

class App:
    
    def __init__(self): 
        pyxel.init(screen_width, screen_height, title="time display", display_scale=my_disp_scale, fps=my_fps)
        self.my_time="-" # initial declaration for time to display
        pyxel.run(self.update, self.draw) 

    def update(self):            
        self.my_time=strftime("%Y-%m-%d %H:%M:%S", gmtime()) # update time to display
        

    def draw(self): 
        pyxel.cls(0)# clear screen
        pyxel.text(10, 10, f"TIME: {self.my_time}", 10) # display text

App()
