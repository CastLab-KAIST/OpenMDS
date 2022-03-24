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

''' U50 Generator '''
def U50_Tcl(filedir, refdir, slr_freq_list, hbm_clk_freq):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, "0_U50.tcl")
    ref_tcl = os.path.join(refdir, "U50.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change SLR Clock Frequency
    for idx, clk in enumerate(slr_freq_list):
        search_name = 'SLR' + str(idx) + '_CLK_FREQ'
        replace_name = clk
        # Replace
        for line in fileinput.input(gen_tcl, inplace=True):
            if search_name in line:
                line = line.replace(search_name, replace_name)
            sys.stdout.write(line)

        search_name = 'HBM_CLK_FREQ'
        replace_name = hbm_clk_freq
        # Replace
        for line in fileinput.input(gen_tcl, inplace=True):
            if search_name in line:
                line = line.replace(search_name, replace_name)
            sys.stdout.write(line)

def main():
    filedir = '../../bd'
    refdir = '../Reference'
    slr_freq_list=['200','200']

    U50_Tcl(filedir, refdir, slr_freq_list)

if __name__ == "__main__":
    main()