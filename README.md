**OpenMDS: An Open-Source Shell Generation Framework for High Performance Design on Multi-Die FPGAs**
=============
<p align="center"><img src="./img/Overview of OpenMDS.JPG" width="525px" height="235px" title="Overview of OpenMDS"></img></p>

Gyeongcheol Shin
## OpenMDS Pipelining
<p align="center"><img src="./img/Pipelined System Interconnect Generation5.png" width="580px" height="400px" title="OpenMDS Pipelining"></img></p>


## OpenMDS Floorplanning
<p align="center"><img src="./img/OpenMDS Floorplanning.JPG" width="580px" height="400px" title="OpenMDS Floorplanning"></img></p>


## Implementation Enviornment
* Ubuntu-18.04 LTS
* GNU/Linux 5.4.0-91-generic x86_64
* Python 3.6.9
* PyInstaller >= 4.5.1
* Vivado 2020.1, 2020.2
* CPU Intel(R) Xeon(R) Gold 6226R CPU @ 2.9GHz
## Shell Generation Command
Set options by file :
<pre><code>python3 src/main.py --board VCU118  \
                   --dir $SHELL_DIR \
                   --file $SHELL_INI_PATH \
                   --version 2020.2

</code></pre>
You shoud write .ini file like this to use option --file

### Example Command
<pre><code>
VCU118
python3 main.py --board VCU118 --dir=../shell/ --file=Experiment_ini/VCU118_s3_d2_shell.ini --version 2020.1

U50
python3 main.py --board U50 --dir=../shell/ --file=Experiment_ini/U50_s2_h16_shell.ini --version 2020.2

</code></pre>
### Command Results
<p align="center"><img src="./img/Command Results.JPG" width="838px" height="854px" title="Command Results"></img></p>

### Generated Outputs
<p align="center"><img src="./img/Generated Files.JPG" width="300px" height="513px" title="Generated Outputs"></img></p>

## INI File for options
<pre><code>
[SLR]
slr_list=0,1,2
slr_freq_list=300,300,300
slr_host_width_list=512,512,512

[DDR]
xdma_ddr_ch=0,1
ddr_slr_list=0,1,2,0,1,2
ddr_ch_list=0,0,0,1,1,1
ddr_dma_list=1,1,1,1,1,1
ddr_dma_width=512,512,512,512,512,512

[HBM]
hbm_clk_freq=450
xdma_hbm_port=31
hbm_slr_list=0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1
hbm_port_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
hbm_dma_list=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
hbm_dma_width=256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256

[Crossing]
cross=False
fifo_src=0,1
fifo_dest=1,0
fifo_number=2,2
fifo_width=256,256
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
|ddr_slr_list|The information of bus between DDR and SLR, pair with ddr_ch_list|
|ddr_ch_list|The information of bus between DDR and SLR, pair with ddr_slr_list|
|ddr_dma_list|Above DDR and SLR bus's number of AXI4 master dma inteface, pair with ddr_dma_width_list|
|ddr_dma_width_list|Above DDR SLR bus's bitwidth of AXI4 master dma interface, pair with ddr_dma_list|
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
|fifo_width|Bitwidth of AXI FIFO|

## CAD Tool Flow

### Vivado Project Generate
Make a Vivado project with your board.

