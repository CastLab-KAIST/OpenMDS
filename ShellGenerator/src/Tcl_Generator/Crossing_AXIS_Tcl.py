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

''' Crossing AXIS Tcl Generate '''
def Crossing_AXIS_Tcl(filedir, refdir, slr_list, slr_freq_list, src_list, dest_list, num_list, data_width_list, vivado_version):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, "CROSSING_AXIS.tcl")
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = 'CROSSING_AXIS'
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)
        
    # Start of Writing tcl file descriptor
    with open(gen_tcl, 'a') as f_d:
        f_d.write("\n")
        # Create Interace Ports
        for i in range (len(src_list)) :
            if(int(data_width_list[i]) % 8 != 0) :
                dw_bytes = str((int(data_width_list[i]) // 8) + 1)
            else :
                dw_bytes = str((int(data_width_list[i]) // 8))
            ###
            for j in range(int(num_list[i])) :
                if(j < 10) :
                    f_d.write("set SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M0" + str(j) + "_AXIS" 
                    + " [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:axis_rtl:1.0 " + "SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M0"+ str(j) +"_AXIS ]\n")
                else :
                    f_d.write("set SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M" + str(j) +"_AXIS" 
                    + " [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:axis_rtl:1.0 " + "SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M"+ str(j) +"_AXIS ]\n")

                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.HAS_TKEEP {0} \\\n")
                f_d.write("\tCONFIG.HAS_TLAST {0} \\\n")
                f_d.write("\tCONFIG.HAS_TREADY {1} \\\n")
                f_d.write("\tCONFIG.HAS_TSTRB {0} \\\n")
                f_d.write("\tCONFIG.LAYERED_METADATA {undef} \\\n")
                f_d.write("\tCONFIG.TDATA_NUM_BYTES {" + dw_bytes + "} \\\n")
                f_d.write("\tCONFIG.TDEST_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.TID_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.TUSER_WIDTH {0} \\\n")
                
                if(j < 10) :
                    f_d.write("\t] $SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M0" + str(j) + "_AXIS" + "\n\n")
                    f_d.write("set SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S0" + str(j)  +"_AXIS"
                    + " [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:axis_rtl:1.0  SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S0" + str(j)  +"_AXIS ]\n\n")
                else :
                    f_d.write("\t] $SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M" + str(j) + "_AXIS" + "\n\n")
                    f_d.write("set SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S" + str(j)  +"_AXIS"
                    + " [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:axis_rtl:1.0  SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S" + str(j)  +"_AXIS ]\n\n")

                # Create fifo instance
                f_d.write("set SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) 
                + " [ create_bd_cell -type ip -vlnv xilinx.com:ip:axis_data_fifo:2.0  SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + " ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.FIFO_DEPTH {16} \\\n")
                f_d.write("\tCONFIG.FIFO_MEMORY_TYPE {distributed} \\\n")
                f_d.write("\tCONFIG.FIFO_MODE {1} \\\n")
                f_d.write("\tCONFIG.HAS_AEMPTY {0} \\\n")
                f_d.write("\tCONFIG.HAS_AFULL {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROG_EMPTY {0} \\\n")
                f_d.write("\tCONFIG.IS_ACLK_ASYNC {1} \\\n")
                f_d.write("\tCONFIG.SYNCHRONIZATION_STAGES {4} \\\n")
                
                f_d.write("\t] $SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) +"\n\n")

                if(j < 10) :
                    f_d.write("connect_bd_intf_net -intf_net SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M0" + str(j) + "_AXIS"
                    + " [get_bd_intf_ports SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M0" + str(j) + "_AXIS]"
                    + " [get_bd_intf_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/S_AXIS] \n")

                    f_d.write("connect_bd_intf_net -intf_net SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S0" + str(j) + "_AXIS"
                    + " [get_bd_intf_ports SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] +  "_S0" + str(j)+ "_AXIS]"
                    + " [get_bd_intf_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/M_AXIS] \n\n")

                else :
                    f_d.write("connect_bd_intf_net -intf_net SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M" + str(j) + "_AXIS"
                    + " [get_bd_intf_ports SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_M" + str(j) + "_AXIS]"
                    + " [get_bd_intf_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/S_AXIS] \n")

                    f_d.write("connect_bd_intf_net -intf_net SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S" + str(j) + "_AXIS"
                    + " [get_bd_intf_ports SLR" + dest_list[i] + "_FROM_SLR" + src_list[i] + "_S" + str(j)+ "_AXIS]"
                    + " [get_bd_intf_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/M_AXIS] \n\n")
            
        # Create clk, resetn ports
        for i in range (len(slr_list)) :
            f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz "+ slr_freq_list[i] + "000000 SLR" + slr_list[i] + "_CLK ]\n")
            f_d.write("set_property -dict [ list \\" + "\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
    
            flag = 0
            for j in range(len(src_list)) :
                if(src_list[j] == slr_list[i]) :
                    for k in range (int(num_list[j])):
                        if(flag == 0) :
                            flag = 1
                            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                        elif(flag == 1) :
                            f_d.write(":")
                        
                        if (k < 10) :
                            f_d.write("SLR" + src_list[j] + "_TO_SLR" + dest_list[j] + "_M0" + str(k) + "_AXIS")

                        else :
                            f_d.write("SLR" + src_list[j] + "_TO_SLR" + dest_list[j] + "_M " + str(k) + "_AXIS")
            
            for j in range(len(dest_list)) :
                if(dest_list[j] == slr_list[i]) :
                    for k in range (int(num_list[j])) :
                        if(flag == 0) :
                            flag = 1
                            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                        elif(flag == 1) :
                            f_d.write(":")

                        if(k < 10) :
                            f_d.write("SLR" + dest_list[j] + "_FROM_SLR" + src_list[j] + "_S0" + str(k) + "_AXIS")
                        else :
                            f_d.write("SLR" + dest_list[j] + "_FROM_SLR" + src_list[j] + "_S" + str(k) + "_AXIS")

            if(flag == 1) :
               f_d.write("} \\\n")
                
            f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")
            f_d.write("set SLR"+ slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]" + "\n\n")

        for i in range(len(src_list)) :
            f_d.write("connect_bd_net -net SLR" + src_list[i] + "_CLK" 
                + " [get_bd_ports SLR" + src_list[i] + "_CLK] ")

            for j in range(int(num_list[i])) :
                f_d.write("[get_bd_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/s_axis_aclk] ")
                
            f_d.write("\n")
            f_d.write("connect_bd_net -net SLR" + src_list[i] + "_CLK_RESETN" 
                + " [get_bd_ports SLR" + src_list[i] + "_CLK_RESETN] ")

            for j in range(int(num_list[i])) :
                f_d.write("[get_bd_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/s_axis_aresetn] ")

            f_d.write("\n")
            f_d.write("connect_bd_net -net SLR" + dest_list[i] + "_CLK" 
                + " [get_bd_ports SLR" + dest_list[i] + "_CLK] ")

            for j in range(int(num_list[i])) :
                f_d.write("[get_bd_pins SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + "/m_axis_aclk] ")
                # print("SLR" + src_list[i] + "_TO_SLR" + dest_list[i] + "_FIFO_" + str(j) + " is generated ")

            f_d.write("\n\n")

    # End of wrting tcl file descriptor
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)