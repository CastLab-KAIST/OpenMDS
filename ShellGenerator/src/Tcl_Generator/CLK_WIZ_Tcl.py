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

def CLK_WIZ_Tcl(filedir, refdir, board, slr_freq_list, hbm_clk_freq, vivado_version):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_CLK_WIZ.tcl")
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)

    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_CLK_WIZ"

    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

    if(hbm_clk_freq == None):
       hbm_clk_temp_freq = '450'
    
    else :
       hbm_clk_temp_freq = hbm_clk_freq
        

    with open(gen_tcl, 'a') as f_d:
        if(board == 'VCU118'):
            # Create Interface Ports
            f_d.write("set CLK_WIZ_S_AXI_LITE [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 CLK_WIZ_S_AXI_LITE ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {16} \\\n")
            f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
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
            f_d.write("\t] $CLK_WIZ_S_AXI_LITE\n\n")

            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {CLK_WIZ_S_AXI_LITE} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ]\n\n")


            #f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir O -type rst HBM_CLK_RESETN ]\n\n")

            for i in range(len(slr_freq_list)):
                f_d.write("set SLR"+ str(i) + "_CLK_RESETN [ create_bd_port -dir O -type rst SLR" + str(i) +"_CLK_RESETN ]\n\n" )
                f_d.write("set SLR" + str(i) +"_CLK [ create_bd_port -dir O -type clk SLR" + str(i) + "_CLK ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + str(i) + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + slr_freq_list[i] + "000000} \\\n")
                f_d.write("\t] $SLR" + str(i) + "_CLK\n")

            # Create Interconnect
            f_d.write("set CLK_WIZ_INC [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 CLK_WIZ_INC ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.M00_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.M01_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.M02_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.NUM_MI {3} \\\n")
            f_d.write("\tCONFIG.S00_HAS_REGSLICE {4} \\\n")
            f_d.write("\t] $CLK_WIZ_INC\n\n")

            # Create REF_CLK_WIZ
            f_d.write("set USER_REF_CLK_WIZ_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 USER_REF_CLK_WIZ_0 ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLKOUT3_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_OUT1_PORT {user_ref_clk0} \\\n")
            f_d.write("\tCONFIG.CLK_OUT2_PORT {user_ref_clk1} \\\n")
            f_d.write("\tCONFIG.CLK_OUT3_PORT {user_ref_clk2} \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT3_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {3} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $USER_REF_CLK_WIZ_0\n\n")

            # Create HBM_CLK_WIZ, Processor System Reset

            for i in range(len(slr_freq_list)):
                f_d.write("set SLR" + str(i) + "_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 SLR" + str(i) + "_CLK_WIZ ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
                f_d.write("\tCONFIG.CLKOUT1_REQUESTED_OUT_FREQ {" + slr_freq_list[i] + "} \\\n")
                f_d.write("\tCONFIG.CLK_OUT1_PORT {SLR" + str(i) + "_CLK} \\\n")
                f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
                f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
                f_d.write("\tCONFIG.USE_DYN_RECONFIG {true} \\\n")
                f_d.write("\t] $SLR" + str(i) + "_CLK_WIZ\n")
                f_d.write("set SLR" + str(i) + "_CLK_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 SLR" + str(i) + "_CLK_RESET ]\n\n")

            # Create interface connections
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_S_AXI_LITE [get_bd_intf_ports CLK_WIZ_S_AXI_LITE] [get_bd_intf_pins CLK_WIZ_INC/S00_AXI]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M00_AXI [get_bd_intf_pins CLK_WIZ_INC/M00_AXI] [get_bd_intf_pins SLR0_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M01_AXI [get_bd_intf_pins CLK_WIZ_INC/M01_AXI] [get_bd_intf_pins SLR1_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M02_AXI [get_bd_intf_pins CLK_WIZ_INC/M02_AXI] [get_bd_intf_pins SLR2_CLK_WIZ/s_axi_lite]\n")
            # Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] [get_bd_pins CLK_WIZ_INC/ACLK] [get_bd_pins CLK_WIZ_INC/S00_ACLK] [get_bd_pins USER_REF_CLK_WIZ_0/clk_in1] ") 
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ACLK] [get_bd_pins CLK_WIZ_INC/M01_ACLK] [get_bd_pins CLK_WIZ_INC/M02_ACLK] ")
            f_d.write("[get_bd_pins SLR0_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR1_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR2_CLK_WIZ/s_axi_aclk]\n")
            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] [get_bd_pins CLK_WIZ_INC/ARESETN] [get_bd_pins CLK_WIZ_INC/S00_ARESETN] ")
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ARESETN] [get_bd_pins CLK_WIZ_INC/M01_ARESETN] [get_bd_pins CLK_WIZ_INC/M02_ARESETN] [get_bd_pins CLK_WIZ_INC/M03_ARESETN] ")
            f_d.write("[get_bd_pins SLR0_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR1_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR2_CLK_WIZ/s_axi_aresetn] ")
            f_d.write("[get_bd_pins SLR0_CLK_RESET/ext_reset_in] [get_bd_pins SLR1_CLK_RESET/ext_reset_in] [get_bd_pins SLR2_CLK_RESET/ext_reset_in] \n")
            
            f_d.write("connect_bd_net -net user_ref_clk0 [get_bd_pins USER_REF_CLK_WIZ_0/user_ref_clk0] [get_bd_pins SLR0_CLK_WIZ/clk_in1]\n ")
            f_d.write("connect_bd_net -net user_ref_clk1 [get_bd_pins USER_REF_CLK_WIZ_0/user_ref_clk1] [get_bd_pins SLR1_CLK_WIZ/clk_in1]\n ")
            f_d.write("connect_bd_net -net user_ref_clk2 [get_bd_pins USER_REF_CLK_WIZ_0/user_ref_clk2] [get_bd_pins SLR2_CLK_WIZ/clk_in1]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_RESETN [get_bd_ports SLR0_CLK_RESETN] [get_bd_pins SLR0_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR0_CLK [get_bd_ports SLR0_CLK] [get_bd_pins SLR0_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR0_CLK_WIZ/SLR0_CLK]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_WIZ_locked [get_bd_pins SLR0_CLK_RESET/dcm_locked] [get_bd_pins SLR0_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_RESETN [get_bd_ports SLR1_CLK_RESETN] [get_bd_pins SLR1_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR1_CLK [get_bd_ports SLR1_CLK] [get_bd_pins SLR1_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR1_CLK_WIZ/SLR1_CLK]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_WIZ_locked [get_bd_pins SLR1_CLK_RESET/dcm_locked] [get_bd_pins SLR1_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR2_CLK_RESETN [get_bd_ports SLR2_CLK_RESETN] [get_bd_pins SLR2_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR2_CLK [get_bd_ports SLR2_CLK] [get_bd_pins SLR2_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR2_CLK_WIZ/SLR2_CLK]\n")
            f_d.write("connect_bd_net -net SLR2_CLK_WIZ_locked [get_bd_pins SLR2_CLK_RESET/dcm_locked] [get_bd_pins SLR2_CLK_WIZ/locked]\n")

            #Create Address Segments
            f_d.write("assign_bd_address -offset 0x00000000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR0_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00001000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR1_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00002000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR2_CLK_WIZ/s_axi_lite/Reg] -force\n")
        # End of VCU118
        elif(board == 'U50'):
            # Create Interface Ports
            f_d.write("set CLK_WIZ_S_AXI_LITE [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:aximm_rtl:1.0 CLK_WIZ_S_AXI_LITE ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ADDR_WIDTH {16} \\\n")
            f_d.write("\tCONFIG.ARUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.AWUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.BUSER_WIDTH {0} \\\n")
            f_d.write("\tCONFIG.DATA_WIDTH {32} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {250000000} \\\n")
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
            f_d.write("\t] $CLK_WIZ_S_AXI_LITE\n\n")

            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {CLK_WIZ_S_AXI_LITE} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ]\n\n")


            #f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir O -type rst HBM_CLK_RESETN ]\n\n")
            f_d.write("set HBM_CLK_SLR0_RESETN [ create_bd_port -dir O -type rst HBM_CLK_SLR0_RESETN ]\n\n")
            f_d.write("set HBM_CLK_SLR1_RESETN [ create_bd_port -dir O -type rst HBM_CLK_SLR1_RESETN ]\n\n")

            f_d.write("set HBM_CLK [ create_bd_port -dir O -type clk HBM_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {HBM_CLK_SLR0_RESETN:HBM_CLK_SLR1_RESETN} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {" + hbm_clk_temp_freq + "000000} \\\n")
            f_d.write("\t] $HBM_CLK\n")

            f_d.write("set HBM_REF_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 HBM_REF_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_OUT1_PORT {HBM_REF_CLK0} \\\n")
            f_d.write("\tCONFIG.CLK_OUT2_PORT {HBM_REF_CLK1} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {2} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $HBM_REF_CLK_WIZ\n\n")

            f_d.write("set HBM_REF_CLK0 [ create_bd_port -dir O -type clk HBM_REF_CLK0 ]\n")
            f_d.write("set HBM_REF_CLK1 [ create_bd_port -dir O -type clk HBM_REF_CLK1 ]\n")
            f_d.write("\n")

            for i in range(len(slr_freq_list)):
                f_d.write("set SLR"+ str(i) + "_CLK_RESETN [ create_bd_port -dir O -type rst SLR" + str(i) +"_CLK_RESETN ]\n\n" )
                f_d.write("set SLR" + str(i) +"_CLK [ create_bd_port -dir O -type clk SLR" + str(i) + "_CLK ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.ASSOCIATED_RESET {SLR" + str(i) + "_CLK_RESETN} \\\n")
                f_d.write("\tCONFIG.FREQ_HZ {" + slr_freq_list[i] + "000000} \\\n")
                f_d.write("\t] $SLR" + str(i) + "_CLK\n")

            # Create Interconnect
            f_d.write("set CLK_WIZ_INC [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 CLK_WIZ_INC ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.M00_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.M01_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.M02_HAS_REGSLICE {4} \\\n")
            f_d.write("\tCONFIG.NUM_MI {3} \\\n")
            f_d.write("\tCONFIG.S00_HAS_REGSLICE {4} \\\n")
            f_d.write("\t] $CLK_WIZ_INC\n\n")

            # Create REF_CLK_WIZ
            f_d.write("set USER_REF_CLK_WIZ_0 [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 USER_REF_CLK_WIZ_0 ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_OUT1_PORT {user_ref_clk0} \\\n")
            f_d.write("\tCONFIG.CLK_OUT2_PORT {user_ref_clk1} \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {2} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $USER_REF_CLK_WIZ_0\n\n")

            f_d.write("set USER_REF_CLK_WIZ_1 [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 USER_REF_CLK_WIZ_1 ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_OUT1_PORT {user_ref_clk2} \\\n")
            f_d.write("\tCONFIG.CLK_OUT2_PORT {user_ref_clk3} \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {2} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $USER_REF_CLK_WIZ_1\n\n")

            # Create HBM_CLK_WIZ, Processor System Reset

            f_d.write("set HBM_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 HBM_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT1_REQUESTED_OUT_FREQ {" + hbm_clk_temp_freq + "} \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.OVERRIDE_MMCM {false} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
            f_d.write("\tCONFIG.USE_DYN_RECONFIG {true} \\\n")
            f_d.write("\t] $HBM_CLK_WIZ\n\n")

            f_d.write("set HBM_CLK_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 HBM_CLK_RESET ]\n\n")
            f_d.write("set HBM_CLK_SLR0_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 HBM_CLK_SLR0_RESET ]\n\n")
            f_d.write("set HBM_CLK_SLR1_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 HBM_CLK_SLR1_RESET ]\n\n")
            
            for i in range(len(slr_freq_list)):
                f_d.write("set SLR" + str(i) + "_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 SLR" + str(i) + "_CLK_WIZ ]\n")
                f_d.write("set_property -dict [ list \\\n")
                f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
                f_d.write("\tCONFIG.CLKOUT1_REQUESTED_OUT_FREQ {" + slr_freq_list[i] + "} \\\n")
                f_d.write("\tCONFIG.CLK_OUT1_PORT {SLR" + str(i) + "_CLK} \\\n")
                f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
                f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
                f_d.write("\tCONFIG.USE_DYN_RECONFIG {true} \\\n")
                f_d.write("\t] $SLR" + str(i) + "_CLK_WIZ\n")
                f_d.write("set SLR" + str(i) + "_CLK_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 SLR" + str(i) + "_CLK_RESET ]\n\n")

            # Create interface connections
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_S_AXI_LITE [get_bd_intf_ports CLK_WIZ_S_AXI_LITE] [get_bd_intf_pins CLK_WIZ_INC/S00_AXI]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M00_AXI [get_bd_intf_pins CLK_WIZ_INC/M00_AXI] [get_bd_intf_pins HBM_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M01_AXI [get_bd_intf_pins CLK_WIZ_INC/M01_AXI] [get_bd_intf_pins SLR0_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M02_AXI [get_bd_intf_pins CLK_WIZ_INC/M02_AXI] [get_bd_intf_pins SLR1_CLK_WIZ/s_axi_lite]\n")
            # Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] [get_bd_pins CLK_WIZ_INC/ACLK] [get_bd_pins CLK_WIZ_INC/S00_ACLK] [get_bd_pins USER_REF_CLK_WIZ_0/clk_in1] [get_bd_pins USER_REF_CLK_WIZ_1/clk_in1] ") 
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ACLK] [get_bd_pins CLK_WIZ_INC/M01_ACLK] [get_bd_pins CLK_WIZ_INC/M02_ACLK] ")
            f_d.write("[get_bd_pins HBM_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR0_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR1_CLK_WIZ/s_axi_aclk]\n")
            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] [get_bd_pins CLK_WIZ_INC/ARESETN] [get_bd_pins CLK_WIZ_INC/S00_ARESETN] ")
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ARESETN] [get_bd_pins CLK_WIZ_INC/M01_ARESETN] [get_bd_pins CLK_WIZ_INC/M02_ARESETN] ")
            f_d.write("[get_bd_pins HBM_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR0_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR1_CLK_WIZ/s_axi_aresetn] ")
            f_d.write("[get_bd_pins HBM_CLK_RESET/ext_reset_in] [get_bd_pins SLR0_CLK_RESET/ext_reset_in] [get_bd_pins SLR1_CLK_RESET/ext_reset_in]\n")
            
            f_d.write("connect_bd_net -net user_ref_clk0 [get_bd_pins USER_REF_CLK_WIZ_0/user_ref_clk0] [get_bd_pins SLR0_CLK_WIZ/clk_in1]\n ")
            f_d.write("connect_bd_net -net user_ref_clk1 [get_bd_pins USER_REF_CLK_WIZ_0/user_ref_clk1] [get_bd_pins SLR1_CLK_WIZ/clk_in1]\n ")
            f_d.write("connect_bd_net -net user_ref_clk2 [get_bd_pins USER_REF_CLK_WIZ_1/user_ref_clk2] [get_bd_pins HBM_CLK_WIZ/clk_in1] \n")
            f_d.write("connect_bd_net -net user_ref_clk3 [get_bd_pins USER_REF_CLK_WIZ_1/user_ref_clk3] [get_bd_pins HBM_REF_CLK_WIZ/clk_in1] \n")
            f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] [get_bd_pins HBM_CLK_RESET/slowest_sync_clk] [get_bd_pins HBM_CLK_WIZ/clk_out1] ")
            f_d.write("[get_bd_pins HBM_CLK_SLR0_RESET/slowest_sync_clk] [get_bd_pins HBM_CLK_SLR1_RESET/slowest_sync_clk] [get_bd_pins HBM_CLK_SLR2_RESET/slowest_sync_clk] \n")
            f_d.write("connect_bd_net -net HBM_CLK_RESETN [get_bd_pins HBM_CLK_RESET/peripheral_aresetn] ")
            f_d.write("[get_bd_pins HBM_CLK_SLR0_RESET/ext_reset_in] [get_bd_pins HBM_CLK_SLR1_RESET/ext_reset_in] [get_bd_pins HBM_CLK_SLR2_RESET/ext_reset_in] \n")
            f_d.write("connect_bd_net -net HBM_CLK_SLR0_RESETN [get_bd_ports HBM_CLK_SLR0_RESETN] [get_bd_pins HBM_CLK_SLR0_RESET/interconnect_aresetn]\n")
            f_d.write("connect_bd_net -net HBM_CLK_SLR1_RESETN [get_bd_ports HBM_CLK_SLR1_RESETN] [get_bd_pins HBM_CLK_SLR1_RESET/interconnect_aresetn]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_HBM_REF_CLK0 [get_bd_ports HBM_REF_CLK0] [get_bd_pins HBM_REF_CLK_WIZ/HBM_REF_CLK0]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_HBM_REF_CLK1 [get_bd_ports HBM_REF_CLK1] [get_bd_pins HBM_REF_CLK_WIZ/HBM_REF_CLK1]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_locked [get_bd_pins HBM_CLK_RESET/dcm_locked] [get_bd_pins HBM_CLK_WIZ/locked] ")
            f_d.write("[get_bd_pins HBM_CLK_SLR0_RESET/dcm_locked] [get_bd_pins HBM_CLK_SLR1_RESET/dcm_locked]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_RESETN [get_bd_ports SLR0_CLK_RESETN] [get_bd_pins SLR0_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR0_CLK [get_bd_ports SLR0_CLK] [get_bd_pins SLR0_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR0_CLK_WIZ/SLR0_CLK]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_WIZ_locked [get_bd_pins SLR0_CLK_RESET/dcm_locked] [get_bd_pins SLR0_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_RESETN [get_bd_ports SLR1_CLK_RESETN] [get_bd_pins SLR1_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR1_CLK [get_bd_ports SLR1_CLK] [get_bd_pins SLR1_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR1_CLK_WIZ/SLR1_CLK]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_WIZ_locked [get_bd_pins SLR1_CLK_RESET/dcm_locked] [get_bd_pins SLR1_CLK_WIZ/locked]\n")

            #Create Address Segments
            f_d.write("assign_bd_address -offset 0x00000000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR0_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00001000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR1_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00002000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs HBM_CLK_WIZ/s_axi_lite/Reg] -force\n")
        # End of U50
    # End of file descriptor
    ref_tcl = os.path.join(refdir, vivado_version + "/Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    filedir = '../../shell/VCU118/bd'
    refdir = '../Reference'
    board = 'VCU118'
    slr_freq_list=['300','300', '300']
    hbm_clk_temp_freq = '450'
    CLK_WIZ_Tcl(filedir, refdir, board, slr_freq_list, hbm_clk_temp_freq)

if __name__ == "__main__":
    main()