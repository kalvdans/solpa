EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L RPI-ADS1115 U?
U 1 1 598B60B4
P 4550 6750
F 0 "U?" H 4500 8100 60  0000 C CNN
F 1 "RPI-ADS1115" H 4500 8100 60  0000 C CNN
F 2 "" H 4500 8100 60  0001 C CNN
F 3 "" H 4500 8100 60  0001 C CNN
	1    4550 6750
	1    0    0    -1  
$EndComp
Text GLabel 5250 3750 1    60   Input ~ 0
Bat-
Text GLabel 3750 3350 1    60   Input ~ 0
Bat+
Text GLabel 3950 3350 1    60   Input ~ 0
Solpa+
Text GLabel 5400 3750 1    60   Input ~ 0
Solpa-
$Comp
L R R1
U 1 1 598B620A
P 4800 4450
F 0 "R1" V 4880 4450 50  0000 C CNN
F 1 "100k" V 4800 4450 50  0000 C CNN
F 2 "" V 4730 4450 50  0000 C CNN
F 3 "" H 4800 4450 50  0000 C CNN
	1    4800 4450
	0    1    1    0   
$EndComp
Connection ~ 5000 4450
Wire Wire Line
	5000 4450 5000 4950
Wire Wire Line
	4950 4450 5000 4450
Connection ~ 4550 4450
Wire Wire Line
	4650 4450 4550 4450
Wire Wire Line
	4550 4250 4550 4950
Connection ~ 5000 4950
Connection ~ 4550 4950
$Comp
L R R2
U 1 1 598B649E
P 4950 4250
F 0 "R2" V 5030 4250 50  0000 C CNN
F 1 "10k" V 4950 4250 50  0000 C CNN
F 2 "" V 4880 4250 50  0000 C CNN
F 3 "" H 4950 4250 50  0000 C CNN
	1    4950 4250
	0    1    1    0   
$EndComp
Wire Wire Line
	4550 4250 4800 4250
Wire Wire Line
	5100 4250 5400 4250
$Comp
L R R?
U 1 1 598B6665
P 4800 4650
F 0 "R?" V 4880 4650 50  0000 C CNN
F 1 "100k" V 4800 4650 50  0000 C CNN
F 2 "" V 4730 4650 50  0000 C CNN
F 3 "" H 4800 4650 50  0000 C CNN
	1    4800 4650
	0    1    1    0   
$EndComp
Connection ~ 5000 4650
Connection ~ 4400 4650
Wire Wire Line
	4650 4650 4400 4650
Wire Wire Line
	4400 4100 4400 4950
$Comp
L R R?
U 1 1 598B6702
P 4950 4100
F 0 "R?" V 5030 4100 50  0000 C CNN
F 1 "10k" V 4950 4100 50  0000 C CNN
F 2 "" V 4880 4100 50  0000 C CNN
F 3 "" H 4950 4100 50  0000 C CNN
	1    4950 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	5100 4100 5250 4100
Wire Wire Line
	4800 4100 4400 4100
Wire Wire Line
	5250 4100 5250 3750
Wire Wire Line
	5400 4250 5400 3750
Connection ~ 4400 4950
Connection ~ 4700 4950
Connection ~ 4850 4950
Connection ~ 4250 4950
Wire Wire Line
	4950 4650 5000 4650
$Comp
L R R?
U 1 1 598B6856
P 4450 3900
F 0 "R?" V 4530 3900 50  0000 C CNN
F 1 "10k" V 4450 3900 50  0000 C CNN
F 2 "" V 4380 3900 50  0000 C CNN
F 3 "" H 4450 3900 50  0000 C CNN
	1    4450 3900
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 598B685E
P 4450 3750
F 0 "R?" V 4530 3750 50  0000 C CNN
F 1 "10k" V 4450 3750 50  0000 C CNN
F 2 "" V 4380 3750 50  0000 C CNN
F 3 "" H 4450 3750 50  0000 C CNN
	1    4450 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	4600 3750 4850 3750
Connection ~ 4700 3900
Connection ~ 4850 3750
Wire Wire Line
	4600 3900 4700 3900
Wire Wire Line
	4700 3600 4700 4950
Wire Wire Line
	4850 3450 4850 4950
Connection ~ 4250 3900
Wire Wire Line
	4250 3300 4250 4950
Wire Wire Line
	4250 3900 4300 3900
Wire Wire Line
	4250 3750 4300 3750
$Comp
L R R?
U 1 1 598B6A01
P 4450 3600
F 0 "R?" V 4530 3600 50  0000 C CNN
F 1 "100k" V 4450 3600 50  0000 C CNN
F 2 "" V 4380 3600 50  0000 C CNN
F 3 "" H 4450 3600 50  0000 C CNN
	1    4450 3600
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 598B6A7D
P 4450 3450
F 0 "R?" V 4530 3450 50  0000 C CNN
F 1 "100k" V 4450 3450 50  0000 C CNN
F 2 "" V 4380 3450 50  0000 C CNN
F 3 "" H 4450 3450 50  0000 C CNN
	1    4450 3450
	0    1    1    0   
$EndComp
Wire Wire Line
	4700 3600 4600 3600
Wire Wire Line
	4850 3450 4600 3450
Wire Wire Line
	3950 3450 4300 3450
Wire Wire Line
	3950 3450 3950 3350
Wire Wire Line
	3750 3600 4300 3600
Wire Wire Line
	3750 3600 3750 3350
Text Notes 4000 2900 1    60   ~ 0
0 .. 36.3 V
Text Notes 3800 2900 1    60   ~ 0
0 .. 36.3 V
Text Notes 5450 3250 1    60   ~ 0
-0.33 .. 3.3 V
Text Notes 5300 3250 1    60   ~ 0
-0.33 .. 3.3 V
Connection ~ 4250 3750
$Comp
L GND #PWR?
U 1 1 598B6F86
P 4250 3300
F 0 "#PWR?" H 4250 3050 50  0001 C CNN
F 1 "GND" H 4250 3150 50  0000 C CNN
F 2 "" H 4250 3300 50  0000 C CNN
F 3 "" H 4250 3300 50  0000 C CNN
	1    4250 3300
	-1   0    0    1   
$EndComp
$EndSCHEMATC
