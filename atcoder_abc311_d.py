
import pyxel

# https://atcoder.jp/contests/abc311/tasks/abc311_d

N=21
M=25
S='''\
#########################
#..............###...####
#..............#..#...###
#........###...#...#...##
#........#..#..#........#
#...##...#..#..#...#....#
#..#..#..###...#..#.....#
#..#..#..#..#..###......#
#..####..#..#...........#
#..#..#..###............#
#..#..#.................#
#........##.............#
#.......#..#............#
#..........#....#.......#
#........###...##....#..#
#..........#..#.#...##..#
#.......#..#....#..#.#..#
##.......##.....#....#..#
###.............#....#..#
####.................#..#
#########################'''.split('\n')
#print(N,M,S)

from collections import defaultdict
D=defaultdict(int)


class App():
    def __init__(self) -> None:
        pyxel.init(M*8,N*8 + 25, title='atcoder abc311 D', fps=60,display_scale=2) # column M for x , row N for y 

        # my code
        self.steps=0 # counter
        self.Q=[(1,1,'S')]# direction S(stop), U, R, D, L
        self.ANS=set()
        self.T=[list(s) for s in S] # display data

        pyxel.run( update=self.update, draw=self.draw)

    def update(self):

        if not self.Q:return # alredy logic is done, no need to calc

        self.steps+=1

        self.r_now, self.c_now,_ = r,c,d=self.Q.pop()# update for draw()           

        # passable position can be registered
        if S[r][c]=='.':
            self.ANS.add((r,c))
            self.T[r][c]='o' # display data update

        if   d=='U'and S[r-1][c]=='.':self.Q.append((r-1,c,d))
        elif d=='R'and S[r][c+1]=='.':self.Q.append((r,c+1,d))
        elif d=='D'and S[r+1][c]=='.':self.Q.append((r+1,c,d))
        elif d=='L'and S[r][c-1]=='.':self.Q.append((r,c-1,d))
        elif d=='S':
            if  D[(r,c)]<1:
                for x in 'URDL':self.Q.append( (r,c,x))
                D[(r,c)]=1
        else:self.Q.append((r,c,'S'))

    def draw(self):
        pyxel.cls(0)

        for r in range(len(S)):
            for c in range(len(S[r])):
                col=5
                if self.T[r][c]=='o':col=3
                if self.T[r][c]=='#':col=2
                if self.r_now==r and self.c_now==c:col=7
                
                #pyxel.text(r*8,c*8, self.T[r][c],col) # wrong layout
                pyxel.text(c*8,r*8, self.T[r][c],col) # c for x , r for y

        pyxel.text(10, 180, self.Q and  f'IN PROGRESS ... (STEPS) {self.steps} / found : {len(self.ANS)}' or f'FINISHED : (STEPS) {self.steps} /  answer = {len(self.ANS)}',7)
        
App()