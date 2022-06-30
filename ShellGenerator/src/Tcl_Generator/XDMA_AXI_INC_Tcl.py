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
def XDMA_AXI_INC_Tcl(filedir, refdir, board, slr_list, slr_freq_list, host_width_list=None, xdma_ddr_ch_list=None, ddr_slr_list=None, ddr_ch_list=None ,ddr_dma_list=None, ddr_dma_width_list=None, 
                hbm_slr_list=None, hbm_port_list=None, hbm_dma_list=None, hbm_dma_width_list=None, xdma_hbm_port=None, hbm_clk_freq=None, vivado_version="2020.2"):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_XDMA_AXI_INC.tcl")
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_0.tcl")

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

    else :
        print("[ERROR] Do Not Support " + board)
        return os.exit()
        

    

    if(ddr_ch_list != None):
        for i in range(len(slr_list)):
            for j in range(len(ddr_ch_list)):
                if(slr_list[i] == ddr_slr_list[j]):
                    slr_ddr_ch_list[i].append(ddr_ch_list[j])

    if(xdma_ddr_ch_list != None):
        for i in range(len(xdma_ddr_ch_list)):
            total_ddr_ch_list[int(xdma_ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(xdma_ddr_ch_list[i])].append('XDMA')
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(ddr_ch_list[i])].append(ddr_slr_list[i])

    if(xdma_ddr_ch_list == None):
        xdma_ddr_ch_list = []
    

    shutil.copy(ref_tcl, gen_tcl)
    # Change Tcl Name
    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_XDMA_AXI_INC"
    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    with open(gen_tcl, 'a') as f_d:
        # Port Instance
        if(board == 'VCU118'):
            # Crate XDMA intf ports
            f_d.write("set XDMA_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_M_AXI ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
            f_d.write("\tCONFIG.ID_WIDTH {4} \\\n")
            f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {32} \\\n")
            f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
            f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
            f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
            f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {0} \\\n")
            f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
            f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
            f_d.write("\t] $XDMA_M_AXI \n\n")

            # SLR Host Interface Instance
            for i in range(len(slr_list)):
                f_d.write("set SLR" + slr_list[i] + "_HOST_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + slr_list[i] + "_HOST_S_AXI ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {" + host_width_list[i] + "} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + slr_freq_list[i] + "} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_HOST_S_AXI\n\n")

            # DDR Interface Instance
            for j in range(len(xdma_ddr_ch_list)) :
                f_d.write("set XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI ] \n")
                f_d.write("set_property -dict [ list \\"+ "\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {300000000} \\\n")
                f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
                f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {4} \\\n")
                f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {4} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI4}" + "\n")
                f_d.write("\t] $XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_S_AXI \n\n")

            # CLK PORT INSTANCE
            # XDMA_CLK Port INSTANCE
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ] \n")
            f_d.write("set_property -dict [list \\\n")
            f_d.write("CONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \n")
            f_d.write("] $XDMA_CLK \n\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ] \n\n")
            # DDR_CLK Port INSTANCE
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] == 'true'):
                    for j in range(len(ddr_ch_intf_list[i])):
                        if(ddr_ch_intf_list[i][j] == 'XDMA'):
                            f_d.write("set DDR{:01d}".format(i) + "_CLK  [ create_bd_port -dir I -type clk -freq_hz 300000000 DDR{:01d}".format(i) + "_CLK ] \n")
                            f_d.write("set_property -dict [list \\\n")
                            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                            f_d.write(ddr_ch_intf_list[i][j] + "_TO_DDR{:01d}".format(i) + "_S_AXI")
                    f_d.write("} \\\n")
                    f_d.write("\tCONFIG.ASSOCIATED_RESET {" + "DDR{:01d}".format(i) + "_CLK_RESETN} \n")
                    f_d.write("\t] $DDR{:01d}".format(i) + "_CLK \n\n")

                    f_d.write("set DDR{:01d}".format(i) + "_CLK_RESETN [ create_bd_port -dir I -type rst DDR{:01d}".format(i) + "_CLK_RESETN ] \n\n")

            # SLR_CLK, SLR_RESETN
            for i in range(len(slr_list)) : 
                f_d.write("set SLR" + slr_list[i] + "_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000" + " SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {")
                f_d.write("SLR" + slr_list[i] + "_HOST_S_AXI")

                f_d.write("} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n")
                f_d.write("set SLR"+ slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]" + "\n\n")
            # Port Instacne is Done

            # INC, SMC Instance
            # XDMA_INC
            f_d.write("set XDMA_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 XDMA_INC_0 ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.NUM_MI {" + str(len(slr_list) + len(xdma_ddr_ch_list)) + "} \\\n")
            for i in range(len(slr_list) + len(xdma_ddr_ch_list)):
                f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_DATA_FIFO {0}\\\n")
                f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_REGSLICE {4}\\\n")

            f_d.write("\tCONFIG.S00_HAS_DATA_FIFO {0} \\\n")
            f_d.write("\tCONFIG.S00_HAS_REGSLICE {4} \\\n")
            f_d.write("\t] $XDMA_INC_0 \n\n")

            #XDMA_TO_SLR SMC
            for i in range(len(slr_list)) :
                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 \n\n")
                
                if(int(slr_list[i]) != 1):
                    num_slr_crossing = 1
                
                elif(int(slr_list[i]) == 1):
                    num_slr_crossing = 0


                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_register_slice:2.1 " + "XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.REG_AR {15} \\\n")
                f_d.write("\tCONFIG.REG_AW {15} \\\n")
                f_d.write("\tCONFIG.REG_B {15} \\\n")
                f_d.write("\tCONFIG.REG_R {15} \\\n")
                f_d.write("\tCONFIG.REG_W {15} \\\n")
                f_d.write("\tCONFIG.NUM_SLR_CROSSINGS {" + str(num_slr_crossing) + "} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AW {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AR {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_W {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_R {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_B {1} \\\n")
                if(num_slr_crossing == 1):
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_AW {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_AR {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_W {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_R {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_B {1} \\\n")
                #f_d.write("\tCONFIG.USE_AUTOPIPELINING {1} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 \n\n")


            # XDMA_TO_DDR SMC
            for j in range(len(xdma_ddr_ch_list)) :
                f_d.write("set XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.HAS_ARESETN {1} \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\tCONFIG.NUM_MI {1} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \n")
                f_d.write("\t] $XDMA_TO_DDR" + xdma_ddr_ch_list[j] + "_SMC_0 \n\n")

                f_d.write("set XDMA_TO_DDR{:01d}".format(int(xdma_ddr_ch_list[j])) + "_REG_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_register_slice:2.1 " + "XDMA_TO_DDR{:01d}".format(int(xdma_ddr_ch_list[j])) + "_REG_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.REG_AR {15} \\\n")
                f_d.write("\tCONFIG.REG_AW {15} \\\n")
                f_d.write("\tCONFIG.REG_B {15} \\\n")
                f_d.write("\tCONFIG.REG_R {15} \\\n")
                f_d.write("\tCONFIG.REG_W {15} \\\n")
                f_d.write("\tCONFIG.NUM_SLR_CROSSINGS {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AW {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AR {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_W {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_R {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_B {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_AW {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_AR {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_W {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_R {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_B {1} \\\n")
                f_d.write("\t] $XDMA_TO_DDR{:01d}".format(int(xdma_ddr_ch_list[j])) + "_REG_0 \n\n")
            # End of INC and SMC Instance
            
            # Interface Connection 
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI [get_bd_intf_ports XDMA_M_AXI] [get_bd_intf_pins XDMA_INC_0/S00_AXI] \n")
            for i in range(len(xdma_ddr_ch_list)):
                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_SMC_M00_AXI [get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_SMC_0/M00_AXI] [get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_REG_0/S_AXI] \n")
                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_S_AXI [get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_REG_0/M_AXI] [get_bd_intf_ports XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_S_AXI] \n")

            # XDMA to SLR Host
            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0_M00_AXI [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/M00_AXI]"
                + " [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/S_AXI] \n")

                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_SLR" + slr_list[i] + "_HOST_S_AXI [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/M_AXI]"
                + " [get_bd_intf_ports SLR" + slr_list[i] + "_HOST_S_AXI] \n")

            # XDMA INC to DDR_SMC and HOST_SMC            
            for i in range (len(xdma_ddr_ch_list) + len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net XDMA_INC_0_M{:02d}".format(i) + "_AXI "
                + "[get_bd_intf_pins XDMA_INC_0/M{:02d}".format(i) + "_AXI] ")

                # TO DDR_SMC
                if(i < len(xdma_ddr_ch_list)) :
                    f_d.write("[get_bd_intf_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i] +"_SMC_0/S00_AXI] \n")

                # TO HOST_SMC
                else :
                    f_d.write("[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)] +"_HOST_SMC_0/S00_AXI] \n")
            f_d.write("\n")
            # End of Interface Connections

            # Start of Port Connections
            # DDR_CLK, DDR_RESETN
            for j in range (len(total_ddr_ch_list)) :
                if(total_ddr_ch_list[j] == 'true'):
                    f_d.write("connect_bd_net -net DDR" + str(j) +"_CLK [get_bd_ports DDR" + str(j) + "_CLK] ")
                    for i in range(len(xdma_ddr_ch_list)):
                        if(int(xdma_ddr_ch_list[i]) == j) :
                            f_d.write("[get_bd_pins XDMA_TO_DDR"+ str(j) + "_SMC_0/aclk1] ")
                            f_d.write("[get_bd_pins XDMA_TO_DDR"+ str(j) + "_REG_0/aclk] ")
                    f_d.write("\n")
    
                    f_d.write("connect_bd_net -net DDR" + str(j) +"_CLK_RESETN [get_bd_ports DDR" + str(j) + "_CLK_RESETN] ")
                    f_d.write("[get_bd_pins XDMA_TO_DDR" + str(j) + "_REG_0/aresetn] ")
    
                    f_d.write("\n")

            # XDMA_CLK, XDMA_RESETN
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] ")
            f_d.write("[get_bd_pins XDMA_INC_0/ACLK] ")
            f_d.write("[get_bd_pins XDMA_INC_0/S00_ACLK] ")
            if(xdma_hbm_port != None):
                for i in range(1 + len(slr_list) + len(xdma_ddr_ch_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ACLK] ")
                    if(i == 0) :
                        if(int(xdma_hbm_port) < 10) :
                            f_d.write("[get_bd_pins XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0/aclk] ")
        
                        else :
                            f_d.write("[get_bd_pins XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0/aclk] ")
                    elif(i < 1 + len(xdma_ddr_ch_list)):
                        f_d.write("[get_bd_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i-1] + "_SMC_0/aclk] ")
    
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)-1] + "_HOST_SMC_0/aclk] ")
            else :
                for i in range(len(slr_list) + len(xdma_ddr_ch_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ACLK] ")
                    
                    if(i < len(xdma_ddr_ch_list)):
                        f_d.write("[get_bd_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i-1] + "_SMC_0/aclk] ")
    
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)] + "_HOST_SMC_0/aclk] ")
            f_d.write("\n")
    
            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] ")
            f_d.write("[get_bd_pins XDMA_INC_0/ARESETN] ")
            f_d.write("[get_bd_pins XDMA_INC_0/S00_ARESETN] ")
            if(xdma_hbm_port != None):
                for i in range(1 + len(slr_list) + len(xdma_ddr_ch_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ARESETN] ")
                    if(i == 0) :
                        if(int(xdma_hbm_port) < 10) :
                            f_d.write("[get_bd_pins XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0/aresetn] ")

                        else :
                            f_d.write("[get_bd_pins XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0/aresetn] ")

                    elif(i < 1 + len(xdma_ddr_ch_list)):
                        f_d.write("[get_bd_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i-1] + "_SMC_0/aresetn] ")
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)-1] + "_HOST_SMC_0/aresetn] ")
            else :
                for i in range(len(slr_list) + len(xdma_ddr_ch_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ARESETN] ")

                    if(i < len(xdma_ddr_ch_list)):
                        f_d.write("[get_bd_pins XDMA_TO_DDR" + xdma_ddr_ch_list[i-1] + "_SMC_0/aresetn] ")
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-len(xdma_ddr_ch_list)] + "_HOST_SMC_0/aresetn] ")
            f_d.write("\n")
            
            # SLR_CLK, SLR_CLK_RESETN
            for i in range(len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk1] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/aclk] ")
                f_d.write("\n")
    
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK_RESETN ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK_RESETN] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/aresetn] ")
                f_d.write("\n")
            f_d.write("\n")
            # End of Port Connections
    
            # Start of Address Creation
            for i in range(len(slr_list) +len(xdma_ddr_ch_list)):
                if(i < len(slr_list)):
                    f_d.write("assign_bd_address -offset 0x000" + slr_list[i] + "00000000 -range 0x000100000000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI] ")
                    f_d.write("[get_bd_addr_segs SLR" + slr_list[i] + "_HOST_S_AXI/Reg] -force \n")
    
                elif(i < len(slr_list) + len(xdma_ddr_ch_list)):
                    f_d.write("assign_bd_address -offset 0x0010"+ str(8*+int(xdma_ddr_ch_list[i-len(slr_list)])) +"0000000 -range 0x000080000000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI] ")
                    f_d.write("[get_bd_addr_segs XDMA_TO_DDR" + xdma_ddr_ch_list[i-len(slr_list)] + "_S_AXI/Reg] -force \n")
        # End of VCU118 Generation
