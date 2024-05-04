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

S='''\
##.......
##.......
.........
.......#.
.....#...
........#
......#..
.........
.........
'''.split('\n')


S='''\
.#.#..#..
###..#.#.
###.....#
..##.....
.##.##..#
###.#.##.
##...#.##
.##....#.
..#.#.#.#
'''.split('\n')



S='''\
....#...#
..#..#..#
.........
...#.....
.#.......
.........
.#.......
.........
...#.....
'''.split('\n')



S='''\
#########
#########
#########
#########
#########
#########
#########
#########
#########
'''.split('\n')



class App():
    def __init__(self):

        pyxel.init(256,256 + 25, title='atcoder abc275 C', fps=60, display_scale=2) # column M for x , row N for y 

        # my code
        self.pos=(0,0,0,0) # 2points for line
        self.ANS=set()
        self.T=[list(s) for s in S]

        self.Z=set()

        for r1 in range(9):
            for c1 in range(9):
                if S[r1][c1]=='.':continue
                for r2 in range(r1,9):
                    for c2 in range(c1,9):
                        if S[r2][c2]=='.':continue  
                        if (r1,c1)==(r2,c2):continue
                    
                        dr,dc=r2-r1,c2-c1
                        
                        r3,c3=r1+dc,c1-dr
                        r4,c4=r2+dc,c2-dr
                        
                        r5,c5=r1-dc,c1+dr
                        r6,c6=r2-dc,c2+dr

                        for a,b,c,d in ((r3,c3,r4,c4),(r5,c5,r6,c6)):
                            if not all(0<=p<9 for p in (a,b,c,d)):continue
                            if not S[a][b]==S[c][d]=='#':continue
                            data=sorted([(a,b),(c,d),(r1,c1),(r2,c2)])
                            self.Z.add(tuple(data))
        
        self.Z=sorted(self.Z)

        self.ans=len(self.Z)

        pyxel.run( update=self.update, draw=self.draw)

    def update(self):

        if not self.Z:return 

        self.pos=self.Z.pop(0) # iteration of the next line 
    

    def draw(self):

        pyxel.cls(0)

        for r in range(len(S)):
            for c in range(len(S[r])):
                col=6
                if self.T[r][c]=='o':col=3
                if self.T[r][c]=='#':col=2
                pyxel.text(c*8,r*8, self.T[r][c],col) # c for x , r for y
        
        if self.Z:
            #self.ans+=1

            def drawline(a,b,c,d,col):pyxel.line(a*8,b*8,c*8,d*8,col) # drawing line

            (r1,c1),(r2,c2),(r3,c3),(r4,c4)=self.pos
            drawline(r1,c1,r2,c2,4)# drawing line
            drawline(r1,c1,r3,c3,7)# drawing line
            drawline(r2,c2,r4,c4,7)# drawing line
            drawline(r3,c3,r4,c4,7)# drawing line


        pyxel.text(50, 180,  f'IN PROGRESS ... found : {self.ans}' or f'FINISHED : answer = {self.ans}',7)
        
App()
