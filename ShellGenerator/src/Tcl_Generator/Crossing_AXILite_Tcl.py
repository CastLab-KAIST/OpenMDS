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

''' Crossing AXI-LITE Tcl Generate '''
def Crossing_AXILite_Tcl(filedir, refdir, slr_list, slr_freq_list, vivado_version):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, "CROSSING_AXI_LITE.tcl")
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = 'CROSSING_AXI_LITE'
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    # Start of Writing tcl file descriptor
    with open(gen_tcl, 'a') as f_d:
        f_d.write("\n")
        # Create interface port
        for i in range (len(slr_list)) :
            for j in range (len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("set SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                    f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
                    f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                    f_d.write("\tCONFIG.ID_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.MAX_BURST_LENGTH {1} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
                    f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                    f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {0} \\\n")
                    f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
                    f_d.write("\t] $SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE\n\n")

        # Next
        for i in range (len(slr_list)) :
            for j in range (len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("set SLR" + slr_list[i] + "_FROM_SLR" + slr_list[j] + "_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + slr_list[i] + "_FROM_SLR" + slr_list[j] + "_S_AXI_LITE ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
                    f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
                    f_d.write("\t] $SLR" + slr_list[i] + "_FROM_SLR" + slr_list[j] + "_S_AXI_LITE\n\n")

        # Create clk, resetn ports
        for i in range (len(slr_list)) :
            f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz "+ slr_freq_list[i] + "000000 SLR" + slr_list[i] + "_CLK ]\n")
            f_d.write("set_property -dict [ list \\" + "\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
            flag = 0
            for j in range(len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    if(flag == 0) :
                        flag = 1

                    elif(flag != 0) :
                        f_d.write(":")
                    f_d.write("SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE"
                    + ":"
                    + "SLR" + slr_list[i] + "_FROM_SLR" + slr_list[j] + "_S_AXI_LITE")
                    
            f_d.write("} \\\n")
            f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")
            f_d.write("set SLR"+ slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]" + "\n\n")

        # Create smc instance
        for i in range (len(slr_list)) :
            for j in range (len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("set SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + " [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] +" ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                    f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                    f_d.write("\t] $SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "\n\n")
                
        # Create interface connections
        for i in range (len(slr_list)) :
            for j in range (len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE "
                    + "[get_bd_intf_ports SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE] "
                    + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "/S00_AXI]\n")
                    
                    f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[j] + "_FROM_SLR" + slr_list[i] + "_S_AXI_LITE "
                    + "[get_bd_intf_ports SLR" + slr_list[j] + "_FROM_SLR" + slr_list[i] + "_S_AXI_LITE] "
                    + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "/M00_AXI]\n")
        f_d.write("\n")
    
        # Create port connections
        for i in range(len(slr_list)):
            f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK [get_bd_ports SLR" + slr_list[i] + "_CLK] ")
            for j in range(len(slr_list)):
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "/aclk] ")
                    f_d.write("[get_bd_pins SLR" + slr_list[j] + "_TO_SLR" + slr_list[i] + "/aclk1] ")
            f_d.write("\n")

        for i in range(len(slr_list)) :
            f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK_RESETN [get_bd_ports SLR" + slr_list[i] + "_CLK_RESETN] ")
            for j in range(len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "/aresetn] ")
            f_d.write("\n")
        f_d.write("\n")

        # Create address segments
        for i in range(len(slr_list)) :
            for j in range(len(slr_list)) :
                if(slr_list[i] != slr_list[j]) :
                    f_d.write("assign_bd_address -offset 0x00000000 -range 0x00010000000000000000 -target_address_space "
                    + "[get_bd_addr_spaces SLR" + slr_list[i] + "_TO_SLR" + slr_list[j] + "_M_AXI_LITE] "
                    + "[get_bd_addr_segs SLR" + slr_list[j] + "_FROM_SLR" + slr_list[i] + "_S_AXI_LITE/Reg] -force\n")

    # End of wrting tcl file descriptor
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)
