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

        pyxel.init(256,256 + 25, title='atcoder abc275 C', fps=15, display_scale=2) # column M for x , row N for y 

        # my code
        self.r_now, self.c_now = r,c=0,0
        d='S' # direction S(stop), U, R, D, L
        self.Q=[(r,c,d)]
        self.ANS=set()
        self.DONE=set()
        self.T=[list(s) for s in S]

        self.Z=[]
        for r in range(9):
            for c in range(9):
                if S[r][c]=='.':continue    
                for u in range(9):
                    for v in range(9):
                        if (r,c)==(u,v):continue
                        if S[u][v]=='.':continue    
                        self.Z.append((c,r,v,u))

        self.pos=(0,0,0,0)
            

        pyxel.run( update=self.update, draw=self.draw)

    def update(self):
        if not self.Z:return 

        self.pos=self.Z.pop(0) # iteration of the next line 
    

    def draw(self):
        def drawline(a,b,c,d):
            pyxel.line(a*8,b*8,c*8,d*8,4) # drawing line
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
        drawline(x,y,u,v)# drawing line
        x1,y1,u1,v1=x+dy,y-dx,u+dy,v-dx
        drawline(x1,y1,u1,v1)# drawing line
        x2,y2,u2,v2=x-dy,y+dx,u-dy,v+dx
        drawline(x2,y2,u2,v2)# drawing line

        try:
            print(S[y1][x1],S[v1][u1],S[y1][x1]==S[v1][u1]=='#')
            if S[y1][x1]==S[v1][u1]=='#':
                data=sorted([(y1,x1),(v1,u1),(y,x),(v,u)])
                self.ANS.add(tuple(data))
        except:
            pass

        try:
            if S[y2][x2]==S[v2][u2]=='#':
                data=sorted([(y2,x2),(v2,u2),(y,x),(v,u)])
                self.ANS.add(tuple(data))
        except:
            pass


        #print(*self.pos)

        pyxel.text(50, 180, self.Q and  f'IN PROGRESS ... found : {len(self.ANS)}' or f'FINISHED : answer = {len(self.ANS)}',7)
        
App()