If you want to make example projet, just type it in your linux kernel to make myproj
<code><pre>
vivado -mode gui -source $Dir_of_your_generated_output/VCU118/bd/*.tcl
</pre></code>

Example
<code><pre>
vivado -mode gui -source ./OpenMDS/ShellGenerator/shell/VCU118/bd/*.tcl
</pre></code>

<p align="center"><img src="./img/0_Vivado Project Generation.JPG" width="640px" height="348px" title="0_Project Generate"></img></p>

### Generate Output Products
Generate output products.

<p align="center"><img src="./img/1_Vivado Project Generation.JPG" width="640px" height="348px" title="1_Project Generate"></img></p>

### Add wrapper, constraints
Add .sv, .xdc files to your project.

<p align="center"><img src="./img/2_Vivado Project Generation.JPG" width="640px" height="348px" title="2_Project Generate"></img></p>

### User Logic Instance
SLR.sv files are generated in wrapper directory. Feel free to instance your own custom hardware inside the SLR kernel.


<p align="center"><img src="./img/SLR Kernel.JPG" width="507px" height="340px" title="SLR Kernel"></img></p>

### Device Programming
Generate Bitstream and Device Programming.

<p align="center"><img src="./img/3_Vivado Project Generation.JPG" width="640px" height="348px" title="3_Project Generate"></img></p>

### XDMA Driver Install
<pre><code>./driver/XilinxAR65444/Linux/build-install-driver-linux.sh
reboot
./driver/XilinxAR65444/Linux/Xilinx_Anser_65444_Linux_Files/tests/load_driver.sh
</code></pre>

If you have problem on installation, following the installation guide of https://github.com/Xilinx/dma_ip_drivers/tree/master/XDMA/linux-kernel

### Global Address Map
This is the generated shell's global address information. You (Host) can access the hardware component through these addresses. This is basic global address information that we provide. However, if you are an expert at Vivado then you can change the address or add another hardware component through Vivado flow since we don't block the modification of the shell.

#### VCU118 Shell
|AXI4 Component|Low Address|High Address|
|---|---|---|
|SLR0|0x00_0000_0000|0x00_FFFF_FFFF|
|SLR1|0x01_0000_0000|0x01_FFFF_FFFF|
|SLR2|0x02_0000_0000|0x02_FFFF_FFFF|
|DDR0|0x10_0000_0000|0x10_7FFF_FFFF|
|DDR1|0X10_8000_0000|0x10_FFFF_FFFF|

|AXI4-Lite Component|Low Address|High Address|
|---|---|---|
|SLR0-LITE|0X10_0000|0x10_FFFF|
|SLR1-LITE|0X11_0000|0x11_FFFF|
|SLR2-LITE|0x12_0000|0x12_FFFF|

|Clock Component|Address Offset|
|---|---|
|SLR0_CLK|0x00_0000|
|SLR1_CLK|0x00_1000|
|SLR2_CLK|0x00_2000|

#### U50 Shell
|AXI4 Component|Low Address|High Address|
|---|---|---|
|SLR0|0x00_0000_0000|0x00_FFFF_FFFF|
|SLR1|0x01_0000_0000|0x01_FFFF_FFFF|
|HBM|0x10_0000_0000|0x11_FFFF_FFFF|

|AXI4-Lite Component|Low Address|High Address|
|---|---|---|
|SLR0-LITE|0x10_0000|0X10_FFFF|
|SLR1-LITE|0X11_0000|0x11_FFFF|

|Clock Component|Address Offset|
|---|---|
|SLR0_CLK|0x00_0000|
|SLR1_CLK|0x00_1000|
|HBM_CLK|0x00_2000|


### Basic API
The basic API is provided by XilinxAR65444, XDMA Driver. Please ref "driver/XilinxAR65444/Linux/Xilinx_Answer_65444_Linux.pdf" to use the basic API

|API|Descriptions|
|---|---|
|dma_to_device|Write operation thorugh XDMA AXI4 interface|
|dma_from_device|Read operation thorugh XDMA AXI4 interface|
|reg_rw|Read/Write operation through XDMA AXI4-LITE interface|

## Clock Scaling Sequence
<p align="center"><img src="./img/Clock Scaling Sequence.JPG" width="512px" height="228px" title="Clock Scaling Sequence"></img></p>

### Clock Adjustment API
|API|Descriptions|
|---|---|
|ClockAdjustment|Based on WNS, change the orignal frequecny to scaled frequency|
|ClockCalculator|Directly changes the clock frequency to desirable frequency|

#### How to use ClockAdjustment and ClockCalculator
cd ./driver/XilinxAR65444/Linux/Xilinx_Anser_65444_Linux_Files/tests

##### Scaling the frequency based on WNS value

Example (U50): HBM freq scaling based on WNS value is 0.059ns
<pre><code>./ClockAdjustment /dev/xdma0_user 0x002000 w 0.059
</code></pre>

##### Read the current frequency

Example : Read SLR0_CLK current frequency
<pre><code>./ClockCalculator /dev/xdma0_user 0X000000 w
</code></pre>


##### Direct change of the frequency to desired value

Example : Adjust SLR0_CLK frequency to 200 MHz
<pre><code>./ClockCalculator /dev/xdma0_user 0x000000 w 200
</code></pre>

## Citation
Utilies and experiment of the OpenMDS is illustrated in the IEEE Computer Architecture Letters paper:

>Gyeongcheol Shin, Junsoo Kim, and Joo-Young Kim,
[**OpenMDS: An Open-Source Shell Generation Framework for High-Performance Design on Xilinx Multi-Die FPGAs**](https://ieeexplore.ieee.org/document/9868126)
IEEE Computer Architecture Letters, vol. 21, no. 2, July-December 2022

Please cite the above work if you make use of the tools provided in this repository.

The presentations of the paper are availagble on YouTube:

