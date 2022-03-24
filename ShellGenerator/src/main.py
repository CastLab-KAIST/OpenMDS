################################################################
# Library
################################################################
import os, shutil
import argparse
import configparser

# Import Python Files 
from Tcl_Generator.AXI_INC_Tcl import *
from Tcl_Generator.XDMA_AXI_INC_Tcl import *
from Tcl_Generator.XDMA_AXI_Lite_INC_Tcl import *
from Tcl_Generator.Crossing_AXIS_Tcl import *
from Tcl_Generator.Crossing_AXILite_Tcl import *
from Tcl_Generator.HBM_Tcl import *
from Tcl_Generator.HBM_AXI_INC_Tcl import *
from Tcl_Generator.VCU118_Tcl import *
from Tcl_Generator.U50_Tcl import *
from Code_Generator.Board_Wrapper import *
from Code_Generator.Shell_Params import *
from Code_Generator.SLR_Wrapper import *
from Code_Generator.UserLogic import *
from Tcl_Generator.DDR_Tcl import *
from Tcl_Generator.DDR_AXI_INC_Tcl import *
from Tcl_Generator.CLK_WIZ_Tcl import CLK_WIZ_Tcl
from Xdc_Generator.SLR_Xdc import *
from Xdc_Generator.INC_Xdc import *
from Xdc_Generator.CLK_Xdc import *
from Xdc_Generator.PIN_Xdc import *
################################################################
# Colors
################################################################

RED = '\033[01;91m'
GREEN = '\033[01;32m'
BLUE = '\033[01;34m'
WHITE = '\033[00m'

PASS = f"{GREEN}Pass {WHITE}"
FAIL = f"{RED}Fail {WHITE}"
ERROR = f"{RED}Error{WHITE}"

################################################################
# Config Constants
################################################################

# Board Config File
board_config = configparser.ConfigParser()
# For Bin File
if getattr(sys, 'frozen', False):
    exe_path = os.path.dirname(sys.executable)
    ref_dir = exe_path
    board_property = os.path.join(exe_path, 'boards.ini')
# For Python File
elif __file__:
    exe_path = os.path.dirname(__file__)
    ref_dir = os.path.join(exe_path, 'Reference/')
    board_property = os.path.join(ref_dir, 'boards.ini')
board_config.read(board_property)

################################################################
# Arguments
################################################################

parser = argparse.ArgumentParser(description='Vivado Shell Script')
parser.add_argument('--board', default='VCU118', type=str,
                    help='Name of FPGA Board')

parser.add_argument('--file', default=None, type=str,
                    help='Path to .ini file that contains options')

parser.add_argument('--dir', default='shell/', type=str,
                    help='Path to directory that saves MDS shell')

parser.add_argument('--slr', default='0', type=str,
                    help='SLR ID that you need')

parser.add_argument('--freq',default='200', type=str,
                    help='Frequency for each SLR')

parser.add_argument('--host_width', default='256,256,256', type=str,
                    help='The data_width of host for each SLR')

parser.add_argument('--ddr_dma', default='5,5,5', type=str,
                    help='The number of each SLR DDR DMA')

parser.add_argument('--ddr_dma_width', default='256,256,256', type=str,
                    help='Data-width of each SLR DDR DMA')

parser.add_argument('--xdma_hbm_port', default='0', type=str,
                    help='AXI Channel ID of HBM XDMA')

parser.add_argument('--hbm_slr', default='0,1', type=str,
                    help='SLR ID list for connection of SLR-HBM')

parser.add_argument('--hbm_port', default='256,256,256', type=str,
                    help='AXI Channel ID list for connection of SLR-HBM')

parser.add_argument('--hbm_dma', default='5,5,5', type=str,
                    help='The number of HBM DMA')

parser.add_argument('--hbm_dma_width', default='256,256,256', type=str,
                    help='Data-width of HBM DMA')

parser.add_argument('--crossing', dest='crossing', action='store_true',
                    help='SLR crossing')

parser.add_argument('--fifo_src', dest='fifo_src', type=str,
                    help='SLR ID for AXI FIFO source')

parser.add_argument('--fifo_dest', dest='fifo_dest', type=str,
                    help='SLR ID for AXI FIFO destination')

parser.add_argument('--fifo_number', dest='fifo_number', type=str,
                    help='The number of AXI FIFO')

