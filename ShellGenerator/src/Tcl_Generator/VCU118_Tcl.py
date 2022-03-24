################################################################
# Library
################################################################
import os
import sys
import shutil
import fileinput

################################################################
# Function
################################################################

''' VCU Generator '''
def VCU118_Tcl(filedir, refdir, slr_freq_list):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, "0_VCU118.tcl")
    ref_tcl = os.path.join(refdir, "VCU118.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    ## Change SLR Clock Frequency
    #for idx, clk in enumerate(slr_freq_list):
    #    search_name = 'SLR' + str(idx) + '_CLK_FREQ'
    #    replace_name = clk
    #    # Replace
    #    for line in fileinput.input(gen_tcl, inplace=True):
    #        if search_name in line:
    #            line = line.replace(search_name, replace_name)
    #        sys.stdout.write(line)
