################################################################
# Library
################################################################
import os
from . import Prefix

################################################################
# Function
################################################################

''' Board Wrapper SV File Generate'''
def Shell_Params(filedir, board, slr_list, host_width_list=None, ddr_slr_list=None, ddr_ch_list=None, ddr_dma_width_list=None , hbm_slr_list=None, hbm_port_list=None, hbm_dma_width_list=None):
    # Create Board Shell_Params SV File
    module_name = board + "_Shell_Params"
    gen_sv = os.path.join(filedir, module_name + ".sv")
    with open(gen_sv, 'w') as f:
        # VCU118 Board
        if board == "VCU118":
            f.write("`timescale 1ns / 1ps\n\n")
            f.write("package " + board + "_Shell_Params;\n\n")

            Prefix.get_bd_parameters(board, f)

            for n in range(len(ddr_slr_list)):
                params, params_len = Prefix.get_ddr_dma_parameters(ddr_slr_list[n], ddr_ch_list[n], ddr_dma_width_list[n], board)
                for i in range(params_len):
                    f.write("    parameter {0:61} = {1};\n".format(params[i][0], params[i][1]))
                f.write("\n")
                        
            for n in range(len(slr_list)):
                params, params_len = Prefix.get_host_parameters(slr_list[n], host_width_list[n])
                for i in range(params_len):
                    f.write("    parameter {0:61} = {1};\n".format(params[i][0], params[i][1]))
                    
            f.write("endpackage")
        # End of VCU118
################
################
################
        # U50 Board
        elif board == "U50":
            f.write("`timescale 1ns / 1ps\n\n")
            f.write("package " + board + "_Shell_Params;\n\n")

            Prefix.get_bd_parameters(board, f)

            for n in range(len(hbm_slr_list)):
                params, params_len = Prefix.get_hbm_dma_parameters(hbm_slr_list[n], hbm_port_list[n], hbm_dma_width_list[n])
                for i in range(params_len):
                    f.write("    parameter {0:61} = {1};\n".format(params[i][0], params[i][1]))
                f.write("\n")

            for n in range(len(slr_list)):
                params, params_len = Prefix.get_host_parameters(slr_list[n], host_width_list[n])
                for i in range(params_len):
                    f.write("    parameter {0:61} = {1};\n".format(params[i][0], params[i][1]))
                f.write("\n")
            f.write("endpackage")
        # End of U50
################
################
################