parser.add_argument('--fifo_width', dest='fifo_width', type=str,
                    help='Data-width of AXI FIFO')

################################################################
# Main
################################################################

def main(args):
    print("="*74 + "\n Vivado Shell Generator\n" + "="*74)
    ############################################################
    # 1. Setting Options
    print("[Info ] Loading Shell Parameters...")

    # Set Board 
    board = args.board
    
    # Load Options by Arguments
    if args.file is None:
        config = config_dict(board_config[board], args=args, file_mode=False)
        crossing = args.crossing
        # SLR Crossing
        if crossing:
            fifo_config = fifo_dict(args=args, file_mode=False)
    # Load Options by .ini File
    else:
        options = configparser.ConfigParser()
        options.read(args.file)
        config = config_dict(board_config[board], ifile=options, file_mode=True)
        crossing = (options["Crossing"]["cross"].lower() == "true")
        # SLR Crossing
        if crossing:
            fifo_config = fifo_dict(ifile=options, file_mode=True)
    print("[{}] Parameter Load Complete!".format(PASS))
    ############################################################
    # 2. Check Options and Make lists
    print("[Info ] Checking Shell Parameters...")
    dma_type = board_config[board]["DMA"].split()
    
    bd_dir, wrapper_dir, xdc_dir =  dir_check(args.dir, board)
    
    for files in os.listdir(xdc_dir):
        path = os.path.join(xdc_dir, files)
        file_check, ext_check = os.path.splitext(path)
        if(ext_check ==".xdc"):
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

    for files in os.listdir(wrapper_dir):
        path = os.path.join(wrapper_dir, files)
        file_check, ext_check = os.path.splitext(path)
        if(ext_check ==".sv"):
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
    
    for files in os.listdir(bd_dir):
        path = os.path.join(bd_dir, files)
        file_check, ext_check = os.path.splitext(path)
        if(ext_check ==".tcl"):
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

    slr_list, slr_freq_list, slr_host_width_list = slr_config(config)
    

    # Memory Type
    if "ddr" in dma_type:
        ddr_dma_max = int(board_config[board]["DDR"])
        ddr_dma_list, ddr_dma_width, xdma_ddr_ch, ddr_slr_list, ddr_ch_list = ddr_dma_config(config, ddr_dma_max)
    else :
        ddr_dma_max = None
        ddr_dma_list, ddr_dma_width, xdma_ddr_ch, ddr_slr_list, ddr_ch_list = None, None, None, None, None

    if "hbm" in dma_type:
        hbm_dma_max = int(board_config[board]["HBM"])
        xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq = hbm_dma_config(config, hbm_dma_max)
    
    else :
        hbm_dma_max = None
        xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq = None, None, None, None, None, None

    
    slr_list, slr_freq_list, slr_host_width_list, \
    xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, \
    xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq = \
    shell_param_check(slr_list, slr_freq_list, slr_host_width_list, 
            xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, 
            xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq)

    # Check ddr_dma_list slr_list
    if 'ddr' in dma_type:
        if(ddr_dma_list != None) :
            if len(slr_list) != len(ddr_dma_list) or \
            len(slr_list) != len(ddr_dma_width) :
                print("[{}] Diffrent Num of SLR and DDR_dma Options!".format(ERROR))
                exit()

    # SLR Crossing FIFO
    if crossing:
        src_list = fifo_config["fifo_src"].split(",")
        dest_list = fifo_config["fifo_dest"].split(",")
        num_list = fifo_config["fifo_number"].split(",")
        data_width_list = fifo_config["fifo_width"].split(",")
        # Check Length of Lists
        if  len(src_list) != len(dest_list)  or \
            len(src_list) != len(num_list)   or \
            len(src_list) != len(data_width_list):
            print("[{}] Wrong FIFO Options!".format(ERROR))
            exit()
    else:
        src_list = None
        dest_list = None
        num_list = None
        data_width_list = None
    print("[{}] Parameter Check Complete!".format(PASS))
    ############################################################
    # 3. Tcl Generator
    print("="*74 + "\n Tcl Generator\n" + "="*74)

    # Board Block Design
    if(board == 'VCU118') :
        slr_phy_list = ['0','1','2']
        slr_phy_freq_list = ['300','300','300']
        for i in range (len(slr_list)):
            for j in range(len(slr_phy_list)):
                if(slr_list[i] == slr_phy_list[j]):
                    slr_phy_freq_list[j] = slr_freq_list[i]
        VCU118_Tcl(bd_dir, ref_dir, slr_phy_freq_list)
    elif(board == 'U50') :
        slr_phy_list = ['0','1']
        slr_phy_freq_list = ['300','300']
        for i in range (len(slr_list)):
            for j in range(len(slr_phy_list)):
                if(slr_list[i] == slr_phy_list[j]):
                    slr_phy_freq_list[j] = slr_freq_list[i]
        U50_Tcl(bd_dir, ref_dir, slr_phy_freq_list, hbm_clk_freq=hbm_clk_freq)
    print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}.tcl".format(board))))

    # CLK WIZ
    CLK_WIZ_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, slr_freq_list=slr_phy_freq_list, hbm_clk_freq=hbm_clk_freq)
    print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_CLK_WIZ.tcl".format(board))))

    # XDMA_AXI Interconnet
    XDMA_AXI_INC_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, slr_list=slr_list, slr_freq_list=slr_freq_list, host_width_list=slr_host_width_list,
                xdma_ddr_ch_list=xdma_ddr_ch, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list ,ddr_dma_list=ddr_dma_list, ddr_dma_width_list=ddr_dma_width,
                hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, hbm_dma_list=hbm_dma_list, hbm_dma_width_list=hbm_dma_width_list, xdma_hbm_port=xdma_hbm_port, hbm_clk_freq=hbm_clk_freq)
    print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_XDMA_AXI_INC.tcl".format(board))))
    
    # AXI-Lite InterConnect
    XDMA_AXI_Lite_INC_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, slr_list=slr_list, slr_freq_list=slr_freq_list) 
    print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_XDMA_AXI_LITE_INC.tcl".format(board))))

    # AXI InterConnect
    AXI_INC_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, slr_list=slr_list, slr_freq_list=slr_freq_list, host_width_list=slr_host_width_list,
                xdma_ddr_ch_list=xdma_ddr_ch, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list ,ddr_dma_list=ddr_dma_list, ddr_dma_width_list=ddr_dma_width,
                hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, hbm_dma_list=hbm_dma_list, hbm_dma_width_list=hbm_dma_width_list, xdma_hbm_port=xdma_hbm_port, hbm_clk_freq=hbm_clk_freq)
    print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_AXI_INC.tcl".format(board))))

    # DDR Block Design
    if "ddr" in dma_type:
        DDR_Tcl(bd_dir, ref_dir, board, xdma_ddr_ch=xdma_ddr_ch, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_DDR.tcl".format(board))))
        DDR_AXI_INC_Tcl(bd_dir, ref_dir, board, xdma_ddr_ch=xdma_ddr_ch, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_DDR_AXI_INC.tcl".format(board))))

    # HBM Block Design
    if "hbm" in dma_type:
        HBM_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, 
                hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, xdma_hbm_port=xdma_hbm_port, hbm_clk_freq=hbm_clk_freq)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_HBM.tcl".format(board))))
        HBM_AXI_INC_Tcl(filedir=bd_dir, refdir=ref_dir, board=board, 
                        hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, xdma_hbm_port=xdma_hbm_port, hbm_clk_freq=hbm_clk_freq)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "{}_HBM_AXI_INC.tcl".format(board))))

    # SLR Crossing
    if crossing:
        Crossing_AXILite_Tcl(filedir=bd_dir, refdir=ref_dir, slr_list=slr_list, slr_freq_list=slr_freq_list)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "CROSSING_AXI_LITE.tcl")))
    
        Crossing_AXIS_Tcl(filedir=bd_dir, refdir=ref_dir, slr_list=slr_list, slr_freq_list=slr_freq_list,
                          src_list=src_list, dest_list=dest_list, num_list=num_list, data_width_list=data_width_list)
        print("[Info ] Writing {}".format(os.path.join(bd_dir, "CROSSING_AXIS.tcl")))
    
    print("[{}] Generating Tcl Complete!".format(PASS))
    ############################################################
    # 4. Code Generator
    print("="*74 + "\n Code Generator\n" + "="*74)

    # Board Wrapper
    Board_Wrapper(filedir=wrapper_dir, board=board, slr_list=slr_list, slr_phy_list=slr_phy_list, 
                  xdma_ddr_ch=xdma_ddr_ch, ddr_dma_list=ddr_dma_list, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list,
                  xdma_hbm_port=xdma_hbm_port, hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, hbm_dma_list=hbm_dma_list)
    Shell_Params(filedir=wrapper_dir, board=board, slr_list=slr_list, 
                 ddr_dma_width_list=ddr_dma_width, host_width_list=slr_host_width_list,
                 hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, hbm_dma_width_list=hbm_dma_width_list)
    print("[Info ] Writing {}".format(os.path.join(wrapper_dir, "{}_Wrapper.sv".format(board))))
    
    # SLR Wrapper
    SLR_Wrapper(filedir=wrapper_dir, board=board, slr_list=slr_list, ddr_dma_list=ddr_dma_list, 
                hbm_slr_list=hbm_slr_list,  hbm_port_list=hbm_port_list,  hbm_dma_list=hbm_dma_list,
                crossing=crossing, src_list=src_list, dest_list=dest_list, num_list=num_list, data_width_list=data_width_list)
    print("[Info ] Writing {}".format(os.path.join(wrapper_dir, "SLR.sv".format(board))))
    
    # UserLogic Wrapper
    UserLogic(filedir=wrapper_dir, board=board, slr_list=slr_list, ddr_dma_list=ddr_dma_list, xdma_hbm_port=xdma_hbm_port,
              hbm_slr_list=hbm_slr_list, hbm_port_list=hbm_port_list, hbm_dma_list=hbm_dma_list, crossing=crossing, 
              src_list=src_list, dest_list=dest_list, num_list=num_list, data_width_list=data_width_list)
    print("[Info ] Writing {}".format(os.path.join(wrapper_dir, "User_Logic.sv".format(board))))
    
    print("[{}] Generating Code Complete!".format(PASS))
    ############################################################
    # 5. Xdc Generator
    print("="*74 + "\n Xdc Generator\n" + "="*74)
    SLR_Xdc(filedir=xdc_dir, board=board, slr_list=slr_list)
    print("[Info ] Writing SLR xdc")
    INC_Xdc(filedir=xdc_dir, board=board, slr_list=slr_list, ddr_dma_list=ddr_dma_list, hbm_slr_list=hbm_slr_list,
            hbm_port_list=hbm_port_list, hbm_dma_list=hbm_dma_list, xdma_hbm_port=xdma_hbm_port,
            xdma_ddr_ch_list=xdma_ddr_ch, ddr_slr_list=ddr_slr_list, ddr_ch_list=ddr_ch_list) 
    print("[Info ] Writing INC xdc")
    CLK_Xdc(filedir=xdc_dir, board=board)
    print("[Info ] Writing CLK xdc")
    PIN_Xdc(filedir=xdc_dir, board=board)
    print("[Info ] Writing PIN xdc")
    print("[{}] Generating XDC Complete!".format(PASS))
    ############################################################
    # 6. End
    print("="*74)

