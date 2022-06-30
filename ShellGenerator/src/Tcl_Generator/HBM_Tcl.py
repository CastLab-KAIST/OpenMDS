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
def HBM_Tcl(filedir, refdir, board, hbm_slr_list, hbm_port_list, xdma_hbm_port, hbm_clk_freq, vivado_version):
    # Copy and Open Reference Tcl File
    total_hbm_port_list = ['false' for i in range(32)]
    hbm_port_intf_list = [[]for i in range(32)]
    if(xdma_hbm_port!=None):
        total_hbm_port_list[int(xdma_hbm_port)] = 'true'
        hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
    if(hbm_port_list!=None):
        for i in range(len(hbm_port_list)) :
            total_hbm_port_list[int(hbm_port_list[i])] = 'true'
            hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])

    if 'true' in total_hbm_port_list : 
        print("HBM Path Exist : HBM.TCL Generated")
    else :
        print("No HBM Path : HBM.Tcl Not Generated")
        return
    
    gen_tcl = os.path.join(filedir, board + "_HBM.tcl")
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_HBM"

    

    # print(len(hbm_port_intf_list))
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        # Start of HBM Instance
        f_d.write("set HBM [ create_bd_cell -type ip -vlnv xilinx.com:ip:hbm:1.0 HBM ] \n")
        f_d.write("set_property -dict [ list \\\n")
        #f_d.write("\tCONFIG.HBM_MMCM1_FBOUT_MULT0 {3} \\\n")
        #f_d.write("\tCONFIG.HBM_MMCM_FBOUT_MULT0 {3} \\\n")
        f_d.write("\tCONFIG.USER_APB_EN {false} \\\n")
        f_d.write("\tCONFIG.USER_AXI_INPUT_CLK1_FREQ {"+ str(hbm_clk_freq) +"} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK1_NS {3.333} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK1_PS {3333} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK1_XDC {3.333} \\\n")
        f_d.write("\tCONFIG.USER_AXI_INPUT_CLK_FREQ {"+ str(hbm_clk_freq) +"} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK_NS {3.333} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK_PS {3333} \\\n")
        #f_d.write("\tCONFIG.USER_AXI_INPUT_CLK_XDC {3.333} \\\n")
        #f_d.write("\tCONFIG.USER_CLK_SEL_LIST0 {AXI_00_ACLK} \\\n")
        #f_d.write("\tCONFIG.USER_CLK_SEL_LIST1 {AXI_16_ACLK} \\\n")
        f_d.write("\tCONFIG.USER_HBM_CP_1 {6} \\\n")
        f_d.write("\tCONFIG.USER_HBM_DENSITY {8GB} \\\n")
        f_d.write("\tCONFIG.USER_HBM_FBDIV_1 {36} \\\n")
        f_d.write("\tCONFIG.USER_HBM_HEX_CP_RES_1 {0x0000A600} \\\n")
        f_d.write("\tCONFIG.USER_HBM_HEX_FBDIV_CLKOUTDIV_1 {0x00000902} \\\n")
        f_d.write("\tCONFIG.USER_HBM_HEX_LOCK_FB_REF_DLY_1 {0x00001f1f} \\\n")
        f_d.write("\tCONFIG.USER_HBM_LOCK_FB_DLY_1 {31} \\\n")
        f_d.write("\tCONFIG.USER_HBM_LOCK_REF_DLY_1 {31} \\\n")
        f_d.write("\tCONFIG.USER_HBM_RES_1 {10} \\\n")
        f_d.write("\tCONFIG.USER_HBM_STACK {2} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_08 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_09 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_10 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_11 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_12 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_13 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_14 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_15 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MC_ENABLE_APB_01 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_MEMORY_DISPLAY {8192} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_08 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_09 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_10 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_11 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_12 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_13 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_14 {TRUE} \\\n")
        f_d.write("\tCONFIG.USER_PHY_ENABLE_15 {TRUE} \\\n")
        for i in range(len(total_hbm_port_list)) :
            if(total_hbm_port_list[i] != 'true') :
                if(i < 10) :
                    f_d.write("\tCONFIG.USER_SAXI_0" + str(i) + " {false} \\\n")
                
                else :
                    f_d.write("\tCONFIG.USER_SAXI_" + str(i) + " {false} \\\n")

        f_d.write("] $HBM \n\n")

        # End of HBM Instance
        
        # Start of Intf Port Instance
        for i in range(len(total_hbm_port_list)) :
            if(total_hbm_port_list[i] == 'true') :
                if(i < 10) :
                    f_d.write("set HBM0" + str(i) +"_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 HBM0" + str(i) + "_S_AXI ]\n")
                else :
                    f_d.write("set HBM" + str(i) +"_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 HBM" + str(i) + "_S_AXI ]\n")

                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {33} \\\n")
                f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {256} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {"+ str(hbm_clk_freq) +"000000} \\\n")
                f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                f_d.write("\tCONFIG.ID_WIDTH {6} \\\n")
                f_d.write("\tCONFIG.MAX_BURST_LENGTH {16} \\\n")
                f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI3} \\\n")
                f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {0} \\\n")
                f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
                
                if(i < 10) :
                    f_d.write("\t] $HBM0" + str(i) +"_S_AXI\n\n")
                else :
                    f_d.write("\t] $HBM" + str(i) +"_S_AXI\n\n")
        # End of Intf Port Instance

        # Start of CLK, RESETN Port Instance
        f_d.write("set HBM_CLK [ create_bd_port -dir I -type clk -freq_hz "+str(hbm_clk_freq)+"000000 HBM_CLK ]\n")
        f_d.write("set_property -dict [ list \\\n")
        f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
        flag = 0
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
        f_d.write("set HBM_REF_CLK0 [ create_bd_port -dir I -type clk -freq_hz 100000000 HBM_REF_CLK0 ] \n\n")
        f_d.write("set HBM_REF_CLK1 [ create_bd_port -dir I -type clk -freq_hz 100000000 HBM_REF_CLK1 ] \n\n")
        # End of CLK, RESETN Port Instance

        # Start of APB_Constant Instance
        f_d.write("set APB_CONSTANT [ create_bd_cell -type ip -vlnv xilinx.com:ip:xlconstant:1.1 APB_CONSTANT ] \n\n")
        # End of APB_Constant Instance

        # Start of Intf Connection
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("connect_bd_intf_net -intf_net HBM0" + str(i) + "_S_AXI ")
                    f_d.write("[get_bd_intf_ports HBM0" + str(i) + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins HBM/SAXI_0" + str(i) + "] \n")
                
                else :
                    f_d.write("connect_bd_intf_net -intf_net HBM" + str(i) + "_S_AXI ")
                    f_d.write("[get_bd_intf_pins HBM" + str(i) + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins HBM/SAXI_" + str(i) + "] \n")

        f_d.write("\n")
        # End of Intf Connection

        # Start of Port Connection
        f_d.write("connect_bd_net -net APB_CONSTANT [get_bd_pins APB_CONSTANT/dout] [get_bd_pins HBM/APB_0_PRESET_N] [get_bd_pins HBM/APB_1_PRESET_N] \n")
        f_d.write("connect_bd_net -net HBM_REF_CLK0 [get_bd_ports HBM_REF_CLK0] [get_bd_pins HBM/APB_0_PCLK] [get_bd_pins HBM/HBM_REF_CLK_0] \n")
        f_d.write("connect_bd_net -net HBM_REF_CLK1 [get_bd_ports HBM_REF_CLK1] [get_bd_pins HBM/APB_1_PCLK] [get_bd_pins HBM/HBM_REF_CLK_1] \n")
        f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] ")
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("[get_bd_pins HBM/AXI_0" + str(i) + "_ACLK] ")
                
                else :
                    f_d.write("[get_bd_pins HBM/AXI_" + str(i) + "_ACLK] ")

        f_d.write("\n")
        f_d.write("connect_bd_net -net HBM_CLK_RESETN [get_bd_ports HBM_CLK_RESETN] ")
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                if(i < 10) :
                    f_d.write("[get_bd_pins HBM/AXI_0" + str(i) + "_ARESET_N] ")
                
                else :
                    f_d.write("[get_bd_pins HBM/AXI_" + str(i) + "_ARESET_N] ")

        f_d.write("\n\n")
        # End of Port Connection
        for i in range(len(hbm_port_intf_list)) :
            if(total_hbm_port_list[i] == 'true'):
                f_d.write("assign_bd_address [get_bd_addr_segs {")
                for j in range(32):
                    if(i < 10) :
                        if(j < 10) :
                            f_d.write(" HBM/SAXI_0" + str(i) + "/HBM_MEM0" + str(j))
                        
                        else :
                            f_d.write(" HBM/SAXI_0" + str(i) + "/HBM_MEM" + str(j))

                    else :
                        if(j < 10) :
                            f_d.write(" HBM/SAXI_" + str(i) + "/HBM_MEM0" + str(j))
                        
                        else :
                            f_d.write(" HBM/SAXI_" + str(i) + "/HBM_MEM" + str(j))
                f_d.write("}] \n")
        # Start of address assign
        # End of address assign
    # End of file descriptor
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    filedir = '../../BD'
    refdir = '../Reference'
    board = 'U50'
    xdma_hbm_port = '31'
    hbm_slr_list = ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1', '0','1', '0','1']
    hbm_port_list = ['0','0','1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12','13','13','14','14','15','15','16','16','17','17','18','18','19','19','20','20','21','21','22','22','23','23','24','24','25','25','26','26','27','27','28','28','29','29', '30', '30', '31', '31']

    HBM_Tcl(filedir, refdir, board, hbm_slr_list, hbm_port_list, xdma_hbm_port, 450)

if __name__ == "__main__":
    main()