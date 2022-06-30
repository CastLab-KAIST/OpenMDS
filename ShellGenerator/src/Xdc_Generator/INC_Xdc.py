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
            xdma_ddr_ch_list=None, ddr_slr_list=None, ddr_ch_list=None, version="2020.2") :
    
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

    gen_xdc = os.path.join(filedir, "INC.xdc")

    with open(gen_xdc, 'w') as f_d:
        if(board == 'VCU118') :
            f_d.write("create_pblock XDMA\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA] [get_cells -quiet [list " + board + "_i/XDMA]] \n")
            f_d.write("resize_pblock [get_pblocks XDMA] -add {CLOCKREGION_X4Y5:CLOCKREGION_X5Y9}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks XDMA]\n")

            f_d.write("create_pblock XDMA_PCIE\n")
            if(version == "2020.1"):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4_ip_i]]\n")
            elif(version == "2020.2"):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4c_ip_i]]\n")
            else:
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4c_ip_i]]\n")

            f_d.write("resize_pblock [get_pblocks XDMA_PCIE] -add {CLOCKREGION_X5Y5:CLOCKREGION_X5Y9}\n")

            f_d.write("create_pblock XDMA_INC\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] "
            +"[get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_INC_0 "+ board +"_XDMA_AXI_LITE_INC_i/XDMA_INC_0]] \n")
            f_d.write("resize_pblock [get_pblocks XDMA_INC] -add {CLOCKREGION_X3Y5:CLOCKREGION_X3Y9}\n")
            f_d.write("set_property CONTAIN_ROUTING false [get_pblocks XDMA_INC]\n")

            f_d.write("#SLR HOST SMC\n")
            for i in range(len(slr_list)):
                f_d.write("create_pblock XDMA_TO_SLR" + slr_list[i] + "\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_SLR" + slr_list[i] +"] -add {SLR" + slr_list[i] + "}\n")

                f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] "
                +"[get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR" + slr_list[i] + "_HOST_SMC_0]] \n")
                
                if(int(slr_list[i]) != 1):
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/*master*]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_SLR" + slr_list[i] + "] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0/*slave*]\n")

                elif(int(slr_list[i]) == 1):
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_SLR" + slr_list[i] + "] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR" + slr_list[i] + "_HOST_REG_0]\n")


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

            if(xdma_ddr_ch_list != None):
                for i in range(len(xdma_ddr_ch_list)):
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_SMC_0]\n")
                    
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_REG_0/*slr_master*]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks DDR" + xdma_ddr_ch_list[i] + "_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_DDR" + xdma_ddr_ch_list[i] + "_REG_0/*slr_slave*]\n")
            
            ## SLR_TO_DDR INC, SMC Bridge Generation
            slr2_ddr0_flag = 0
            slr2_ddr1_flag = 0
            slr1_ddr0_flag = 0
            slr1_ddr1_flag = 0
            slr0_ddr0_flag = 0
            slr0_ddr1_flag = 0

            if(ddr_slr_list!=None):
                for i in range(len(ddr_slr_list)):
                    if(int(ddr_slr_list[i]) == 0):
                        if(int(ddr_ch_list[i]) == 0):
                            slr0_ddr0_flag = slr0_ddr0_flag + 1
                        elif(int(ddr_ch_list[i]) == 1):
                            slr0_ddr1_flag = slr0_ddr1_flag + 1
                    elif(int(ddr_slr_list[i]) == 1):
                        if(int(ddr_ch_list[i]) == 0):
                            slr1_ddr0_flag = slr1_ddr0_flag + 1
                        elif(int(ddr_ch_list[i]) == 1):
                            slr1_ddr1_flag = slr1_ddr1_flag + 1
                    elif(int(ddr_slr_list[i]) == 2):
                        if(int(ddr_ch_list[i]) == 0):
                            slr2_ddr0_flag = slr2_ddr0_flag + 1
                        elif(int(ddr_ch_list[i]) == 1):
                            slr2_ddr1_flag = slr2_ddr1_flag + 1
                
                if(slr0_ddr0_flag != 0 or slr0_ddr1_flag != 0):
                    f_d.write("create_pblock SLR0_TO_DDR\n")
                    f_d.write("resize_pblock [get_pblocks SLR0_TO_DDR] -add {CLOCKREGION_X0Y0:CLOCKREGION_X0Y4 CLOCKREGION_X0Y4:CLOCKREGION_X2Y4}\n")
                if(slr1_ddr0_flag != 0 or slr1_ddr1_flag != 0 or slr2_ddr1_flag != 0 or slr0_ddr0_flag != 0):
                    f_d.write("create_pblock SLR1_TO_DDR\n")
                    f_d.write("resize_pblock [get_pblocks SLR1_TO_DDR] -add {CLOCKREGION_X0Y5:CLOCKREGION_X0Y9 CLOCKREGION_X0Y5:CLOCKREGION_X2Y5 CLOCKREGION_X0Y9:CLOCKREGION_X2Y9}\n")
                if(slr2_ddr0_flag != 0 or slr2_ddr1_flag != 0):
                    f_d.write("create_pblock SLR2_TO_DDR\n")
                    f_d.write("resize_pblock [get_pblocks SLR2_TO_DDR] -add {CLOCKREGION_X0Y10:CLOCKREGION_X0Y14 CLOCKREGION_X0Y10:CLOCKREGION_X2Y10}\n")
            
                if(slr0_ddr0_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR0_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR0_TO_DDR0_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR0_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR0_TO_DDR0_SMC_0]]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR0_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR0_TO_DDR0_REG_0/*slr_master*]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR0_TO_DDR0_REG_0/*slr_middle*]\n")
                
                    f_d.write("add_cells_to_pblock [get_pblocks DDR0_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR0_TO_DDR0_REG_0/*slr_slave*]\n")
                
                if(slr0_ddr1_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR0_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR0_TO_DDR1_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR0_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR0_TO_DDR1_SMC_0]]\n")
                if(slr1_ddr0_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR0_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR0_SMC_0]]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR1_TO_DDR0_REG_0/*slr_master*]\n")
                
                    f_d.write("add_cells_to_pblock [get_pblocks DDR0_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR1_TO_DDR0_REG_0/*slr_slave*]\n")
                if(slr1_ddr1_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR1_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR1_TO_DDR1_SMC_0]]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR1_TO_DDR1_REG_0/*slr_master*]\n")
                
                    f_d.write("add_cells_to_pblock [get_pblocks DDR1_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR1_TO_DDR1_REG_0/*slr_slave*]\n")
                if(slr2_ddr0_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR2_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR2_TO_DDR0_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR2_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR2_TO_DDR0_SMC_0]]\n")
                if(slr2_ddr1_flag != 0):
                    f_d.write("add_cells_to_pblock [get_pblocks SLR2_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR2_TO_DDR1_INC_0]]\n")
                    f_d.write("add_cells_to_pblock [get_pblocks SLR2_TO_DDR] [get_cells -quiet [list " + board + "_AXI_INC_i/SLR2_TO_DDR1_SMC_0]]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR2_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR2_TO_DDR1_REG_0/*slr_master*]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks SLR1_TO_DDR] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR2_TO_DDR1_REG_0/*slr_middle*]\n")
                
                    f_d.write("add_cells_to_pblock [get_pblocks DDR1_INC] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR2_TO_DDR1_REG_0/*slr_slave*]\n")
        #End of VCU118
#########################
#########################
#########################
        elif(board == 'U50') :
            total_hbm_port_list = ['false' for i in range(32)]
            hbm_port_intf_list = [[]for i in range(32)]
            total_hbm_port_list[int(xdma_hbm_port)] = 'true'
            hbm_port_intf_list[int(xdma_hbm_port)].append('xdma')
            for i in range(len(hbm_port_list)) :
                total_hbm_port_list[int(hbm_port_list[i])] = 'true'
                hbm_port_intf_list[int(hbm_port_list[i])].append(hbm_slr_list[i])
            
            # XDMA Pblock
            f_d.write("create_pblock XDMA\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA] [get_cells -quiet [list " + board + "_i/XDMA]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA] -add {CLOCKREGION_X7Y0:CLOCKREGION_X7Y7 CLOCKREGION_X6Y3:CLOCKREGION_X6Y4}\n")

            f_d.write("create_pblock XDMA_PCIE\n")
            if(version == "2020.1"):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4_ip_i]]\n")
            elif(version == "2020.2"):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4c_ip_i]]\n")
            else:
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_PCIE] [get_cells -quiet [list " + board + "_i/XDMA/inst/pcie4c_ip_i]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA_PCIE] -add {CLOCKREGION_X7Y0:CLOCKREGION_X7Y3 CLOCKREGION_X6Y3:CLOCKREGION_X6Y3}\n")

            f_d.write("create_pblock XDMA_UDMA\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA_UDMA] [get_cells -quiet [list " + board + "_i/XDMA/inst/udma_wrapper " + board +"_i/XDMA/inst/ram_top]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA_UDMA] -add {CLOCKREGION_X7Y4:CLOCKREGION_X7Y7 CLOCKREGION_X6Y4:CLOCKREGION_X6Y4}\n")

            f_d.write("create_pblock XDMA_INC\n")
            f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] [get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_INC_0]]\n")
            f_d.write("resize_pblock [get_pblocks XDMA_INC] -add {CLOCKREGION_X4Y7:CLOCKREGION_X7Y7}\n")

            if("0" in slr_list):
                f_d.write("create_pblock XDMA_TO_SLR1\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_SLR1] -add {SLR1}\n")
                f_d.write("create_pblock XDMA_TO_SLR0\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_SLR0] -add {SLR0}\n")
            
            elif("1" in slr_list):
                f_d.write("create_pblock XDMA_TO_SLR1\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_SLR1] -add {SLR1}\n")


            for i in range(len(slr_list)):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] [get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR{:01d}_HOST".format(int(slr_list[i])) + "_SMC_0]]\n")
                if(int(slr_list[i]) == 0):
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_SLR1] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR{:01d}_HOST".format(int(slr_list[i])) + "_REG_0/*slr_master*]\n")

                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_SLR0] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR{:01d}_HOST".format(int(slr_list[i])) + "_REG_0/*slr_slave*]\n")

                elif(int(slr_list[i]) == 1):
                    f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_SLR1] "
                    + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_SLR{:01d}_HOST".format(int(slr_list[i])) + "_REG_0]\n")


            if(xdma_hbm_port!=None):
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_INC] [get_cells -quiet [list " + board + "_XDMA_AXI_INC_i/XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_SMC_0]]\n")
                
                f_d.write("create_pblock XDMA_TO_MEM_SLR1\n")
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_MEM_SLR1] "
                + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0/*slr_master*]\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_MEM_SLR1] -add {SLR1}\n")
                f_d.write("create_pblock XDMA_TO_MEM_SLR0\n")
                f_d.write("add_cells_to_pblock [get_pblocks XDMA_TO_MEM_SLR0] "
                + "[get_cells -hierarchical -filter NAME=~*" + board + "_XDMA_AXI_INC_i/XDMA_TO_HBM{:02d}".format(int(xdma_hbm_port)) + "_REG_0/*slr_slave*]\n")
                f_d.write("resize_pblock [get_pblocks XDMA_TO_MEM_SLR0] -add {SLR0}\n")


            ######################################################################################################
            ######################################################################################################
            # SLR TO HBM INC and SMC
            # Flag Generation
            slr1_hbm0_left_flag = 0
            slr1_hbm0_right_flag = 0
            slr1_hbm1_left_flag = 0
            slr1_hbm1_right_flag = 0
            slr0_hbm0_left_flag = 0
            slr0_hbm0_right_flag = 0
            slr0_hbm1_left_flag = 0
            slr0_hbm1_right_flag = 0
            if(hbm_slr_list!=None):
                for i in range(len(hbm_slr_list)):
                    if(int(hbm_slr_list[i]) == 0):
                        if(int(hbm_port_list[i]) < 8):
                            slr0_hbm0_left_flag = slr0_hbm0_left_flag + 1
                        elif(int(hbm_port_list[i]) < 16):
                            slr0_hbm0_right_flag = slr0_hbm0_right_flag + 1
                        elif(int(hbm_port_list[i]) < 24):
                            slr0_hbm1_left_flag = slr0_hbm1_left_flag + 1
                        elif(int(hbm_port_list[i]) < 32):
                            slr0_hbm1_right_flag = slr0_hbm1_right_flag + 1
                        else :
                            print("ERROR hbm_port_list should be 0~31")
                            return os.exit()

                    elif(int(hbm_slr_list[i]) == 1):
                        if(int(hbm_port_list[i]) < 8):
                            slr1_hbm0_left_flag = slr1_hbm0_left_flag + 1
                        elif(int(hbm_port_list[i]) < 16):
                            slr1_hbm0_right_flag = slr1_hbm0_right_flag + 1
                        elif(int(hbm_port_list[i]) < 24):
                            slr1_hbm1_left_flag = slr1_hbm1_left_flag + 1
                        elif(int(hbm_port_list[i]) < 32):
                            slr1_hbm1_right_flag = slr1_hbm1_right_flag + 1
                        else :
                            print("ERROR hbm_port_list should be 0~31")
                            return os.exit()

                    else:
                        print("ERROR hbm_slr_list should be 0~1")
                        return os.exit()
            # Flag Generation Done
            
            f_d.write("\n## PBLOCK Generation ##\n\n")
            # PBLOCK Generation
            # SLR_HBM_INC Generation

            if(slr1_hbm0_left_flag != 0):
                f_d.write("create_pblock SLR1_HBM0_LEFT_SMC_BRIDGE\n")
                f_d.write("create_pblock SLR0_HBM0_LEFT_SMC_BRIDGE\n")

            elif(slr0_hbm0_left_flag != 0):
                f_d.write("create_pblock SLR0_HBM0_LEFT_SMC_BRIDGE\n")
                
            if(slr1_hbm0_right_flag != 0):
                f_d.write("create_pblock SLR1_HBM0_RIGHT_SMC_BRIDGE\n")
                f_d.write("create_pblock SLR0_HBM0_RIGHT_SMC_BRIDGE\n")
                
            elif(slr0_hbm0_right_flag != 0):
                f_d.write("create_pblock SLR0_HBM0_RIGHT_SMC_BRIDGE\n")                

            
            if(slr1_hbm1_left_flag != 0):
                f_d.write("create_pblock SLR1_HBM1_LEFT_SMC_BRIDGE\n")
                f_d.write("create_pblock SLR0_HBM1_LEFT_SMC_BRIDGE\n")

            elif(slr0_hbm1_left_flag != 0):
                f_d.write("create_pblock SLR0_HBM1_LEFT_SMC_BRIDGE\n")


            if(slr1_hbm1_right_flag != 0):
                f_d.write("create_pblock SLR1_HBM1_RIGHT_SMC_BRIDGE\n")
                f_d.write("create_pblock SLR0_HBM1_RIGHT_SMC_BRIDGE\n")

            elif(slr0_hbm1_right_flag != 0):
                f_d.write("create_pblock SLR0_HBM1_RIGHT_SMC_BRIDGE\n")

            # Pblock SLR_HBM_SMC_BRIDGE Generation Done
            
            # Module PBLOCK Assign
            # SLR_HBM_INC Assign
            if(hbm_slr_list!=None):
                for i in range(len(hbm_slr_list)):
                    if(int(hbm_port_list[i]) < 8):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_".format(int(hbm_slr_list[i])) + "HBM0_LEFT_SMC_BRIDGE] "
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_INC_0]]\n")                
                    elif(int(hbm_port_list[i]) < 16):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_".format(int(hbm_slr_list[i])) + "HBM0_RIGHT_SMC_BRIDGE] "
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_INC_0]]\n")     
                    elif(int(hbm_port_list[i]) < 24):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_".format(int(hbm_slr_list[i])) + "HBM1_LEFT_SMC_BRIDGE] "
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_INC_0]]\n")
                    elif(int(hbm_port_list[i]) < 32):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_".format(int(hbm_slr_list[i])) + "HBM1_RIGHT_SMC_BRIDGE] "
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_INC_0]]\n")
                # SLR_HBM_INC Assign Done
                # SLR_HBM_SMC Assign
                for i in range(len(hbm_slr_list)):
                    if(int(hbm_port_list[i]) < 8):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_HBM0_LEFT_SMC_BRIDGE] ".format(int(hbm_slr_list[i]))
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_SMC_0]]\n")         
                    elif(int(hbm_port_list[i]) < 16):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_HBM0_RIGHT_SMC_BRIDGE] ".format(int(hbm_slr_list[i]))
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_SMC_0]]\n")   
                    elif(int(hbm_port_list[i]) < 24):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_HBM1_LEFT_SMC_BRIDGE] ".format(int(hbm_slr_list[i]))
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_SMC_0]]\n")
                    elif(int(hbm_port_list[i]) < 32):
                        f_d.write("add_cells_to_pblock [get_pblocks SLR{:01d}_HBM1_RIGHT_SMC_BRIDGE] ".format(int(hbm_slr_list[i]))
                        + "[get_cells -quiet [list " + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_SMC_0]]\n")   
    
                    if(int(hbm_slr_list[i]) == 1):
                        if(int(hbm_port_list[i]) < 8):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_HBM0_LEFT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_master*]\n")         
                        elif(int(hbm_port_list[i]) < 16):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_HBM0_RIGHT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_master*]\n")
                        elif(int(hbm_port_list[i]) < 24):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_HBM1_LEFT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_master*]\n")
                        elif(int(hbm_port_list[i]) < 32):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR1_HBM1_RIGHT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_master*]\n")

                        if(int(hbm_port_list[i]) < 8):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR0_HBM0_LEFT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_slave*]\n")         
                        elif(int(hbm_port_list[i]) < 16):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR0_HBM0_RIGHT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_slave*]\n")
                        elif(int(hbm_port_list[i]) < 24):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR0_HBM1_LEFT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_slave*]\n")
                        elif(int(hbm_port_list[i]) < 32):
                            f_d.write("add_cells_to_pblock [get_pblocks SLR0_HBM1_RIGHT_SMC_BRIDGE] "
                            + "[get_cells -hierarchical -filter NAME=~*" + board + "_AXI_INC_i/SLR{:01d}_TO_".format(int(hbm_slr_list[i])) +  "HBM{:02d}".format(int(hbm_port_list[i])) + "_REG_0/*slr_slave*]\n")

            # Module PBLOCK Assign Done
            f_d.write("\n## PBLOCK Resize ##\n\n")
            # PBLOCK Resize
            # For Outer region add
            initial_param = 0 # to give initial space for SMC Bridge
            width_param = 7
            hbm0_right_slice_x_end=116
            hbm1_left_slice_x_start=117


            if(slr1_hbm0_left_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR1_HBM0_LEFT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X0Y240:SLICE_X" + str(0 + (width_param*(slr1_hbm0_left_flag) - 1) + initial_param) + "Y479 SLICE_X0Y240:SLICE_X56Y299} \n")       
                         
            if(slr1_hbm0_right_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR1_HBM0_RIGHT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(hbm0_right_slice_x_end - (width_param*(slr1_hbm0_right_flag) - 1) + initial_param) + "Y240:SLICE_X" + str(hbm0_right_slice_x_end) + "Y479} \n")
            
                
            if(slr1_hbm1_left_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR1_HBM1_LEFT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(hbm1_left_slice_x_start) + "Y240:SLICE_X" + str(hbm1_left_slice_x_start + (width_param*(slr1_hbm1_left_flag) - 1) + initial_param) + "Y479 SLICE_X117Y240:SLICE_X175Y299} \n")
                
            if(slr1_hbm1_right_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR1_HBM1_RIGHT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(175 - (width_param*(slr1_hbm1_right_flag) - 1)) + "Y240:SLICE_X205Y479 SLICE_X146Y240:SLICE_X205Y299} \n")
                
            

            if(slr0_hbm0_left_flag != 0 or slr1_hbm0_left_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR0_HBM0_LEFT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X0Y0:SLICE_X" + str(0 + (width_param*(slr0_hbm0_left_flag + slr1_hbm0_left_flag) - 1) + initial_param) + "Y239 SLICE_X0Y0:SLICE_X56Y59 SLICE_X0Y180:SLICE_X56Y239} \n")
            if(slr0_hbm0_right_flag != 0 or slr1_hbm0_right_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR0_HBM0_RIGHT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(hbm0_right_slice_x_end - (width_param*(slr0_hbm0_right_flag + slr1_hbm0_right_flag) - 1) + initial_param) + "Y0:SLICE_X" + str(hbm0_right_slice_x_end) + "Y239 SLICE_X57Y0:SLICE_X116Y59 SLICE_X57Y180:SLICE_X116Y239} \n")
            if(slr0_hbm1_left_flag != 0 or slr1_hbm1_left_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR0_HBM1_LEFT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(hbm1_left_slice_x_start) + "Y0:SLICE_X" + str(hbm1_left_slice_x_start + (width_param*(slr0_hbm1_left_flag + slr1_hbm1_left_flag) - 1) + initial_param) + "Y239 SLICE_X117Y0:SLICE_X175Y59 SLICE_X117Y180:SLICE_X175Y239} \n")
            if(slr0_hbm1_right_flag != 0 or slr1_hbm1_right_flag != 0):
                f_d.write("resize_pblock [get_pblocks SLR0_HBM1_RIGHT_SMC_BRIDGE] -add ")
                f_d.write("{SLICE_X" + str(205 - (width_param*(slr0_hbm1_right_flag + slr1_hbm1_right_flag) - 1) + initial_param) + "Y0:SLICE_X205Y239 SLICE_X176Y0:SLICE_X232Y59 SLICE_X176Y180:SLICE_X232Y239} \n")
            # PBLOCK Resize Done
            ######################################################################################################
            ######################################################################################################
            # HBM INC Pblock
                
            if 'true' in total_hbm_port_list[0:7] :
                f_d.write("create_pblock HBM0_LEFT\n")
                f_d.write("resize_pblock [get_pblocks HBM0_LEFT] -add {SLICE_X0Y0:SLICE_X56Y59}\n")

                for i in range(0,8):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM0_LEFT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[8:15]:
                f_d.write("create_pblock HBM0_RIGHT\n")
                f_d.write("resize_pblock [get_pblocks HBM0_RIGHT] -add {SLICE_X57Y0:SLICE_X116Y59}\n")

                for i in range(8,16):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM0_RIGHT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[16:23]:
                f_d.write("create_pblock HBM1_LEFT\n")
                f_d.write("resize_pblock [get_pblocks HBM1_LEFT] -add {SLICE_X117Y0:SLICE_X175Y59}\n")

                for i in range(16,24):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM1_LEFT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")
            if 'true' in total_hbm_port_list[24:31]:
                f_d.write("create_pblock HBM1_RIGHT\n")
                f_d.write("resize_pblock [get_pblocks HBM1_RIGHT] -add {SLICE_X176Y0:SLICE_X232Y59}\n")

                for i in range(24,32):
                    if(total_hbm_port_list[i] == 'true'):
                        f_d.write("add_cells_to_pblock [get_pblocks HBM1_RIGHT] [get_cells -quiet [list " + board + "_HBM_AXI_INC_i/HBM{:02d}".format(i) + "_INC_0]]\n")

        #End of U50 descriptor
#########################
#########################
#########################
    return