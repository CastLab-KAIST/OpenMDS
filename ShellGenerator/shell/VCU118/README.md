## VCU118 Shell

## Global Address Map

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