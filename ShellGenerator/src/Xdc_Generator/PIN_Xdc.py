################################################################
# Library
################################################################
import os 
import sys
import fileinput
import shutil

################################################################
# Function
################################################################

def PIN_Xdc (filedir, board) :

    gen_xdc = os.path.join(filedir, "PIN.xdc")
    
    with open(gen_xdc, 'w') as f_d:
        if(board == 'VCU118'):
            for i in range(3):
                f_d.write("")
        
        elif(board == 'U50'):
            f_d.write("set_property -dict {PACKAGE_PIN J18 IOSTANDARD LVCMOS18} [get_ports gnd_out]")