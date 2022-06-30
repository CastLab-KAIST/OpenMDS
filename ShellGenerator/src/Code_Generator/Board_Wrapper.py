################################################################
# Library
################################################################
import os
from . import Prefix
import pdb
################################################################
# Function
################################################################

''' Board Wrapper SV File Generate'''
def Board_Wrapper(filedir, board, slr_list, slr_phy_list, xdma_ddr_ch=None, ddr_dma_list=None, ddr_slr_list=None, ddr_ch_list=None,
                    xdma_hbm_port=None, hbm_slr_list=None,  hbm_port_list=None,  hbm_dma_list=None):
    # Create  Board Wrapper SV File
    module_name = board + "_Wrapper"
    gen_sv = os.path.join(filedir, module_name + ".sv")

    if(board == 'VCU118'):
        slr_ddr_ch_list = [[]for i in range(len(slr_list))]
        total_ddr_ch_list = ['false' for i in range(2)]
        ddr_ch_intf_list = [[]for i in range(2)]
    
    elif(board == 'U50'):
        total_ddr_ch_list = ['false']
        ddr_ch_intf_list = []

    elif(board =='U250'):
        slr_ddr_ch_list = [[]for i in range(len(slr_list))]
        total_ddr_ch_list = ['false' for i in range(4)]
        ddr_ch_intf_list = [[]for i in range(4)]
        print("Implementing")
        return os.exit()

    elif(board == 'U280'):
        slr_ddr_ch_list = [[]for i in range(len(slr_list))]
        total_ddr_ch_list = ['false' for i in range(2)]
        ddr_ch_intf_list = [[]for i in range(2)]

    if(ddr_ch_list != None):
        for i in range(len(slr_list)):
            for j in range(len(ddr_ch_list)):
                if(slr_list[i] == ddr_slr_list[j]):
                    slr_ddr_ch_list[i].append(ddr_ch_list[j])

    if(xdma_ddr_ch != None):
        for i in range(len(xdma_ddr_ch)):
            total_ddr_ch_list[int(xdma_ddr_ch[i])] = 'true'
            ddr_ch_intf_list[int(xdma_ddr_ch[i])].append('XDMA')
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(ddr_ch_list[i])].append(ddr_slr_list[i])

    total_hbm_port_list = ['false' for i in range(32)]
    hbm_port_intf_list = [[]for i in range(32)]
    if(xdma_hbm_port!=None):
        total_hbm_port_list[int(xdma_hbm_port)] = 'true'
        hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
    if(hbm_port_list!=None):
        for i in range(len(hbm_port_list)) :
            total_hbm_port_list[int(hbm_port_list[i])] = 'true'
            hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])


    with open(gen_sv, 'w') as f:
        # VCU118 Board
        if board == "VCU118":
            ########################################################
            # Write Header
            f.write("import " + board + "_Shell_Params::*;\n\n")
            f.write("`timescale 1 ps / 1 ps\n\n")
            f.write("module " + module_name + "\n")
            f.write("(\n")

            ########################################################
            # Write Board Ports
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, i, port_type=0)
                    for v in range(vcu_ddr_prefix_len):
                        f.write("    {},\n".format(vcu_ddr_prefix[v][1]))
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, i, port_type=1)
                    for v in range(vcu_ddr_prefix_len):
                        f.write("    {},\n".format(vcu_ddr_prefix[v][1]))

            vcu_prefix, vcu_prefix_len = Prefix.get_vcu_prefix()
            for v in range(vcu_prefix_len-1):
                f.write("    {},\n".format(vcu_prefix[v][1]))
            f.write("    {}\n);\n".format(vcu_prefix[v+1][1]))
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, i, port_type=0)
                    for v in range(vcu_ddr_prefix_len):
                        f.write("    {0:6} wire {1:71} {2};\n".format(
                            vcu_ddr_prefix[v][0], vcu_ddr_prefix[v][2], vcu_ddr_prefix[v][1]))
            for i in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[i] != 'false'):
                    vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, i ,port_type=1)
                    for v in range(vcu_ddr_prefix_len):
                        f.write("    {0:6} wire {1:71} {2};\n".format(
                            vcu_ddr_prefix[v][0], vcu_ddr_prefix[v][2], vcu_ddr_prefix[v][1]))

            for v in range(vcu_prefix_len):
                f.write("    {0:6} wire {1:71} {2};\n".format(
                    vcu_prefix[v][0], vcu_prefix[v][2], vcu_prefix[v][1]))

            f.write("\n")
            ########################################################
            # Write Wires

            # DDR Wires
            f.write("    // DDR Wires\n")
            for ddr_num in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[ddr_num] != 'false'):
                    ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=0)
                    for w in range(ddr_prefix_len):
                        f.write("    logic {0:77} {1};\n".format(ddr_prefix[w][2], ddr_prefix[w][1]))
            
            f.write("    // TO_DDR Wires\n")
            # XDMA_TO_DDR Wires
            if(xdma_ddr_ch != None):
                for i in range (len(xdma_ddr_ch)):
                    xdma_to_ddr_prefix, xdma_to_ddr_prefix_len = Prefix.get_ddr_xdma_prefix(ddr_num=int(xdma_ddr_ch[i]), port_type=0)
                    for w in range(xdma_to_ddr_prefix_len):
                            f.write("    logic {0:77} {1};\n".format(xdma_to_ddr_prefix[w][2], xdma_to_ddr_prefix[w][3]))
            # SLR_TO_DDR Wires
            if(ddr_slr_list != None):
                for i in range(len(ddr_slr_list)) :
                    slr_to_ddr_prefix, slr_to_ddr_prefix_len = Prefix.get_ddr_slr_prefix(slr_num=ddr_slr_list[i], ddr_num=int(ddr_ch_list[i]), port_type=0)
                    for w in range(slr_to_ddr_prefix_len):
                        f.write("    logic {0:77} {1};\n".format(slr_to_ddr_prefix[w][2], slr_to_ddr_prefix[w][3]))

            # GPIO Wires
            #gpio_prefix, gpio_prefix_len = Prefix.get_gpio_prefix()
            #f.write("    // GPIO Wires\n")
            #for w in range(gpio_prefix_len):
            #    f.write("    wire {0:78} {1};\n".format(gpio_prefix[w][2], gpio_prefix[w][1]))
            
            # CLK_WIZ Wires
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            f.write("    // CLK_WIZ Wires\n")
            for w in range(clk_wiz_prefix_len):
                f.write("    wire {0:78} {1};\n".format(clk_wiz_prefix[w][2], clk_wiz_prefix[w][1]))

            # SLR Wires
            f.write("    // SLR Wires\n")
            for slr_num in slr_phy_list:
                slr_prefix, slr_prefix_len = Prefix.get_slr_prefix(slr_num)
                for w in range(slr_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(slr_prefix[w][2], slr_prefix[w][1]))
            # XDMA Wires
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=5)
            f.write("    // XDMA Wires\n")
            for w in range(xdma_prefix_len):
                f.write("    logic {0:77} {1};\n".format(xdma_prefix[w][2], xdma_prefix[w][1]))
            # AXI-Lite Host Wires
            f.write("    // Host Wires\n")
            for slr_num in slr_list:
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for w in range(host_lite_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(host_lite_prefix[w][2], host_lite_prefix[w][3]))
            # AXI Host Wires
            for slr_num in slr_list:
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for w in range(host_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(host_prefix[w][2], host_prefix[w][3]))
            # DDR DMA Ports Wires
            for idx, slr_num in enumerate(slr_list):
                for n in range(len(ddr_slr_list)):
                    if slr_num == ddr_slr_list[n]:
                        for hbm_ddr_num in range(int(ddr_dma_list[n])):
                            ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(ddr_slr_list[n], ddr_ch_list[n], hbm_ddr_num)
                            for m in range(ddr_dma_prefix_len):
                                f.write("    wire {0:78} {1};\n".format(ddr_dma_prefix[m][2], ddr_dma_prefix[m][3]))


            f.write("\n\n")

            ########################################################
            # Instance Board
            inst_name = board
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            ## GPIO Ports
            #f.write("        // GPIO Ports\n")
            #for v in range(gpio_prefix_len):
            #    f.write("        .{0:78} ({1}),\n".format(gpio_prefix[v][1], gpio_prefix[v][1]))
            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=1)
            for v in range(xdma_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            # Board Ports
            f.write("        // Board Ports\n")
            for v in range(0, vcu_prefix_len-2):
                f.write("        .{0:78} ({1}),\n".format(vcu_prefix[v][1], vcu_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(vcu_prefix[v+1][1], vcu_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            # Instance CLK_WIZ
            inst_name = board + "_CLK_WIZ"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # CLK_WIZ Ports
            f.write("        // CLK_WIZ Ports\n")
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            for v in range(clk_wiz_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(clk_wiz_prefix[v][1], clk_wiz_prefix[v][1]))
            # SLR_CLK Ports
            f.write("        // SLR_CLK Ports\n")
            for i in range (3):
                slr_prefix, _ = Prefix.get_slr_prefix(i)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
            # XDMA_CLK Ports
            f.write("        // XDMA_CLK Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=0)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN
            # Physical CLK Ports
            #f.write("        // Physical CLK Ports\n")
            #physical_clk_prefix, physical_clk_prefix_len = Prefix.get_vcu_prefix()
            #f.write("        .{0:78} ({1}),\n".format(physical_clk_prefix[0][1], physical_clk_prefix[0][1]))
            #f.write("        .{0:78} ({1})\n".format(physical_clk_prefix[1][1], physical_clk_prefix[1][1]))
            # Close Instanciation
            f.write("    );\n\n")
            ########################################################
            # Instance DDR 
            if 'true' in total_ddr_ch_list :
                inst_name = board + "_DDR"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                # DDR Ports
                f.write("        // DDR Ports\n")
                for ddr_num in range(len(total_ddr_ch_list)):
                    if(total_ddr_ch_list[ddr_num] != 'false'):
                        ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=2)
                        for v in range(ddr_prefix_len):
                            f.write("        .{0:78} ({1}),\n".format(ddr_prefix[v][1], ddr_prefix[v][1]))

                for ddr_num in range(len(total_ddr_ch_list)):
                    if(total_ddr_ch_list[ddr_num] != 'false'):
                        vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, ddr_num, port_type=0)
                        for v in range(vcu_ddr_prefix_len):
                            f.write("        .{0:78} ({1}),\n".format(vcu_ddr_prefix[v][1], vcu_ddr_prefix[v][1]))

                for ddr_num in range(len(total_ddr_ch_list)):
                    if(total_ddr_ch_list[ddr_num] != 'false'):
                        vcu_ddr_prefix, vcu_ddr_prefix_len = Prefix.get_board_ddr_prefix(board, ddr_num, port_type=1)
                        for v in range(vcu_ddr_prefix_len):
                            f.write("        .{0:78} ({1}),\n".format(vcu_ddr_prefix[v][1], vcu_ddr_prefix[v][1]))


                f.write("        .{0:78} ({1})\n".format('reset', 'reset'))
                f.write("    );\n\n")
            # Close Instanciation
            ########################################################
            # Instance AXI-Lite InterConnect
            inst_name = board + "_XDMA_AXI_LITE_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # CLK_WIZ Ports
            f.write("        // CLK_WIZ Ports\n")
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            for v in range(clk_wiz_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(clk_wiz_prefix[v][1], clk_wiz_prefix[v][1]))
            # GPIO Ports
            #f.write("        // GPIO Ports\n")
            #for v in range(gpio_prefix_len):
            #    f.write("        .{0:78} ({1}),\n".format(gpio_prefix[v][1], gpio_prefix[v][1]))
            # SLR Host Ports
            f.write("        // SLR Ports\n")
            for slr_num in slr_list:
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                for v in range(host_lite_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[v][3], host_lite_prefix[v][3]))
            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=0)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN
            for v in range(2, 21 - 1):                                                              # AXI-Lite
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[v+1][1], xdma_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            # Instance AXI InterConnect
            inst_name = board + "_AXI_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # DDR Ports
            f.write("        // DDR CLK, RESETN Ports\n")
            for ddr_num in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[ddr_num] != 'false'):
                    ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=3)
                    for v in range(ddr_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(ddr_prefix[v][1], ddr_prefix[v][1]))
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                ddr_dma_total_num = ddr_dma_list[idx]
                # SLR CLK and RESETN
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
                # SLR DMA
                for n in range(len(ddr_slr_list)):
                    if slr_num == ddr_slr_list[n]:
                        for hbm_ddr_num in range(int(ddr_dma_list[n])):
                            ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(ddr_slr_list[n], ddr_ch_list[n], hbm_ddr_num)
                            for m in range(ddr_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(ddr_dma_prefix[m][3], ddr_dma_prefix[m][3]))
                
                for ddr_num in range(len(slr_ddr_ch_list[idx])):
                    slr_to_ddr_prefix, slr_to_ddr_prefix_len = Prefix.get_ddr_slr_prefix(slr_num=slr_num, ddr_num=int(slr_ddr_ch_list[idx][ddr_num]), port_type=1)

                    if(idx == len(slr_list) - 1 and ddr_num == len(slr_ddr_ch_list[idx]) - 1):
                        for v in range(slr_to_ddr_prefix_len - 1):
                            f.write("        .{0:78} ({1}),\n".format(slr_to_ddr_prefix[v][3], slr_to_ddr_prefix[v][3]))
                        f.write("        .{0:78} ({1})\n".format(slr_to_ddr_prefix[v+1][3], slr_to_ddr_prefix[v+1][3]))
                    else : 
                        for v in range(slr_to_ddr_prefix_len):
                            f.write("        .{0:78} ({1}),\n".format(slr_to_ddr_prefix[v][3], slr_to_ddr_prefix[v][3]))

            ## Close Instanciation
            f.write("    );\n\n")
            ########################################################
            # Instance XDMA AXI InterConnect
            inst_name = board + "_XDMA_AXI_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                ddr_dma_total_num = ddr_dma_list[idx]
                # SLR CLK and RESETN
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
                # SLR Host
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for v in range(host_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[v][3], host_prefix[v][3]))

            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=5)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN

            # DDR Ports
            f.write("        // DDR CLK, RESETN Ports\n")
            for ddr_num in range(len(total_ddr_ch_list)):
                if(total_ddr_ch_list[ddr_num] != 'false'):
                    ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=3)
                    for v in range(ddr_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(ddr_prefix[v][1], ddr_prefix[v][1]))
            
            # XDMA_TO_DDR Ports
            f.write("        // XDMA_TO_DDR Ports\n")
            if(xdma_ddr_ch != None):
                for ddr_num in range (len(xdma_ddr_ch)):                                                  # TO_DDR                                                            
                    xdma_to_ddr_prefix, xdma_to_ddr_prefix_len = Prefix.get_ddr_xdma_prefix(ddr_num=ddr_num, port_type=1)
                    for v in range(xdma_to_ddr_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(xdma_to_ddr_prefix[v][3], xdma_to_ddr_prefix[v][3]))    

            
            for v in range(21, xdma_prefix_len-1):                                                  # AXI
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[v+1][1], xdma_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            # Instance DDR_AXI Interconnect
            if 'true' in total_ddr_ch_list :
                inst_name = board + "_DDR_AXI_INC"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                # DDR Ports
                f.write("        // DDR Ports\n")
                for ddr_num in range(len(total_ddr_ch_list)):
                    if(total_ddr_ch_list[ddr_num] != 'false'):
                        if(len(ddr_ch_intf_list[ddr_num]) < 2) :
                            ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=1)
                        else :
                            ddr_prefix, ddr_prefix_len = Prefix.get_ddr_prefix(ddr_num=ddr_num, port_type=0)

                        for v in range(ddr_prefix_len):
                            f.write("        .{0:78} ({1}),\n".format(ddr_prefix[v][1], ddr_prefix[v][1]))
                f.write("        // SLR_TO_DDR Ports\n")
                for i in range(len(ddr_slr_list)):
                    slr_to_ddr_prefix, slr_to_ddr_prefix_len = Prefix.get_ddr_slr_prefix(slr_num=ddr_slr_list[i], ddr_num=int(ddr_ch_list[i]), port_type=0)
                    for v in range(slr_to_ddr_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(slr_to_ddr_prefix[v][3], slr_to_ddr_prefix[v][3]))


                if(xdma_ddr_ch != None):
                    f.write("        // XDMA_TO_DDR Ports\n")
                    for i in range(len(xdma_ddr_ch)):
                        xdma_to_ddr_prefix, xdma_to_ddr_prefix_len = Prefix.get_ddr_xdma_prefix(ddr_num=int(xdma_ddr_ch[i]), port_type=0)
                        if(i == len(xdma_ddr_ch) - 1) :
                            for v in range(xdma_to_ddr_prefix_len-1):
                                f.write("        .{0:78} ({1}),\n".format(xdma_to_ddr_prefix[v][3], xdma_to_ddr_prefix[v][3]))
                            f.write("        .{0:78} ({1})\n".format(xdma_to_ddr_prefix[v+1][3], xdma_to_ddr_prefix[v+1][3]))
                        else :
                            for v in range(xdma_to_ddr_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(xdma_to_ddr_prefix[v][3], xdma_to_ddr_prefix[v][3]))

                # Close Instanciation
                f.write("    );\n\n")
            ########################################################
            # Instance User Logic
            inst_name = "User_Logic"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                ddr_dma_total_num = ddr_dma_list[idx]
                # SLR CLK and RESETN
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
                # SLR DMA
                for n in range(len(ddr_slr_list)):
                    if slr_num == ddr_slr_list[n]:
                        for hbm_ddr_num in range(int(ddr_dma_list[n])):
                            ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(ddr_slr_list[n], ddr_ch_list[n], hbm_ddr_num)
                            for m in range(ddr_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(ddr_dma_prefix[m][3], ddr_dma_prefix[m][3]))
                # SLR Host AXI-Lite
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for v in range(host_lite_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[v][3], host_lite_prefix[v][3]))
                # SLR Host
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for v in range(host_prefix_len-1):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[v][3], host_prefix[v][3]))
                f.write("        .{0:78} ({1})".format(host_prefix[v+1][3], host_prefix[v+1][3]))
                # Last Comma
                if idx == len(slr_list) - 1:
                    f.write("\n")
                else:
                    f.write(",\n")
            f.write("    ); \n\n")

            ########################################################
            f.write("    always_comb begin\n")
            f.write("        XDMA_M_AXI_arqos = 'd0;\n")
            f.write("        XDMA_M_AXI_awqos = 'd0;\n")
            f.write("        XDMA_M_AXI_arregion = 'd0;\n")
            f.write("        XDMA_M_AXI_awregion = 'd0;\n")
            if(xdma_ddr_ch != None):
                for i in range(len(xdma_ddr_ch)):
                    f.write("        XDMA_TO_DDR{}_S_AXI_arregion = 'd0;\n".format(xdma_ddr_ch[i]))
                    f.write("        XDMA_TO_DDR{}_S_AXI_awregion = 'd0;\n".format(xdma_ddr_ch[i]))
            if(total_ddr_ch_list != None):
                for i in range(len(total_ddr_ch_list)):
                    if(total_ddr_ch_list[i] != 'false' and len(ddr_ch_intf_list[i]) < 2) :
                        f.write("        DDR{:01d}_S_AXI_arid   = 'd0;\n".format(i))
                        f.write("        DDR{:01d}_S_AXI_awid   = 'd0;\n".format(i))
            if(ddr_slr_list != None):
                for i in range(len(ddr_slr_list)) :
                    f.write("        SLR" + ddr_slr_list[i] + "_TO_DDR" + ddr_ch_list[i] + "_S_AXI_arregion = 'd0;\n")
                    f.write("        SLR" + ddr_slr_list[i] + "_TO_DDR" + ddr_ch_list[i] + "_S_AXI_awregion = 'd0;\n")
            f.write("    end\n\n")
            f.write("endmodule")
        # End of VCU118
