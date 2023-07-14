#

def main():
  N=int(input())
  A=[[*map(int,input())]for i in range(N)]
  D=[]
  for _ in range(4):
      D+=A[0][:N-1]
      A=[*zip(*A)][::-1]
  D=[D[-1]]+D[:-1]
  for _ in range(4):
      A=[*map(list,A)]
      for i in range(N-1):A[0][i]=D[i]
      D,A=D[N-1:],[*zip(*A)][::-1]
  for x in A:print(''.join(map(str,x)))


'''
4
0101
1101
1111
0000

'''

for 
