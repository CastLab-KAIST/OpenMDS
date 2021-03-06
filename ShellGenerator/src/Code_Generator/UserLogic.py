################################################################
# Library
################################################################
import os
from . import Prefix

################################################################
# Function
################################################################

''' User Logic SV File Generate '''
def UserLogic(filedir, board, slr_list, ddr_slr_list=None, ddr_ch_list=None, ddr_dma_list=None, hbm_slr_list=None, hbm_port_list=None, hbm_dma_list=None,
              crossing=False, src_list=None, dest_list=None, num_list=None, data_width_list=None):
    # Create User Logic File
    module_name = "User_Logic"
    gen_sv = os.path.join(filedir, module_name + ".sv")
    with open(gen_sv, 'w') as f:
        # VCU118 Board:
        if board == "VCU118":
            ########################################################
            # Write Header
            f.write("import " + board + "_Shell_Params::*;\n\n")
            f.write("module " + module_name+"\n")
            f.write("(\n")

            ########################################################
            # Write Board Ports
            for idx, slr_num in enumerate(slr_list):
                # Write CLK and RESET Ports
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[0][1]))
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[1][1]))
                # Write DDR DMA AXI Port
                for n in range(len(ddr_slr_list)):
                    if slr_num == ddr_slr_list[n]:
                        for hbm_ddr_num in range(int(ddr_dma_list[n])):
                            ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(ddr_slr_list[n], ddr_ch_list[n], hbm_ddr_num)
                            for m in range(ddr_dma_prefix_len):
                                f.write("    {0:6} {1:5} {2:70} {3},\n".format(ddr_dma_prefix[m][0], ddr_dma_prefix[m][1], ddr_dma_prefix[m][2], ddr_dma_prefix[m][3]))
                # Write Host AXI-Lite Ports
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h][0], host_lite_prefix[h][1], host_lite_prefix[h][2], host_lite_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h+1][0], host_lite_prefix[h+1][1], host_lite_prefix[h+1][2], host_lite_prefix[h+1][3]))
                # Write Host AXI Ports
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num=slr_num)
                for h in range(host_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_prefix[h][0], host_prefix[h][1], host_prefix[h][2], host_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3}".format(host_prefix[h+1][0], host_prefix[h+1][1], host_prefix[h+1][2], host_prefix[h+1][3]))
                # Last Comma
                if idx < len(slr_list) - 1:
                    f.write(",\n")
                else:
                    f.write("\n")
            f.write(");\n\n")

            ########################################################
            # Write Crossing Wires
            if crossing:
                # FIFO AXI-Stream
                f.write("    // FIFO AXI-Stream Wires\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("    wire {0:78} {1};\n".format(crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("    wire {0:78} {1};\n".format(crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))
                
                f.write("        // FIFO AXI-Lite Wires\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    # AXI-Lite
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("    wire {0:78} {1};\n".format(crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_dest, slr_src)
                            for n in range(0, 19):
                                f.write("    wire {0:78} {1};\n".format(crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
            f.write("\n")
            ########################################################
            # Instance CROSSING_AXIS
            slr_clk_done_list = [0 for k in range(len(slr_list))]
            if crossing:
                inst_name = "CROSSING_AXIS"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))
                    f.write("        // SLR CLK Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                        if(slr_num == dest_list):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                    
                for i in range(len(slr_clk_done_list)):
                    if(slr_clk_done_list[i] == 1):
                        slr_clk_done_list[i] = 0
                        slr_prefix, _ = Prefix.get_slr_prefix(slr_list[i])
                        if(1 in slr_clk_done_list):
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN

                        else:
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1})\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN
                # Close Instanciation
                f.write("    );\n\n")
                ## Close Instanciation



            ########################################################
            # Instance CROSSING_AXI_LITE
            if crossing:
                inst_name = "CROSSING_AXI_LITE"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(0, 19):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    f.write("        // SLR CLK Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                        if(slr_num == dest_list):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                    
                for i in range(len(slr_clk_done_list)):
                    if(slr_clk_done_list[i] == 1):
                        slr_clk_done_list[i] = 0
                        slr_prefix, _ = Prefix.get_slr_prefix(slr_list[i])
                        if(1 in slr_clk_done_list):
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN

                        else:
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1})\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN
                f.write("    );\n\n")
                ## Close Instanciation

            ########################################################
            ########################################################
            # Instance SLR
            for idx, slr_num in enumerate(slr_list):
                inst_name = "SLR" + slr_num
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                # SLR CLK and RESETN
                f.write("        // SLR Ports\n")
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
                # DDR DMA AXI Ports
                f.write("        // DDR DMA Ports\n")
                for n in range(len(ddr_slr_list)):
                    if slr_num == ddr_slr_list[n]:
                        for hbm_ddr_num in range(int(ddr_dma_list[n])):
                            ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(ddr_slr_list[n], ddr_ch_list[n], hbm_ddr_num)
                            for m in range(ddr_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(ddr_dma_prefix[m][3], ddr_dma_prefix[m][3]))
                    #for n in range(ddr_dma_prefix_len):
                # SLR Crossing Ports
                if crossing:
                    f.write("        // FIFO AXI-Stream Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))
                    
                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))

                    # AXI-Lite
                    f.write("        // FIFO AXI-Lite Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_dest, slr_src)
                            for n in range(0, 19):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                # Write HOST AXI-Lite Ports
                f.write("        // Host AXI-Lite Ports\n")
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len - 1):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[h][3], host_lite_prefix[h][3]))
                f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[h+1][3], host_lite_prefix[h+1][3]))
                # Write HOST AXI Ports
                f.write("        // Host Ports\n")
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for h in range(host_prefix_len - 1):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[h][3], host_prefix[h][3]))
                f.write("        .{0:78} ({1})\n".format(host_prefix[h+1][3], host_prefix[h+1][3]))
                # Close Instanciation
                f.write("    );\n\n")

            f.write("endmodule")

        # U50 Board:
        if board == "U50":
            ########################################################
            # Write Header
            f.write("import " + board + "_Shell_Params::*;\n\n")
            f.write("module " + module_name+"\n")
            f.write("(\n")

            ########################################################
            # Write Board Ports
            for idx, slr_num in enumerate(slr_list):
                # Write CLK and RESET Ports
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[0][1]))
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[1][1]))
                # Write HBM DMA AXI Port
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("    {0:6} {1:5} {2:70} {3},\n".format(hbm_dma_prefix[m][0], hbm_dma_prefix[m][1], hbm_dma_prefix[m][2], hbm_dma_prefix[m][3]))
                # Host Port
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h][0], host_lite_prefix[h][1], host_lite_prefix[h][2], host_lite_prefix[h][3]))
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for h in range(host_prefix_len-1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_prefix[h][0], host_prefix[h][1], host_prefix[h][2], host_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3}".format(host_prefix[h+1][0], host_prefix[h+1][1], host_prefix[h+1][2], host_prefix[h+1][3]))
                # Last Comma
                if idx == len(slr_list) - 1:
                    f.write("\n")
                else:
                    f.write(",\n")
            f.write(");\n\n")

            ########################################################
            # Write Crossing Wires
            if crossing:
                # FIFO AXI-Stream
                f.write("    // FIFO AXI-Stream Wires\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("    wire {0:78} {1};\n".format(crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("    wire {0:78} {1};\n".format(crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))
                
                f.write("        // FIFO AXI-Lite Wires\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    # AXI-Lite
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("    wire {0:78} {1};\n".format(crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_dest, slr_src)
                            for n in range(0, 19):
                                f.write("    wire {0:78} {1};\n".format(crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
            f.write("\n")
            ########################################################
            # Instance CROSSING_AXIS
            slr_clk_done_list = [0 for k in range(len(slr_list))]
            if crossing:
                inst_name = "CROSSING_AXIS"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))
                    f.write("        // SLR CLK Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                        if(slr_num == dest_list):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                    
                for i in range(len(slr_clk_done_list)):
                    if(slr_clk_done_list[i] == 1):
                        slr_clk_done_list[i] = 0
                        slr_prefix, _ = Prefix.get_slr_prefix(slr_list[i])
                        if(1 in slr_clk_done_list):
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN

                        else:
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1})\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN
                # Close Instanciation
                f.write("    );\n\n")
                ## Close Instanciation



            ########################################################
            # Instance CROSSING_AXI_LITE
            if crossing:
                inst_name = "CROSSING_AXI_LITE"
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                
                for idx in range(len(slr_list)):
                    slr_num = slr_list[idx]
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(0, 19):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    f.write("        // SLR CLK Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                        if(slr_num == dest_list):
                            if(slr_clk_done_list[idx] == 0):
                                slr_clk_done_list[idx] = 1
                    
                    
                for i in range(len(slr_clk_done_list)):
                    if(slr_clk_done_list[i] == 1):
                        slr_clk_done_list[i] = 0
                        slr_prefix, _ = Prefix.get_slr_prefix(slr_list[i])
                        if(1 in slr_clk_done_list):
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN

                        else:
                            f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                            f.write("        .{0:78} ({1})\n".format(slr_prefix[1][1], slr_prefix[1][1]))        # RESETN
                f.write("    );\n\n")
                ## Close Instanciation

            ########################################################
            # Instance SLR
            for idx, slr_num in enumerate(slr_list):
                inst_name = "SLR" + slr_num
                f.write("    " + inst_name + " " + inst_name + "_i\n    (\n")
                # SLR CLK and RESETN
                f.write("        // SLR Ports\n")
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[0][1], slr_prefix[0][1]))      # CLK
                f.write("        .{0:78} ({1}),\n".format(slr_prefix[1][1], slr_prefix[1][1]))      # RESETN
                # HBM DMA AXI Ports
                f.write("        // HBM DMA Ports\n")
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(hbm_dma_prefix[m][3], hbm_dma_prefix[m][3]))
                # SLR Crossing Ports
                if crossing:
                    f.write("        // FIFO AXI-Stream Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                                for n in range(3, crossing_stream_prefix_len):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))
                    
                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            fifo_width = data_width_list[i]
                            fifo_number = num_list[i]
                            for fifo_num in range(int(fifo_number)):
                                crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_dest, slr_src, fifo_width, fifo_num)
                                for n in range(0, 3):
                                    f.write("        .{0:78} ({1}),\n".format(crossing_stream_prefix[n][3], crossing_stream_prefix[n][3]))

                    # AXI-Lite
                    f.write("        // FIFO AXI-Lite Ports\n")
                    for i in range(len(src_list)):
                        if(slr_num == src_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                            for n in range(19, crossing_lite_prefix_len):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                    for i in range(len(dest_list)):
                        if(slr_num == dest_list[i]):
                            slr_src = src_list[i]
                            slr_dest = dest_list[i]
                            crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_dest, slr_src)
                            for n in range(0, 19):
                                f.write("        .{0:78} ({1}),\n".format(crossing_lite_prefix[n][3], crossing_lite_prefix[n][3]))

                # Write HOST AXI-Lite Ports
                f.write("        // Host AXI-Lite Ports\n")
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len - 1):
                    f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[h][3], host_lite_prefix[h][3]))
                f.write("        .{0:78} ({1}),\n".format(host_lite_prefix[h+1][3], host_lite_prefix[h+1][3]))
                # Write HOST AXI Ports
                f.write("        // Host Ports\n")
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for h in range(host_prefix_len - 1):
                    f.write("        .{0:78} ({1}),\n".format(host_prefix[h][3], host_prefix[h][3]))
                f.write("        .{0:78} ({1})\n".format(host_prefix[h+1][3], host_prefix[h+1][3]))
                # Close Instanciation
                f.write("    );\n\n")

            f.write("endmodule")
        
        return