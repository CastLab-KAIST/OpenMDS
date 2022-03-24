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

''' DDR Tcl Generate '''
def DDR_Tcl(filedir, refdir, board, xdma_ddr_ch=None, ddr_slr_list=None, ddr_ch_list=None):
    
    if(board == 'VCU118'):
        total_ddr_ch_list = ['false' for i in range(2)]
    
    elif(board == 'U50'):
        total_ddr_ch_list = ['false']

    elif(board =='U250'):
        total_ddr_ch_list = ['false' for i in range(4)]
        print("Implementing")
        return os.exit()

    elif(board == 'U280'):
        total_ddr_ch_list = ['false' for i in range(2)]
        print("Implementing")
        return os.exit()
    
    if(xdma_ddr_ch != None):
        for i in range(len(xdma_ddr_ch)):
            total_ddr_ch_list[int(xdma_ddr_ch[i])] = 'true'
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'

    if 'true' in total_ddr_ch_list :
        print("total_ddr_ch_list")
        print(total_ddr_ch_list)

    else :
        print("No DDR Path : DDR.Tcl Not Generated")
        return

    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_DDR.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_DDR"

    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    

    with open(gen_tcl, 'a') as f_d:
        if(board == 'VCU118'): # Start of VCU118
            # Start of DDR Interface and CLK, RESET Port
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("set DDR" + str(i) + "_S_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 DDR" + str(i) + "_S_AXI ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {31} \\\n")
                    f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
                    f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {1} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                    f_d.write("\tCONFIG.ID_WIDTH {4} \\\n")
                    f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {4} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {4} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
                    f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                    f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {1} \\\n")
                    f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
                    f_d.write("\t] $DDR" + str(i) + "_S_AXI \n\n")

                    f_d.write("set ddr4_sdram_c" + str(i + 1) +" [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:ddr4_rtl:1.0 ddr4_sdram_c"+ str(i + 1)+" ]\n\n")

                    f_d.write("set default_250mhz_clk" + str(i + 1) + " [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:diff_clock_rtl:1.0 default_250mhz_clk"  + str(i + 1) + " ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
                    f_d.write("\t] $default_250mhz_clk" + str(i + 1) + "\n\n")

                    f_d.write("set DDR" + str(i) + "_CLK [ create_bd_port -dir O -type clk DDR" + str(i) + "_CLK ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_BUSIF {DDR" + str(i) + "_S_AXI} \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_RESET {DDR" + str(i) + "_CLK_RESETN} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
                    f_d.write("\t] $DDR" + str(i) +"_CLK \n\n")

                    f_d.write("set DDR" + str(i) + "_CLK_RESETN [ create_bd_port -dir O -from 0 -to 0 -type rst DDR" + str(i) + "_CLK_RESETN ]\n\n")

            # End of DDR Interface and CLK, RESET Port
            # Start of fpga reset port
            f_d.write("set reset [ create_bd_port -dir I -type rst reset ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.POLARITY {ACTIVE_HIGH} \\\n")
            f_d.write("\t] $reset \n\n")
            # End of fpga reset port

            # Start of Processor System Reset Instance
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("set DDR" + str(i) + "_CLK_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 DDR" + str(i) + "_CLK_RESET ] \n\n")
            # End of Processor System Reset Instance

            # Start of DDR Instance
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    if(i == 0):
                        f_d.write("set DDR0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:ddr4:2.2 DDR0 ]\n")
                        f_d.write("set_property -dict [ list \\\n")
                        f_d.write("\tCONFIG.C0_CLOCK_BOARD_INTERFACE {default_250mhz_clk1} \\\n")
                        f_d.write("\tCONFIG.C0_DDR4_BOARD_INTERFACE {ddr4_sdram_c1} \\\n")
                        f_d.write("\tCONFIG.RESET_BOARD_INTERFACE {reset} \\\n")
                        f_d.write("\t] $DDR0 \n\n")
                    elif(i == 1):
                        f_d.write("set DDR1 [ create_bd_cell -type ip -vlnv xilinx.com:ip:ddr4:2.2 DDR1 ]\n")
                        f_d.write("set_property -dict [ list \\\n")
                        f_d.write("\tCONFIG.C0_CLOCK_BOARD_INTERFACE {default_250mhz_clk2} \\\n")
                        f_d.write("\tCONFIG.C0_DDR4_BOARD_INTERFACE {ddr4_sdram_c2} \\\n")
                        f_d.write("\tCONFIG.RESET_BOARD_INTERFACE {reset} \\\n")
                        f_d.write("\t] $DDR1 \n\n")
            # End of DDR Instance


            # Start of interface connection
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("connect_bd_intf_net -intf_net DDR" + str(i) + "_S_AXI [get_bd_intf_ports DDR" + str(i) + "_S_AXI] "
                    + "[get_bd_intf_pins DDR" + str(i) + "/C0_DDR4_S_AXI]\n")
                    f_d.write("connect_bd_intf_net -intf_net ddr4_sdram_c" + str(i + 1) + " [get_bd_intf_ports ddr4_sdram_c"  + str(i + 1) + "] "
                    + "[get_bd_intf_pins DDR" + str(i) + "/C0_DDR4]\n")
                    f_d.write("connect_bd_intf_net -intf_net default_250mhz_clk" + str(i + 1) + " [get_bd_intf_ports default_250mhz_clk"  + str(i + 1) + "] "
                    + "[get_bd_intf_pins DDR" + str(i) + "/C0_SYS_CLK]\n")
            # End of interface connection
            f_d.write("\n")
            # Start of Port connection
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("connect_bd_net -net DDR" + str(i) + "_CLK [get_bd_ports DDR" + str(i) + "_CLK] "
                    + "[get_bd_pins DDR" + str(i) + "/c0_ddr4_ui_clk] "
                    + "[get_bd_pins DDR" + str(i) + "_CLK_RESET/slowest_sync_clk]\n")
                    f_d.write("connect_bd_net -net DDR" + str(i) + "_CLK_RESETN [get_bd_ports DDR" + str(i) + "_CLK_RESETN] "
                    + "[get_bd_pins DDR" + str(i) + "/c0_ddr4_aresetn] "
                    + "[get_bd_pins DDR" + str(i) + "_CLK_RESET/peripheral_aresetn]\n")

            f_d.write("connect_bd_net -net reset [get_bd_ports reset] ")
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("[get_bd_pins DDR{:01d}/sys_rst] ".format(i))
                    f_d.write("[get_bd_pins DDR{:01d}_CLK_RESET/ext_reset_in] ".format(i))
            # End of Port connection
            f_d.write("\n\n")
            # Start of address
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("assign_bd_address -offset 0x00000000 -range 0x80000000 -target_address_space [get_bd_addr_spaces DDR{:01d}_S_AXI] [get_bd_addr_segs DDR{:01d}/C0_DDR4_MEMORY_MAP/C0_DDR4_ADDRESS_BLOCK] -force\n".format(i,i))                    
            # End of address
            f_d.write("\n")
        # End of VCU118 generate
        elif(board == 'U280') :
            print("not yet u280")
    # End of file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    filedir = '../../shell/VCU118/bd'
    refdir = '../Reference'
    board = 'VCU118'
    xdma_ddr_ch = ['0']
    ddr_slr_list = ['1']
    ddr_ch_list = ['1']
    DDR_Tcl(filedir, refdir, board, xdma_ddr_ch, ddr_slr_list, ddr_ch_list)

if __name__ == "__main__":
    main()