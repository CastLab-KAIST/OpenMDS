################################################################
# Function
################################################################

from sys import prefix

def get_ddr_dma_prefix(ddr_slr, ddr_ch, ddr_dma_num):
    slr = "SLR{:01d}".format(int(ddr_slr))
    ddr = "DDR{:01d}".format(int(ddr_ch))
    dma = "DMA{:02d}".format(int(ddr_dma_num))
    prefix = [
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_ADDR_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_araddr"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_BURST_BITS-1:0]", slr+"_"+ddr+"_"+dma+"_M_AXI_arburst"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_CACHE_BITS-1:0]", slr+"_"+ddr+"_"+dma+"_M_AXI_arcache"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_LEN_BITS-1:0]",   slr+"_"+ddr+"_"+dma+"_M_AXI_arlen"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_LOCK_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_arlock"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_PROT_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_arprot"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_QOS_BITS-1:0]",   slr+"_"+ddr+"_"+dma+"_M_AXI_arqos"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_arready"],
        #["output",  "logic",    "["+slr+"_"+ddr+"_DMA_REGION_BITS-1:0]",slr+"_"+ddr+"_"+dma+"_M_AXI_arregion"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_SIZE_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_arsize"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_arvalid"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_ADDR_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_awaddr"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_BURST_BITS-1:0]", slr+"_"+ddr+"_"+dma+"_M_AXI_awburst"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_CACHE_BITS-1:0]", slr+"_"+ddr+"_"+dma+"_M_AXI_awcache"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_LEN_BITS-1:0]",   slr+"_"+ddr+"_"+dma+"_M_AXI_awlen"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_LOCK_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_awlock"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_PROT_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_awprot"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_QOS_BITS-1:0]",   slr+"_"+ddr+"_"+dma+"_M_AXI_awqos"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_awready"],
        #["output",  "logic",    "["+slr+"_"+ddr+"_DMA_REGION_BITS-1:0]",slr+"_"+ddr+"_"+dma+"_M_AXI_awregion"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_SIZE_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_awsize"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_awvalid"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_bready"],
        ["input",   "logic",    "["+slr+"_"+ddr+"_DMA_RESP_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_bresp"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_bvalid"],
        ["input",   "logic",    "["+slr+"_"+ddr+"_DMA_DATA_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_rdata"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_rlast"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_rready"],
        ["input",   "logic",    "["+slr+"_"+ddr+"_DMA_RESP_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_rresp"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_rvalid"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_DATA_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_wdata"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_wlast"],
        ["input",   "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_wready"],
        ["output",  "logic",    "["+slr+"_"+ddr+"_DMA_STRB_BITS-1:0]",  slr+"_"+ddr+"_"+dma+"_M_AXI_wstrb"],
        ["output",  "logic",    " ",                                    slr+"_"+ddr+"_"+dma+"_M_AXI_wvalid"]
    ]

    return prefix, len(prefix)

def get_ddr_xdma_prefix(ddr_num, port_type):
    ddr = "DDR{:d}".format(int(ddr_num))
    if(port_type == 0): # With region
        prefix = [
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_araddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_arburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_arcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_arlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_arqos"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_arready"],
            ["output",   "logic",   "[DDR_REGION_BITS-1:0]",                "XDMA_TO_"+ddr+"_S_AXI_arregion"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arsize"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_arvalid"],
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awaddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_awburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_awcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_awlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_awqos"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_awready"],
            ["output",  "logic",    "[DDR_REGION_BITS-1:0]",                "XDMA_TO_"+ddr+"_S_AXI_awregion"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awsize"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_awvalid"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_bready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_bresp"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_bvalid"],
            ["input",   "logic",    "[DDR_DATA_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_rdata"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rlast"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_rresp"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rvalid"],
            ["output",  "logic",    "[DDR_DATA_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_wdata"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wlast"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wready"],
            ["output",  "logic",    "[DDR_STRB_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_wstrb"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wvalid"]
        ]

    elif(port_type == 1): # No region
        prefix = [
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_araddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_arburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_arcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_arlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_arqos"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_arready"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_arsize"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_arvalid"],
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awaddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_awburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 "XDMA_TO_"+ddr+"_S_AXI_awcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_awlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   "XDMA_TO_"+ddr+"_S_AXI_awqos"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_awready"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_awsize"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_awvalid"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_bready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_bresp"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_bvalid"],
            ["input",   "logic",    "[DDR_DATA_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_rdata"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rlast"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_rresp"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_rvalid"],
            ["output",  "logic",    "[DDR_DATA_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_wdata"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wlast"],
            ["input",   "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wready"],
            ["output",  "logic",    "[DDR_STRB_BITS-1:0]",                  "XDMA_TO_"+ddr+"_S_AXI_wstrb"],
            ["output",  "logic",    " ",                                    "XDMA_TO_"+ddr+"_S_AXI_wvalid"]
        ]

    return prefix, len(prefix)
    

def get_ddr_slr_prefix(slr_num, ddr_num, port_type):
    slr = "SLR{:d}".format(int(slr_num))
    ddr = "DDR{:d}".format(int(ddr_num))
    if(port_type == 0): # With region
        prefix = [
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_araddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_arburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_arcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_arlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_arqos"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_arready"],
            ["output",   "logic",   "[DDR_REGION_BITS-1:0]",                slr+"_TO_"+ddr+"_S_AXI_arregion"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arsize"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_arvalid"],
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awaddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_awburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_awcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_awlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_awqos"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_awready"],
            ["output",  "logic",    "[DDR_REGION_BITS-1:0]",                slr+"_TO_"+ddr+"_S_AXI_awregion"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awsize"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_awvalid"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_bready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_bresp"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_bvalid"],
            ["input",   "logic",    "[DDR_DATA_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_rdata"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rlast"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_rresp"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rvalid"],
            ["output",  "logic",    "[DDR_DATA_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_wdata"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wlast"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wready"],
            ["output",  "logic",    "[DDR_STRB_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_wstrb"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wvalid"]
        ]

    elif(port_type == 1): # No region
        prefix = [
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_araddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_arburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_arcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_arlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_arqos"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_arready"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_arsize"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_arvalid"],
            ["output",  "logic",    "[DDR_ADDR_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awaddr"],
            ["output",  "logic",    "[DDR_BURST_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_awburst"],
            ["output",  "logic",    "[DDR_CACHE_BITS-1:0]",                 slr+"_TO_"+ddr+"_S_AXI_awcache"],
            ["output",  "logic",    "[DDR_LEN_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_awlen"],
            ["output",  "logic",    "[DDR_LOCK_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awlock"],
            ["output",  "logic",    "[DDR_PROT_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awprot"],
            ["output",  "logic",    "[DDR_QOS_BITS-1:0]",                   slr+"_TO_"+ddr+"_S_AXI_awqos"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_awready"],
            ["output",  "logic",    "[DDR_SIZE_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_awsize"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_awvalid"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_bready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_bresp"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_bvalid"],
            ["input",   "logic",    "[DDR_DATA_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_rdata"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rlast"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rready"],
            ["input",   "logic",    "[DDR_RESP_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_rresp"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_rvalid"],
            ["output",  "logic",    "[DDR_DATA_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_wdata"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wlast"],
            ["input",   "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wready"],
            ["output",  "logic",    "[DDR_STRB_BITS-1:0]",                  slr+"_TO_"+ddr+"_S_AXI_wstrb"],
            ["output",  "logic",    " ",                                    slr+"_TO_"+ddr+"_S_AXI_wvalid"]
        ]

    return prefix, len(prefix)

def get_hbm_dma_prefix(hbm_slr, hbm_port, hbm_dma_num):
    slr = "SLR{:d}".format(int(hbm_slr))
    hbm = "HBM{:02d}".format(int(hbm_port))
    dma = "DMA{:02d}".format(int(hbm_dma_num))
    prefix = [
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_ADDR_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_araddr"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_BURST_BITS-1:0]", slr+"_"+hbm+"_"+dma+"_M_AXI_arburst"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_CACHE_BITS-1:0]", slr+"_"+hbm+"_"+dma+"_M_AXI_arcache"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_LEN_BITS-1:0]",   slr+"_"+hbm+"_"+dma+"_M_AXI_arlen"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_LOCK_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_arlock"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_PROT_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_arprot"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_QOS_BITS-1:0]",   slr+"_"+hbm+"_"+dma+"_M_AXI_arqos"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_arready"],
        #["output",  "logic",    "["+slr+"_"+hbm+"_DMA_REGION_BITS-1:0]",slr+"_"+hbm+"_"+dma+"_M_AXI_arregion"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_SIZE_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_arsize"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_arvalid"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_ADDR_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_awaddr"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_BURST_BITS-1:0]", slr+"_"+hbm+"_"+dma+"_M_AXI_awburst"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_CACHE_BITS-1:0]", slr+"_"+hbm+"_"+dma+"_M_AXI_awcache"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_LEN_BITS-1:0]",   slr+"_"+hbm+"_"+dma+"_M_AXI_awlen"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_LOCK_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_awlock"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_PROT_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_awprot"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_QOS_BITS-1:0]",   slr+"_"+hbm+"_"+dma+"_M_AXI_awqos"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_awready"],
        #["output",  "logic",    "["+slr+"_"+hbm+"_DMA_REGION_BITS-1:0]",slr+"_"+hbm+"_"+dma+"_M_AXI_awregion"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_SIZE_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_awsize"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_awvalid"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_bready"],
        ["input",   "logic",    "["+slr+"_"+hbm+"_DMA_RESP_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_bresp"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_bvalid"],
        ["input",   "logic",    "["+slr+"_"+hbm+"_DMA_DATA_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_rdata"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_rlast"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_rready"],
        ["input",   "logic",    "["+slr+"_"+hbm+"_DMA_RESP_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_rresp"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_rvalid"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_DATA_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_wdata"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_wlast"],
        ["input",   "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_wready"],
        ["output",  "logic",    "["+slr+"_"+hbm+"_DMA_STRB_BITS-1:0]",  slr+"_"+hbm+"_"+dma+"_M_AXI_wstrb"],
        ["output",  "logic",    " ",                                    slr+"_"+hbm+"_"+dma+"_M_AXI_wvalid"]
    ]

    return prefix, len(prefix)

def get_hbm_slr_prefix(hbm_slr, hbm_port):
    slr = "SLR{:d}".format(int(hbm_slr))
    hbm = "HBM{:02d}".format(int(hbm_port))
    prefix = [
        ["output",  "logic",    "[HBM_ADDR_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_araddr"],
        ["output",  "logic",    "[HBM_BURST_BITS-1:0]",                 slr+"_TO_"+hbm+"_S_AXI_arburst"],
        ["output",  "logic",    "[HBM_CACHE_BITS-1:0]",                 slr+"_TO_"+hbm+"_S_AXI_arcache"],
        ["output",  "logic",    "[HBM_LEN_BITS-1:0]",                   slr+"_TO_"+hbm+"_S_AXI_arlen"],
        ["output",  "logic",    "[HBM_LOCK_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_arlock"],
        ["output",  "logic",    "[HBM_PROT_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_arprot"],
        ["output",  "logic",    "[HBM_QOS_BITS-1:0]",                   slr+"_TO_"+hbm+"_S_AXI_arqos"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_arready"],
        ["output",  "logic",    "[HBM_SIZE_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_arsize"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_arvalid"],
        ["output",  "logic",    "[HBM_ADDR_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_awaddr"],
        ["output",  "logic",    "[HBM_BURST_BITS-1:0]",                 slr+"_TO_"+hbm+"_S_AXI_awburst"],
        ["output",  "logic",    "[HBM_CACHE_BITS-1:0]",                 slr+"_TO_"+hbm+"_S_AXI_awcache"],
        ["output",  "logic",    "[HBM_LEN_BITS-1:0]",                   slr+"_TO_"+hbm+"_S_AXI_awlen"],
        ["output",  "logic",    "[HBM_LOCK_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_awlock"],
        ["output",  "logic",    "[HBM_PROT_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_awprot"],
        ["output",  "logic",    "[HBM_QOS_BITS-1:0]",                   slr+"_TO_"+hbm+"_S_AXI_awqos"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_awready"],
        ["output",  "logic",    "[HBM_SIZE_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_awsize"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_awvalid"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_bready"],
        ["input",   "logic",    "[HBM_RESP_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_bresp"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_bvalid"],
        ["input",   "logic",    "[HBM_DATA_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_rdata"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_rlast"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_rready"],
        ["input",   "logic",    "[HBM_RESP_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_rresp"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_rvalid"],
        ["output",  "logic",    "[HBM_DATA_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_wdata"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_wlast"],
        ["input",   "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_wready"],
        ["output",  "logic",    "[HBM_STRB_BITS-1:0]",                  slr+"_TO_"+hbm+"_S_AXI_wstrb"],
        ["output",  "logic",    " ",                                    slr+"_TO_"+hbm+"_S_AXI_wvalid"]
    ]

    return prefix, len(prefix)

def get_axilite_host_prefix(slr_num):
    slr = "SLR" + str(slr_num)
    prefix = [
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_ADDR_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_araddr"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_PROT_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_arprot"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_arready"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_arvalid"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_ADDR_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_awaddr"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_PROT_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_awprot"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_awready"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_awvalid"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_bready"],
        ["output", "logic",    "["+slr+"_HOST_AXI_LITE_RESP_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_bresp"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_bvalid"],
        ["output", "logic",    "["+slr+"_HOST_AXI_LITE_DATA_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_rdata"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_rready"],
        ["output", "logic",    "["+slr+"_HOST_AXI_LITE_RESP_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_rresp"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_rvalid"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_DATA_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_wdata"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_wready"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LITE_STRB_BITS-1:0]",  slr+"_HOST_S_AXI_LITE_wstrb"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_LITE_wvalid"]
    ]

    return prefix, len(prefix)

def get_axi_host_prefix(slr_num):
    slr = "SLR" + str(slr_num) 
    prefix = [
        ["input",  "logic",    "["+slr+"_HOST_AXI_ADDR_BITS-1:0]",       slr+"_HOST_S_AXI_araddr"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_BURST_BITS-1:0]",      slr+"_HOST_S_AXI_arburst"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_CACHE_BITS-1:0]",      slr+"_HOST_S_AXI_arcache"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LEN_BITS-1:0]",        slr+"_HOST_S_AXI_arlen"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LOCK_BITS-1:0]",       slr+"_HOST_S_AXI_arlock"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_PROT_BITS-1:0]",       slr+"_HOST_S_AXI_arprot"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_QOS_BITS-1:0]",        slr+"_HOST_S_AXI_arqos"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_arready"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_SIZE_BITS-1:0]",       slr+"_HOST_S_AXI_arsize"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_arvalid"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_ADDR_BITS-1:0]",       slr+"_HOST_S_AXI_awaddr"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_BURST_BITS-1:0]",      slr+"_HOST_S_AXI_awburst"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_CACHE_BITS-1:0]",      slr+"_HOST_S_AXI_awcache"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LEN_BITS-1:0]",        slr+"_HOST_S_AXI_awlen"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_LOCK_BITS-1:0]",       slr+"_HOST_S_AXI_awlock"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_PROT_BITS-1:0]",       slr+"_HOST_S_AXI_awprot"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_QOS_BITS-1:0]",        slr+"_HOST_S_AXI_awqos"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_awready"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_SIZE_BITS-1:0]",       slr+"_HOST_S_AXI_awsize"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_awvalid"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_bready"],
        ["output", "logic",    "["+slr+"_HOST_AXI_RESP_BITS-1:0]",       slr+"_HOST_S_AXI_bresp"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_bvalid"],
        ["output", "logic",    "["+slr+"_HOST_AXI_DATA_BITS-1:0]",       slr+"_HOST_S_AXI_rdata"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_rlast"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_rready"],
        ["output", "logic",    "["+slr+"_HOST_AXI_RESP_BITS-1:0]",       slr+"_HOST_S_AXI_rresp"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_rvalid"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_DATA_BITS-1:0]",       slr+"_HOST_S_AXI_wdata"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_wlast"],
        ["output", "logic",    " ",                                      slr+"_HOST_S_AXI_wready"],
        ["input",  "logic",    "["+slr+"_HOST_AXI_STRB_BITS-1:0]",       slr+"_HOST_S_AXI_wstrb"],
        ["input",  "logic",    " ",                                      slr+"_HOST_S_AXI_wvalid"]
    ]

    return prefix, len(prefix)


def get_crossing_stream_prefix(slr_a, slr_b, fifo_width, fifo_num):
    slr_a = "SLR" + str(slr_a)
    slr_b = "SLR" + str(slr_b)
    fifo_num = "{:02d}".format(int(fifo_num))
    data_width = str(int(fifo_width) - 1)
    prefix = [
        ["input",   "logic",    "["+data_width+":0]",                   slr_a+"_FROM_"+slr_b+"_S"+fifo_num+"_AXIS_tdata"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S"+fifo_num+"_AXIS_tready"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S"+fifo_num+"_AXIS_tvalid"],
        ["output",  "logic",    "["+data_width+":0]",                   slr_a+"_TO_"+slr_b+"_M"+fifo_num+"_AXIS_tdata"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M"+fifo_num+"_AXIS_tready"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M"+fifo_num+"_AXIS_tvalid"]
    ]
    return prefix, len(prefix)

def get_crossing_lite_prefix(slr_a, slr_b):
    slr_a = "SLR" + str(slr_a)
    slr_b = "SLR" + str(slr_b)
    prefix = [
        ["input",   "logic",    "["+slr_a+"_DMA_ADDR_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_araddr"],
        ["input",   "logic",    "["+slr_a+"_DMA_PROT_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_arprot"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_arready"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_arvalid"],
        ["input",   "logic",    "["+slr_a+"_DMA_ADDR_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_awaddr"],
        ["input",   "logic",    "["+slr_a+"_DMA_PROT_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_awprot"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_awready"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_awvalid"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_bready"],
        ["output",  "logic",    "["+slr_a+"_DMA_RESP_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_bresp"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_bvalid"],
        ["output",  "logic",    "["+slr_a+"_DMA_DATA_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_rdata"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_rready"],
        ["output",  "logic",    "["+slr_a+"_DMA_RESP_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_rresp"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_rvalid"],
        ["input",   "logic",    "["+slr_a+"_DMA_DATA_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_wdata"],
        ["output",  "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_wready"],
        ["input",   "logic",    "["+slr_a+"_DMA_STRB_BITS-1:0]",        slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_wstrb"],
        ["input",   "logic",    " ",                                    slr_a+"_FROM_"+slr_b+"_S_AXI_LITE_wvalid"],
        ["output",  "logic",    "["+slr_a+"_DMA_ADDR_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_araddr"],
        ["output",  "logic",    "["+slr_a+"_DMA_PROT_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_arprot"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_arready"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_arvalid"],
        ["output",  "logic",    "["+slr_a+"_DMA_ADDR_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_awaddr"],
        ["output",  "logic",    "["+slr_a+"_DMA_PROT_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_awprot"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_awready"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_awvalid"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_bready"],
        ["input",   "logic",    "["+slr_a+"_DMA_RESP_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_bresp"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_bvalid"],
        ["input",   "logic",    "["+slr_a+"_DMA_DATA_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_rdata"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_rready"],
        ["input",   "logic",    "["+slr_a+"_DMA_RESP_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_rresp"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_rvalid"],
        ["output",  "logic",    "["+slr_a+"_DMA_DATA_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_wdata"],
        ["input",   "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_wready"],
        ["output",  "logic",    "["+slr_a+"_DMA_STRB_BITS-1:0]",        slr_a+"_TO_"+slr_b+"_M_AXI_LITE_wstrb"],
        ["output",  "logic",    " ",                                    slr_a+"_TO_"+slr_b+"_M_AXI_LITE_wvalid"]
    ]
    return prefix, len(prefix)

def get_board_ddr_prefix(board, ddr_ch, port_type=0):
    if(board == 'VCU118') :
        if(port_type == 0):
            prefix = [
                ["output",    "ddr4_sdram_c{:01d}_act_n".format(int(ddr_ch) + 1),            " "],
                ["output",    "ddr4_sdram_c{:01d}_adr".format(int(ddr_ch) + 1),              "[16:0]"],
                ["output",    "ddr4_sdram_c{:01d}_ba".format(int(ddr_ch) + 1),               "[1:0]"],
                ["output",    "ddr4_sdram_c{:01d}_bg".format(int(ddr_ch) + 1),               " "],
                ["output",    "ddr4_sdram_c{:01d}_ck_c".format(int(ddr_ch) + 1),             " "],
                ["output",    "ddr4_sdram_c{:01d}_ck_t".format(int(ddr_ch) + 1),             " "],
                ["output",    "ddr4_sdram_c{:01d}_cke".format(int(ddr_ch) + 1),              " "],
                ["output",    "ddr4_sdram_c{:01d}_cs_n".format(int(ddr_ch) + 1),             " "],
                ["inout",     "ddr4_sdram_c{:01d}_dm_n".format(int(ddr_ch) + 1),             "[7:0]"],
                ["inout",     "ddr4_sdram_c{:01d}_dq".format(int(ddr_ch) + 1),               "[63:0]"],
                ["inout",     "ddr4_sdram_c{:01d}_dqs_c".format(int(ddr_ch) + 1),            "[7:0]"],
                ["inout",     "ddr4_sdram_c{:01d}_dqs_t".format(int(ddr_ch) + 1),            "[7:0]"],
                ["output",    "ddr4_sdram_c{:01d}_odt".format(int(ddr_ch) + 1),              " "],
                ["output",    "ddr4_sdram_c{:01d}_reset_n".format(int(ddr_ch) + 1),          " "]
            ]

        elif(port_type == 1):
            prefix = [
                ["input",     "default_250mhz_clk{:01d}_clk_n".format(int(ddr_ch) + 1),      " "],
                ["input",     "default_250mhz_clk{:01d}_clk_p".format(int(ddr_ch) + 1),      " "]
            ]

    else : 
        print("ERROR : {} is not supported".format(board))
    return prefix, len(prefix)
    

def get_vcu_prefix():
    prefix = [
        #["input",     "user_si570_clock_clk_n",         " "],
        #["input",     "user_si570_clock_clk_p",         " "],
        #["input",     "dip_switches_4bits_tri_i",       "[3:0]"],
        ["input",     "pci_express_x16_rxn",            "[15:0]"],
        ["input",     "pci_express_x16_rxp",            "[15:0]"],
        ["output",    "pci_express_x16_txn",            "[15:0]"],
        ["output",    "pci_express_x16_txp",            "[15:0]"],
        ["input",     "pcie_perstn",                    " "],
        ["input",     "pcie_refclk_clk_n",              " "],
        ["input",     "pcie_refclk_clk_p",              " "],
        ["input",     "reset",                          " "]
    ]
    return prefix, len(prefix)

def get_u50_prefix():
    prefix = [
        #["input",    "cmc_clk_clk_n",                   " "],
        #["input",    "cmc_clk_clk_p",                   " "],
        #["input",    "hbm_clk_clk_n",                   " "],
        #["input",    "hbm_clk_clk_p",                   " "],
        #["input",    "gpio_si5394_tri_i",               "[2:0]"],
        ["input",    "pci_express_x16_rxn",             "[15:0]"],
        ["input",    "pci_express_x16_rxp",             "[15:0]"],
        ["output",   "pci_express_x16_txn",             "[15:0]"],
        ["output",   "pci_express_x16_txp",             "[15:0]"],
        ["input",    "pcie_perstn",                     " "],
        ["input",    "pcie_refclk_clk_n",               " "],
        ["input",    "pcie_refclk_clk_p",               " "]
    ]
    return prefix, len(prefix)


def get_clk_wiz_prefix():
    prefix = [
        ["input",     "CLK_WIZ_S_AXI_LITE_araddr",       "[CLK_WIZ_LITE_ADDR_BITS-1:0]"],
        ["input",     "CLK_WIZ_S_AXI_LITE_arprot",       "[CLK_WIZ_LITE_PROT_BITS-1:0]"],
        ["output",    "CLK_WIZ_S_AXI_LITE_arready",      " "],
        ["input",     "CLK_WIZ_S_AXI_LITE_arvalid",      " "],
        ["input",     "CLK_WIZ_S_AXI_LITE_awaddr",       "[CLK_WIZ_LITE_ADDR_BITS-1:0]"],
        ["input",     "CLK_WIZ_S_AXI_LITE_awprot",       "[CLK_WIZ_LITE_PROT_BITS-1:0]"],
        ["output",    "CLK_WIZ_S_AXI_LITE_awready",      ""],
        ["input",     "CLK_WIZ_S_AXI_LITE_awvalid",      " "],
        ["input",     "CLK_WIZ_S_AXI_LITE_bready",       " "],
        ["output",    "CLK_WIZ_S_AXI_LITE_bresp",        "[CLK_WIZ_LITE_RESP_BITS-1:0]"],
        ["output",    "CLK_WIZ_S_AXI_LITE_bvalid",       " "],
        ["output",    "CLK_WIZ_S_AXI_LITE_rdata",        "[CLK_WIZ_LITE_DATA_BITS-1:0]"],
        ["input",     "CLK_WIZ_S_AXI_LITE_rready",       " "],
        ["output",    "CLK_WIZ_S_AXI_LITE_rresp",        "[CLK_WIZ_LITE_RESP_BITS-1:0]"],
        ["output",    "CLK_WIZ_S_AXI_LITE_rvalid",       " "],
        ["input",     "CLK_WIZ_S_AXI_LITE_wdata",        "[CLK_WIZ_LITE_DATA_BITS-1:0]"],
        ["output",    "CLK_WIZ_S_AXI_LITE_wready",       " "],
        ["input",     "CLK_WIZ_S_AXI_LITE_wstrb",        "[CLK_WIZ_LITE_STRB_BITS-1:0]"],
        ["input",     "CLK_WIZ_S_AXI_LITE_wvalid",       " "]
    ]
    return prefix, len(prefix)
    
def get_ddr_prefix(ddr_num, port_type):
    ddr = "DDR{}".format(int(ddr_num))
    
    if(port_type == 0): # region with ID
        prefix = [
            ["output",    ddr+"_CLK",                       " "],
            ["output",    ddr+"_CLK_RESETN",                "[0:0]"],
            ["input",     ddr+"_S_AXI_araddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arid",                "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_arready",             " "],
            ["input",     ddr+"_S_AXI_arregion",            "[DDR_REGION_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arvalid",             " "],
            ["input",     ddr+"_S_AXI_awaddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awid",                "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_awready",             " "],
            ["input",     ddr+"_S_AXI_awregion",            "[DDR_REGION_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awvalid",             " "],
            ["output",    ddr+"_S_AXI_bid",                 "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_bready",              " "],
            ["output",    ddr+"_S_AXI_bresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_bvalid",              " "],
            ["output",    ddr+"_S_AXI_rdata",               "[DDR_DATA_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rid",                 "[DDR_ID_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rlast",               " "],
            ["input",     ddr+"_S_AXI_rready",              " "],
            ["output",    ddr+"_S_AXI_rresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rvalid",              " "],
            ["input",     ddr+"_S_AXI_wdata",               "[DDR_DATA_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wlast",               " "],
            ["output",    ddr+"_S_AXI_wready",              " "],
            ["input",     ddr+"_S_AXI_wstrb",               "[DDR_STRB_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wvalid",              " "]
        ]

    if(port_type == 1): # region with no ID
        prefix = [
            ["output",    ddr+"_CLK",                       " "],
            ["output",    ddr+"_CLK_RESETN",                "[0:0]"],
            ["input",     ddr+"_S_AXI_araddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_arready",             " "],
            ["input",     ddr+"_S_AXI_arregion",            "[DDR_REGION_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arvalid",             " "],
            ["input",     ddr+"_S_AXI_awaddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_awready",             " "],
            ["input",     ddr+"_S_AXI_awregion",            "[DDR_REGION_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awvalid",             " "],
            ["input",     ddr+"_S_AXI_bready",              " "],
            ["output",    ddr+"_S_AXI_bresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_bvalid",              " "],
            ["output",    ddr+"_S_AXI_rdata",               "[DDR_DATA_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rlast",               " "],
            ["input",     ddr+"_S_AXI_rready",              " "],
            ["output",    ddr+"_S_AXI_rresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rvalid",              " "],
            ["input",     ddr+"_S_AXI_wdata",               "[DDR_DATA_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wlast",               " "],
            ["output",    ddr+"_S_AXI_wready",              " "],
            ["input",     ddr+"_S_AXI_wstrb",               "[DDR_STRB_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wvalid",              " "]
        ]

    elif(port_type==2): # no region with ID
        prefix = [
            ["output",    ddr+"_CLK",                       " "],
            ["output",    ddr+"_CLK_RESETN",                "[0:0]"],
            ["input",     ddr+"_S_AXI_araddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arid",                "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_arready",             " "],
            ["input",     ddr+"_S_AXI_arsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_arvalid",             " "],
            ["input",     ddr+"_S_AXI_awaddr",              "[DDR_ADDR_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awburst",             "[DDR_BURST_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awcache",             "[DDR_CACHE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awid",                "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlen",               "[DDR_LEN_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awlock",              "[DDR_LOCK_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awprot",              "[DDR_PROT_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awqos",               "[DDR_QOS_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_awready",             " "],
            ["input",     ddr+"_S_AXI_awsize",              "[DDR_SIZE_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_awvalid",             " "],
            ["output",    ddr+"_S_AXI_bid",                 "[DDR_ID_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_bready",              " "],
            ["output",    ddr+"_S_AXI_bresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_bvalid",              " "],
            ["output",    ddr+"_S_AXI_rdata",               "[DDR_DATA_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rid",                 "[DDR_ID_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rlast",               " "],
            ["input",     ddr+"_S_AXI_rready",              " "],
            ["output",    ddr+"_S_AXI_rresp",               "[DDR_RESP_BITS-1:0]"],
            ["output",    ddr+"_S_AXI_rvalid",              " "],
            ["input",     ddr+"_S_AXI_wdata",               "[DDR_DATA_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wlast",               " "],
            ["output",    ddr+"_S_AXI_wready",              " "],
            ["input",     ddr+"_S_AXI_wstrb",               "[DDR_STRB_BITS-1:0]"],
            ["input",     ddr+"_S_AXI_wvalid",              " "]
        ]
    
    if(port_type == 3):
        prefix = [
            ["output",    ddr+"_CLK",                       " "],
            ["output",    ddr+"_CLK_RESETN",                "[0:0]"]
        ]

    return prefix, len(prefix)

def get_hbm_prefix(hbm_num, port_type=0):

    if int(hbm_num) == -2:
        prefix = [
            ["input",     "HBM_CLK",                        " "],
            ["input",     "HBM_CLK_RESETN",                 " "]
        ]

    elif int(hbm_num) == -1:
        prefix = [
            ["input",     "HBM_REF_CLK0",                   " "],
            ["input",     "HBM_REF_CLK1",                   " "],
            ["input",     "HBM_CLK",                        " "],
            ["input",     "HBM_CLK_RESETN",                 " "]
        ]

    else:
        hbm = "HBM{:02d}".format(int(hbm_num))

        if int(port_type) == 0:
            prefix = [
                ["input",     hbm+"_S_AXI_araddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_arready",             " "],
                ["input",     hbm+"_S_AXI_arsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arvalid",             " "],
                ["input",     hbm+"_S_AXI_awaddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_awready",             " "],
                ["input",     hbm+"_S_AXI_awsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awvalid",             " "],
                ["output",    hbm+"_S_AXI_bid",                 "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_bready",              " "],
                ["output",    hbm+"_S_AXI_bresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_bvalid",              " "],
                ["output",    hbm+"_S_AXI_rdata",               "[HBM_DATA_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rid",                 "[HBM_ID_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rlast",               " "],
                ["input",     hbm+"_S_AXI_rready",              " "],
                ["output",    hbm+"_S_AXI_rresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rvalid",              " "],
                ["input",     hbm+"_S_AXI_wdata",               "[HBM_DATA_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wlast",               " "],
                ["output",    hbm+"_S_AXI_wready",              " "],
                ["input",     hbm+"_S_AXI_wstrb",               "[HBM_STRB_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wvalid",              " "]
            ]

        elif int(port_type) == 1:
            prefix = [
                ["input",     hbm+"_S_AXI_araddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlen",               "[HBM_LEN_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_arready",             " "],
                ["input",     hbm+"_S_AXI_arsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arvalid",             " "],
                ["input",     hbm+"_S_AXI_awaddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlen",               "[HBM_LEN_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_awready",             " "],
                ["input",     hbm+"_S_AXI_awsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awvalid",             " "],
                ["output",    hbm+"_S_AXI_bid",                 "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_bready",              " "],
                ["output",    hbm+"_S_AXI_bresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_bvalid",              " "],
                ["output",    hbm+"_S_AXI_rdata",               "[HBM_DATA_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rid",                 "[HBM_ID_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rlast",               " "],
                ["input",     hbm+"_S_AXI_rready",              " "],
                ["output",    hbm+"_S_AXI_rresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rvalid",              " "],
                ["input",     hbm+"_S_AXI_wdata",               "[HBM_DATA_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wlast",               " "],
                ["output",    hbm+"_S_AXI_wready",              " "],
                ["input",     hbm+"_S_AXI_wstrb",               "[HBM_STRB_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wvalid",              " "]
            ]

        elif int(port_type) == 2:
            prefix = [
                ["input",     hbm+"_S_AXI_araddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_arready",             " "],
                ["input",     hbm+"_S_AXI_arsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arvalid",             " "],
                ["input",     hbm+"_S_AXI_awaddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_awready",             " "],
                ["input",     hbm+"_S_AXI_awsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awvalid",             " "],
                ["input",     hbm+"_S_AXI_bready",              " "],
                ["output",    hbm+"_S_AXI_bresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_bvalid",              " "],
                ["output",    hbm+"_S_AXI_rdata",               "[HBM_DATA_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rlast",               " "],
                ["input",     hbm+"_S_AXI_rready",              " "],
                ["output",    hbm+"_S_AXI_rresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rvalid",              " "],
                ["input",     hbm+"_S_AXI_wdata",               "[HBM_DATA_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wlast",               " "],
                ["output",    hbm+"_S_AXI_wready",              " "],
                ["input",     hbm+"_S_AXI_wstrb",               "[HBM_STRB_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wvalid",              " "]
            ]
        
        elif int(port_type) == 3:
            prefix = [
                ["input",     hbm+"_S_AXI_araddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlen",               "[HBM_LEN_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_arready",             " "],
                ["input",     hbm+"_S_AXI_arsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arvalid",             " "],
                ["input",     hbm+"_S_AXI_awaddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlen",               "[HBM_LEN_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_awready",             " "],
                ["input",     hbm+"_S_AXI_awsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awvalid",             " "],
                ["input",     hbm+"_S_AXI_bready",              " "],
                ["output",    hbm+"_S_AXI_bresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_bvalid",              " "],
                ["output",    hbm+"_S_AXI_rdata",               "[HBM_DATA_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rlast",               " "],
                ["input",     hbm+"_S_AXI_rready",              " "],
                ["output",    hbm+"_S_AXI_rresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rvalid",              " "],
                ["input",     hbm+"_S_AXI_wdata",               "[HBM_DATA_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wlast",               " "],
                ["output",    hbm+"_S_AXI_wready",              " "],
                ["input",     hbm+"_S_AXI_wstrb",               "[HBM_STRB_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wvalid",              " "]
            ]

        elif int(port_type) == 4:
            prefix = [
                ["input",     hbm+"_S_AXI_araddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_arready",             " "],
                ["input",     hbm+"_S_AXI_arsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_arvalid",             " "],
                ["input",     hbm+"_S_AXI_awaddr",              "[HBM_ADDR_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awburst",             "[HBM_BURST_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awcache",             "[HBM_CACHE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awid",                "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlen",               "[HBM_LEN_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awlock",              "[HBM_LOCK_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awprot",              "[HBM_PROT_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awqos",               "[HBM_QOS_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_awready",             " "],
                ["input",     hbm+"_S_AXI_awsize",              "[HBM_SIZE_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_awvalid",             " "],
                ["output",    hbm+"_S_AXI_bid",                 "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_bready",              " "],
                ["output",    hbm+"_S_AXI_bresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_bvalid",              " "],
                ["output",    hbm+"_S_AXI_rdata",               "[HBM_DATA_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rid",                 "[HBM_ID_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rlast",               " "],
                ["input",     hbm+"_S_AXI_rready",              " "],
                ["output",    hbm+"_S_AXI_rresp",               "[HBM_RESP_BITS-1:0]"],
                ["output",    hbm+"_S_AXI_rvalid",              " "],
                ["input",     hbm+"_S_AXI_wdata",               "[HBM_DATA_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wid",                 "[HBM_ID_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wlast",               " "],
                ["output",    hbm+"_S_AXI_wready",              " "],
                ["input",     hbm+"_S_AXI_wstrb",               "[HBM_STRB_BITS-1:0]"],
                ["input",     hbm+"_S_AXI_wvalid",              " "]
            ]

    return prefix, len(prefix)

def get_gpio_prefix():
    prefix = [
        ["input",     "GPIO_S_AXI_LITE_araddr",       "[GPIO_LITE_ADDR_BITS-1:0]"],
        ["output",    "GPIO_S_AXI_LITE_arready",      " "],
        ["input",     "GPIO_S_AXI_LITE_arvalid",      " "],
        ["input",     "GPIO_S_AXI_LITE_awaddr",       "[GPIO_LITE_ADDR_BITS-1:0]"],
        ["output",    "GPIO_S_AXI_LITE_awready",      ""],
        ["input",     "GPIO_S_AXI_LITE_awvalid",      " "],
        ["input",     "GPIO_S_AXI_LITE_bready",       " "],
        ["output",    "GPIO_S_AXI_LITE_bresp",        "[GPIO_LITE_RESP_BITS-1:0]"],
        ["output",    "GPIO_S_AXI_LITE_bvalid",       " "],
        ["output",    "GPIO_S_AXI_LITE_rdata",        "[GPIO_LITE_DATA_BITS-1:0]"],
        ["input",     "GPIO_S_AXI_LITE_rready",       " "],
        ["output",    "GPIO_S_AXI_LITE_rresp",        "[GPIO_LITE_RESP_BITS-1:0]"],
        ["output",    "GPIO_S_AXI_LITE_rvalid",       " "],
        ["input",     "GPIO_S_AXI_LITE_wdata",        "[GPIO_LITE_DATA_BITS-1:0]"],
        ["output",    "GPIO_S_AXI_LITE_wready",       " "],
        ["input",     "GPIO_S_AXI_LITE_wstrb",        "[GPIO_LITE_STRB_BITS-1:0]"],
        ["input",     "GPIO_S_AXI_LITE_wvalid",       " "]
    ]

    return prefix, len(prefix)

def get_xdma_prefix(port_type):
    
    if(port_type == 0): # With Qos No id No Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    elif(port_type==1): # No Qos, With ID No Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["input",     "XDMA_M_AXI_bid",               "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rid",               "[XDMA_ID_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    elif(port_type == 2): # With Qos With ID No Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["input",     "XDMA_M_AXI_bid",               "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rid",               "[XDMA_ID_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    elif(port_type == 3): # With Qos No id With Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    elif(port_type==4): # No Qos, With ID With Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["input",     "XDMA_M_AXI_bid",               "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rid",               "[XDMA_ID_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    elif(port_type == 5): # With Qos With ID With Region
        prefix = [
            ["output",    "XDMA_CLK",                     " "],
            ["output",    "XDMA_CLK_RESETN",              " "],
            ["output",    "XDMA_M_AXI_LITE_araddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_arprot",       "[XDMA_LITE_PROT_BITS-1:0] "],
            ["input",     "XDMA_M_AXI_LITE_arready",      " "],
            ["output",    "XDMA_M_AXI_LITE_arvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_awaddr",       "[XDMA_LITE_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_awprot",       "[XDMA_LITE_PROT_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_awready",      " "],
            ["output",    "XDMA_M_AXI_LITE_awvalid",      " "],
            ["output",    "XDMA_M_AXI_LITE_bready",       " "],
            ["input",     "XDMA_M_AXI_LITE_bresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_bvalid",       " "],
            ["input",     "XDMA_M_AXI_LITE_rdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_rready",       " "],
            ["input",     "XDMA_M_AXI_LITE_rresp",        "[XDMA_LITE_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_rvalid",       " "],
            ["output",    "XDMA_M_AXI_LITE_wdata",        "[XDMA_LITE_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_LITE_wready",       " "],
            ["output",    "XDMA_M_AXI_LITE_wstrb",        "[XDMA_LITE_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_LITE_wvalid",       " "],
            ["output",    "XDMA_M_AXI_araddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_arready",           " "],
            ["output",    "XDMA_M_AXI_arregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_arvalid",           " "],
            ["output",    "XDMA_M_AXI_awaddr",            "[XDMA_ADDR_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awburst",           "[XDMA_BURST_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awcache",           "[XDMA_CACHE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awid",              "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlen",             "[XDMA_LEN_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awlock",            "[XDMA_LOCK_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awprot",            "[XDMA_PROT_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awqos",             "[XDMA_QOS_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_awready",           " "],
            ["output",    "XDMA_M_AXI_awregion",          "[XDMA_REGION_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awsize",            "[XDMA_SIZE_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_awvalid",           " "],
            ["input",     "XDMA_M_AXI_bid",               "[XDMA_ID_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_bready",            " "],
            ["input",     "XDMA_M_AXI_bresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_bvalid",            " "],
            ["input",     "XDMA_M_AXI_rdata",             "[XDMA_DATA_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rid",               "[XDMA_ID_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rlast",             " "],
            ["output",    "XDMA_M_AXI_rready",            " "],
            ["input",     "XDMA_M_AXI_rresp",             "[XDMA_RESP_BITS-1:0]"],
            ["input",     "XDMA_M_AXI_rvalid",            " "],
            ["output",    "XDMA_M_AXI_wdata",             "[XDMA_DATA_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wlast",             " "],
            ["input",     "XDMA_M_AXI_wready",            " "],
            ["output",    "XDMA_M_AXI_wstrb",             "[XDMA_STRB_BITS-1:0]"],
            ["output",    "XDMA_M_AXI_wvalid",            " "]
        ]

    return prefix, len(prefix)

def get_xdma_hbm_prefix(hbm_num):
    hbm = "HBM{:02d}".format(int(hbm_num))
    prefix = [
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_araddr",   "[HBM_ADDR_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arburst",  "[HBM_BURST_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arcache",  "[HBM_CACHE_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arlen",    "[HBM_LEN_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arlock",   "[HBM_LOCK_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arprot",   "[HBM_PROT_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arqos",    "[HBM_QOS_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arready",  " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arsize",   "[HBM_SIZE_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_arvalid",  " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awaddr",   "[HBM_ADDR_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awburst",  "[HBM_BURST_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awcache",  "[HBM_CACHE_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awlen",    "[HBM_LEN_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awlock",   "[HBM_LOCK_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awprot",   "[HBM_PROT_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awqos",    "[HBM_QOS_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awready",  " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awsize",   "[HBM_SIZE_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_awvalid",  " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_bready",   " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_bresp",    "[HBM_RESP_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_bvalid",   " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_rdata",    "[HBM_DATA_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_rlast",    " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_rready",   " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_rresp",    "[HBM_RESP_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_rvalid",   " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_wdata",    "[HBM_DATA_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_wlast",    " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_wready",   " "],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_wstrb",    "[HBM_STRB_BITS-1:0]"],
        ["input",     "XDMA_TO_"+hbm+"_S_AXI_wvalid",   " "]
    ]

    return prefix, len(prefix)

def get_slr_prefix(slr_num):
    slr = "SLR" + str(slr_num)
    prefix = [
        ["input",     slr + "_CLK",                     " "],
        ["input",     slr + "_CLK_RESETN",              "[0:0]"]
    ]

    return prefix, len(prefix)

def get_ddr_dma_parameters(ddr_slr, ddr_ch, ddr_dma_width,board):
    slr = "SLR" + str(ddr_slr)
    ddr = "DDR{:01d}".format(int(ddr_ch))
    if(board == 'VCU118'):
        params = [
            [slr + "_" + ddr + "_DMA_ADDR_BITS",              "31"],
            [slr + "_" + ddr + "_DMA_BURST_BITS",             "2"],
            [slr + "_" + ddr + "_DMA_CACHE_BITS",             "4"],
            [slr + "_" + ddr + "_DMA_LEN_BITS",               "8"],
            [slr + "_" + ddr + "_DMA_LOCK_BITS",              "1"],
            [slr + "_" + ddr + "_DMA_PROT_BITS",              "3"],
            [slr + "_" + ddr + "_DMA_QOS_BITS",               "4"],
            [slr + "_" + ddr + "_DMA_REGION_BITS",            "4"],
            [slr + "_" + ddr + "_DMA_SIZE_BITS",              "3"],
            [slr + "_" + ddr + "_DMA_RESP_BITS",              "2"],
            [slr + "_" + ddr + "_DMA_DATA_BITS",              str(ddr_dma_width)],
            [slr + "_" + ddr + "_DMA_STRB_BITS",              slr + "_" + ddr + "_DMA_DATA_BITS / 8"]
        ]
    else:
        params = [
            [slr + "_" + ddr + "_DMA_ADDR_BITS",              "34"],
            [slr + "_" + ddr + "_DMA_BURST_BITS",             "2"],
            [slr + "_" + ddr + "_DMA_CACHE_BITS",             "4"],
            [slr + "_" + ddr + "_DMA_LEN_BITS",               "8"],
            [slr + "_" + ddr + "_DMA_LOCK_BITS",              "1"],
            [slr + "_" + ddr + "_DMA_PROT_BITS",              "3"],
            [slr + "_" + ddr + "_DMA_QOS_BITS",               "4"],
            [slr + "_" + ddr + "_DMA_REGION_BITS",            "4"],
            [slr + "_" + ddr + "_DMA_SIZE_BITS",              "3"],
            [slr + "_" + ddr + "_DMA_RESP_BITS",              "2"],
            [slr + "_" + ddr + "_DMA_DATA_BITS",              str(ddr_dma_width)],
            [slr + "_" + ddr + "_DMA_STRB_BITS",              slr + "_" + ddr + "_DMA_DATA_BITS / 8"]
        ]
    
    return params, len(params)

#def get_ddr_dma_parameters(slr_num, ddr_dma_width):
#    slr = "SLR" + str(slr_num)
#    ddr = "DDR"
#    params = [
#        [slr + "_" + ddr + "_DMA_ADDR_BITS",              "64"],
#        [slr + "_" + ddr + "_DMA_BURST_BITS",             "2"],
#        [slr + "_" + ddr + "_DMA_CACHE_BITS",             "4"],
#        [slr + "_" + ddr + "_DMA_LEN_BITS",               "8"],
#        [slr + "_" + ddr + "_DMA_LOCK_BITS",              "1"],
#        [slr + "_" + ddr + "_DMA_PROT_BITS",              "3"],
#        [slr + "_" + ddr + "_DMA_QOS_BITS",               "4"],
#        [slr + "_" + ddr + "_DMA_REGION_BITS",            "4"],
#        [slr + "_" + ddr + "_DMA_SIZE_BITS",              "3"],
#        [slr + "_" + ddr + "_DMA_RESP_BITS",              "2"],
#        [slr + "_" + ddr + "_DMA_DATA_BITS",              str(ddr_dma_width)],
#        [slr + "_" + ddr + "_DMA_STRB_BITS",              slr + "_" + ddr + "_DMA_DATA_BITS / 8"]
#    ]
#    
#    return params, len(params)

def get_hbm_dma_parameters(hbm_slr, host_port, hbm_dma_width):
    slr = "SLR" + str(hbm_slr)
    hbm = "HBM{:02d}".format(int(host_port))
    params = [
        [slr + "_" + hbm + "_DMA_ADDR_BITS",              "33"],
        [slr + "_" + hbm + "_DMA_BURST_BITS",             "2"],
        [slr + "_" + hbm + "_DMA_CACHE_BITS",             "4"],
        [slr + "_" + hbm + "_DMA_LEN_BITS",               "8"],
        [slr + "_" + hbm + "_DMA_LOCK_BITS",              "1"],
        [slr + "_" + hbm + "_DMA_PROT_BITS",              "3"],
        [slr + "_" + hbm + "_DMA_QOS_BITS",               "4"],
        [slr + "_" + hbm + "_DMA_REGION_BITS",            "4"],
        [slr + "_" + hbm + "_DMA_SIZE_BITS",              "3"],
        [slr + "_" + hbm + "_DMA_RESP_BITS",              "2"],
        [slr + "_" + hbm + "_DMA_DATA_BITS",              str(hbm_dma_width)],
        [slr + "_" + hbm + "_DMA_STRB_BITS",              slr + "_" + hbm + "_DMA_DATA_BITS / 8"]
    ]
    
    return params, len(params)

def get_host_parameters(slr_num, host_width):
    slr = "SLR" + str(slr_num)
    params = [
        [slr + "_HOST_AXI_LITE_ADDR_BITS",    "32"],
        [slr + "_HOST_AXI_LITE_PROT_BITS",    "3"],
        [slr + "_HOST_AXI_LITE_RESP_BITS",    "2"],
        [slr + "_HOST_AXI_LITE_DATA_BITS",    "32"],
        [slr + "_HOST_AXI_LITE_STRB_BITS",    slr + "_HOST_AXI_LITE_DATA_BITS / 8"],
        [slr + "_HOST_AXI_ADDR_BITS",         "64"],
        [slr + "_HOST_AXI_BURST_BITS",        "2"],
        [slr + "_HOST_AXI_CACHE_BITS",        "4"],
        [slr + "_HOST_AXI_LEN_BITS",          "8"],
        [slr + "_HOST_AXI_LOCK_BITS",         "1"],
        [slr + "_HOST_AXI_PROT_BITS",         "3"],
        [slr + "_HOST_AXI_QOS_BITS",          "4"],
        [slr + "_HOST_AXI_SIZE_BITS",         "3"],
        [slr + "_HOST_AXI_RESP_BITS",         "2"],
        [slr + "_HOST_AXI_DATA_BITS",         str(host_width)],
        [slr + "_HOST_AXI_STRB_BITS",         slr + "_HOST_AXI_DATA_BITS / 8"]
    ]
    
    return params, len(params)

def get_bd_parameters(bd_name, f_d):
    if bd_name == "VCU118" :
        f_d.write("    parameter DDR_ADDR_BITS                                                 = 31;\n"                         )
        f_d.write("    parameter DDR_BURST_BITS                                                = 2;\n"                          )
        f_d.write("    parameter DDR_CACHE_BITS                                                = 4;\n"                          )
        f_d.write("    parameter DDR_ID_BITS                                                   = 4;\n"                          )
        f_d.write("    parameter DDR_LEN_BITS                                                  = 8;\n"                          )
        f_d.write("    parameter DDR_LOCK_BITS                                                 = 1;\n"                          )
        f_d.write("    parameter DDR_PROT_BITS                                                 = 3;\n"                          )
        f_d.write("    parameter DDR_QOS_BITS                                                  = 4;\n"                          )
        f_d.write("    parameter DDR_REGION_BITS                                               = 4;\n"                          )
        f_d.write("    parameter DDR_SIZE_BITS                                                 = 3;\n"                          )
        f_d.write("    parameter DDR_RESP_BITS                                                 = 2;\n"                          )
        f_d.write("    parameter DDR_DATA_BITS                                                 = 512;\n"                        )
        f_d.write("    parameter DDR_STRB_BITS                                                 = DDR_DATA_BITS / 8;\n"          )
        f_d.write("    parameter XDMA_ADDR_BITS                                                = 64;\n"                         )
        f_d.write("    parameter XDMA_BURST_BITS                                               = 2;\n"                          )
        f_d.write("    parameter XDMA_CACHE_BITS                                               = 4;\n"                          )
        f_d.write("    parameter XDMA_ID_BITS                                                  = 4;\n"                          )
        f_d.write("    parameter XDMA_LEN_BITS                                                 = 8;\n"                          )
        f_d.write("    parameter XDMA_LOCK_BITS                                                = 1;\n"                          )
        f_d.write("    parameter XDMA_PROT_BITS                                                = 3;\n"                          )
        f_d.write("    parameter XDMA_QOS_BITS                                                 = 4;\n"                          )
        f_d.write("    parameter XDMA_REGION_BITS                                              = 4;\n"                          )
        f_d.write("    parameter XDMA_SIZE_BITS                                                = 3;\n"                          )
        f_d.write("    parameter XDMA_RESP_BITS                                                = 2;\n"                          )
        f_d.write("    parameter XDMA_DATA_BITS                                                = 512;\n"                        )
        f_d.write("    parameter XDMA_STRB_BITS                                                = XDMA_DATA_BITS / 8;\n"         )
        f_d.write("    parameter XDMA_LITE_ADDR_BITS                                           = 32;\n"                         )
        f_d.write("    parameter XDMA_LITE_PROT_BITS                                           = 3;\n"                          )
        f_d.write("    parameter XDMA_LITE_RESP_BITS                                           = 2;\n"                          )
        f_d.write("    parameter XDMA_LITE_DATA_BITS                                           = 32;\n"                         )
        f_d.write("    parameter XDMA_LITE_STRB_BITS                                           = XDMA_LITE_DATA_BITS / 8;\n"    )
        f_d.write("    parameter GPIO_LITE_ADDR_BITS                                           = XDMA_LITE_ADDR_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_RESP_BITS                                           = XDMA_LITE_RESP_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_DATA_BITS                                           = XDMA_LITE_DATA_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_STRB_BITS                                           = XDMA_LITE_STRB_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_ADDR_BITS                                        = XDMA_LITE_ADDR_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_PROT_BITS                                        = XDMA_LITE_PROT_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_RESP_BITS                                        = XDMA_LITE_RESP_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_DATA_BITS                                        = XDMA_LITE_DATA_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_STRB_BITS                                        = XDMA_LITE_STRB_BITS;\n"        )
    
    elif bd_name == "U50" :
        f_d.write("    parameter HBM_ADDR_BITS                                                 = 33;\n"                         )
        f_d.write("    parameter HBM_BURST_BITS                                                = 2;\n"                          )
        f_d.write("    parameter HBM_CACHE_BITS                                                = 4;\n"                          )
        f_d.write("    parameter HBM_ID_BITS                                                   = 6;\n"                          )
        f_d.write("    parameter HBM_LEN_BITS                                                  = 4;\n"                          )
        f_d.write("    parameter HBM_LOCK_BITS                                                 = 2;\n"                          )
        f_d.write("    parameter HBM_PROT_BITS                                                 = 3;\n"                          )
        f_d.write("    parameter HBM_QOS_BITS                                                  = 4;\n"                          )
        f_d.write("    parameter HBM_SIZE_BITS                                                 = 3;\n"                          )
        f_d.write("    parameter HBM_RESP_BITS                                                 = 2;\n"                          )
        f_d.write("    parameter HBM_DATA_BITS                                                 = 256;\n"                        )
        f_d.write("    parameter HBM_STRB_BITS                                                 = HBM_DATA_BITS / 8;\n"          )
        f_d.write("    parameter XDMA_ADDR_BITS                                                = 64;\n"                         )
        f_d.write("    parameter XDMA_BURST_BITS                                               = 2;\n"                          )
        f_d.write("    parameter XDMA_CACHE_BITS                                               = 4;\n"                          )
        f_d.write("    parameter XDMA_ID_BITS                                                  = 4;\n"                          )
        f_d.write("    parameter XDMA_LEN_BITS                                                 = 8;\n"                          )
        f_d.write("    parameter XDMA_LOCK_BITS                                                = 1;\n"                          )
        f_d.write("    parameter XDMA_PROT_BITS                                                = 3;\n"                          )
        f_d.write("    parameter XDMA_QOS_BITS                                                 = 4;\n"                          )
        f_d.write("    parameter XDMA_REGION_BITS                                              = 4;\n"                          )
        f_d.write("    parameter XDMA_SIZE_BITS                                                = 3;\n"                          )
        f_d.write("    parameter XDMA_RESP_BITS                                                = 2;\n"                          )
        f_d.write("    parameter XDMA_DATA_BITS                                                = 512;\n"                        )
        f_d.write("    parameter XDMA_STRB_BITS                                                = XDMA_DATA_BITS / 8;\n"         )
        f_d.write("    parameter XDMA_LITE_ADDR_BITS                                           = 32;\n"                         )
        f_d.write("    parameter XDMA_LITE_PROT_BITS                                           = 3;\n"                          )
        f_d.write("    parameter XDMA_LITE_RESP_BITS                                           = 2;\n"                          )
        f_d.write("    parameter XDMA_LITE_DATA_BITS                                           = 32;\n"                         )
        f_d.write("    parameter XDMA_LITE_STRB_BITS                                           = XDMA_LITE_DATA_BITS / 8;\n"    )
        f_d.write("    parameter GPIO_LITE_ADDR_BITS                                           = XDMA_LITE_ADDR_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_RESP_BITS                                           = XDMA_LITE_RESP_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_DATA_BITS                                           = XDMA_LITE_DATA_BITS;\n"        )
        f_d.write("    parameter GPIO_LITE_STRB_BITS                                           = XDMA_LITE_STRB_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_ADDR_BITS                                        = XDMA_LITE_ADDR_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_PROT_BITS                                        = XDMA_LITE_PROT_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_RESP_BITS                                        = XDMA_LITE_RESP_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_DATA_BITS                                        = XDMA_LITE_DATA_BITS;\n"        )
        f_d.write("    parameter CLK_WIZ_LITE_STRB_BITS                                        = XDMA_LITE_STRB_BITS;\n"        )

    f_d.write("\n")

    return