#######################################
#######################################
#######################################
#######################################
        elif(board == 'U50'):
            for i in range(len(slr_list)):
                f_d.write("set SLR" + slr_list[i] + "_HOST_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 SLR" + slr_list[i] + "_HOST_S_AXI ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
                f_d.write("\tCONFIG.DATA_WIDTH {" + host_width_list[i] + "} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + slr_freq_list[i] + "} \\\n")
                f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_HOST_S_AXI\n\n")

            # Crate XDMA intf ports
            f_d.write("set XDMA_M_AXI [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_M_AXI ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {64} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {512} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
            f_d.write("\tCONFIG.HAS_BRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_BURST {0} \\\n")
            f_d.write("\tCONFIG.HAS_CACHE {1} \\\n")
            f_d.write("\tCONFIG.HAS_LOCK {1} \\\n")
            f_d.write("\tCONFIG.HAS_PROT {1} \\\n")
            f_d.write("\tCONFIG.HAS_QOS {0} \\\n")
            f_d.write("\tCONFIG.HAS_REGION {0} \\\n")
            f_d.write("\tCONFIG.HAS_RRESP {1} \\\n")
            f_d.write("\tCONFIG.HAS_WSTRB {1} \\\n")
            f_d.write("\tCONFIG.ID_WIDTH {4} \\\n")
            f_d.write("\tCONFIG.MAX_BURST_LENGTH {256} \\\n")
            f_d.write("\tCONFIG.NUM_READ_OUTSTANDING {32} \\\n")
            f_d.write("\tCONFIG.NUM_READ_THREADS {1} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_OUTSTANDING {16} \\\n")
            f_d.write("\tCONFIG.NUM_WRITE_THREADS {1} \\\n")
            f_d.write("\tCONFIG.PROTOCOL {AXI4} \\\n")
            f_d.write("\tCONFIG.READ_WRITE_MODE {READ_WRITE} \\\n")
            f_d.write("\tCONFIG.RUSER_BITS_PER_BYTE {0} \\\n")
            f_d.write("\tCONFIG.RUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.SUPPORTS_NARROW_BURST {0} \\\n")
            f_d.write("\tCONFIG.WUSER_BITS_PER_BYTE {0} \\\n")
            f_d.write("\tCONFIG.WUSER_WIDTH {0} \\\n")
            f_d.write("\t] $XDMA_M_AXI \n\n")

            if(xdma_hbm_port.isdecimal()):
                if(int(xdma_hbm_port) < 10) :
                    f_d.write("set XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI ]\n")
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
                    f_d.write("\t] $XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI \n\n")
                else :
                    f_d.write("set XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:aximm_rtl:1.0 XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI ]\n")
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
                    f_d.write("\t] $XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI \n\n")
            # End of XDMA intf Ports
            # Start of CLK, RESETN Ports
            f_d.write("set HBM_CLK [ create_bd_port -dir I -type clk -freq_hz " + str(hbm_clk_freq) + "000000 HBM_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {HBM_CLK_RESETN} \\\n")
            if(xdma_hbm_port.isdecimal()):
                if(int(xdma_hbm_port) < 10) :
                    f_d.write("\tCONFIG.ASSOCIATED_BUSIF {XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI")
                else :
                    f_d.write("\tCONFIG.ASSOCIATED_BUSIF {XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI")
            f_d.write("} \\\n")
            f_d.write("\t] $HBM_CLK \n\n")
            f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir I -type rst HBM_CLK_RESETN ] \n\n")
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {XDMA_M_AXI} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK \n\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ]\n\n")
            for i in range(len(slr_list)) :
                f_d.write("set SLR" + slr_list[i] +"_CLK [ create_bd_port -dir I -type clk -freq_hz " + slr_freq_list[i] + "000000 SLR" + slr_list[i] + "_CLK ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + slr_list[i] + "_CLK_RESETN} \\\n" )
                f_d.write("\tCONFIG.ASSOCIATED_BUSIF {SLR" + slr_list[i] + "_HOST_S_AXI")
                f_d.write("} \\\n")
                f_d.write("\t] $SLR" + slr_list[i] + "_CLK \n\n" )
                f_d.write("set SLR" + slr_list[i] + "_CLK_RESETN [ create_bd_port -dir I -type rst SLR" + slr_list[i] + "_CLK_RESETN ]\n\n")
            # End of CLK, RESETN Ports
            # Start of INC Instance
            f_d.write("set XDMA_INC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 XDMA_INC_0 ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.NUM_MI {" + str(1 + len(slr_list)) + "} \\\n")
            for i in range(1+len(slr_list)):
                f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_DATA_FIFO {0}\\\n")
                f_d.write("\tCONFIG.M{:02d}".format(i) + "_HAS_REGSLICE {4}\\\n")
            f_d.write("\tCONFIG.S00_HAS_DATA_FIFO {0} \\\n")
            f_d.write("\tCONFIG.S00_HAS_REGSLICE {4} \\\n")
            f_d.write("\t] $XDMA_INC_0 \n\n")
            # End of INC Instance
    
            # Start of SMC Instacne
            if(int(xdma_hbm_port) < 10) :
                f_d.write("set XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_HBM0" + xdma_hbm_port+ "_SMC_0 ]\n")
    
            else :
                f_d.write("set XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_HBM" + xdma_hbm_port+ "_SMC_0 ]\n")
    
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
            f_d.write("\tCONFIG.NUM_SI {1} \\\n")
        
            if(xdma_hbm_port != None):
                if(int(xdma_hbm_port) < 10) :
                    f_d.write("\t] $XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0 \n\n")

                else :
                    f_d.write("\t] $XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0 \n\n")

                f_d.write("set XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_register_slice:2.1 " + "XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.REG_AR {15} \\\n")
                f_d.write("\tCONFIG.REG_AW {15} \\\n")
                f_d.write("\tCONFIG.REG_B {15} \\\n")
                f_d.write("\tCONFIG.REG_R {15} \\\n")
                f_d.write("\tCONFIG.REG_W {15} \\\n")
                f_d.write("\tCONFIG.NUM_SLR_CROSSINGS {1} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AW {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AR {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_W {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_R {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_B {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_AW {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_AR {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_W {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_R {2} \\\n")
                f_d.write("\tCONFIG.PIPELINES_SLAVE_B {2} \\\n")
                f_d.write("\t] $XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0 \n\n")
            
            for i in range(len(slr_list)) :
                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:smartconnect:1.0 XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.NUM_CLKS {2} \\\n")
                f_d.write("\tCONFIG.NUM_SI {1} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0 \n\n")
                
                num_slr_crossing = 1 - int(slr_list[i])
                f_d.write("set XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_register_slice:2.1 " + "XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 ] \n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.REG_AR {15} \\\n")
                f_d.write("\tCONFIG.REG_AW {15} \\\n")
                f_d.write("\tCONFIG.REG_B {15} \\\n")
                f_d.write("\tCONFIG.REG_R {15} \\\n")
                f_d.write("\tCONFIG.REG_W {15} \\\n")
                f_d.write("\tCONFIG.NUM_SLR_CROSSINGS {" + str(num_slr_crossing) + "} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AW {0} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_AR {0} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_W {0} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_R {0} \\\n")
                f_d.write("\tCONFIG.PIPELINES_MASTER_B {0} \\\n")
                if(num_slr_crossing == 1):
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_AW {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_AR {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_W {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_R {1} \\\n")
                    f_d.write("\tCONFIG.PIPELINES_SLAVE_B {1} \\\n")
                f_d.write("\t] $XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0 \n\n")
    
            # End of SMC Instacne

            # Start of Interface Connections
            # XDMA Connection 
            f_d.write("connect_bd_intf_net -intf_net XDMA_M_AXI [get_bd_intf_ports XDMA_M_AXI] [get_bd_intf_pins XDMA_INC_0/S00_AXI] \n")
            # XDMA to SLR Host
            for i in range(len(slr_list)) :
                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0_M00_AXI [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/M00_AXI]"
                + " [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/S_AXI] \n")

                f_d.write("connect_bd_intf_net -intf_net XDMA_TO_SLR" + slr_list[i] + "_HOST_S_AXI [get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/M_AXI]"
                + " [get_bd_intf_ports SLR" + slr_list[i] + "_HOST_S_AXI] \n")
            # XDMA to HBM 
            if(xdma_hbm_port !=None):
                for i in range (len(slr_list) + 1) :
                    f_d.write("connect_bd_intf_net -intf_net XDMA_INC_0_M{:02d}".format(i) + "_AXI "
                    + "[get_bd_intf_pins XDMA_INC_0/M{:02d}".format(i) + "_AXI] ")

                    # TO HOST_SMC
                    if (i == 0):
                        f_d.write("[get_bd_intf_pins XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_SMC_0/S00_AXI] \n")
                    else:
                        f_d.write("[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i-1] +"_HOST_SMC_0/S00_AXI] \n")
                        

                if(int(xdma_hbm_port) < 10) :
                    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_M00_AXI ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0/M00_AXI] ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM0" + xdma_hbm_port + "_REG_0/S_AXI] \n")

                    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI ")
                    f_d.write("[get_bd_intf_ports XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM0" + xdma_hbm_port + "_REG_0/M_AXI] \n")
                else :
                    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM" + xdma_hbm_port + "_SMC_M00_AXI ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0/M00_AXI] ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM" + xdma_hbm_port + "_REG_0/S_AXI] \n")

                    f_d.write("connect_bd_intf_net -intf_net XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI ")
                    f_d.write("[get_bd_intf_ports XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI] ")
                    f_d.write("[get_bd_intf_pins XDMA_TO_HBM" + xdma_hbm_port + "_REG_0/M_AXI] \n")
            else:
                for i in range (len(slr_list)) :
                    f_d.write("connect_bd_intf_net -intf_net XDMA_INC_0_M{:02d}".format(i) + "_AXI "
                    + "[get_bd_intf_pins XDMA_INC_0/M{:02d}".format(i) + "_AXI] ")
    
                    f_d.write("[get_bd_intf_pins XDMA_TO_SLR" + slr_list[i] +"_HOST_SMC_0/S00_AXI] \n")
            f_d.write("\n")
            # End of Interface Connections
    
            # Start of Port Connections
            f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] ")
            if(xdma_hbm_port != None):
                f_d.write("[get_bd_pins XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_SMC_0/aclk1] ")
                f_d.write("[get_bd_pins XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0/aclk] ")

                f_d.write("\n")
    
            f_d.write("connect_bd_net -net HBM_CLK_RESETN [get_bd_ports HBM_CLK_RESETN] ")
            if(xdma_hbm_port != None):
                f_d.write("[get_bd_pins XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0/aresetn] ")
                f_d.write("\n")


            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] ")
            f_d.write("[get_bd_pins XDMA_INC_0/ACLK] ")
            f_d.write("[get_bd_pins XDMA_INC_0/S00_ACLK] ")

            if(xdma_hbm_port != None):
                for i in range(1 + len(slr_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ACLK] ")
                    if(i == 0) :
                        if(int(xdma_hbm_port) < 10) :
                            f_d.write("[get_bd_pins XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0/aclk] ")

                        else :
                            f_d.write("[get_bd_pins XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0/aclk] ")
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-1] + "_HOST_SMC_0/aclk] ")
                f_d.write("\n")
    
            elif(xdma_hbm_port == None):
                for i in range(len(slr_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ACLK] ")
                    f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk] ")
                f_d.write("\n")


            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] ")
            f_d.write("[get_bd_pins XDMA_INC_0/ARESETN] ")
            f_d.write("[get_bd_pins XDMA_INC_0/S00_ARESETN] ")
            
            if(xdma_hbm_port != None):
                for i in range(1 + len(slr_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ARESETN] ")
                    if(i == 0) :
                        if(int(xdma_hbm_port) < 10) :
                            f_d.write("[get_bd_pins XDMA_TO_HBM0" + xdma_hbm_port + "_SMC_0/aresetn] ")

                        else :
                            f_d.write("[get_bd_pins XDMA_TO_HBM" + xdma_hbm_port + "_SMC_0/aresetn] ")
                    else :
                        f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i-1] + "_HOST_SMC_0/aresetn] ")
                f_d.write("\n")

            elif(xdma_hbm_port == None):
                for i in range(len(slr_list)) :
                    f_d.write("[get_bd_pins XDMA_INC_0/M0" + str(i) + "_ARESETN] ")
                    f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aresetn] ")
                f_d.write("\n")
            
            for i in range(len(slr_list)) :
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0/aclk1] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/aclk] ")
                f_d.write("\n")
    
                f_d.write("connect_bd_net -net SLR" + slr_list[i] + "_CLK_RESETN ")
                f_d.write("[get_bd_ports SLR" + slr_list[i] + "_CLK_RESETN] ")
                f_d.write("[get_bd_pins XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/aresetn] ")
                f_d.write("\n")
            f_d.write("\n")
                
            # End of Port Connections
    
            # Start of Address Creation
    
            for i in range(1+len(slr_list)):
                if(i == 0) :
                    f_d.write("assign_bd_address -offset 0x10_00000000 -range 0x000200000000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI] ")
                    if(int(xdma_hbm_port) < 10) :
                        f_d.write("[get_bd_addr_segs XDMA_TO_HBM0" + xdma_hbm_port + "_S_AXI/Reg] -force \n")
    
                    else :
                        f_d.write("[get_bd_addr_segs XDMA_TO_HBM" + xdma_hbm_port + "_S_AXI/Reg] -force \n")
    
                else :
                    f_d.write("assign_bd_address -offset 0x000" + str(int(slr_list[i-1])) + "00000000 -range 0x0001_0000_0000 -target_address_space [get_bd_addr_spaces XDMA_M_AXI] ")
                    f_d.write("[get_bd_addr_segs SLR" + slr_list[i-1] + "_HOST_S_AXI/Reg] -force \n")

            # End of Address Creation
        # End of U50 Generation
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
    # End of wrting file descriptor
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_1.tcl")
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