################################################################
# Function
################################################################

# Create Config Dictionary
def config_dict(board_config, file_mode=True, args=None, ifile=None):
    # Create Dictionary by Board Property
    config = {}
    config["SLR"] = {"slr_list" : None, "slr_freq_list" : None, "slr_host_width_list" : None}
    config["DDR"] = {"xdma_ddr_ch" : None, "ddr_slr_list"  : None, "ddr_ch_list" : None, "ddr_dma_list" : None, "ddr_dma_width" : None }
    config["HBM"] = {"hbm_clk_freq" : None, "xdma_hbm_port" : None, "hbm_slr_list" : None, "hbm_port_list" : None, "hbm_dma_list": None, "hbm_dma_width" : None}
    # .ini File Mode
    if file_mode:
        if "SLR" in ifile.keys():
            config["SLR"]["slr_list"] = ifile["SLR"]["slr_list"].split(",")
            config["SLR"]["slr_freq_list"] = ifile["SLR"]["slr_freq_list"].split(",")
            config["SLR"]["slr_host_width_list"] = ifile["SLR"]["slr_host_width_list"].split(",")


        if "DDR" in ifile.keys():
            config["DDR"]["xdma_ddr_ch"] = ifile["DDR"]["xdma_ddr_ch"].split(",")
            config["DDR"]["ddr_slr_list"] = ifile["DDR"]["ddr_slr_list"].split(",")
            config["DDR"]["ddr_ch_list"] = ifile["DDR"]["ddr_ch_list"].split(",")
            config["DDR"]["ddr_dma_list"] = ifile["DDR"]["ddr_dma_list"].split(",")
            config["DDR"]["ddr_dma_width"] = ifile["DDR"]["ddr_dma_width"].split(",")
        
        if "HBM" in ifile.keys(): 
            config["HBM"]["hbm_clk_freq"] = ifile["HBM"]["hbm_clk_freq"]
            config["HBM"]["xdma_hbm_port"] = ifile["HBM"]["xdma_hbm_port"]
            config["HBM"]["hbm_slr_list"] = ifile["HBM"]["hbm_slr_list"].split(",")
            config["HBM"]["hbm_port_list"] = ifile["HBM"]["hbm_port_list"].split(",")
            config["HBM"]["hbm_dma_list"] = ifile["HBM"]["hbm_dma_list"].split(",")
            config["HBM"]["hbm_dma_width_list"] = ifile["HBM"]["hbm_dma_width"].split(",")
    # Argument Mode
    else:
        for idx, slr in enumerate(args.slr.split(",")):
            # Check Valid SLR
            if slr not in config.keys():
                print("[{}] This board has only '{}' SLRs".format(ERROR, config.keys()))
                close()
            config[slr]["USE"] = True
            config[slr]["FREQUENCY"] = args.freq.split(",")[idx]
            config[slr]["HOST"] = args.host_width.split(",")[idx]
            if "DDR" in config[slr].keys():
                config[slr]["DDR"] = [args.ddr_dma.split(",")[idx], args.ddr_dma_width.split(",")[idx]]
            if "HBM" in config[slr].keys():
                config[slr]["HBM"] = [args.xdma_hbm_port,
                                      args.hbm_slr.split(",")[idx], args.hbm_port.split(",")[idx],
                                      args.hbm_dma.split(",")[idx], args.hbm_dma_width.split(",")[idx]]
        if "HBM" in config.keys(): 
            config["HBM"]["xdma_hbm_port"] = args.xdma_hbm_port
            config["HBM"]["hbm_slr_list"] = args.hbm_slr.split(",")
            config["HBM"]["hbm_port_list"] = args.hbm_port.split(",")
            config["HBM"]["hbm_dma_list"] = args.hbm_dma.split(",")
            config["HBM"]["hbm_dma_width_list"] = args.hbm_dma_width.split(",")
    # Return Dictionary
    return config