##############################
##############################
##############################
        # U50 Board
        elif board == "U50":
            hbm_port_intf_list = [[]for i in range(32)]
            hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
            for i in range(len(hbm_port_list)) :
                hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])
            ########################################################
            # Write Header
            f.write("import " + board + "_Shell_Params::*;\n\n")
            f.write("`timescale 1 ps / 1 ps\n\n")
            f.write("module " + module_name + "\n")
            f.write("(\n")

            ########################################################
            # Write Board Ports
            u50_prefix, u50_prefix_len = Prefix.get_u50_prefix()
            f.write("    {},\n".format("gnd_out"))
            for v in range(u50_prefix_len-1):
                f.write("    {},\n".format(u50_prefix[v][1]))
            f.write("    {}\n);\n\n".format(u50_prefix[v+1][1]))

            ########################################################
            # Write Board Ports
            f.write("    {0:6} logic {1:70} {2};\n".format(
                    "output", " ", "gnd_out"))
            for v in range(u50_prefix_len):
                f.write("    {0:6} wire {1:71} {2};\n".format(
                    u50_prefix[v][0], u50_prefix[v][2], u50_prefix[v][1]))
            f.write("\n")
            

            ########################################################
            # Write Wires
            #hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=-1)
            #for w in range(hbm_prefix_len):
            #    f.write("    wire {0:78} {1};\n".format(hbm_prefix[w][2], hbm_prefix[w][1]))
            # HBM CLK Wires
            f.write("    // HBM_CLK Wires\n")
            #hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=-1)
            f.write("    wire {0:78} {1};\n".format("", "HBM_REF_CLK0"))
            f.write("    wire {0:78} {1};\n".format("", "HBM_REF_CLK1"))
            f.write("    wire {0:78} {1};\n".format("", "HBM_CLK"))
            f.write("    wire {0:78} {1};\n".format("", "HBM_CLK_SLR0_RESETN"))
            f.write("    wire {0:78} {1};\n".format("", "HBM_CLK_SLR1_RESETN"))

            f.write("\n")
            # HBM Wires
            f.write("    // HBM Wires\n")
            for hbm_num in range(len(hbm_port_intf_list)):
                if(len(hbm_port_intf_list[hbm_num]) != 0):
                    hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=hbm_num)
                    for w in range(hbm_prefix_len):
                        f.write("    logic {0:77} {1};\n".format(hbm_prefix[w][2], hbm_prefix[w][1]))
            f.write("\n")

            # XDMA Wires
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=5)
            f.write("    // XDMA Wires\n")
            for w in range(xdma_prefix_len):
                f.write("    logic {0:77} {1};\n".format(xdma_prefix[w][2], xdma_prefix[w][1]))
            xdma_hbm_prefix, xdma_hbm_prefix_len = Prefix.get_xdma_hbm_prefix(hbm_num=xdma_hbm_port)
            f.write("\n")
            for w in range(xdma_hbm_prefix_len):
                f.write("    wire {0:78} {1};\n".format(xdma_hbm_prefix[w][2], xdma_hbm_prefix[w][1]))
            f.write("\n")

            # GPIO Wires
            gpio_prefix, gpio_prefix_len = Prefix.get_gpio_prefix()
            f.write("    // GPIO Wires\n")
            for w in range(gpio_prefix_len):
                f.write("    wire {0:78} {1};\n".format(gpio_prefix[w][2], gpio_prefix[w][1]))
            
            # CLK_WIZ Wires
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            f.write("    // CLK_WIZ Wires\n")
            for w in range(clk_wiz_prefix_len):
                f.write("    wire {0:78} {1};\n".format(clk_wiz_prefix[w][2], clk_wiz_prefix[w][1]))

            # SLR Wires
            f.write("    // SLR Wires\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, slr_prefix_len = Prefix.get_slr_prefix(slr_num)
                for w in range(slr_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(slr_prefix[w][2], slr_prefix[w][1]))
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("    wire {0:78} {1};\n".format(hbm_dma_prefix[m][2], hbm_dma_prefix[m][3]))
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for w in range(host_lite_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(host_lite_prefix[w][2], host_lite_prefix[w][3]))
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for w in range(host_prefix_len):
                    f.write("    wire {0:78} {1};\n".format(host_prefix[w][2], host_prefix[w][3]))
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_slr_prefix, hbm_slr_prefix_len = Prefix.get_hbm_slr_prefix(hbm_slr_list[n], hbm_port_list[n])
                            for m in range(hbm_slr_prefix_len):
                                f.write("    wire {0:78} {1};\n".format(hbm_slr_prefix[m][2], hbm_slr_prefix[m][3]))
            f.write("\n")        

            ########################################################
            # Instance Board
            inst_name = board
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # GPIO Ports
            #f.write("        // GPIO Ports\n")
            #for v in range(gpio_prefix_len):
            #    f.write("        .{0:78} ({1}),\n".format(gpio_prefix[v][1], gpio_prefix[v][1]))
            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=1)
            for v in range(xdma_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            # Board Ports
            f.write("        // Board Ports\n")
            for v in range(0, u50_prefix_len-1):
                f.write("        .{0:78} ({1}),\n".format(u50_prefix[v][1], u50_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(u50_prefix[v+1][1], u50_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            ########################################################
            # Instance CLK_WIZ
            inst_name = board + "_CLK_WIZ"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # CLK_WIZ Ports
            f.write("        // CLK_WIZ Ports\n")
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            for v in range(clk_wiz_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(clk_wiz_prefix[v][1], clk_wiz_prefix[v][1]))
            # HBM_CLK PortS
            f.write("        // HBM_CLK Ports\n")
            #hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=-1)
            #for v in range(hbm_prefix_len):
            #    f.write("        .{0:78} ({1}),\n".format(hbm_prefix[v][1], hbm_prefix[v][1]))
            f.write("        .{0:78} ({1}),\n".format("HBM_REF_CLK0", "HBM_REF_CLK0"))
            f.write("        .{0:78} ({1}),\n".format("HBM_REF_CLK1", "HBM_REF_CLK1"))
            f.write("        .{0:78} ({1}),\n".format("HBM_CLK", "HBM_CLK"))
            f.write("        .{0:78} ({1}),\n".format("HBM_CLK_SLR0_RESETN", "HBM_CLK_SLR0_RESETN"))
            f.write("        .{0:78} ({1}),\n".format("HBM_CLK_SLR1_RESETN", "HBM_CLK_SLR1_RESETN"))

            # SLR_CLK Ports
            f.write("        // SLR_CLK Ports\n")
            for i in range (2):
                slr_prefix, _ = Prefix.get_slr_prefix(i)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
            # XDMA_CLK Ports
            f.write("        // XDMA_CLK Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=0)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN
            # Close Instanciation
            f.write("    );\n\n")
            ########################################################
            # Instance XDMA AXI-Lite InterConnect
            inst_name = board + "_XDMA_AXI_LITE_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # CLK_WIZ Ports
            f.write("        // CLK_WIZ Ports\n")
            clk_wiz_prefix, clk_wiz_prefix_len = Prefix.get_clk_wiz_prefix()
            for v in range(clk_wiz_prefix_len):
                f.write("        .{0:78} ({1}),\n".format(clk_wiz_prefix[v][1], clk_wiz_prefix[v][1]))

            # SLR Host Ports
            f.write("        // SLR Ports\n")
            for slr_num in slr_list:
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                for v in range(host_lite_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[v][3], host_lite_prefix[v][3]))
            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=0)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN
            for v in range(2, 21 - 1):                                                              # AXI-Lite
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[v+1][1], xdma_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            # Instance XDMA_AXI InterConnect
            inst_name = board + "_XDMA_AXI_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, slr_prefix_len = Prefix.get_slr_prefix(slr_num)
                for v in range(slr_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(slr_prefix[v][1], slr_prefix[v][1]))
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for v in range(host_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[v][3], host_prefix[v][3]))
            if(xdma_hbm_port!=None):
                for v in range(xdma_hbm_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(xdma_hbm_prefix[v][1], xdma_hbm_prefix[v][1]))
                # HBM Ports
                f.write("        // HBM CLK, RESETN Ports\n")
                f.write("        .{0:78} ({1}),\n".format("HBM_CLK", "HBM_CLK"))
                f.write("        .{0:78} ({1}),\n".format("HBM_CLK_RESETN", "HBM_CLK_SLR1_RESETN"))

                    # HBM Ports
            #if('true' in total_hbm_port_list):
            #    f.write("        // HBM CLK, RESETN Ports\n")
            #    f.write("        .{0:78} ({1}),\n".format("HBM_CLK", "HBM_CLK"))
            #    f.write("        .{0:78} ({1}),\n".format("HBM_CLK_RESETN", "HBM_CLK_SLR1_RESETN"))
            
            # XDMA Ports
            f.write("        // XDMA Ports\n")
            xdma_prefix, xdma_prefix_len = Prefix.get_xdma_prefix(port_type=5)
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[0][1], xdma_prefix[0][1]))        # CLK
            f.write("        .{0:78} ({1}),\n".format(xdma_prefix[1][1], xdma_prefix[1][1]))        # RESETN
            for v in range(21, xdma_prefix_len-1):                                                    # AXI
                f.write("        .{0:78} ({1}),\n".format(xdma_prefix[v][1], xdma_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(xdma_prefix[v+1][1], xdma_prefix[v+1][1]))

            # Close Instanciation
            f.write("    );\n\n")
            ########################################################
            # Instance AXI InterConnect
            inst_name = board + "_AXI_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, slr_prefix_len = Prefix.get_slr_prefix(slr_num)
                for v in range(slr_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(slr_prefix[v][1], slr_prefix[v][1]))
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(hbm_dma_prefix[m][3], hbm_dma_prefix[m][3]))
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_slr_prefix, hbm_slr_prefix_len = Prefix.get_hbm_slr_prefix(hbm_slr_list[n], hbm_port_list[n])
                            for m in range(hbm_slr_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(hbm_slr_prefix[m][3], hbm_slr_prefix[m][3]))
            # HBM Ports
            f.write("        // HBM Ports\n")
            if('true' in total_hbm_port_list):
                f.write("        .{0:78} ({1}),\n".format("HBM_CLK", "HBM_CLK"))
                f.write("        .{0:78} ({1})\n".format("HBM_CLK_RESETN", "HBM_CLK_SLR1_RESETN"))
                #f.write("        .{0:78} ({1})\n".format("HBM_CLK_SLR1_RESETN", "HBM_CLK_SLR1_RESETN"))
                #f.write("        .{0:78} ({1})\n".format("HBM_CLK_SLR2_RESETN", "HBM_CLK_SLR2_RESETN"))
            # Close Instanciation
            f.write("    );\n\n")
            ########################################################
            # Instance HBM AXI InterConnect
            inst_name = board + "_HBM_AXI_INC"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # HBM AXI Ports
            f.write("        // HBM Ports\n")
            for hbm_num in range(len(hbm_port_intf_list)):
                if(len(hbm_port_intf_list[hbm_num]) != 0) :
                    if(len(hbm_port_intf_list[hbm_num]) == 1) :
                        port_type = 2
                    
                    else :
                        port_type = 4
                    hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=hbm_num, port_type=port_type)
                    for w in range(hbm_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(hbm_prefix[w][1], hbm_prefix[w][1]))

            #hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=-2)
            #for v in range(hbm_prefix_len):
            #    f.write("        .{0:78} ({1}),\n".format(hbm_prefix[v][1], hbm_prefix[v][1]))
            f.write("        .{0:78} ({1}),\n".format("HBM_CLK", "HBM_CLK"))
            f.write("        .{0:78} ({1}),\n".format("HBM_CLK_RESETN", "HBM_CLK_SLR0_RESETN"))
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_slr_prefix, hbm_slr_prefix_len = Prefix.get_hbm_slr_prefix(hbm_slr_list[n], hbm_port_list[n])
                            for m in range(hbm_slr_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(hbm_slr_prefix[m][3], hbm_slr_prefix[m][3]))
            # XDMA HBM Ports
            for v in range(xdma_hbm_prefix_len-1):
                f.write("        .{0:78} ({1}),\n".format(xdma_hbm_prefix[v][1], xdma_hbm_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(xdma_hbm_prefix[v+1][1], xdma_hbm_prefix[v+1][1]))
            # Close Instanciation
            f.write("    );\n\n")


            ########################################################
            # Instance HBM
            inst_name = board + "_HBM"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # HBM AXI Ports
            f.write("        // HBM Ports\n")
            for hbm_num in range(len(hbm_port_intf_list)):
                if(len(hbm_port_intf_list[hbm_num]) != 0) :
                    port_type = 1
                    hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=hbm_num, port_type=port_type)
                    for w in range(hbm_prefix_len):
                        f.write("        .{0:78} ({1}),\n".format(hbm_prefix[w][1], hbm_prefix[w][1]))

            hbm_prefix, hbm_prefix_len = Prefix.get_hbm_prefix(hbm_num=-1)
            for v in range(hbm_prefix_len-1):
                f.write("        .{0:78} ({1}),\n".format(hbm_prefix[v][1], hbm_prefix[v][1]))
            f.write("        .{0:78} ({1})\n".format(hbm_prefix[v+1][1], "HBM_CLK_SLR0_RESETN"))
            # Close Instanciation
            f.write("    );\n\n")

            ########################################################
            # Instance User Logic
            inst_name = "User_Logic"
            f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
            # SLR Ports
            f.write("        // SLR Ports\n")
            for idx, slr_num in enumerate(slr_list):
                slr_prefix, slr_prefix_len = Prefix.get_slr_prefix(slr_num)
                for v in range(slr_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(slr_prefix[v][1], slr_prefix[v][1]))
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(hbm_dma_prefix[m][3], hbm_dma_prefix[m][3]))
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for v in range(host_lite_prefix_len):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[v][3], host_lite_prefix[v][3]))
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for v in range(host_prefix_len-1):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[v][3], host_prefix[v][3]))
                f.write("        .{0:78} ({1})".format(host_prefix[v+1][3], host_prefix[v+1][3]))
                # Last Comma
                if idx == len(slr_list) - 1:
                    f.write("\n")
                else:
                    f.write(",\n")
            # Close Instanciation
            f.write("    ); \n\n")

            f.write("    always_comb begin\n")
            f.write("        gnd_out    = 'd0;\n")
            f.write("        XDMA_M_AXI_arqos = 'd0;\n")
            f.write("        XDMA_M_AXI_awqos = 'd0;\n")
            f.write("        XDMA_M_AXI_arregion = 'd0;\n")
            f.write("        XDMA_M_AXI_awregion = 'd0;\n")
            for hbm_num in range(len(hbm_port_intf_list)):
                if(len(hbm_port_intf_list[hbm_num]) == 1) :
                    if(hbm_num < 10) :
                        f.write("        HBM0" + str(hbm_num) + "_S_AXI_arid = 'd0;\n")
                        f.write("        HBM0" + str(hbm_num) + "_S_AXI_awid = 'd0;\n")
                    else :
                        f.write("        HBM" + str(hbm_num) + "_S_AXI_arid = 'd0;\n")
                        f.write("        HBM" + str(hbm_num) + "_S_AXI_awid = 'd0;\n")
            f.write("    end\n\n")

            f.write("endmodule")
        # End of u50
##############################
##############################
############################## 
        # U280 Board
        elif board == "U280":
            return
##############################
##############################
############################## 
        elif board == "U250":
            return

        else:
            return