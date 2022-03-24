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

def INC_Xdc (filedir, board, slr_list, ddr_dma_list, hbm_slr_list, hbm_port_list, hbm_dma_list, xdma_hbm_port, 
            xdma_ddr_ch_list=None, ddr_slr_list=None, ddr_ch_list=None) :
    
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
        for i in range(len(xdma_ddr_ch_list)):
            total_ddr_ch_list[int(xdma_ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(xdma_ddr_ch_list[i])].append('XDMA')
    
    if(ddr_ch_list != None):
        for i in range(len(ddr_ch_list)):
            total_ddr_ch_list[int(ddr_ch_list[i])] = 'true'
            ddr_ch_intf_list[int(ddr_ch_list[i])].append(ddr_slr_list[i])

    gen_xdc = os.path.join(filedir, "INC.xdc")

    with open(gen_xdc, 'w') as f_d:
        if(board == 'VCU118') :
            f_d.write("create_pblock XDMA\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA] [get_cells -quiet [list VCU118_i/XDMA]] \n")
            f_d.write("resize_pblock [get_pblocks XDMA] -add {CLOCKREGION_X4Y5:CLOCKREGION_X5Y8}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks XDMA]\n")
            #f_d.write("set_property PARENT SLR1 [get_pblocks XDMA]\n")

            f_d.write("create_pblock XDMA_INC\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC]  "
            +"[get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_M_AXI_INC_0 "+ board +"_XDMA_AXI_LITE_INC_i/XDMA_M_AXI_LITE_INC_0]] \n")
            f_d.write("resize_pblock [get_pblocks XDMA_INC] -add {CLOCKREGION_X3Y6:CLOCKREGION_X3Y8}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks XDMA_INC]\n")
            #f_d.write("set_property PARENT SLR1 [get_pblocks XDMA_INC]\n")

            if(total_ddr_ch_list != None):
                for i in range(len(total_ddr_ch_list)) :
                    if(total_ddr_ch_list[i] != 'false'):
                        if(i == 0):
                            f_d.write("create_pblock DDR" + str(i) +"_INC\n")
                            f_d.write("add_cells_to_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "[get_cells -quiet [list " + board + "_DDR_AXI_INC_i/DDR" + str(i) +"_INC_0]] \n")
                            f_d.write("resize_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "-add {CLOCKREGION_X1Y10:CLOCKREGION_X4Y10}\n")
                            f_d.write("resize_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "-add {CLOCKREGION_X4Y10:CLOCKREGION_X4Y14}\n")
                            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks DDR" + str(i) +"_INC]\n")
                        elif(i == 1):
                            f_d.write("create_pblock DDR" + str(i) +"_INC\n")
                            f_d.write("add_cells_to_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "[get_cells -quiet [list " + board + "_DDR_AXI_INC_i/DDR" + str(i) +"_INC_0]] \n")
                            f_d.write("resize_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "-add {CLOCKREGION_X1Y4:CLOCKREGION_X4Y4}\n")
                            f_d.write("resize_pblock [get_pblocks DDR" + str(i) +"_INC] "
                            + "-add {CLOCKREGION_X2Y1:CLOCKREGION_X2Y4}\n")
                            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks DDR" + str(i) +"_INC]\n")


                        #if(i == 0):
                        #    f_d.write("set_property PARENT SLR2 [get_pblocks DDR" + str(i) +"_INC]\n")
#
                        #elif(i == 1):
                        #    f_d.write("set_property PARENT SLR0 [get_pblocks DDR" + str(i) +"_INC]\n")
            if(slr_ddr_ch_list != None):
                for i in range(len(slr_ddr_ch_list)):
                    if(len(slr_ddr_ch_list[i]) != 0):
                        f_d.write("create_pblock SLR" + slr_list[i] +"_DMA_INC\n")
                        if(int(ddr_dma_list[i] != 0)) :
                            f_d.write("add_cells_to_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC]  "
                            + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR" + slr_list[i] +"_DMA_INC_0]] \n")

                        if(int(slr_list[i]) == 0) :
                            if '0' in ddr_ch_intf_list[1]:
                                f_d.write("add_cells_to_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC]  "
                                + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR" + slr_list[i] +"_TO_DDR1_SMC_0]] \n")

                            f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC] " 
                            + "-add {CLOCKREGION_X0Y2:CLOCKREGION_X0Y4}\n")

                        elif(int(slr_list[i]) == 1) :
                            f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC] "
                            + "-add {CLOCKREGION_X1Y6:CLOCKREGION_X1Y8}\n")

                        elif(int(slr_list[i]) == 2) :
                            if '2' in ddr_ch_intf_list[0]:
                                f_d.write("add_cells_to_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC]  "
                                + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR" + slr_list[i] +"_TO_DDR0_SMC_0]] \n")

                            f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] +"_DMA_INC] " 
                            + "-add {CLOCKREGION_X0Y10:CLOCKREGION_X0Y12}\n")
                        f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR" + slr_list[i] +"_DMA_INC]\n")
                        #f_d.write("set_property PARENT SLR" + slr_list[i] + " [get_pblocks SLR" + slr_list[i] +"_DMA_INC]\n")

            f_d.write("create_pblock SMC_BRIDGE\n")
            flag = 0
            if(slr_ddr_ch_list != None):
                for i in range(len(slr_ddr_ch_list)):
                    for j in range(len(slr_ddr_ch_list[i])):
                        if((int(slr_list[i]) == 0 and int(slr_ddr_ch_list[i][j]) == 0 ) \
                            or (int(slr_list[i]) == 2 and int(slr_ddr_ch_list[i][j]) == 1)) :
                            flag = flag + 1
                            f_d.write("add_cells_to_pblock [get_pblocks SMC_BRIDGE]  "
                            + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR" + slr_list[i] +"_TO_DDR"+ slr_ddr_ch_list[i][j] +"_SMC_0]] \n")
            
            if(flag != 0 ):
                f_d.write("resize_pblock [get_pblocks SMC_BRIDGE] -add {SLICE_X0Y300:SLICE_X" + str(flag*7-1) + "Y599}\n")
            elif(flag == 0):
                f_d.write("delete_pblocks SMC_BRIDGE \n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SMC_BRIDGE]\n")
            #f_d.write("set_property PARENT SLR1 [get_pblocks SMC_BRIDGE]\n")

            f_d.write("create_pblock SLR1_TOP\n")
            if(xdma_ddr_ch_list != None):
                for i in range(len(xdma_ddr_ch_list)):
                    if(int(xdma_ddr_ch_list[i]) == 0):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR1_TOP] [get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_TO_DDR0_SMC_0]] \n")
            
            if(slr_ddr_ch_list != None):
                for i in range(len(slr_ddr_ch_list)):
                    for j in range(len(slr_ddr_ch_list[i])):
                        if(int(slr_list[i]) == 0 and int(slr_ddr_ch_list[i][j]) == 0):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_TOP] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR0_TO_DDR0_SMC_1]] \n")

                        elif(int(slr_list[i]) == 1 and int(slr_ddr_ch_list[i][j]) == 0):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_TOP] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR0_SMC_0]] \n")
            f_d.write("resize_pblock [get_pblocks SLR1_TOP] -add {CLOCKREGION_X1Y9:CLOCKREGION_X4Y9}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR1_TOP]\n")
            #f_d.write("set_property PARENT SLR1 [get_pblocks SLR1_TOP]\n")



            f_d.write("create_pblock SLR1_BOTTOM\n")
            if(xdma_ddr_ch_list != None):
                for i in range(len(xdma_ddr_ch_list)):
                    if(int(xdma_ddr_ch_list[i]) == 1):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR1_BOTTOM] [get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_TO_DDR1_SMC_0]] \n")
            if(slr_ddr_ch_list != None):
                for i in range(len(slr_ddr_ch_list)):
                    for j in range(len(slr_ddr_ch_list[i])):
                        if(int(slr_list[i]) == 1 and int(slr_ddr_ch_list[i][j]) == 1):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_BOTTOM] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR1_SMC_0]] \n")
                        elif(int(slr_list[i]) == 2 and int(slr_ddr_ch_list[i][j]) == 1):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_BOTTOM] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR2_TO_DDR1_SMC_1]] \n")
            f_d.write("resize_pblock [get_pblocks SLR1_BOTTOM] -add {CLOCKREGION_X1Y5:CLOCKREGION_X4Y5}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR1_BOTTOM]\n")
            #f_d.write("set_property PARENT SLR1 [get_pblocks SLR1_BOTTOM]\n")

        #End of VCU118
        elif(board == 'U50') :
            total_hbm_port_list = ['false' for i in range(32)]
            hbm_port_intf_list = [[]for i in range(32)]
            total_hbm_port_list[int(xdma_hbm_port)] = 'true'
            hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
            for i in range(len(hbm_port_list)) :
                total_hbm_port_list[int(hbm_port_list[i])] = 'true'
                hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])
            
            #for i in range(len(slr_list)):
            #    f_d.write("create_pblock SLR" + slr_list[i] + "\n")
            #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] + "]"
            #    + " -add {SLR" + slr_list[i] +"}\n")
            #    f_d.write("set_property CONTAIN_ROUTING false [get_pblocks SLR" + slr_list[i] + "]\n")
            #    #f_d.write("set_property gridtypes {SLICE DSP48E2 RAMB18 RAMB36 URAM288} [get_pblocks SLR" + slr_list[i] + "]\n")

            f_d.write("create_pblock XDMA\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA] [get_cells -quiet [list U50_i/XDMA]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA] -add {CLOCKREGION_X7Y0:CLOCKREGION_X7Y4 CLOCKREGION_X6Y2:CLOCKREGION_X6Y4}\n")
            #for i in range(len(slr_list)):
            #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] + "] -remove {CLOCKREGION_X7Y0:CLOCKREGION_X7Y4 CLOCKREGION_X6Y3:CLOCKREGION_X6Y4}\n")
            f_d.write("create_pblock XDMA_INC\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] [get_cells -quiet [list U50_XDMA_AXI_INC_i/XDMA_INC_0 U50_XDMA_AXI_LITE_INC_i/XDMA_M_AXI_LITE_INC_0]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA_INC] -add {CLOCKREGION_X6Y5:CLOCKREGION_X7Y5}\n")
            #for i in range(len(slr_list)):
            #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[i] + "] -remove {CLOCKREGION_X6Y5:CLOCKREGION_X7Y5}\n")

            ######################################################################################################
            ######################################################################################################
            for i in range(len(slr_list)) :
                slr_num = 'SLR' + slr_list[i]
                for j in range(2) :
                    if(j == 0):
                        if(int(slr_list[i]) == 0) :
                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")
                            flag = 0
                            for k in range(0, 8) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] -add {SLICE_X0Y0:SLICE_X" + str(7*flag-1) + "Y119 SLICE_X0Y0:SLICE_X56Y59}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT]\n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X0Y0:SLICE_X" + str(7*flag-1) + "Y119 SLICE_X0Y0:SLICE_X56Y29}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")

                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                            flag = 0
                            for k in range(8, 16) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] -add {SLICE_X57Y0:SLICE_X116Y59 SLICE_X" + str(116-7*flag+1) + "Y0:SLICE_X116Y119}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT]\n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X57Y0:SLICE_X116Y29 SLICE_X" + str(116-7*flag+1) + "Y0:SLICE_X116Y119}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                                
                        elif(int(slr_list[i]) == 1) :
                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")
                            flag = 0
                            for k in range(0, 8) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] -add {SLICE_X0Y240:SLICE_X" + str(7*flag-1) + "Y299}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT]\n")
                                f_d.write("")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X0Y240:SLICE_X" + str(7*flag-1) + "Y299}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")

                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                            flag = 0
                            for k in range(8, 16) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        +"]]\n")
                            if(flag != 0 ):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] -add {SLICE_X" + str(116-7*flag+1) + "Y240:SLICE_X116Y299}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT]\n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X" + str(116-7*flag+1) + "Y240:SLICE_X116Y299}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")

                    elif(j == 1):
                        if(int(slr_list[i]) == 0) :
                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")
                            flag = 0
                            for k in range(16, 24) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] -add {SLICE_X117Y0:SLICE_X" + str(117+7*flag-1) + "Y119 SLICE_X117Y0:SLICE_X175Y59}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] \n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X117Y0:SLICE_X" + str(117+7*flag-1) + "Y119 SLICE_X117Y0:SLICE_X175Y29}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")

                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                            flag = 0
                            for k in range(24, 32) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] -add {SLICE_X176Y0:SLICE_X232Y59 SLICE_X" + str(205-7*flag+1) + "Y30:SLICE_X205Y119}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] \n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X176Y0:SLICE_X232Y29 SLICE_X" + str(205-7*flag+1) + "Y30:SLICE_X205Y179}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")

                        elif(int(slr_list[i]) == 1) :
                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")
                            flag = 0 
                            for k in range(16, 24) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] -add {SLICE_X117Y240:SLICE_X" + str(117+7*flag-1) + "Y299}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT] \n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X117Y240:SLICE_X" + str(117+7*flag-1) + "Y299}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_LEFT\n")

                            f_d.write("create_pblock " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                            flag = 0
                            for k in range(24, 32) :
                                for l in range(len(hbm_port_intf_list[k])):
                                    if(hbm_port_intf_list[k][l] == slr_list[i]):
                                        flag = flag + 1
                                        f_d.write("add_cells_to_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] " )
                                        f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_INC_0 "
                                        +"]]\n")
                            if(flag != 0):
                                f_d.write("resize_pblock [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] -add {SLICE_X" + str(175-7*flag+1) + "Y240:SLICE_X175Y299}\n")
                                f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT] \n")
                                #for m in range(len(slr_list)):
                                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X" + str(175-7*flag+1) + "Y240:SLICE_X175Y299}\n")
                            elif(flag == 0):
                                f_d.write("delete_pblocks " + slr_num +"_TO_HBM" + str(j) + "_RIGHT\n")
                                
            ######################################################################################################
            ######################################################################################################
            slr_num = 'SLR1'
            for j in range(2):
                if(j == 0) :
                    f_d.write("create_pblock HBM" + str(j) +"_LEFT_SMC_BRIDGE\n")
                    flag = 0
                    for k in range(0, 8):
                        for l in range(len(hbm_port_intf_list[k])):
                            if(hbm_port_intf_list[k][l] == '1'):
                                flag = flag + 1
                                f_d.write("add_cells_to_pblock [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE] ")
                                f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                                f_d.write("set_property USER_SLL_REG TRUE [get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                    
                    if(flag != 0):
                        f_d.write("resize_pblock [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE] -add {SLICE_X0Y60:SLICE_X" + str(7*flag-1) + "Y239}\n")
                        f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE]\n")
                        #for m in range(len(slr_list)):
                        #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X0Y60:SLICE_X" +  str(7*flag-1) + "Y239}\n")
                    elif(flag == 0) :
                        f_d.write("delete_pblocks HBM" + str(j) +"_LEFT_SMC_BRIDGE\n")

                    f_d.write("create_pblock HBM" + str(j) +"_RIGHT_SMC_BRIDGE\n")
                    flag = 0
                    for k in range(8, 16):
                        for l in range(len(hbm_port_intf_list[k])):
                            if(hbm_port_intf_list[k][l] == '1'):
                                flag = flag + 1
                                f_d.write("add_cells_to_pblock [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] ")
                                f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                                f_d.write("set_property USER_SLL_REG TRUE [get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                    if(flag != 0):
                        f_d.write("resize_pblock [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] -add {SLICE_X" + str(116-7*flag+1) + "Y60:SLICE_X116Y239}\n")
                        f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE]\n")
                        #for m in range(len(slr_list)):
                        #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X" + str(116-7*flag+1) +"Y60:SLICE_X116Y239}\n")
                    elif(flag == 0):
                        f_d.write("delete_pblocks HBM" + str(j) +"_RIGHT_SMC_BRIDGE\n")

                elif(j == 1):
                    f_d.write("create_pblock HBM" + str(j) +"_LEFT_SMC_BRIDGE\n")
                    flag = 0
                    for k in range(16, 24):
                        for l in range(len(hbm_port_intf_list[k])):
                            if(hbm_port_intf_list[k][l] == '1'):
                                flag = flag + 1
                                f_d.write("add_cells_to_pblock [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE] ")
                                f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                                f_d.write("set_property USER_SLL_REG TRUE [get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")

                    if(flag != 0):
                        f_d.write("resize_pblock [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE] -add {SLICE_X117Y60:SLICE_X" + str(117+7*flag-1) + "Y239}\n")
                        f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM" + str(j) + "_LEFT_SMC_BRIDGE] \n")
                        #for m in range(len(slr_list)):
                        #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X117Y60:SLICE_X" + str(117+7*flag-1) + "Y239}\n")
                    elif(flag == 0):
                        f_d.write("delete_pblocks HBM" + str(j) +"_LEFT_SMC_BRIDGE\n")


                    f_d.write("create_pblock HBM" + str(j) +"_RIGHT_SMC_BRIDGE\n")
                    flag = 0
                    for k in range(24, 32):
                        for l in range(len(hbm_port_intf_list[k])):
                            if(hbm_port_intf_list[k][l] == '1'):
                                flag = flag + 1
                                f_d.write("add_cells_to_pblock [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] ")
                                f_d.write("[get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                                f_d.write("set_property USER_SLL_REG TRUE [get_cells -quiet [list " + board + "_AXI_INC_i/" + slr_num + "_TO_HBM{:02d}".format(k)+ "_SMC_0" +"]]\n")
                    if(flag != 0):
                        #f_d.write("resize_pblock [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] -add {SLICE_X" + str(175-7*flag+1) + "Y120:SLICE_X175Y239 SLICE_X" + str(175-7*flag+1) + "Y120:SLICE_X205Y179}\n")
                        f_d.write("resize_pblock [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] -add {SLICE_X" + str(175-7*flag+1) + "Y60:SLICE_X175Y239}\n")
                        f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM" + str(j) + "_RIGHT_SMC_BRIDGE] \n")
                        #for m in range(len(slr_list)):
                        #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X" + str(175-7*flag+1) + "Y120:SLICE_X175Y239 SLICE_X" + str(175-7*flag+2) + "Y120:SLICE_X205Y179}\n")
                    elif(flag == 0):
                        f_d.write("delete_pblocks HBM" + str(j) +"_RIGHT_SMC_BRIDGE\n")
                
            if 'true' in total_hbm_port_list[0:7] :
                f_d.write("create_pblock HBM0_LEFT\n")
                f_d.write("resize_pblock [get_pblocks HBM0_LEFT] -add {SLICE_X0Y0:SLICE_X56Y59}\n")
                #f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM0_LEFT]\n")
                #for m in range(len(slr_list)):
                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X0Y0:SLICE_X56Y29}\n")
                for i in range(0,8):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM0_LEFT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[8:15]:
                f_d.write("create_pblock HBM0_RIGHT\n")
                f_d.write("resize_pblock [get_pblocks HBM0_RIGHT] -add {SLICE_X57Y0:SLICE_X116Y59}\n")
                #f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM0_RIGHT]\n")
                #for m in range(len(slr_list)):
                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X57Y0:SLICE_X116Y29}\n")
                for i in range(8,16):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM0_RIGHT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[16:23]:
                f_d.write("create_pblock HBM1_LEFT\n")
                f_d.write("resize_pblock [get_pblocks HBM1_LEFT] -add {SLICE_X117Y0:SLICE_X175Y59}\n")
                #f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM1_LEFT]\n")
                #for m in range(len(slr_list)):
                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X117Y0:SLICE_X175Y29}\n")
                for i in range(16,24):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM1_LEFT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[24:31]:
                f_d.write("create_pblock HBM1_RIGHT\n")
                f_d.write("resize_pblock [get_pblocks HBM1_RIGHT] -add {SLICE_X176Y0:SLICE_X232Y59}\n")
                #f_d.write("set_property gridtypes {SLICE LAGUNA} [get_pblocks HBM1_RIGHT]\n")
                #for m in range(len(slr_list)):
                #    f_d.write("resize_pblock [get_pblocks SLR" + slr_list[m] + "] -remove {SLICE_X176Y0:SLICE_X232Y29}\n")
                for i in range(24,32):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM1_RIGHT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
                    


        #End of U50 descriptor
        #for i in range(len(slr_list)):
        #    f_d.write("add_cells_to_pblock [get_pblocks SLR" + slr_list[i] + "]"
        #    + " [get_cells -quiet [list User_Logic_i/SLR" + slr_list[i] + "_i]] \n")

    return