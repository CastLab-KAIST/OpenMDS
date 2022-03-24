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

''' AXI InterConnect Tcl Generate '''
def AXI_INC_Tcl(filedir, refdir, board, slr_list, slr_freq_list, host_width_list=None, xdma_ddr_ch_list=None, ddr_slr_list=None, ddr_ch_list=None ,ddr_dma_list=None, ddr_dma_width_list=None, 
                hbm_slr_list=None, hbm_port_list=None, hbm_dma_list=None, hbm_dma_width_list=None, xdma_hbm_port=None, hbm_clk_freq=None):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_AXI_INC.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")

    slr_ddr_ch_list = [[]for i in range(len(slr_list))]
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

    else :
        print("[ERROR] Do Not Support " + board)
        return os.exit()
        

    

    if(ddr_ch_list != None):
        for i in range(len(slr_list)):
            for j in range(len(ddr_ch_list)):
                if(slr_list[i] == ddr_slr_list[j]):
                    slr_ddr_ch_list[i].append(ddr_ch_list[j])

    if(xdma_ddr_ch_list != None):
        print(xdma_ddr_ch_list)
        for i in range(len(xdma_ddr_ch_list)):
            total_ddr_ch_list[int(xdma_ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(xdma_ddr_ch_list[i])].append('XDMA')
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(ddr_ch_list[i])].append(ddr_slr_list[i])

    if(xdma_ddr_ch_list == None):
        xdma_ddr_ch_list = []
    #print("ddr_slr_list")
    #print(ddr_slr_list)
    #print("ddr_ch_list")
    #print(ddr_ch_list)
