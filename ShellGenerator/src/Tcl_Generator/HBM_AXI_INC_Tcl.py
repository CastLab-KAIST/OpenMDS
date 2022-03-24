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

''' HBM Tcl Generate '''
def HBM_AXI_INC_Tcl(filedir, refdir, board, hbm_slr_list, hbm_port_list, xdma_hbm_port, hbm_clk_freq):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_HBM_AXI_INC.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_HBM_AXI_INC"

    total_hbm_port_list = ['false' for i in range(32)]
    hbm_port_intf_list = [[]for i in range(32)]
    total_hbm_port_list[int(xdma_hbm_port)] = 'true'
    hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
    for i in range(len(hbm_port_list)) :
        total_hbm_port_list[int(hbm_port_list[i])] = 'true'
        hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])

    # print(len(hbm_port_intf_list))
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        # Start of Intf Port Instance
        for i in range(len(hbm_port_intf_list)) :
            for j in range(len(hbm_port_intf_list[i])):
                if(i < 10) :
                    if(hbm_port_intf_list[i][j] == 'xdma') :
                        f_d.write("set XDMA_TO_HBM0" + str(i) + "_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_HBM0" + str(i) + "_S_AXI ]\n")
                    
                    else :
                        f_d.write("set SLR" + hbm_port_intf_list[i][j] +"_TO_HBM0" + str(i) + "_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + hbm_port_intf_list[i][j] +"_TO_HBM0" + str(i) + "_S_AXI ]\n")
                else : 
                    if(hbm_port_intf_list[i][j] == 'xdma') :
                        f_d.write("set XDMA_TO_HBM" + str(i) + "_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_HBM" + str(i) + "_S_AXI ]\n")
                    
                    else :
                        f_d.write("set SLR" + hbm_port_intf_list[i][j] +"_TO_HBM" + str(i) + "_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + hbm_port_intf_list[i][j] +"_TO_HBM" + str(i) + "_S_AXI ]\n")
                        
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {33} \\\n")
                f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {256} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + str(hbm_clk_freq) +"000000} \\\n")
                f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                f_d.write("\tCONFIG.ID_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.MAX_BURST_LENGTH {16} \\\n")
                f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI3} \\\n")
                f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {1} \\\n")
                f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")

                if(i < 10) :
                    if(hbm_port_intf_list[i][j] == 'xdma') :
                        f_d.write("\t] $XDMA_TO_HBM0" + str(i) + "_S_AXI\n\n")
                    
                    else :
                        f_d.write("\t] $SLR" + hbm_port_intf_list[i][j] +"_TO_HBM0" + str(i) + "_S_AXI\n\n")
                else : 
                    if(hbm_port_intf_list[i][j] == 'xdma') :
                        f_d.write("\t] $XDMA_TO_HBM" + str(i) + "_S_AXI\n\n")
                    
                    else :
                        f_d.write("\t] $SLR" + hbm_port_intf_list[i][j] +"_TO_HBM" + str(i) + "_S_AXI\n\n")

        for i in range(len(total_hbm_port_list)) :
            if(total_hbm_port_list[i] == 'true') :
                if(i < 10) :
                    f_d.write("set HBM0" + str(i) +"_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 HBM0" + str(i) + "_S_AXI ]\n")
                else :
                    f_d.write("set HBM" + str(i) +"_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 HBM" + str(i) + "_S_AXI ]\n")

                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {33} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {256} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + str(hbm_clk_freq) + "000000} \\\n")
                f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI3} \\\n")
                f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                
                if(i < 10) :
                    f_d.write("\t] $HBM0" + str(i) +"_S_AXI\n\n")
                else :
                    f_d.write("\t] $HBM" + str(i) +"_S_AXI\n\n")

        # End of Intf Port Instance

        # Start of CLK, RESETN Port Instance
        f_d.write("set HBM_CLK [ create_bd_port -dir I -type clk -freq_hz " + str(hbm_clk_freq) + "000000 HBM_CLK ]\n")
        f_d.write("set_property -dict [ list \\\n")
        f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
        flag = 0
        for i in range(len(hbm_port_intf_list)) :
            for j in range(len(hbm_port_intf_list[i])):
                if(flag == 0) :
                    flag = 1
                    if(i < 10) :
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("XDMA_TO_HBM0" + str(i) + "_S_AXI")

                        else :
                            f_d.write("SLR" + hbm_port_intf_list[i][j] +"_TO_HBM0" + str(i) + "_S_AXI")
                    else : 
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("XDMA_TO_HBM" + str(i) + "_S_AXI")

                        else :
                            f_d.write("SLR" + hbm_port_intf_list[i][j] +"_TO_HBM" + str(i) + "_S_AXI")

                elif(flag == 1) :
                    f_d.write(":")
                    if(i < 10) :
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("XDMA_TO_HBM0" + str(i) + "_S_AXI")

                        else :
                            f_d.write("SLR" + hbm_port_intf_list[i][j] +"_TO_HBM0" + str(i) + "_S_AXI")
                    else : 
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("XDMA_TO_HBM" + str(i) + "_S_AXI")

                        else :
                            f_d.write("SLR" + hbm_port_intf_list[i][j] +"_TO_HBM" + str(i) + "_S_AXI")

        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true') :
                if(flag == 0) :
                    flag = 1
                    if(i < 10) :
                        f_d.write("HBM0" + str(i) +"_S_AXI")
                    else :
                        f_d.write("HBM" + str(i) +"_S_AXI")

                elif(flag ==1) :
                    f_d.write(":")
                    if(i < 10) :
                        f_d.write("HBM0" + str(i) +"_S_AXI")
                    else :
                        f_d.write("HBM" + str(i) +"_S_AXI")
        f_d.write("} \\\n")
        f_d.write("] $HBM_CLK\n\n")
        
        f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir I -type rst HBM_CLK_RESETN ] \n\n")
        # End of CLK, RESETN Port Instance

        # Start of INC Instance
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("set HBM0" + str(i) + "_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 HBM0" + str(i) + "_INC_0 ]\n")
                else :
                    f_d.write("set HBM" + str(i) + "_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 HBM" + str(i) + "_INC_0 ]\n")

                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.M00_HAS_DATA_FIFO {0} \\\n")
                f_d.write("\tCONFIG.M00_HAS_REGSLICE {0} \\\n")
                f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                f_d.write("\tCONFIG.NUM_SI {" + str(len(hbm_port_intf_list[i])) +"} \\\n")
                for j in range(len(hbm_port_intf_list[i])) :
                    f_d.write("\tCONFIG.S0" + str(j) + "_HAS_DATA_FIFO {0} \\\n")
                    f_d.write("\tCONFIG.S0" + str(j) + "_HAS_REGSLICE {4} \\\n")

                if(i < 10) :
                    f_d.write("\t] $HBM0" + str(i) + "_INC_0\n\n")
                else :
                    f_d.write("\t] $HBM" + str(i) + "_INC_0\n\n")
        # End of INC Instance

        # Start of Intf Connection
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                for j in range(len(hbm_port_intf_list[i])):
                    if(i < 10) :
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM0" + str(i) + "_S_AXI ")
                            f_d.write("[get_bd_intf_ports XDMA_TO_HBM0" + str(i) + "_S_AXI] ")
                        else :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_port_intf_list[i][j] + "_TO_HBM0" + str(i) + "_S_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_port_intf_list[i][j] + "_TO_HBM0" + str(i) + "_S_AXI] ")

                        f_d.write("[get_bd_intf_pins HBM0" + str(i) + "_INC_0/S0" + str(j) + "_AXI]\n")
                    else :
                        if(hbm_port_intf_list[i][j] == 'xdma') :
                            f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM" + str(i) + "_S_AXI ")
                            f_d.write("[get_bd_intf_ports XDMA_TO_HBM" + str(i) + "_S_AXI] ")
                        
                        else :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_port_intf_list[i][j] + "_TO_HBM" + str(i) + "_S_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_port_intf_list[i][j] + "_TO_HBM" + str(i) + "_S_AXI] ")
                            
                        f_d.write("[get_bd_intf_pins HBM" + str(i) + "_INC_0/S0" + str(j) + "_AXI]\n")
                if(i < 10) :
                    f_d.write("connect_bd_intf_net -intf_net HBM0" + str(i) + "_S_AXI ")
                    f_d.write("[get_bd_intf_pins HBM0" + str(i) + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins HBM0" + str(i) + "_INC_0/M00_AXI] \n")
                
                else :
                    f_d.write("connect_bd_intf_net -intf_net HBM" + str(i) + "_S_AXI ")
                    f_d.write("[get_bd_intf_pins HBM" + str(i) + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins HBM" + str(i) + "_INC_0/M00_AXI] \n")

        f_d.write("\n")
        # End of Intf Connection

        # Start of Port Connection
        f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] ")
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/ACLK] ")
                    f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/M00_ACLK] ")
                
                else :
                    f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/ACLK] ")
                    f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/M00_ACLK] ")

                for j in range(len(hbm_port_intf_list[i])):
                    if(i < 10) :
                        f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/S0" + str(j) + "_ACLK] ")
                    else :
                        f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/S0" + str(j) + "_ACLK] ")
        f_d.write("\n")
        f_d.write("connect_bd_net -net HBM_CLK_RESETN [get_bd_ports HBM_CLK_RESETN] ")
        for i in range(len(total_hbm_port_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/ARESETN] ")
                    f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/M00_ARESETN] ")
                
                else :
                    f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/ARESETN] ")
                    f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/M00_ARESETN] ")

                for j in range(len(hbm_port_intf_list[i])):
                    if(i < 10) :
                        f_d.write("[get_bd_pins HBM0" + str(i) + "_INC_0/S0" + str(j) + "_ARESETN] ")
                    else :
                        f_d.write("[get_bd_pins HBM" + str(i) + "_INC_0/S0" + str(j) + "_ARESETN] ")
        f_d.write("\n\n")
        # End of Port Connection
        # Start of address assign
        for i in range(len(total_hbm_port_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("assign_bd_address -offset 0x00000000 -range 0x000200000000 [get_bd_addr_segs {HBM0" + str(i) +"_S_AXI/Reg }] \n")
                else :
                    f_d.write("assign_bd_address -offset 0x00000000 -range 0x000200000000 [get_bd_addr_segs {HBM" + str(i) +"_S_AXI/Reg }] \n")
        # End of address assign

        #f_d.write("group_bd_cells hier [get_bd_cells [list *]]\n")
        #f_d.write("validate_bd_design\n")
        #f_d.write("startgroup\n")
        #f_d.write("set curdesign [current_bd_design]\n")
        #f_d.write("create_bd_design -cell [get_bd_cells /hier] " + board + "_HBM_AXI_INC_container\n")
        #f_d.write("current_bd_design $curdesign\n")
        #f_d.write("set new_cell [create_bd_cell -type container -reference " + board + "_HBM_AXI_INC_container hier_temp]\n")
        #f_d.write("replace_bd_cell [get_bd_cells /hier] $new_cell\n")
        #f_d.write("delete_bd_objs  [get_bd_cells /hier]\n")
        #f_d.write("set_property name hier $new_cell\n")
        #f_d.write("endgroup\n")
        #f_d.write("current_bd_design [get_bd_designs " + board + "_HBM_AXI_INC_container]\n")
        #f_d.write("update_compile_order -fileset sources_1\n")
        #f_d.write("current_bd_design [get_bd_designs " + board + "_HBM_AXI_INC]\n")
        #f_d.write("set_property -dict [list CONFIG.ENABLE_DFX {true}] [get_bd_cells hier]\n")
    # End of file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    filedir = '../../Bd'
    refdir = '../Reference'
    board = 'U50'
    xdma_hbm_port = '0'
    hbm_slr_list = ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1', '0','1', '0','1']
    hbm_port_list = ['0','0','1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12','13','13','14','14','15','15','16','16','17','17','18','18','19','19','20','20','21','21','22','22','23','23','24','24','25','25','26','26','27','27','28','28','29','29', '30', '30', '31', '31']

    HBM_AXI_INC_Tcl(filedir, refdir, board, hbm_slr_list, hbm_port_list, xdma_hbm_port, 450)

if __name__=="__main__":
    main()