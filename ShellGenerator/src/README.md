## Enviornment
* Ubuntu-18.04 LTS
* Python 3.6.9
* PyInstaller >= 4.5.1

## Command
Set options by file :
<pre><code>python3 src/main.py --board VCU118  \
                   --dir $SHELL_DIR \
                   --file $SHELL_INI_PATH
</code></pre>
You shoud write .ini file like this to use option --file

Example Command
<pre><code>
VCU118
python3 main.py --board VCU118 --dir=../shell/ --file=shell.ini

U50
python3 main.py --board U50 --dir=../shell/ --file=shell.ini
</code></pre>

|Options|Descriptions|
|---|---|
|SLR||
|slr_list|SLR Kernel that want to use|
|slr_freq_list|Each SLR Kernel's target frequency|
|slr_host_width_list|Each SLR Kernel's AXI4 slave interface data bitwidth|
|---|---|
|DDR||
|xdma_ddr_ch|PCIe to DDR channel bus information|
|ddr_dma_list|Each SLR Kernel's number of AXI4 master dma inteface, pair with ddr_dma_width_list|
|ddr_dma_width_list|Each SLR Kernel's AXI4 master dma interface bitwidth, pair with ddr_dma_list|
|ddr_slr_list|The information of bus between DDR and SLR, pair with ddr_ch_list|
|ddr_ch_list|The information of bus between DDR and SLR, pair with ddr_slr_list|
|---|---|
|HBM||
|hbm_clk_freq|HBM bus's target frequency|
|xdma_hbm_port|PCIe to HBM channel bus information|
|hbm_slr_list|The information of bus between HBM and SLR, pair with hbm_port_list|
|hbm_port_list|The information of bus between HBM and SLR, pair with hbm_slr_list|
|hbm_dma_list|Above HBM and SLR bus's number of AXI4 master dma interface, pair with hbm_dma_width|
|hbm_dma_width|Above HBM and SLR bus's bitwidth of AXI4 master dma interface, pair with hbm_dma_list|
|---|---|
|Crossing||
|cross|Option for SLR internal crossing|
|fifo_src|SLR ID for AXI FIFO source|
|fifo_dest|SLR ID for AXI FIFO destination|
|fifo_number|The number of AXI FIFO|
|fifo_width|Data-width of AXI FIFO|