import pyxel # pip install pyxel

# https://atcoder.jp/contests/adt_medium_20240502_3/tasks/abc275_c


S='''\
.#.......
#.#......
.#.......
.........
....#.#.#
.........
....#.#.#
........#
.........
'''.split('\n')

class App():
    def __init__(self):

        pyxel.init(256,256 + 25, title='atcoder abc275 C', fps=60, display_scale=2) # column M for x , row N for y 

        # my code
        r,c=1,1
        d='S' # direction S(stop), U, R, D, L
        self.Q=[(r,c,d)]
        self.ANS=set()
        self.DONE=set()
        self.T=[list(s) for s in S]

        pyxel.run( update=self.update, draw=self.draw)

    def update(self):

        if not self.Q:return # alredy logic is done, no need to calc

        r,c,d=self.Q.pop()

        self.r_now, self.c_now = r,c # update for draw()
        
        # when player stops, can try 4 direction
        if d=='S' and (r,c) not in self.DONE: # try U,R,D,L 
            for x in 'URDL':self.Q.append( (r,c,x))
            self.DONE.add((r,c))
        elif d=='U':
            self.Q.append( S[r-1][c]=='.' and (r-1,c,d) or (r,c,'S'))
        elif d=='R':
            self.Q.append( S[r][c+1]=='.' and (r,c+1,d) or (r,c,'S'))
        elif d=='D':
            self.Q.append( S[r+1][c]=='.' and (r+1,c,d) or (r,c,'S'))
        elif d=='L':
            self.Q.append( S[r][c-1]=='.' and (r,c-1,d) or (r,c,'S'))

        # passable position can be registered
        if S[r][c]=='.':
            self.ANS.add((r,c))
            self.T[r][c]='o' # data update
            

    def draw(self):
        pyxel.cls(0)

        for r in range(len(S)):
            for c in range(len(S[r])):
                col=6
                if self.T[r][c]=='o':col=3
                if self.T[r][c]=='#':col=2
                if self.r_now==r and self.c_now==c:col=7
                
                #pyxel.text(r*8,c*8, self.T[r][c],col) # wrong layout
                pyxel.text(c*8,r*8, self.T[r][c],col) # c for x , r for y

        pyxel.text(50, 180, self.Q and  f'IN PROGRESS ... found : {len(self.ANS)}' or f'FINISHED : answer = {len(self.ANS)}',7)
        
App()