# Create FIFO Dictionary
def fifo_dict(file_mode=True, args=None, ifile=None):
    # Create Dictionary
    fifo = {}
    # .ini File Mode
    if file_mode:
        fifo = ifile["Crossing"]
    # Argument Mode
    else:
        fifo["cross"] = args.crossing
        fifo["fifo_src"] = args.fifo_src
        fifo["fifo_dest"] = args.fifo_dest
        fifo["fifo_number"] = args.fifo_number
        fifo["fifo_width"] = args.fifo_width
    # Return Dictionary
    return fifo        

# Dircotry Check & Make Directory
def dir_check(filedir, board):
    # Check Directory
    if os.path.isdir(filedir):
        bd_dir = os.path.join(filedir, board, "bd/")
        wrapper_dir = os.path.join(filedir, board, "wrapper/")
        xdc_dir = os.path.join(filedir, board, "constraints/")
        # Make Directory if it does not exist
        if not os.path.exists(bd_dir):
            os.makedirs(bd_dir)
        if not os.path.exists(wrapper_dir):
            os.makedirs(wrapper_dir)
        if not os.path.exists(xdc_dir) :
            os.makedirs(xdc_dir)
        # Return Sub Directories
        return bd_dir, wrapper_dir, xdc_dir
    # Print Error if not extis
    else:
        print("[{}] No such file or directory: '{}'".format(ERROR, filedir))
        close()

