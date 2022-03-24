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

''' AXI-LITE InterConnect Tcl Generate '''
def AXILite_INC_Tcl(filedir, refdir, board, slr_list, slr_freq_list):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_AXI_LITE_INC.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_AXI_LITE_INC"
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        if(board == 'VCU118') :
            f_d.write("set XDMA_M_AXI_LITE [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_M_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
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
            f_d.write("\t] $XDMA_M_AXI_LITE \n\n")

            f_d.write("set GPIO_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 GPIO_S_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
            f_d.write("\t] $GPIO_S_AXI_LITE \n\n")

            f_d.write("set CLK_WIZ_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 CLK_WIZ_S_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
            f_d.write("\t] $CLK_WIZ_S_AXI_LITE \n\n")


            for i in range (len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] + "_HOST_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR"  + slr_list[i] + "_HOST_S_AXI_LITE ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {"+ slr_freq_list[i] +"000000} \\\n")
                f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
                f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_HOST_S_AXI_LITE \n\n")


            # Create CLK PORT
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK \n\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ] \n\n")

            for i in range (len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000" + " SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {SLR" + slr_list[i] + "_HOST_S_AXI_LITE} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")

            # End of create port

            # Create interconnect  smartconnect
            f_d.write("set XDMA_M_AXI_LITE_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 XDMA_M_AXI_LITE_INC_0 ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.NUM_SI {1} \\\n")
            f_d.write("\tCONFIG.NUM_MI {" + str(2 + len(slr_list)) + "} \\\n")
            f_d.write("\t] $XDMA_M_AXI_LITE_INC_0 \n\n")

            for i in range(len(slr_list)) :
                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_SMC_0 [  create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_SLR" + slr_list[i] + "_SMC_0 ] \n" )
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.HAS_ARESETN {1} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_SMC_0 \n\n")

            # Create interface connections

            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE [get_bd_intf_ports XDMA_M_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/S00_AXI] \n")
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M00_AXI [get_bd_intf_ports GPIO_S_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M00_AXI] \n")
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M01_AXI [get_bd_intf_ports CLK_WIZ_S_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M01_AXI] \n")

            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_HOST_S_AXI_LITE "
                + "[get_bd_intf_ports SLR"  + slr_list[i]  + "_HOST_S_AXI_LITE] "
                + "[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/M00_AXI] \n")

            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M0" + str(2+ i) + "_AXI "
                + "[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/S00_AXI] "
                + "[get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2 + i)+ "_AXI] \n")

            # Create interface connections Done
            f_d.write("\n")

            # Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/S00_ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M00_ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M01_ACLK] ")
            for i in range (len(slr_list)) : 
                f_d.write("[get_bd_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2+i) + "_ACLK] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] +"_SMC_0/aclk] ")

            f_d.write("\n")

            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/S00_ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M00_ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M01_ARESETN] ")
            for i in range (len(slr_list)) : 
                f_d.write("[get_bd_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2+i) + "_ARESETN] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] +"_SMC_0/aresetn] ")

            f_d.write("\n")


            for i in range (len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK [get_bd_ports SLR" + slr_list[i] + "_CLK] "
                + "[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/aclk1] \n")

            # Create Port Connections Done
            f_d.write("\n")

            # Create Address Segments
            f_d.write("assign_bd_address -offset 0x00000 -range 0x00010000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] [get_bd_addr_segs GPIO_S_AXI_LITE/Reg] -force \n")
            f_d.write("assign_bd_address -offset 0x40000 -range 0x00010000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] [get_bd_addr_segs CLK_WIZ_S_AXI_LITE/Reg] -force \n")

            for i in range(len(slr_list)) :
                f_d.write("assign_bd_address -offset " + str(hex(1 + int(slr_list[i]))) + "0000 -range 0x00010000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] "
                + "[get_bd_addr_segs SLR" + slr_list[i] + "_HOST_S_AXI_LITE/Reg] -force \n")
        # End of VCU 118 Generation

        elif(board == 'U50') :
            f_d.write("set XDMA_M_AXI_LITE [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_M_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
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
            f_d.write("\t] $XDMA_M_AXI_LITE \n\n")

            f_d.write("set GPIO_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 GPIO_S_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
            f_d.write("\t] $GPIO_S_AXI_LITE \n\n")

            f_d.write("set CLK_WIZ_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 CLK_WIZ_S_AXI_LITE ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
            f_d.write("\t] $CLK_WIZ_S_AXI_LITE \n\n")

            for i in range (len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] + "_HOST_S_AXI_LITE [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR"  + slr_list[i] + "_HOST_S_AXI_LITE ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {32} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {"+ slr_freq_list[i] +"000000} \\\n")
                f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
                f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI4LITE} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_HOST_S_AXI_LITE \n\n")
                
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK \n\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ] \n\n")

            for i in range (len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000" + " SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {SLR" + slr_list[i] + "_HOST_S_AXI_LITE} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")

            f_d.write("set XDMA_M_AXI_LITE_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 XDMA_M_AXI_LITE_INC_0 ] \n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.NUM_SI {1} \\\n")
            f_d.write("\tCONFIG.NUM_MI {" + str(2 + len(slr_list)) + "} \\\n")
            f_d.write("\t] $XDMA_M_AXI_LITE_INC_0 \n\n")

            for i in range(len(slr_list)) :
                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_SMC_0 [  create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_SLR" + slr_list[i] + "_SMC_0 ] \n" )
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.HAS_ARESETN {1} \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_SMC_0 \n\n")

            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE [get_bd_intf_ports XDMA_M_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/S00_AXI] \n")
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M00_AXI [get_bd_intf_ports GPIO_S_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M00_AXI] \n")
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M01_AXI [get_bd_intf_ports CLK_WIZ_S_AXI_LITE] [get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M01_AXI] \n")

            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_HOST_S_AXI_LITE "
                + "[get_bd_intf_ports SLR"  + slr_list[i]  + "_HOST_S_AXI_LITE] "
                + "[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/M00_AXI] \n")

            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_LITE_INC_0_M0" + str(2+ i) + "_AXI "
                + "[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/S00_AXI] "
                + "[get_bd_intf_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2 + i)+ "_AXI] \n")

            # Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/S00_ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M00_ACLK] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M01_ACLK] ")
            for i in range (len(slr_list)) : 
                f_d.write("[get_bd_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2+i) + "_ACLK] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] +"_SMC_0/aclk] ")

            f_d.write("\n")

            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/S00_ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M00_ARESETN] "
            + "[get_bd_pins XDMA_M_AXI_LITE_INC_0/M01_ARESETN] ")
            for i in range (len(slr_list)) : 
                f_d.write("[get_bd_pins XDMA_M_AXI_LITE_INC_0/M0" + str(2+i) + "_ARESETN] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] +"_SMC_0/aresetn] ")

            f_d.write("\n")


            for i in range (len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK [get_bd_ports SLR" + slr_list[i] + "_CLK] "
                + "[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_SMC_0/aclk1] \n")

            f_d.write("\n")
            f_d.write("assign_bd_address -offset 0x00000 -range 0x00020000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] [get_bd_addr_segs GPIO_S_AXI_LITE/Reg] -force \n")
            f_d.write("assign_bd_address -offset 0x40000 -range 0x00010000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] [get_bd_addr_segs CLK_WIZ_S_AXI_LITE/Reg] -force \n")
            for i in range(len(slr_list)) :
                f_d.write("assign_bd_address -offset " + str(hex(2 + int(slr_list[i]))) + "0000 -range 0x00010000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI_LITE] "
                + "[get_bd_addr_segs SLR" + slr_list[i] + "_HOST_S_AXI_LITE/Reg] -force \n")
    # End of wrting file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    board = 'VCU118'
    filedir = "../../shell/" + board + "/bd"
    refdir = '../Reference'
    slr_list = ['0','1','2']
    slr_freq_list = ['200', '200', '200']

    AXILite_INC_Tcl(filedir, refdir, board, slr_list, slr_freq_list)

if __name__ == "__main__":
    main()