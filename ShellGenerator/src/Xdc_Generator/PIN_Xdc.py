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
            f_d.write("")
        
        elif(board == 'U50'):
            f_d.write("set_property -dict {PACKAGE_PIN J18 IOSTANDARD LVCMOS18} [get_ports gnd_out]\n")
            # Version 2020.1
            #f_d.write("set_property LOC PCIE4CE4_X1Y1 [get_cells [list " + board + "_i/XDMA/inst/pcie4c_ip_i/inst/pcie_4_0_pipe_inst/pcie_4_c_e4_inst]]\n")
            # Version 2020.2
            f_d.write("set_property LOC PCIE4CE4_X1Y1 [get_cells [list " + board + "_i/XDMA/inst/pcie4c_ip_i/inst/" + board + "_XDMA_0_pcie4c_ip_pcie_4_0_pipe_inst/pcie_4_c_e4_inst]]\n")