def list_none_check(list):
    if(list != None):
        for i in range(len(list)):
            if (list[i].isalpha() == True):
                list = None
                return list
    return list

def none_check(slr_list, slr_freq_list, slr_host_width_list, 
            xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, 
            xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq):
        
    slr_list = list_none_check(slr_list)
    slr_freq_list = list_none_check(slr_freq_list)
    slr_host_width_list = list_none_check(slr_host_width_list)
    xdma_ddr_ch = list_none_check(xdma_ddr_ch)
    ddr_slr_list = list_none_check(ddr_slr_list)
    ddr_ch_list = list_none_check(ddr_ch_list)
    ddr_dma_list = list_none_check(ddr_dma_list)
    ddr_dma_width = list_none_check(ddr_dma_width)
    hbm_clk_freq = list_none_check(hbm_clk_freq)
    xdma_hbm_port = list_none_check(xdma_hbm_port)
    hbm_slr_list = list_none_check(hbm_slr_list)
    hbm_port_list = list_none_check(hbm_port_list)
    hbm_dma_list = list_none_check(hbm_dma_list)
    hbm_dma_width_list = list_none_check(hbm_dma_width_list)
    
    return slr_list, slr_freq_list, slr_host_width_list, \
        xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, \
        xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq


# Print Shell Params
def shell_param_check(slr_list, slr_freq_list, slr_host_width_list, 
            xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, 
            xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq):
    # Shell Params
    slr_list, slr_freq_list, slr_host_width_list, \
    xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, \
    xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq = \
    none_check(slr_list, slr_freq_list, slr_host_width_list, 
                xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, 
                xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq)

    print("slr_list             = " + str(slr_list))
    print("slr_freq_list        = " + str(slr_freq_list))
    print("slr_host_width_list  = " + str(slr_host_width_list))
    print("xdma_ddr_ch_list     = " + str(xdma_ddr_ch))
    print("ddr_slr_list         = " + str(ddr_slr_list))
    print("ddr_ch_list          = " + str(ddr_ch_list))
    print("ddr_dma_list         = " + str(ddr_dma_list))
    print("ddr_dma_width        = " + str(ddr_dma_width))
    print("hbm_clk_freq         = " + str(hbm_clk_freq))
    print("xdma_hbm_port        = " + str(xdma_hbm_port))
    print("hbm_slr_list         = " + str(hbm_slr_list))
    print("hbm_port_list        = " + str(hbm_port_list))
    print("hbm_dma_list         = " + str(hbm_dma_list))
    print("hbm_dma_width_list   = " + str(hbm_dma_width_list))
    
    return slr_list, slr_freq_list, slr_host_width_list, \
        xdma_ddr_ch, ddr_slr_list, ddr_ch_list, ddr_dma_list, ddr_dma_width, \
        xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq

