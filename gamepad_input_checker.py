import pyxel

my_img='''\
0000000000000000
00c0000000000d00
00c0000000000d00
0000000000000000
0mmmm000000nnnn0
0000000000000000
0333000000003330
3000300000030003
30k030i00j030l03
3000300000030003
0333000000003330
0000000000h00000
0000o00000000000
000q2r00g000f000
0000p00000000000
0000000000e00000
'''.split() 

stick_Lpos=(8,2)
stick_Rpos=(8,13)

KEYPOS=[]    
for x in 'abcdefghizjklmnopqrstuv':
    data=[''.join(f'{int(c==x)}' for c in line) for line in my_img ]
    KEYPOS.append(data)

my_img=[''.join(str(int('0'<c)) for c in line) for line in my_img ]

image_base=0
image_triggered=1

keylist={}
myDict={} # name : value

class App:
    def __init__(self):
        pyxel.init(256, 512, title='gamepad input', display_scale=2)

        pyxel.image(image_base).set(0, 0, my_img) # assigning string list to image(0)
        self.stick_LX=0
        self.stick_LY=0
        self.stick_RX=0
        self.stick_RY=0
        self.stick_LT=0
        self.stick_RT=0
        
        

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.my_img_trigger=[['0']*16 for _ in range(16)] # data reset

        gamepadnum='GAMEPAD1_'
        direction='LEFTX LEFTY RIGHTX RIGHTY TRIGGERLEFT TRIGGERRIGHT'.split() # a a b b c d 

        for i,x in enumerate(direction):
            data_to_check=gamepadnum + 'AXIS_' + x
            value=pyxel.btnv(eval("pyxel."+ data_to_check))

            keylist[i]=data_to_check
            myDict[data_to_check]= ' '*(0<=value)+f'{value:016b}'#formatted_string = f'{value:+016b}' if value >= 0 else f'{(1 << 16) + value:016b}'
            #myDict[data_to_check]= f'{value:+016b}' if value >= 0 else f'{(1 << 16) + value:016b}'
            myDict[data_to_check]= f'{value}'

            if x=='LEFTX':self.stick_LX=value//4096
            if x=='LEFTY':self.stick_LY=value//4096
            if x=='RIGHTX':self.stick_RX=value//4096
            if x=='RIGHTY':self.stick_RY=value//4096
            
        button='A B X Y BACK GUIDE START LEFTSTICK RIGHTSTICK LEFTSHOULDER RIGHTSHOULDER DPAD_UP DPAD_DOWN DPAD_LEFT DPAD_RIGHT'.split() # e f g h i z j k l m n o p q r
        for i,x in enumerate(button):
            data_to_check=gamepadnum + 'BUTTON_' + x
            value=pyxel.btn(eval("pyxel."+ data_to_check))

            keylist[i+6]=data_to_check
            myDict[data_to_check]=value

            if value: # add white pixel for highlight
                for r in range(16):
                    for c in range(16):
                        if KEYPOS[i+4][r][c]=='1': # if matching key position
                            if self.my_img_trigger[r][c]=='0':self.my_img_trigger[r][c]='7' # turn white if not

        pyxel.image(image_triggered).set(0, 0, [''.join(R) for R in self.my_img_trigger]) # assigning data for highlight to image(1)

    def draw(self):
        pyxel.cls(0)

        # key state in text
        for i,data_to_check in keylist.items(): 
            pyxel.text(10,10+10*i+256, f'{data_to_check} : {myDict[data_to_check]}', myDict[data_to_check] and 7 or 2)

        pyxel.blt(5, 5, image_base, 0, 0, 16, 16, 0)         # gamepad base image
        pyxel.blt(5, 5, image_triggered, 0 ,0, 16, 16, 0)    # gamepad trigger image

        #pyxel.line(100+self.stick_L_X,100+self.stick_L_Y,135+self.stick_R_X,100+self.stick_R_Y,8)
        offsetX=50
        offsetY=50
        gap=16
        pyxel.line(offsetX,offsetY,offsetX+self.stick_LX,offsetY+self.stick_LY,7)
        pyxel.line(offsetX+gap+2,offsetY,offsetX+gap+2+self.stick_RX,offsetY+self.stick_RY,7)
        pyxel.pset(offsetX+self.stick_LX,offsetY+self.stick_LY,5)
        pyxel.pset(offsetX+gap+2+self.stick_RX,offsetY+self.stick_RY,5)
        pyxel.circb(offsetX,offsetY,8,5)
        pyxel.circb(offsetX+gap+2,offsetY,8,5)

        pyxel.text(200,40, f'wip',  1)


App()
