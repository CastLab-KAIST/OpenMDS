################################################################
# Library
################################################################
import os
from . import Prefix

################################################################
# Function
################################################################

''' SLR Wrapper Generate '''
def SLR_Wrapper(filedir, board, slr_list, ddr_dma_list=None, hbm_slr_list=None,  hbm_port_list=None,  hbm_dma_list=None,
                crossing=False, src_list=None, dest_list=None, num_list=None, data_width_list=None):
    for idx, slr_num in enumerate(slr_list):
        # Create and Write SLL0.sv file
        module_name = "SLR" + slr_num
        gen_sv = os.path.join(filedir, module_name + ".sv")
        with open(gen_sv, 'w') as f:
            # VCU118 Board
            if board == "VCU118":
                ########################################################
                # Write Header
                f.write("import " + board + "_Shell_Params::*;\n\n")
                f.write("module " + module_name+"\n")
                f.write("(\n")

                ########################################################
                # Write SLR Ports
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[0][1]))           # CLK
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[1][1]))           # RESETN
                # DDR DMA AXI Ports
                for ddr_dma_num in range(int(ddr_dma_list[idx])):
                    ddr_dma_prefix, ddr_dma_prefix_len = Prefix.get_ddr_dma_prefix(slr_num, ddr_dma_num)
                    for n in range(ddr_dma_prefix_len):
                        f.write("    {0:6} {1:5} {2:70} {3},\n".format(ddr_dma_prefix[n][0], ddr_dma_prefix[n][1], ddr_dma_prefix[n][2], ddr_dma_prefix[n][3]))
                # SLR Crossing Ports
                if crossing:
                    pos = [x for x in range(len(slr_list)) if slr_list[x] == slr_num]
                    # AXI-Stream
                    for idx in pos:
                        slr_src = src_list[idx]
                        slr_dest = dest_list[idx]
                        fifo_width = data_width_list[idx]
                        fifo_number = num_list[idx]
                        for fifo_num in range(int(fifo_number)):
                            crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                            for n in range(crossing_stream_prefix_len):
                                f.write("    {0:6} {1:5} {2:70} {3},\n".format(crossing_stream_prefix[n][0], crossing_stream_prefix[n][1], crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))
                    # AXI-Lite
                    for idx in pos:
                        slr_src = src_list[idx]
                        slr_dest = dest_list[idx]
                        crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                        for n in range(crossing_lite_prefix_len):
                            f.write("    {0:6} {1:5} {2:70} {3},\n".format(crossing_lite_prefix[n][0], crossing_lite_prefix[n][1], crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
                # Host AXI-Lite Ports
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h][0], host_lite_prefix[h][1], host_lite_prefix[h][2], host_lite_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h+1][0], host_lite_prefix[h+1][1], host_lite_prefix[h+1][2], host_lite_prefix[h+1][3]))

                # Host AXI Ports
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for h in range(host_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_prefix[h][0], host_prefix[h][1], host_prefix[h][2], host_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3}\n".format(host_prefix[h+1][0], host_prefix[h+1][1], host_prefix[h+1][2], host_prefix[h+1][3]))


                f.write(");\n")
                f.write("\n\nendmodule")

            # U50 Board
            if board == "U50":
                ########################################################
                # Write Header
                f.write("import " + board + "_Shell_Params::*;\n\n")
                f.write("module " + module_name+"\n")
                f.write("(\n")

                ########################################################
                # Write SLR Ports
                slr_prefix, _ = Prefix.get_slr_prefix(slr_num)
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[0][1]))           # CLK
                f.write("    input  {0:76} {1},\n".format("logic", slr_prefix[1][1]))           # RESETN
                # HBM DMA AXI Ports
                for n in range(len(hbm_slr_list)):
                    if slr_num == hbm_slr_list[n]:
                        for hbm_ddr_num in range(int(hbm_dma_list[n])):
                            hbm_dma_prefix, hbm_dma_prefix_len = Prefix.get_hbm_dma_prefix(hbm_slr_list[n], hbm_port_list[n], hbm_ddr_num)
                            for m in range(hbm_dma_prefix_len):
                                f.write("    {0:6} {1:5} {2:70} {3},\n".format(hbm_dma_prefix[m][0], hbm_dma_prefix[m][1], hbm_dma_prefix[m][2], hbm_dma_prefix[m][3]))
                # SLR Crossing Ports
                if crossing:
                    pos = [x for x in range(len(slr_list)) if slr_list[x] == slr_num]
                    # AXI-Stream
                    for idx in pos:
                        slr_src = src_list[idx]
                        slr_dest = dest_list[idx]
                        fifo_width = data_width_list[idx]
                        fifo_number = num_list[idx]
                        for fifo_num in range(int(fifo_number)):
                            crossing_stream_prefix, crossing_stream_prefix_len = Prefix.get_crossing_stream_prefix(slr_src, slr_dest, fifo_width, fifo_num)
                            for n in range(crossing_stream_prefix_len):
                                f.write("    {0:6} {1:5} {2:70} {3},\n".format(crossing_stream_prefix[n][0], crossing_stream_prefix[n][1], crossing_stream_prefix[n][2], crossing_stream_prefix[n][3]))
                    # AXI-Lite
                    for idx in pos:
                        slr_src = src_list[idx]
                        slr_dest = dest_list[idx]
                        crossing_lite_prefix, crossing_lite_prefix_len = Prefix.get_crossing_lite_prefix(slr_src, slr_dest)
                        for n in range(crossing_lite_prefix_len):
                            f.write("    {0:6} {1:5} {2:70} {3},\n".format(crossing_lite_prefix[n][0], crossing_lite_prefix[n][1], crossing_lite_prefix[n][2], crossing_lite_prefix[n][3]))
                # Host AXI-Lite Ports
                host_lite_prefix, host_lite_prefix_len = Prefix.get_axilite_host_prefix(slr_num)
                for h in range(host_lite_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h][0], host_lite_prefix[h][1], host_lite_prefix[h][2], host_lite_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_lite_prefix[h+1][0], host_lite_prefix[h+1][1], host_lite_prefix[h+1][2], host_lite_prefix[h+1][3]))

                # Host AXI Ports
                host_prefix, host_prefix_len = Prefix.get_axi_host_prefix(slr_num)
                for h in range(host_prefix_len - 1):
                    f.write("    {0:6} {1:5} {2:70} {3},\n".format(host_prefix[h][0], host_prefix[h][1], host_prefix[h][2], host_prefix[h][3]))
                f.write("    {0:6} {1:5} {2:70} {3}\n".format(host_prefix[h+1][0], host_prefix[h+1][1], host_prefix[h+1][2], host_prefix[h+1][3]))


                f.write(");\n")
                f.write("\n\nendmodule")
            
            # U280 Board
            if board == "U280":
                return