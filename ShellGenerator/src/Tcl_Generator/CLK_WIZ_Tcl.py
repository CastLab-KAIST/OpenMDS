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

def CLK_WIZ_Tcl(filedir, refdir, board, slr_freq_list, hbm_clk_freq):
    # Copy and Open Reference Tcl File
    gen_tcl = os.path.join(filedir, board + "_CLK_WIZ.tcl")
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_0.tcl")
    shutil.copy(ref_tcl, gen_tcl)

    search_name = 'DESIGN_BOARD_NAME'
    replace_name = board + "_CLK_WIZ"

    for line in fileinput.input(gen_tcl, inplace=True):
        if search_name in line:
            line = line.replace(search_name, replace_name)
        sys.stdout.write(line)

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

            f_d.write("set user_si570_clock [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:diff_clock_rtl:1.0 user_si570_clock ]\n")
            f_d.write("\tset_property -dict [ list \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {156250000} \\\n")
            f_d.write("\t] $user_si570_clock\n\n")

            # Create Ports
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {CLK_WIZ_S_AXI_LITE} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ]\n\n")

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

            # Create CLK WIZ, Processor System Reset
            f_d.write("set REF_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 REF_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLK_IN1_BOARD_INTERFACE {user_si570_clock} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {Differential_clock_capable_pin} \\\n")
            f_d.write("\tCONFIG.USE_BOARD_FLOW {true} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $REF_CLK_WIZ\n")

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

            #Create interface connections
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M00_AXI [get_bd_intf_pins CLK_WIZ_INC/M00_AXI] [get_bd_intf_pins SLR0_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M01_AXI [get_bd_intf_pins CLK_WIZ_INC/M01_AXI] [get_bd_intf_pins SLR1_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_INC_M02_AXI [get_bd_intf_pins CLK_WIZ_INC/M02_AXI] [get_bd_intf_pins SLR2_CLK_WIZ/s_axi_lite]\n")
            f_d.write("connect_bd_intf_net -intf_net CLK_WIZ_S_AXI_LITE [get_bd_intf_ports CLK_WIZ_S_AXI_LITE] [get_bd_intf_pins CLK_WIZ_INC/S00_AXI]\n")
            f_d.write("connect_bd_intf_net -intf_net user_si570_clock [get_bd_intf_ports user_si570_clock] [get_bd_intf_pins REF_CLK_WIZ/CLK_IN1_D]\n")

            #Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] [get_bd_pins CLK_WIZ_INC/ARESETN] ")
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ARESETN] [get_bd_pins CLK_WIZ_INC/M01_ARESETN] [get_bd_pins CLK_WIZ_INC/M02_ARESETN] [get_bd_pins CLK_WIZ_INC/S00_ARESETN] ")
            f_d.write("[get_bd_pins SLR0_CLK_RESET/ext_reset_in] [get_bd_pins SLR0_CLK_WIZ/s_axi_aresetn] ")
            f_d.write("[get_bd_pins SLR1_CLK_RESET/ext_reset_in] [get_bd_pins SLR1_CLK_WIZ/s_axi_aresetn] ")
            f_d.write("[get_bd_pins SLR2_CLK_RESET/ext_reset_in] [get_bd_pins SLR2_CLK_WIZ/s_axi_aresetn]\n")
            f_d.write("connect_bd_net -net SLR0_CLK [get_bd_ports SLR0_CLK] [get_bd_pins SLR0_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR0_CLK_WIZ/SLR0_CLK]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_RESETN [get_bd_ports SLR0_CLK_RESETN] [get_bd_pins SLR0_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_WIZ_locked [get_bd_pins SLR0_CLK_RESET/dcm_locked] [get_bd_pins SLR0_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR1_CLK [get_bd_ports SLR1_CLK] [get_bd_pins SLR1_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR1_CLK_WIZ/SLR1_CLK]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_RESETN [get_bd_ports SLR1_CLK_RESETN] [get_bd_pins SLR1_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_WIZ_locked [get_bd_pins SLR1_CLK_RESET/dcm_locked] [get_bd_pins SLR1_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR2_CLK [get_bd_ports SLR2_CLK] [get_bd_pins SLR2_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR2_CLK_WIZ/SLR2_CLK]\n")
            f_d.write("connect_bd_net -net SLR2_CLK_RESETN [get_bd_ports SLR2_CLK_RESETN] [get_bd_pins SLR2_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR2_CLK_WIZ_locked [get_bd_pins SLR2_CLK_RESET/dcm_locked] [get_bd_pins SLR2_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] [get_bd_pins CLK_WIZ_INC/ACLK] [get_bd_pins CLK_WIZ_INC/M00_ACLK] [get_bd_pins CLK_WIZ_INC/M01_ACLK] [get_bd_pins CLK_WIZ_INC/M02_ACLK] [get_bd_pins CLK_WIZ_INC/S00_ACLK] [get_bd_pins SLR0_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR1_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR2_CLK_WIZ/s_axi_aclk]\n")
            f_d.write("connect_bd_net -net REF_CLK [get_bd_pins REF_CLK_WIZ/clk_out1] [get_bd_pins SLR0_CLK_WIZ/clk_in1] [get_bd_pins SLR1_CLK_WIZ/clk_in1] [get_bd_pins SLR2_CLK_WIZ/clk_in1]\n")

            #Create address Segments
            f_d.write("assign_bd_address -offset 0x00001000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR0_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00002000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR1_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00003000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR2_CLK_WIZ/s_axi_lite/Reg] -force\n")

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

            f_d.write("set cmc_clk [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:diff_clock_rtl:1.0 cmc_clk ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {100000000} \\\n")
            f_d.write("\t] $cmc_clk\n\n")

            f_d.write("set hbm_clk [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:diff_clock_rtl:1.0 hbm_clk ]\n\n")

            # Create Ports
            f_d.write("set XDMA_CLK [ create_bd_port -dir I -type clk -freq_hz 250000000 XDMA_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_BUSIF {CLK_WIZ_S_AXI_LITE} \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {XDMA_CLK_RESETN} \\\n")
            f_d.write("\t] $XDMA_CLK\n")
            f_d.write("set XDMA_CLK_RESETN [ create_bd_port -dir I -type rst XDMA_CLK_RESETN ]\n\n")


            f_d.write("set HBM_CLK [ create_bd_port -dir O -type clk HBM_CLK ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.ASSOCIATED_RESET {HBM_CLK_RESETN} \\\n")
            f_d.write("\tCONFIG.FREQ_HZ {" + hbm_clk_freq + "000000} \\\n")
            f_d.write("\t] $HBM_CLK\n")

            f_d.write("set HBM_CLK_RESETN [ create_bd_port -dir O -type rst HBM_CLK_RESETN ]\n\n")

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

            # Create CLK WIZ, Processor System Reset
            f_d.write("set CMC_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 CMC_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_JITTER {115.831} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_PHASE_ERROR {87.180} \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_IN1_BOARD_INTERFACE {cmc_clk} \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.MMCM_CLKOUT1_DIVIDE {12} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {2} \\\n")
            f_d.write("\tCONFIG.USE_BOARD_FLOW {true} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $CMC_CLK_WIZ\n\n")

            f_d.write("set HBM_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 HBM_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLKOUT1_DRIVES {No_buffer} \\\n")
            f_d.write("\tCONFIG.CLKOUT1_REQUESTED_OUT_FREQ {" + hbm_clk_freq + "} \\\n")
            f_d.write("\tCONFIG.FEEDBACK_SOURCE {FDBK_ONCHIP} \\\n")
            f_d.write("\tCONFIG.OVERRIDE_MMCM {false} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {No_buffer} \\\n")
            f_d.write("\tCONFIG.USE_DYN_RECONFIG {true} \\\n")
            f_d.write("\t] $HBM_CLK_WIZ\n\n")
            f_d.write("set HBM_CLK_RESET [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 HBM_CLK_RESET ]\n\n")

            f_d.write("set HBM_REF_CLK_WIZ [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:6.0 HBM_REF_CLK_WIZ ]\n")
            f_d.write("set_property -dict [ list \\\n")
            f_d.write("\tCONFIG.CLKOUT2_USED {true} \\\n")
            f_d.write("\tCONFIG.CLK_IN1_BOARD_INTERFACE {hbm_clk} \\\n")
            f_d.write("\tCONFIG.CLK_OUT1_PORT {HBM_REF_CLK0} \\\n")
            f_d.write("\tCONFIG.CLK_OUT2_PORT {HBM_REF_CLK1} \\\n")
            f_d.write("\tCONFIG.NUM_OUT_CLKS {2} \\\n")
            f_d.write("\tCONFIG.PRIM_SOURCE {Differential_clock_capable_pin} \\\n")
            f_d.write("\tCONFIG.USE_LOCKED {false} \\\n")
            f_d.write("\tCONFIG.USE_RESET {false} \\\n")
            f_d.write("\t] $HBM_REF_CLK_WIZ\n\n")
            
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
            f_d.write("connect_bd_intf_net -intf_net cmc_clk [get_bd_intf_ports cmc_clk] [get_bd_intf_pins CMC_CLK_WIZ/CLK_IN1_D]\n")
            f_d.write("connect_bd_intf_net -intf_net hbm_clk [get_bd_intf_ports hbm_clk] [get_bd_intf_pins HBM_REF_CLK_WIZ/CLK_IN1_D]\n")
            # Create Port Connections
            f_d.write("connect_bd_net -net XDMA_CLK [get_bd_ports XDMA_CLK] [get_bd_pins CLK_WIZ_INC/ACLK] [get_bd_pins CLK_WIZ_INC/S00_ACLK] ") 
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ACLK] [get_bd_pins CLK_WIZ_INC/M01_ACLK] [get_bd_pins CLK_WIZ_INC/M02_ACLK] ")
            f_d.write("[get_bd_pins HBM_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR0_CLK_WIZ/s_axi_aclk] [get_bd_pins SLR1_CLK_WIZ/s_axi_aclk] \n")
            f_d.write("connect_bd_net -net XDMA_CLK_RESETN [get_bd_ports XDMA_CLK_RESETN] [get_bd_pins CLK_WIZ_INC/ARESETN] [get_bd_pins CLK_WIZ_INC/S00_ARESETN] ")
            f_d.write("[get_bd_pins CLK_WIZ_INC/M00_ARESETN] [get_bd_pins CLK_WIZ_INC/M01_ARESETN] [get_bd_pins CLK_WIZ_INC/M02_ARESETN] ")
            f_d.write("[get_bd_pins HBM_CLK_RESET/ext_reset_in] [get_bd_pins SLR0_CLK_RESET/ext_reset_in] [get_bd_pins SLR1_CLK_RESET/ext_reset_in] ")
            f_d.write("[get_bd_pins HBM_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR0_CLK_WIZ/s_axi_aresetn] [get_bd_pins SLR1_CLK_WIZ/s_axi_aresetn] \n")
            f_d.write("connect_bd_net -net CMC_CLK_WIZ_clk_out1 [get_bd_pins CMC_CLK_WIZ/clk_out1] [get_bd_pins SLR0_CLK_WIZ/clk_in1]\n")
            f_d.write("connect_bd_net -net CMC_CLK_WIZ_clk_out2 [get_bd_pins CMC_CLK_WIZ/clk_out2] [get_bd_pins SLR1_CLK_WIZ/clk_in1]\n")
            f_d.write("connect_bd_net -net HBM_CLK [get_bd_ports HBM_CLK] [get_bd_pins HBM_CLK_RESET/slowest_sync_clk] [get_bd_pins HBM_CLK_WIZ/clk_out1]\n")
            f_d.write("connect_bd_net -net HBM_CLK_RESETN [get_bd_ports HBM_CLK_RESETN] [get_bd_pins HBM_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_HBM_REF_CLK0 [get_bd_ports HBM_REF_CLK0] [get_bd_pins HBM_CLK_WIZ/clk_in1] [get_bd_pins HBM_REF_CLK_WIZ/HBM_REF_CLK0]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_HBM_REF_CLK1 [get_bd_ports HBM_REF_CLK1] [get_bd_pins HBM_REF_CLK_WIZ/HBM_REF_CLK1]\n")
            f_d.write("connect_bd_net -net HBM_CLK_WIZ_locked [get_bd_pins HBM_CLK_RESET/dcm_locked] [get_bd_pins HBM_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_RESETN [get_bd_ports SLR0_CLK_RESETN] [get_bd_pins SLR0_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR0_CLK [get_bd_ports SLR0_CLK] [get_bd_pins SLR0_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR0_CLK_WIZ/SLR0_CLK]\n")
            f_d.write("connect_bd_net -net SLR0_CLK_WIZ_locked [get_bd_pins SLR0_CLK_RESET/dcm_locked] [get_bd_pins SLR0_CLK_WIZ/locked]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_RESETN [get_bd_ports SLR1_CLK_RESETN] [get_bd_pins SLR1_CLK_RESET/peripheral_aresetn]\n")
            f_d.write("connect_bd_net -net SLR1_CLK [get_bd_ports SLR1_CLK] [get_bd_pins SLR1_CLK_RESET/slowest_sync_clk] [get_bd_pins SLR1_CLK_WIZ/SLR1_CLK]\n")
            f_d.write("connect_bd_net -net SLR1_CLK_WIZ_locked [get_bd_pins SLR1_CLK_RESET/dcm_locked] [get_bd_pins SLR1_CLK_WIZ/locked]\n")

            #Create Address Segments
            f_d.write("assign_bd_address -offset 0x00000000 -range 0x00002000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs HBM_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00002000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR0_CLK_WIZ/s_axi_lite/Reg] -force\n")
            f_d.write("assign_bd_address -offset 0x00003000 -range 0x00001000 -target_address_space [get_bd_addr_spaces CLK_WIZ_S_AXI_LITE] [get_bd_addr_segs SLR1_CLK_WIZ/s_axi_lite/Reg] -force\n")
        # End of U50
    # End of file descriptor
    ref_tcl = os.path.join(refdir, "Tcl_Necessary_1.tcl")
    with open(gen_tcl, 'a') as f_d, open(ref_tcl, 'r') as f_r:
        for line in f_r:
            f_d.write(line)

def main():
    filedir = '../../shell/VCU118/bd'
    refdir = '../Reference'
    board = 'VCU118'
    slr_freq_list=['300','300', '300']
    hbm_clk_freq = '450'
    CLK_WIZ_Tcl(filedir, refdir, board, slr_freq_list, hbm_clk_freq)

if __name__ == "__main__":
    main()