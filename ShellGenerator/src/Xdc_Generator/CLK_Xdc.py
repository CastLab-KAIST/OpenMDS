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

def CLK_Xdc (filedir, board) :
    
    gen_xdc = os.path.join(filedir, "CLK.xdc")
    
    with open(gen_xdc, 'w') as f_d:
        if(board == 'VCU118'):
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets VCU118_CLK_WIZ_i/USER_REF_CLK_WIZ_0/inst/user_ref_clk0_BUFGCE]\n")
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets VCU118_CLK_WIZ_i/USER_REF_CLK_WIZ_0/inst/user_ref_clk1_BUFGCE]\n")
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets VCU118_CLK_WIZ_i/USER_REF_CLK_WIZ_0/inst/user_ref_clk2_BUFGCE]\n")
            #f_d.write("")
        
        elif(board == 'U50'):
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets U50_CLK_WIZ_i/USER_REF_CLK_WIZ_0/inst/user_ref_clk0_BUFGCE]\n")
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets U50_CLK_WIZ_i/USER_REF_CLK_WIZ_0/inst/user_ref_clk1_BUFGCE]\n")
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets U50_CLK_WIZ_i/USER_REF_CLK_WIZ_1/inst/user_ref_clk2_BUFGCE]\n")
            f_d.write("set_property CLOCK_DEDICATED_ROUTE BACKBONE [get_nets U50_CLK_WIZ_i/USER_REF_CLK_WIZ_1/inst/user_ref_clk3_BUFGCE]\n")
        
    return