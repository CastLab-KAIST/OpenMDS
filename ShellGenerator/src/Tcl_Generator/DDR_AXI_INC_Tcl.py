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

''' DDR AXI_INC Tcl Generate '''
def DDR_AXI_INC_Tcl(filedir, refdir, board, xdma_ddr_ch=None, ddr_slr_list=None, ddr_ch_list=None):
    # Copy and Open Reference Tcl File

    gen_tcl = os.path.join(filedir, board + "_DDR_AXI_INC.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")

    if(board == 'VCU118'):
        total_ddr_ch_list = ['false' for i in range(2)]
        ddr_ch_intf_list = [[]for i in range(2)]
    
    elif(board == 'U50'):
        total_ddr_ch_list = ['false']
        ddr_ch_intf_list = []

    elif(board =='U250'):
        total_ddr_ch_list = ['false' for i in range(4)]
        ddr_ch_intf_list = [[]for i in range(4)]
        print("Implementing")
        return os.exit()

    elif(board == 'U280'):
        total_ddr_ch_list = ['false' for i in range(2)]
        ddr_ch_intf_list = [[]for i in range(2)]
        print("Implementing")
        return os.exit()


    if(xdma_ddr_ch != None):
        for i in range(len(xdma_ddr_ch)):
            total_ddr_ch_list[int(xdma_ddr_ch[i])] = 'true'
            ddr_ch_intf_list[int(xdma_ddr_ch[i])].append('XDMA')
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(ddr_ch_list[i])].append(ddr_slr_list[i])

    if 'true' in total_ddr_ch_list :
        print("total_ddr_ch_list")
        print(total_ddr_ch_list)
        print("ddr_ch_intf_list")
        print(ddr_ch_intf_list)
    else :
        print("No DDR Path : DDR_AXI_INC.Tcl Not Generated")
        return

    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_DDR_AXI_INC"

    # print(len(hbm_port_intf_list))
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        if(board == 'VCU118') :
        # Start of VCU118
            # Start of Interface
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("set DDR" + str(i) + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 DDR" + str(i) + "_S_AXI ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {4} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {4} \\\n")
                    f_d.write("\t] $DDR" + str(i) + "_S_AXI \n\n")

            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    for j in range(len(ddr_ch_intf_list[i])):
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write("set XDMA_TO_DDR" + str(i) + "_S_AXI "
                            + "[ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_DDR" + str(i) + "_S_AXI ]\n")
                        else :
                            f_d.write("set SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR" + str(i) + "_S_AXI "
                            + "[ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR" + str(i) + "_S_AXI ]\n")
                        f_d.write("\tset_property -dict [ list \\\n")
                        f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
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
                        f_d.write("\tCONFIG.ID_WIDTH {0} \\\n")
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
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write("\t] $XDMA_TO_DDR" + str(i) + "_S_AXI \n\n")
                        else :
                            f_d.write("\t] $SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR" + str(i) + "_S_AXI \n\n")
            # End of Interface
            f_d.write("\n")
            # Start of Ports
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("set DDR" + str(i) + "_CLK [ create_bd_port -dir I -type clk -freq_hz 300000000 DDR" + str(i) + "_CLK ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                    f_d.write("DDR"+ str(i) + "_S_AXI")
                    for j in range(len(ddr_ch_intf_list[i])):
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write(":"+ ddr_ch_intf_list[i][j] + "_TO_DDR{:01d}".format(i) + "_S_AXI")
                        else :
                            f_d.write(":SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR{:01d}".format(i) + "_S_AXI")
                    f_d.write("} \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_RESET {DDR" + str(i) + "_CLK_RESETN}\\\n")
                    f_d.write("\t] $DDR" + str(i) + "_CLK\n\n")
                    f_d.write("set DDR" +str(i) + "_CLK_RESETN [ create_bd_port -dir I -type rst DDR" +str(i) + "_CLK_RESETN]\n\n")
            # End of Ports

            # Start of Instances
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("set DDR" + str(i) + "_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 DDR" + str(i) + "_INC_0 ]\n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.M00_HAS_DATA_FIFO {1} \\\n")
                    f_d.write("\tCONFIG.M00_HAS_REGSLICE {4} \\\n")
                    f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                    f_d.write("\tCONFIG.NUM_SI {" + str(len(ddr_ch_intf_list[i])) + "} \\\n")
                    for j in range(len(ddr_ch_intf_list[i])):
                        f_d.write("\tCONFIG.S0" + str(j) + "_HAS_DATA_FIFO {1} \\\n")
                        f_d.write("\tCONFIG.S0" + str(j) + "_HAS_REGSLICE {4} \\\n")
                    f_d.write("\t] $DDR" + str(i) + "_INC_0 \n\n")
            # End of Instacnes
            
            # Start of Interface connection
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("connect_bd_intf_net -intf_net DDR" + str(i) + "_S_AXI "
                    + "[get_bd_intf_ports DDR" + str(i) + "_S_AXI] "
                    + "[get_bd_intf_pins DDR"+ str(i) + "_INC_0/M00_AXI]\n")

                    for j in range(len(ddr_ch_intf_list[i])):
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write("connect_bd_intf_net -intf_net XDMA_TO_DDR" + str(i) +"_S_AXI ")
                            f_d.write("[get_bd_intf_ports XDMA_TO_DDR" + str(i) +"_S_AXI] ")
                        else :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + ddr_ch_intf_list[i][j] +"_TO_DDR" + str(i) +"_S_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + ddr_ch_intf_list[i][j] +"_TO_DDR" + str(i) +"_S_AXI] ")

                        f_d.write("[get_bd_intf_pins DDR" + str(i) + "_INC_0/S{:02d}".format(j) + "_AXI]\n")

            # End of Interface Connection
            f_d.write("\n")
            # Start of Port Connections
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("connect_bd_net -net DDR" + str(i) + "_CLK "
                    + "[get_bd_ports DDR" + str(i) + "_CLK] "
                    + "[get_bd_pins DDR" + str(i) + "_INC_0/ACLK] "
                    + "[get_bd_pins DDR" + str(i) + "_INC_0/M00_ACLK] ")

                    for j in range(len(ddr_ch_intf_list[i])):
                        f_d.write("[get_bd_pins DDR" + str(i) + "_INC_0/S{:02d}".format(j) + "_ACLK] ")
                    
                    f_d.write("\n")

                    f_d.write("connect_bd_net -net DDR" +  str(i) + "_CLK_RESETN "
                    + "[get_bd_ports DDR" +  str(i) + "_CLK_RESETN] "
                    + "[get_bd_pins DDR" +  str(i) + "_INC_0/ARESETN] "
                    + "[get_bd_pins DDR" + str(i) + "_INC_0/M00_ARESETN] ")
                    
                    for j in range(len(ddr_ch_intf_list[i])):
                        f_d.write("[get_bd_pins DDR" + str(i) + "_INC_0/S{:02d}".format(j) + "_ARESETN] ")

                    f_d.write("\n")
            # End of Port Connections
            f_d.write("\n")
            # Start of Address Segments
            for i in range(len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[i] != 'false'):
                    f_d.write("assign_bd_address -offset " + str(hex(8*i)) + "0000000 -range 0x80000000 [get_bd_addr_segs DDR{:01d}".format(i) +"_S_AXI/Reg]\n")
            # End of Address Segments
            f_d.write("\n")
        # End of VCU118
        elif(board == 'U280') :
            print("not Yet support U280")
    # End of file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    board = 'VCU118'
    refdir = '../Reference'
    filedir = "../../shell/"+ board +"/bd"
    xdma_ddr_ch = None
    ddr_slr_list = None
    ddr_ch_list = None

    DDR_AXI_INC_Tcl(filedir, refdir, board, xdma_ddr_ch, ddr_slr_list, ddr_ch_list)

if __name__=="__main__":
    main()