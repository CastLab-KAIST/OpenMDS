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

def SLR_Xdc (filedir, board, slr_list) :
    
    gen_xdc = os.path.join(filedir, "SLR.xdc")
    
    with open(gen_xdc, 'w') as f_d:
        if(board == 'VCU118'):
            for i in range(len(slr_list)):
                f_d.write("create_pblock SLR" + slr_list[i] + "\n")
                f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] + "]"
                + " -add {SLR" + slr_list[i] +"}\n")
                f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR" + slr_list[i] + "]\n")
        
        elif(board == 'U50'):
            for i in range(len(slr_list)):
                f_d.write("create_pblock SLR" + slr_list[i] + "\n")
                f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] + "]"
                + " -add {SLR" + slr_list[i] +"}\n")
                f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR" + slr_list[i] + "]\n")

        for i in range(len(slr_list)):
            f_d.write("add_cells_to_pblock [get_pblocks SLR" + slr_list[i] + "]"
            + " [get_cells -quiet [list User_Logic_i/SLR" + slr_list[i] + "_i]] \n")

    return