#
    #print("slr_ddr_ch_list")
    #print(slr_ddr_ch_list)
    #print("total_ddr_ch_list")
    #print(total_ddr_ch_list)
    #print("ddr_ch_intf_list")
    #print(ddr_ch_intf_list)

    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_AXI_INC"
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        # Port Instance
        if(board == 'VCU118'):
            #for i in range (len(slr_list)) : 
            #    f_d.write("set SLR" + slr_list[i] + "_HOST_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 " + "SLR" + slr_list[i] +"_HOST_S_AXI ] \n")
            #    f_d.write("set_property -dict [ list \\\n")
            #    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
            #    f_d.write("\tCONFIG.DATA_WIDTH " + "{" + host_width_list[i] +"}"+ " \\\n")
            #    f_d.write("\tCONFIG.FREQ_HZ " + "{" + slr_freq_list[i] + "000000" +"}"+ " \\\n")
            #    f_d.write("\tCONFIG.HAS_REGION {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
            #    f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
            #    f_d.write("\t] $SLR"+ slr_list[i] + "_HOST_S_AXI \n\n")

            # XDMA_M_AXI PORT INSTANCE
            #f_d.write("set XDMA_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_M_AXI ] \n")
            #f_d.write("set_property -dict [ list \\\n")
            #f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
            #f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
            #f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
            #f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
            #f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
            #f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            #f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
            #f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            #f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
            #f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
            #f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
            #f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            #f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            #f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
            #f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
            #f_d.write("\tCONFIG.ID_WIDTH {4} \\\n")
            #f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
            #f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {32} \\\n")
            #f_d.write("\tCONFIG.NUM_READ_THREADS {4} \\\n")
            #f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
            #f_d.write("\tCONFIG.NUM_WRITE_THREADS {4} \\\n")
            #f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
            #f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
            #f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
            #f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
            #f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
            #f_d.write("\tCONFIG.WUSER_WIDTH {0}" + "\n")
            #f_d.write("\t] $XDMA_M_AXI \n\n")

            for i in range (len(slr_list)) :
                for j in range (int(ddr_dma_list[i])) :
                    f_d.write("set SLR" + slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 " 
                    + "SLR" + slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI ] \n")
                    f_d.write("set_property -dict [ list \\"+ "\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH " + "{" + ddr_dma_width_list[i] +"}" + " \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ " + "{" + slr_freq_list[i] + "000000" +"}" + " \\\n")
                    f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {1} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {1} \\\n")
                    f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                    f_d.write("\tCONFIG.ID_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
                    f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                    f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {1} \\\n")
                    f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.WUSER_WIDTH {0}" + "\n")
                    f_d.write("\t] $SLR"+ slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI \n\n")

            # SLR, XDMA TO DD0_S_AXI, DDR1_S_AXI PORT INSTACNE
            #for j in range(len(xdma_ddr_ch_list)) :
            #    f_d.write("set XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI ] \n")
            #    f_d.write("set_property -dict [ list \\"+ "\n")
            #    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
            #    f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
            #    f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
            #    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            #    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {4} \\\n")
            #    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {4} \\\n")
            #    f_d.write("\tCONFIG.PROTOCOL {AXI4}" + "\n")
            #    f_d.write("\t] $XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI \n\n")

            for i in range(len(slr_list)):
                if(slr_ddr_ch_list != None):
                    for j in range(len(slr_ddr_ch_list[i])) :
                        f_d.write("set SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI ] \n")
                        f_d.write("set_property -dict [ list \\"+ "\n")
                        f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                        f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
                        f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
                        f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                        f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {4} \\\n")
                        f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {4} \\\n")
                        f_d.write("\tCONFIG.PROTOCOL {AXI4}" + "\n")
                        f_d.write("\t] $SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI \n\n")

            # CLK PORT INSTANCE
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] == 'true'):
                    f_d.write("set DDR{:01d}".format(i) + "_CLK  [ create_bd_port -dir I -type clk -freq_hz 300000000 DDR{:01d}".format(i) + "_CLK ] \n")
                    f_d.write("set_property -dict [list \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                    flag = 0
                    for j in range(len(ddr_ch_intf_list[i])):
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write("")
                        elif(flag == 0) :
                            flag = flag + 1
                            f_d.write("SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR{:01d}".format(i) + "_S_AXI")
                        elif(flag != 0) :
                            flag = flag + 1
                            f_d.write(":SLR" + ddr_ch_intf_list[i][j] + "_TO_DDR{:01d}".format(i) + "_S_AXI")
                    f_d.write("} \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_RESET {" + "DDR{:01d}".format(i) + "_CLK_RESETN} \n")
                    f_d.write("\t] $DDR{:01d}".format(i) + "_CLK \n\n")

                    f_d.write("set DDR{:01d}".format(i) + "_CLK_RESETN [ create_bd_port -dir I -type rst DDR{:01d}".format(i) + "_CLK_RESETN ] \n\n")


            #f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ] \n")
            #f_d.write("set_property -dict [list \\\n")
            #f_d.write("CONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \n")
            #f_d.write("] $XDMA_CLK \n\n")
#
            #f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ] \n\n")

            for i in range(len(slr_list)) : 
                f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000" + " SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                #f_d.write("SLR" + slr_list[i] + "_HOST_S_AXI")
                flag = 0
                for j in range(int(ddr_dma_list[i])) :
                    if(flag == 0) :
                        f_d.write("")
                        flag = flag + 1
                    elif(flag != 0 ):
                        f_d.write(":")
                    f_d.write("SLR" + slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI")

                f_d.write("} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")
                f_d.write("set SLR"+ slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]" + "\n\n")
            # Port Instacne is Done

            # INC and SMC Instance
            # SLR_DMA_INC
            for i in range (len(slr_list)) :
                if(len(slr_ddr_ch_list[i]) != 0):
                    f_d.write("set SLR" + slr_list[i] + "_DMA_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 " + "SLR" + slr_list[i] + "_DMA_INC_0 ] \n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.NUM_MI {" + str(len(slr_ddr_ch_list[i])) +"} \\\n")
                    for j in range(len(slr_ddr_ch_list[i])) :
                        f_d.write("\tCONFIG.M{:02d}".format(j) + "_HAS_REGSLICE {4} \\\n")
                        f_d.write("\tCONFIG.M{:02d}".format(j) + "_HAS_DATA_FIFO {0} \\\n")

                    for j in range (int(ddr_dma_list[i])) :
                        f_d.write("\tCONFIG.S{:02d}".format(j) + "_HAS_REGSLICE {4} \\\n")
                        f_d.write("\tCONFIG.S{:02d}".format(j) + "_HAS_DATA_FIFO {0} \\\n")

                    f_d.write("\tCONFIG.NUM_SI {" + ddr_dma_list[i] + "} \\\n")
                    f_d.write("\t] $SLR" + slr_list[i] + "_DMA_INC_0 \n\n")

            # XDMA_M_AXI_INC_0
            #f_d.write("set XDMA_M_AXI_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 XDMA_M_AXI_INC_0 ] \n")
            #f_d.write("set_property -dict [ list \\\n")
            #f_d.write("\tCONFIG.NUM_MI {" + str(len(xdma_ddr_ch_list) + len(slr_list)) + "} \\\n")
            #for i in range(len(xdma_ddr_ch_list)+len(slr_list)):
            #    f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_DATA_FIFO {0}\\\n")
            #    f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_REGSLICE {4}\\\n")
            #f_d.write("\tCONFIG.S00_HAS_DATA_FIFO {0} \\\n")
            #f_d.write("\tCONFIG.S00_HAS_REGSLICE {4} \\\n")
            #f_d.write("\t] $XDMA_M_AXI_INC_0 \n\n")

            # SLR_TO_DDR_SMC Instance
            for i in range (len(slr_list)) :
                for j in range(len(slr_ddr_ch_list[i])) :
                    f_d.write("set SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 " + "SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0 ] \n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                    f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                    f_d.write("\tCONFIG.NUM_SI {1} \n")
                    f_d.write("\t] $SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0 \n\n")

                    if((int(slr_list[i]) == 0 and int(slr_ddr_ch_list[i][j]) == 0) or (int(slr_list[i]) == 2 and int(slr_ddr_ch_list[i][j]) == 1)) :
                        f_d.write("set SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_1 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 " + "SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_1 ] \n")
                        f_d.write("set_property -dict [ list \\\n")
                        f_d.write("\tCONFIG.NUM_CLKS {1} \\\n")
                        f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                        f_d.write("\tCONFIG.NUM_SI {1} \n")
                        f_d.write("\t] $SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_1 \n\n")



            # XDMA_TO_DDR_SMC_0
            #for j in range(len(xdma_ddr_ch_list)) :
            #    f_d.write("set XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 ] \n")
            #    f_d.write("set_property -dict [ list \\\n")
            #    f_d.write("\tCONFIG.HAS_ARESETN {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
            #    f_d.write("\tCONFIG.NUM_MI {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_SI {1} \n")
            #    f_d.write("\t] $XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 \n\n")

            # XDMA_TO_HOST_SMC_0
            #for i in range(len(slr_list)) :
            #    f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 ] \n")
            #    f_d.write("set_property -dict [ list \\\n")
            #    f_d.write("\tCONFIG.HAS_ARESETN {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
            #    f_d.write("\tCONFIG.NUM_MI {1} \\\n")
            #    f_d.write("\tCONFIG.NUM_SI {1} \n")
            #    f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 \n\n")

            # Interface Connection
            #f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI [get_bd_intf_ports XDMA_M_AXI] [get_bd_intf_pins XDMA_M_AXI_INC_0/S00_AXI] \n")
            #for i in range(len(xdma_ddr_ch_list)):
            #    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_S_AXI [get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_SMC_0/M00_AXI] [get_bd_intf_ports XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_S_AXI] \n")

            # XDMA to SLR Host
            #for i in range(len(slr_list)) :
            #    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0_M00_AXI [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/M00_AXI]"
            #    + " [get_bd_intf_ports SLR" + slr_list[i] + "_HOST_S_AXI] \n")

            # XDMA INC to DDR_SMC and HOST_SMC
            #for i in range (len(xdma_ddr_ch_list) + len(slr_list)) :
            #    f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI_INC_0_M{:02d}".format(i) + "_AXI "
            #    + "[get_bd_intf_pins XDMA_M_AXI_INC_0/M{:02d}".format(i) + "_AXI] ")
#
            #    # TO DDR_SMC
            #    if(i < len(xdma_ddr_ch_list)) :
            #        f_d.write("[get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] +"_SMC_0/S00_AXI] \n")
#
            #    # TO HOST_SMC
            #    else :
            #        f_d.write("[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)] +"_HOST_SMC_0/S00_AXI] \n")

            # SLR DMA TO DDR FIRST
            for i in range(len(slr_list)) : 
                for j in range(int(ddr_dma_list[i])) :
                    f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI [get_bd_intf_ports SLR" + slr_list[i] + "_DDR_DMA{:02d}".format(j) + "_M_AXI] "
                    + "[get_bd_intf_pins SLR" + slr_list[i]  + "_DMA_INC_0/S{:02d}".format(j) +"_AXI] \n")

                for j in range(len(slr_ddr_ch_list[i])) :
                    f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_DMA_INC_0_M{:02d}".format(j) + "_M_AXI [get_bd_intf_pins SLR" + slr_list[i] + "_DMA_INC_0/M{:02d}".format(j) + "_AXI] "
                    + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0/S00_AXI] \n")

                    if((int(slr_list[i]) == 0 and int(slr_ddr_ch_list[i][j]) == 0) or (int(slr_list[i]) == 2 and int(slr_ddr_ch_list[i][j]) == 1)) :
                        f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j]  + "_SMC_0_M00_AXI"
                        + " [get_bd_intf_pins SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0/M00_AXI] "
                        + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j]  + "_SMC_1/S00_AXI] \n")