# Create SLR Configuration
def slr_config(config, physical=False):
    # SLR List & Frequency List
    slr_list = config["SLR"]["slr_list"]
    slr_freq_list = config["SLR"]["slr_freq_list"]
    slr_host_with_list = config["SLR"]["slr_host_width_list"]
    return slr_list, slr_freq_list, slr_host_with_list

# Create DDR DMA Configuration
def ddr_dma_config(config, ddr_dma_max):
    xdma_ddr_ch = config["DDR"]["xdma_ddr_ch"]
    ddr_slr_list = config["DDR"]["ddr_slr_list"]
    ddr_ch_list = config["DDR"]["ddr_ch_list"]
    ddr_dma_list = config["DDR"]["ddr_dma_list"]
    ddr_dma_width = config["DDR"]["ddr_dma_width"]

    # Return Lists
    return ddr_dma_list, ddr_dma_width, xdma_ddr_ch, ddr_slr_list, ddr_ch_list

# Create HBM DMA Configuration
def hbm_dma_config(config, hbm_dma_max):
    # DMA List & Bitwidth List
    hbm_clk_freq = config["HBM"]["hbm_clk_freq"]
    xdma_hbm_port = config["HBM"]["xdma_hbm_port"]
    hbm_slr_list = config["HBM"]["hbm_slr_list"]
    hbm_port_list = config["HBM"]["hbm_port_list"]
    hbm_dma_list = config["HBM"]["hbm_dma_list"]
    hbm_dma_width_list = config["HBM"]["hbm_dma_width_list"]

    # Return Lists
    return xdma_hbm_port, hbm_slr_list, hbm_port_list, hbm_dma_list, hbm_dma_width_list, hbm_clk_freq

# Exit Python code
def close():
    print("="*74)
    exit()

if __name__ == '__main__':
    # Load Arguements
    args = parser.parse_args()
    # Call Main Function
    main(args)
