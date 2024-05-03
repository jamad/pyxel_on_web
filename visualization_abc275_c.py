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

        pyxel.init(256,256 + 25, title='atcoder abc275 C', fps=2, display_scale=2) # column M for x , row N for y 

        # my code
        self.r_now, self.c_now = r,c=0,0
        d='S' # direction S(stop), U, R, D, L
        self.Q=[(r,c,d)]
        self.ANS=set()
        self.DONE=set()
        self.T=[list(s) for s in S]

        self.Z=[]
        self.pos=(0,0,0,0)
            

        pyxel.run( update=self.update, draw=self.draw)

    def update(self):
        if not self.Z:
            for r in range(9):
                for c in range(9):
                    if S[r][c]=='.':continue    
                    for u in range(9):
                        for v in range(9):
                            if (r,c)==(u,v):continue
                            if S[u][v]=='.':continue    

                            self.Z.append((c*8,r*8,v*8,u*8))

        self.pos=self.Z.pop(0) # iteration of the next line 
    

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

        x,y,u,v=self.pos
        dx,dy=u-x,v-y
        pyxel.line(x,y,u,v,4) # drawing line
        pyxel.line(x+dy,y-dx,u+dy,v-dx,5)
        pyxel.line(x-dy,y+dx,u-dy,v+dx,5)

        print(*self.pos)

        pyxel.text(50, 180, self.Q and  f'IN PROGRESS ... found : {len(self.ANS)}' or f'FINISHED : answer = {len(self.ANS)}',7)
        
App()