###########
###########
###########
###########``
            # SLR DMA TO DDR SECOND
            for i in range(len(slr_list)) :
                for j in range (len(slr_ddr_ch_list[i])) :
                    if((int(slr_list[i]) == 0 and int(slr_ddr_ch_list[i][j]) == 0) or (int(slr_list[i]) == 2 and int(slr_ddr_ch_list[i][j]) == 1)) :
                        f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] +"_S_AXI " 
                        + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_1/M00_AXI] "
                        + "[get_bd_intf_ports SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI] \n")

                    else :
                        f_d.write("connect_bd_intf_net -intf_net SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] +"_S_AXI " 
                        + "[get_bd_intf_pins SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0/M00_AXI] "
                        + "[get_bd_intf_ports SLR" + slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI] \n")

            f_d.write("\n")

            # Interface Connection Done

            # CLK, RESETN Port Conection 
            # DDR_CLK, RESETN CONNECT
            for j in range (len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[j] == 'true'):
                    f_d.write("connect_bd_net -net DDR" + str(j) +"_CLK [get_bd_ports DDR" + str(j) + "_CLK] ")
                    #for i in range(len(xdma_ddr_ch_list)):
                    #    if(int(xdma_ddr_ch_list[i]) == j) :
                    #        f_d.write("[get_bd_pins XDMA_TO_DDR"+ str(j) + "_SMC_0/aclk1] ")

                    for i in range(len(slr_ddr_ch_list)) :
                        for k in range(len(slr_ddr_ch_list[i])):
                            if(int(slr_ddr_ch_list[i][k]) == j) :
                                f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_DDR" + str(j) + "_SMC_0/aclk1] ")
                                if((int(slr_list[i]) == 0 and j == 0) or (int(slr_list[i]) == 2 and j == 1)) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_DDR" + str(j) + "_SMC_1/aclk] ")
    
                    f_d.write("\n")
                    f_d.write("connect_bd_net -net DDR" + str(j) +"_CLK_RESETN [get_bd_ports DDR" + str(j) + "_CLK_RESETN] ")
                    for i in range(len(slr_ddr_ch_list)) :
                        for k in range(len(slr_ddr_ch_list[i])) :
                            if(int(slr_ddr_ch_list[i][k]) == j) :
                                if((int(slr_list[i]) == 0 and j == 0) or (int(slr_list[i]) == 2 and j == 1)) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] +"_TO_DDR" + str(j) + "_SMC_1/aresetn] ")
    
                    f_d.write("\n")


            # SLR_CLK, SLR_RESETN
            for i in range (len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK [get_bd_ports SLR" + slr_list[i] + "_CLK] ")
                #f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk1] ")
                
                if(len(slr_ddr_ch_list[i]) != 0):
                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/ACLK] ")
                    for j in range(len(slr_ddr_ch_list[i])):
                        f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/M{:02d}".format(j) +"_ACLK] ")

                    for j in range (int(ddr_dma_list[i])) :
                        f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/S{:02d}".format(j) + "_ACLK] ")

                    for j in range(len(slr_ddr_ch_list[i])) : # Num of DDR
                        f_d.write("[get_bd_pins SLR" + slr_list[i] +"_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0/aclk] ")

                f_d.write("\n")

                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK_RESETN [get_bd_ports SLR" + slr_list[i] + "_CLK_RESETN] ")
                
                if(len(slr_ddr_ch_list[i]) != 0):
                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/ARESETN] ")
                    for j in range(len(slr_ddr_ch_list[i])):
                        f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/M{:02d}".format(j) +"_ARESETN] ")

                    for j in range (int(ddr_dma_list[i])) :
                        f_d.write("[get_bd_pins SLR" + slr_list[i] + "_DMA_INC_0/S{:02d}".format(j) +  "_ARESETN] ")
 
                    for j in range(len(slr_ddr_ch_list[i])) : # Num of DDR
                        f_d.write("[get_bd_pins SLR" + slr_list[i] +"_TO_DDR" + slr_ddr_ch_list[i][j] + "_SMC_0/aresetn] ")

                f_d.write("\n")

            # XDMA_CLK
            #f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] ")
            #f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/ACLK] ")
            #f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/S00_ACLK] ")
            #for i in range(len(xdma_ddr_ch_list) + len(slr_list)):
            #    f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/M{:02d}".format(i) + "_ACLK] ")
            #
            #for i in xdma_ddr_ch_list:
            #    f_d.write("[get_bd_pins XDMA_TO_DDR" + i + "_SMC_0/aclk] ")
            #    
            #for i in range (len(slr_list)) :
            #    f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk] ")
            #f_d.write("\n")

            # XDMA CLK RESETN Necessary
            #f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] ")
            #f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/ARESETN] ")
            #f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/S00_ARESETN] ")
            #for i in range(len(xdma_ddr_ch_list) + len(slr_list)):
            #    f_d.write("[get_bd_pins XDMA_M_AXI_INC_0/M{:02d}".format(i) + "_ARESETN] ")
            #
            #for i in xdma_ddr_ch_list:
            #    f_d.write("[get_bd_pins XDMA_TO_DDR" + i + "_SMC_0/aresetn] ")
            #    
            #for i in range (len(slr_list)) :
            #    f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aresetn] ")
            #f_d.write("\n")


            f_d.write("\n")
            # CLK, RESETN Port Conection Done

            # ADDRESS Assign
            #for j in range(len(xdma_ddr_ch_list)) :
            #    f_d.write("assign_bd_address -offset " + str(hex(8*int(xdma_ddr_ch_list[j]))) + "0000000 -range 0x80000000 -target_address_space "
            #    + "[get_bd_addr_spaces XDMA_M_AXI] "
            #    + "[get_bd_addr_segs XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI/Reg] -force" + "\n")


            for i in range(len(slr_ddr_ch_list)) :
                for j in range (len(slr_ddr_ch_list[i])) : # DDR Num
                    f_d.write("assign_bd_address -offset " + str(hex(8*int(slr_ddr_ch_list[i][j]))) + "0000000 -range 0x80000000 ")
                    f_d.write("[get_bd_addr_segs SLR"+ slr_list[i] + "_TO_DDR" + slr_ddr_ch_list[i][j] + "_S_AXI/Reg]" + "\n")

            #for i in range(len(slr_list)):
            #    f_d.write("assign_bd_address -offset " + str(hex(1+int(slr_list[i]))) + "00000000 -range 0x100000000 -target_address_space "
            #    + "[get_bd_addr_spaces XDMA_M_AXI] "
            #    + "[get_bd_addr_segs SLR" + slr_list[i] + "_HOST_S_AXI/Reg] -force" + "\n")
        # End of VCU118 Generation
