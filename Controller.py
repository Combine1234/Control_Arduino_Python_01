import pyfirmata

comport='COM8'

board=pyfirmata.Arduino(comport)

def Cpin13_on():
    board.digital[13].write(0)
    
def Cpin13_off():
    board.digital[13].write(1)

def Cpin12_on():
    board.digital[12].write(0)
    
def Cpin12_off():
    board.digital[12].write(1)

def Cpin11_on():
    board.digital[11].write(0)
    
def Cpin11_off():
    board.digital[11].write(1)

def Cpin10_on():
    board.digital[10].write(0)
    
def Cpin10_off():
    board.digital[10].write(1)

def Cpin9_on():
    board.digital[9].write(0)
    
def Cpin9_off():
    board.digital[9].write(1)

def Cpin8_on():
    board.digital[8].write(0)
    
def Cpin8_off():
    board.digital[8].write(1)

def Cpin7_on():
    board.digital[7].write(0)
    
def Cpin7_off():
    board.digital[7].write(1)

def Cpin6_on():
    board.digital[6].write(0)
    
def Cpin6_off():
    board.digital[6].write(1)

def Cpin5_on():
    board.digital[5].write(0)
    
def Cpin5_off():
    board.digital[5].write(1)

def Cpin4_on():
    board.digital[4].write(0)
    
def Cpin4_off():
    board.digital[4].write(1)

def Cpin3_on():
    board.digital[3].write(0)
    
def Cpin3_off():
    board.digital[3].write(1)

def Cpin2_on():
    board.digital[2].write(0)
    
def Cpin2_off():
    board.digital[2].write(1)