#######################################
#######################################
#######################################
#######################################
        elif(board == 'U50'):
            for i in range(len(hbm_slr_list)):
                hbm_slr_freq = ''
                for j in range (len(slr_list)) :
                    if(hbm_slr_list[i] == slr_list[j]) :
                        hbm_slr_freq = slr_freq_list[j]

                if(hbm_slr_freq == '') :
                    print("[ERROR] no matching hbm_slr in slr_list")
                    return

                for j in range(int(hbm_dma_list[i])):
                    if(int(hbm_port_list[i]) < 10) :
                        if(j < 10) :
                            f_d.write("set SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 "
                            + "SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI ] \n")
                    
                        else :
                            f_d.write("set SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 "
                            + "SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI ] \n")
                    else :
                        if(j < 10) :
                            f_d.write("set SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 "
                            + "SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI ] \n")
                    
                        else :
                            f_d.write("set SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 "
                            + "SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI ] \n")

                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                    #f_d.write("\tCONFIG.ARUER_WIDTH {0} \\\n")
                    #f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
                    #f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {" + hbm_dma_width_list[i] + "} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {"+ hbm_slr_freq + "000000} \\\n")
                    f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_BURST {1} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {1} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {1} \\\n")
                    f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
                    f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
                    f_d.write("\tCONFIG.ID_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {1} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
                    f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
                    f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
                    f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {1} \\\n")
                    f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
                    f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
                    f_d.write("\t] $")
                    if(int(hbm_port_list[i]) < 10) :
                        if(j < 10) :
                            f_d.write("SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI \n")
                    
                        else :
                            f_d.write("SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI \n")
                    else :
                        if(j < 10) :
                            f_d.write("SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI \n")
                    
                        else :
                            f_d.write("SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI \n")
                    f_d.write("\n")

                if(int(hbm_port_list[i]) < 10) : 
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI "
                    + "[ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI ] \n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {33} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {256} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {" + str(hbm_clk_freq) + "000000} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {16} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI3} \\\n")
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI \n\n")

                else : 
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI "
                    + "[ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI ] \n")
                    f_d.write("set_property -dict [ list \\\n")
                    f_d.write("\tCONFIG.ADDR_WIDTH {33} \\\n")
                    f_d.write("\tCONFIG.DATA_WIDTH {256} \\\n")
                    f_d.write("\tCONFIG.FREQ_HZ {" + str(hbm_clk_freq) + "000000} \\\n")
                    f_d.write("\tCONFIG.HAS_CACHE {0} \\\n")
                    f_d.write("\tCONFIG.HAS_LOCK {0} \\\n")
                    f_d.write("\tCONFIG.HAS_PROT {0} \\\n")
                    f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
                    f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                    f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {16} \\\n")
                    f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
                    f_d.write("\tCONFIG.PROTOCOL {AXI3} \\\n")
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI \n\n")
            # End of SLR hbm list intf port generation
            # Start of CLK, RESETN Ports
            f_d.write("set HBM_CLK [ create_bd_port -dir I -type clk -freq_hz " + str(hbm_clk_freq) + "000000 HBM_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {HBM_CLK_RESETN} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
            flag = 0
            for i in range (len(hbm_slr_list)) :
                if(flag == 0):
                    flag = 1
                else : 
                    f_d.write(":")
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI")
                else :
                    f_d.write("SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI")
            f_d.write("} \\\n")
            f_d.write("\t] $HBM_CLK \n\n")
            f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir I -type rst HBM_CLK_RESETN ] \n\n")
            for i in range(len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] +"_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000 SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n" )
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                flag = 0
                for j in range(len(hbm_slr_list)) :
                    if(hbm_slr_list[j] == slr_list[i]) :
                        if(flag == 0):
                            flag = 1
                        else:
                            f_d.write(":")
                        for k in range(int(hbm_dma_list[j])):
                            if(int(hbm_port_list[j]) < 10) :
                                if(k < 10) :
                                    f_d.write("SLR" + slr_list[i] + "_HBM0" + hbm_port_list[j] + "_DMA0" + str(k) + "_M_AXI")
                                else :
                                    f_d.write("SLR" + slr_list[i] + "_HBM0" + hbm_port_list[j] + "_DMA" + str(k) + "_M_AXI")
                            else : 
                                if(k < 10) :
                                    f_d.write("SLR" + slr_list[i] + "_HBM" + hbm_port_list[j] + "_DMA0" + str(k) + "_M_AXI")
                                else :
                                    f_d.write("SLR" + slr_list[i] + "_HBM" + hbm_port_list[j] + "_DMA" + str(k) + "_M_AXI")
                f_d.write("} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n" )
                f_d.write("set SLR" + slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]\n\n")
            # End of CLK, RESETN Ports
            # Start of INC Instance
            for i in range(len(hbm_slr_list)) :
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 SLR"
                    + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0 ] \n")
    
                else :
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 SLR"
                    + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0 ] \n")
    
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.M00_HAS_DATA_FIFO {0} \\\n")
                f_d.write("\tCONFIG.M00_HAS_REGSLICE {4} \\\n")
                f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                f_d.write("\tCONFIG.NUM_SI {" + hbm_dma_list[i] + "} \\\n")
                for j in range (int(hbm_dma_list[i])) :
                    if(j < 10) :
                        f_d.write("\tCONFIG.S0" + str(j) +"_HAS_DATA_FIFO {0} \\\n")
                        f_d.write("\tCONFIG.S0" + str(j) +"_HAS_REGSLICE {4} \\\n")
                    else :
                        f_d.write("\tCONFIG.S" + str(j) +"_HAS_DATA_FIFO {0} \\\n")
                        f_d.write("\tCONFIG.S" + str(j) +"_HAS_REGSLICE {4} \\\n")
    
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0 \n\n")
    
                else :
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0 \n\n")
    
            # End of INC Instance
    
            # Start of SMC Instacne
            for i in range(len(hbm_slr_list)) :
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0 " 
                    + "[ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0 ] \n")
                
                else :
                    f_d.write("set SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0 " 
                    + "[ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0 \n")
                
                else :
                    f_d.write("\t] $SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0 \n")
                f_d.write("\n")
            # End of SMC Instacne
    
            # Start of Interface Connections
            for i in range(len(hbm_slr_list)) :
                if(int(hbm_port_list[i]) < 10) :
                    for j in range(int(hbm_dma_list[i])) :
                        if(j < 10) :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI] ")
                            f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0/S0" + str(j) + "_AXI] \n")
    
                        else :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI] ")
                            f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0/S" + str(j) + "_AXI] \n")
                    
                    f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0_M00_AXI ")
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_INC_0/M00_AXI] ")
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0/S00_AXI] \n")
                    
                    f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI ")
                    f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI] " )
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0/M00_AXI] \n")
    
                else :
                    for j in range(int(hbm_dma_list[i])):
                        if(j < 10) :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i]  + "_DMA0" + str(j) + "_M_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI] ")
                            f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0/S0" + str(j) + "_AXI] \n")
                        else :
                            f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI ")
                            f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI] ")
                            f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0/S" + str(j) + "_AXI] \n")
    
                    f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0_M00_AXI ")
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_INC_0/M00_AXI] ")
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0/S00_AXI] \n")
    
                    f_d.write("connect_bd_intf_net -intf_net SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI ")
                    f_d.write("[get_bd_intf_ports SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI] " )
                    f_d.write("[get_bd_intf_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0/M00_AXI] \n")
            f_d.write("\n")
    
            # End of Interface Connections
    
            # Start of Port Connections
            f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] ")
            for i in range(len(hbm_slr_list)) :
                if(int(hbm_port_list[i]) < 10) :
                    f_d.write("[get_bd_pins SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_SMC_0/aclk1] ")
                else :
                    f_d.write("[get_bd_pins SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_SMC_0/aclk1] ")
            f_d.write("\n")
            for i in range(len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk1] ")
                for j in range(len(hbm_slr_list)):
                    if(slr_list[i] == hbm_slr_list[j]) :
                        if(int(hbm_port_list[j]) < 10) :
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/ACLK] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/M00_ACLK] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_SMC_0/aclk] ")
                        
                        else :
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/ACLK] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/M00_ACLK] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_SMC_0/aclk] ")
    
                        for k in range(int(hbm_dma_list[j])):
                            if(int(hbm_port_list[j]) < 10) :
                                if(k < 10) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/S0" + str(k) +"_ACLK] ")
                                    
                                else :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/S" + str(k) +"_ACLK] ")
    
                            else :
                                if(k < 10) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/S0" + str(k) +"_ACLK] ")
    
                                else :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/S" + str(k) +"_ACLK] ")
                f_d.write("\n")
    
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK_RESETN ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK_RESETN] ")
                for j in range(len(hbm_slr_list)):
                    if(slr_list[i] == hbm_slr_list[j]) :
                        if(int(hbm_port_list[j]) < 10) :
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/ARESETN] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/M00_ARESETN] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_SMC_0/aresetn] ")
                        
                        else :
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/ARESETN] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/M00_ARESETN] ")
                            f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_SMC_0/aresetn] ")
    
                        for k in range(int(hbm_dma_list[j])):
                            if(int(hbm_port_list[j]) < 10) :
                                if(k < 10) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/S0" + str(k) +"_ARESETN] ")
                                    
                                else :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM0" + hbm_port_list[j] + "_INC_0/S" + str(k) +"_ARESETN] ")
    
                            else :
                                if(k < 10) :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/S0" + str(k) +"_ARESETN] ")
    
                                else :
                                    f_d.write("[get_bd_pins SLR" + slr_list[i] + "_TO_HBM" + hbm_port_list[j] + "_INC_0/S" + str(k) +"_ARESETN] ")
                f_d.write("\n")
            f_d.write("\n")
                
            # End of Port Connections
    
            # Start of Address Creation
            for i in range(len(hbm_slr_list)) :
                for j in range(int(hbm_dma_list[i])) :
                    f_d.write("assign_bd_address -offset 0x00000000 -range 0x000200000000 -target_address_space ")
                    if(int(hbm_port_list[i]) < 10) :
                        if (j < 10):
                            f_d.write("[get_bd_addr_spaces SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI] ")
                        else :
                            f_d.write("[get_bd_addr_spaces SLR" + hbm_slr_list[i] + "_HBM0" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI] ")
                        
                        f_d.write("[get_bd_addr_segs SLR" + hbm_slr_list[i] + "_TO_HBM0" + hbm_port_list[i] + "_S_AXI/Reg] -force \n")
                    else :
                        if(j < 10) :
                            f_d.write("[get_bd_addr_spaces SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA0" + str(j) + "_M_AXI] ")
                        
                        else :
                            f_d.write("[get_bd_addr_spaces SLR" + hbm_slr_list[i] + "_HBM" + hbm_port_list[i] + "_DMA" + str(j) + "_M_AXI] ")
    
                        f_d.write("[get_bd_addr_segs SLR" + hbm_slr_list[i] + "_TO_HBM" + hbm_port_list[i] + "_S_AXI/Reg] -force \n")
            # End of Address Creation
            #if(hbm_slr_list != None):
            #    f_d.write("# DFX Design Flow\n")
            #    f_d.write("group_bd_cells hier [get_bd_cells [list SLR*]]\n")
            #    f_d.write("validate_bd_design\n")
            #    f_d.write("startgroup\n")
            #    f_d.write("set curdesign [current_bd_design]\n")
            #    f_d.write("create_bd_design -cell [get_bd_cells /hier] " + board + "_AXI_INC_container\n")
            #    f_d.write("current_bd_design $curdesign\n")
            #    f_d.write("set new_cell [create_bd_cell -type container -reference " + board + "_AXI_INC_container hier_temp]\n")
            #    f_d.write("replace_bd_cell [get_bd_cells /hier] $new_cell\n")
            #    f_d.write("delete_bd_objs  [get_bd_cells /hier]\n")
            #    f_d.write("set_property name hier $new_cell\n")
            #    f_d.write("endgroup\n")
            #    f_d.write("current_bd_design [get_bd_designs " + board + "_AXI_INC_container]\n")
            #    f_d.write("update_compile_order -fileset sources_1\n")
            #    f_d.write("current_bd_design [get_bd_designs " + board + "_AXI_INC]\n")
            #    f_d.write("set_property -dict [list CONFIG.ENABLE_DFX {true}] [get_bd_cells hier]\n")
        # End of U50 Generation
    # End of wrting file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)
def main():
    board = 'VCU118'
    refdir = '../Reference'
    filedir = "../../shell/"+ board +"/bd"
    slr_list = ['0','1','2']
    slr_freq_list = ['300','300','300']
    host_width_list = ['256','256','256']
    xdma_ddr_ch_list = None
    ddr_slr_list = None
    ddr_ch_list = None
    ddr_dma_list = ['0','0','0']
    ddr_dma_width_list = ['512','512','512']
    xdma_hbm_port = '0'
    hbm_slr_list = ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1', '0','1', '0','1']
    hbm_port_list = ['0','0','1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12','13','13','14','14','15','15','16','16','17','17','18','18','19','19','20','20','21','21','22','22','23','23','24','24','25','25','26','26','27','27','28','28','29','29', '30', '30', '31', '31']
    hbm_dma_list = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
    hbm_dma_width_list = ['256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256','256']

    AXI_INC_Tcl(filedir, refdir, board, slr_list, slr_freq_list, host_width_list,xdma_ddr_ch_list, ddr_slr_list, ddr_ch_list,
    ddr_dma_list, ddr_dma_width_list, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, xdma_hbm_port, 450)

if __name__ == "__main__":
    main()