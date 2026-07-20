<img width="1983" height="793" alt="image" src="https://github.com/user-attachments/assets/2afa957b-46be-457b-8863-d1457923a744" />



***OSHWLAB Viewing link --->  https://oshwlab.com/dhairyak/project_nxljfiwq***


# Agni - the 60% keyboard
### by Dhairya


## About The Keyboard

**Agni is a custom 60% keyboard i have been working on for a few days. It is wired and connects to the laptop via USB-C. It also has an OLED on the top right corner to display data such as time, keyboard settings, etc.**



## Features 

- **60% default keyboard layout** - I chose this as it wouldf allow me to type easily and faster withought having to move my hand a lot.
- **Powered by a RP2040 at its core** - This runs the software required and allows the keyboard signals to be understood by the computer. It also runs the software to control the RGB lights and the OLED screen. 
- **Individual RGB lights for each Key** - So i added individual LED lights under each switch to give it better control to the lighting.


## Repo Structure 

- `src/` - source files for PCB and CAD
- `src/easyeda/` - EasyEDA source files
  - `src/easyeda/keyboard plate/` - src files for the keybard plate PCB
- `src/freecad/` - mechanical CAD sources
`production/` - **for fabrication outputs**
- `production/Keyboard plate PCB/` - PCB fabrication files for the keyboard plate
- `production/Main Keyboard PCB/` - PCB fabrication files for main keyboard PCB  (Gerbers, BOM, Pick & Place)
- `production/cad/` - 3D printing files
- `production/keyboard plate pcb/` -  Plate PCB Gerbers 
- `pics/` - images used in the README and documentation


## Schematic
<img width="632" height="403" alt="image" src="https://github.com/user-attachments/assets/3fb0678b-10f9-4dc3-aec9-3ae926a29cf6" />

<img width="322" height="265" alt="image" src="https://github.com/user-attachments/assets/2ad9c0a6-1501-45e6-a3aa-ee1c7be764d0" />

<img width="700" height="194" alt="image" src="https://github.com/user-attachments/assets/ad948597-ea5a-4027-aca0-a1ab8234e2df" />


## PCB 
<img width="944" height="412" alt="image" src="https://github.com/user-attachments/assets/c9b152b0-44d9-452e-a932-dedd2f1ee436" />

<img width="710" height="422" alt="image" src="https://github.com/user-attachments/assets/5d9ce43c-7ac1-464b-a893-8c8dd81270b7" />

<img width="552" height="347" alt="Screenshot 2026-06-05 220443" src="https://github.com/user-attachments/assets/0ff191ba-d9b7-405c-90ea-077fcfa34334" />
<img width="572" height="297" alt="Screenshot 2026-06-05 220346" src="https://github.com/user-attachments/assets/e81f929a-d488-4ba7-86f7-6c18594b3a71" />
<img width="639" height="299" alt="Screenshot 2026-06-05 220334" src="https://github.com/user-attachments/assets/a3c18fa1-33bf-43ca-b4e5-15562fd8b163" />
<img width="259" height="232" alt="Screenshot 2026-06-04 170705" src="https://github.com/user-attachments/assets/048edcca-d89f-4640-b854-27aef8701f37" />
<img width="959" height="500" alt="Screenshot 2026-06-05 223629" src="https://github.com/user-attachments/assets/299e8c96-8b86-4b02-837c-3f506c52ba1f" />
<img width="650" height="305" alt="Screenshot 2026-06-05 223526" src="https://github.com/user-attachments/assets/44c8de14-adc5-48a0-8203-f3ffaa8a4a23" />



## CAD

<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/83b73c1b-093d-4017-9541-a2dab579d4b4" />

<img width="562" height="290" alt="image" src="https://github.com/user-attachments/assets/86726fd7-fff2-4026-bca5-511899e38ed7" />



- ***Required 3d Printed part***

<img width="586" height="289" alt="image" src="https://github.com/user-attachments/assets/7a216c62-20f0-40ac-a93f-ce510c443c80" />



## How to replicate it (making it yourself) 


***Here are the steps to make this for yourself-***

- - ***ORDERING THE PCB***

- Step 1 - Basically Just Clone or downlaod this repo from github. U can do this by either going to the code button on this repo page and pressing download Zip or u can clone this Repo Or you can go to the Releases on this repo and download the Zip File there too (the fastest way to download is like just going to code and pressing download Zip Or by cloning the Repo.)

- Step 2 - In the the production folder you will find the CAD and PCB folders.
- Step 3 - The CAD folder contains all the 3d Pritnable files for the case of the keyboard. If you wish to u can make any changes to the design or make your own design and use that instead.
- Step 4 - The PCB folder contains the Gerbers, BOM , and CPL files. These are the files that allow you to get the PCB manufactured from JLCPCB (im using JLCPCB) or any other PCB manufacturer(like PCBway or others).
- Step 5 - Upload the gerbers zip file in JLCPCB "Place order / get instant quote" Page (u will need to sign up to order but can get a quote without signing up)
- Step 6 - Change the colour of the PCB in the options JLC gives (if u use JLC PCB most of the times canging colours does not add any charge acc to what i know)
- Step 7 - Select PCBA if u want JLCPCB to assemble the PCB for you but ngl soldering all components by hand is cheaper and saves u a ton of money and also is pretty fun (im hand soldering all components)
- Step 8 - Upload the CPL and BOM files whe JLCPCB asks u to.
- Step 9 - Recheck the position of all components (i faced no problem with this as all components were in the correct place but i have faced issues with the placement in one of my other projects i made in KiCAD)
- Step 10 - Add to cart and order the PCB!! **(if you are Hand soldering the components you will need to buy them from some other place i am using Robu.in as they have cheap components and a very vast library of components and they are cheaper than LCSC in india)**

- Step 11 - If you dont have a 3D PRINTER jlcpcb has a 3d printing service too caled JLC3DP so u can upload the files for the case there and get it printed too but if u have a 3d printer you can just print it youreslf and save a lot of money.

- - ***ORDERING THE KEYBOARD PLATE***

- Step 1 - In the `production/keyboard plate pcb/` folder u will find the gerbers for the Keyboard Plate
- Step 2 - Upload the gerbers to JLCPCB or any other manufacturer and order it after changing the colour if u want to make sure that the thickness is 1.6mm (if u are using any other manufacturer if possible choose 1.5mm thickness but 1.6 too is fine)
- ***NOTE -*** The gerbers in JLCPCB gerber viewer show just a single panel but that is bcs JLCPCB gerber viewer is shitty at showing slot regions however they are there and will be cut btw in the viewer if u zoom in u can see the space outline and a little gap btw the cutouts and the main board so yeah it shows as a single pannel due to JLCPCB's gerber viewer limitations. i checked in other gerber viewers and the holes are perfectly visible



- ***OTHER GERBER VIEWERS -***
<img src="https://cdn.hackclub.com/019e9ba0-ede9-71d3-934f-7710117e75ba/image.png" alt="image"/>

<br/>
<br/>

- ***JLCPCB GERBER VEIWER-***

<br/>
<br/>

  -  **2d -**
<img src="https://cdn.hackclub.com/019e9ba2-2d9b-7b47-9245-ebba229ec75a/image.png" alt="image"/>

<br/>
<br/>

  -  **3d -**
<img src="https://cdn.hackclub.com/019e9ba2-fe02-7c81-841b-a491804c0286/image.png" alt="image"/>



- Step 3 - **NOW TIME TO ASSEMBLE!!!!**

<br/>
<br/>
<br/>

- - ***Assembly***

- Step 1 - WAIT WAIT WAIT for your parts to be delivered
- Step 2 - Once you have all the parts (PCB, CASE and the componets if u are hand soldering the components) place the PCB in the Case (u will need to first hand solder the components if u are handsoldering it and if u chose economic PCBA then u will have to hand solder the switches too first)
- Step 3 - Now put the keyboard plate in the Case too and screw in the screws into the mounting holes in the case.
- Step 4 - Then use a cable to connect the OLED display to the pin headers for it on the main PCB and make sure it is secured properly. Then fit the OLED on the gap on the top part of the case which has the cutout for the OLED. (u might have to like get creative to fix the Oled to the hole but yeah i will just use a bit of hot glue and it should be fine or i might use the spacers that come with the screen if the spacers are tall enough)
- Step 5 - Once the PCB is secured inside the case glue Top Part of the Case shut (top header which has the screen cutout).
- Step 6 - Attatch the Keycaps on the switches...... and then --->
- Step 7 - **BOOM  THERE YOU GO U HAVE IT MADE!!!**


## BOM- Bill Of Materials


| No. | Qty | Comment / Part | Designator | Footprint | Value | Manufacturer Part | Manufacturer | Supplier |
|:--:|:--:|---|---|---|---|---|---|---|
| 1 | 75 | 100nF Capacitor | C1, C70-C143 | C0805 | 100nF | - | - | - |
| 2 | 2 | 15pF Capacitor | C65, C66 | C0805 | 15pF | - | - | - |
| 3 | 2 | 10uF Capacitor | C67, C68 | C0805 | 10uF | - | - | - |
| 4 | 61 | 1N4148W-7-F Diode | D1-D61 | SOD-123_L2.7-W1.6-LS3.7-RD-1 | 1N4148W-7-F | - | DIODES (美台) | C83528 |
| 5 | 61 | SK6812MINI-E RGB LED | LED1-LED61 | LED-SMD_4P-L3.2-W2.8-LS5.9_SK6812MINI-E | - | SK6812MINI-E | 欧思科光电 | C5149201 |
| 6 | 1 | OLED Header | OLED1 | HDR-TH_4P-P2.00-V-M | - | PZ200V-11-04P | XFCN (兴飞) | C541858 |
| 7 | 2 | 4.7K Resistor | R1, R72 | R0805 | 4.7K | - | - | - |
| 8 | 2 | 5.1K Resistor | R65, R66 | R0805 | 5.1K | - | - | - |
| 9 | 2 | 27Ω Resistor | R67, R68 | R0805 | 27Ω | - | - | - |
| 10 | 2 | 10K Resistor | R70, R71 | R0805 | 10K | - | - | - |
| 11 | 61 | 100Ω Resistor | R73-R133 | R0805 | 100Ω | - | - | - |
| 12 | 2 | Reset / Boot Push Button | SW3, SW4 | SW-SMD_4P-L6.0-W6.0-P4.50-LS9.0_H5.0 | KH-6X6X5H-STM | KH-6X6X5H-STM | Kinghelm (金航标) | C2837531 |
| 13 | 61 | Kailh MX Hot Swap Socket | SW5-SW65 | KEY-TH_CPG1511F01S0X | CPG151101S03 | CPG151101S03 | Kailh (凯华) | C404350 |
| 14 | 1 | RP2040 MCU | U2 | LQFN-56_L7.0-W7.0-P0.4-EP | RP2040 | RP2040 | Raspberry Pi | C2040 |
| 15 | 1 | SPI Flash | U3 | SOIC-8_L5.3-W5.3-P1.27-LS8.0-BL | W25Q16JVSSIQ | W25Q16JVSSIQ | Winbond (华邦) | C131025 |
| 16 | 1 | 12MHz Crystal | U4 | CRYSTAL-SMD_4P-L3.2-W2.5-BL | 12MHz | ABM8-272-T3 | Abracon | C20625731 |
| 17 | 1 | 3.3V Voltage Regulator | U5 | SOT-89-3_L4.5-W2.5-P1.50-LS4.2-BR | AMS1117-3.3 | AMS1117-3.3 | GOODWORK (固得沃克) | C6067465 |
| 18 | 1 | USB Type-C Connector | USB1 | USB-C-SMD_TYPE-C-16PIN-2MD-073 | TYPE-C 16PIN 2MD(073) | TYPE-C 16PIN 2MD(073) | SHOU HAN (首韩) | C2765186 |
| 19 | 7 | Gateron G Switches (Pack of 10) | - | - | - | - | - | Meckeys |
| 20 | 1 | 60% Keycap Set | - | - | - | - | - | Amazon |
| 21 | 1 | Soldering Iron | - | - | - | - | - | Amazon |
| 22 | 1 | Plate Mount Stabilizer Set | - | - | - | - | - | GenesisPC |
| 23 | 1 | PCB (Main Keyboard PCB + Plate) | - | - | - | - | - | JLCPCB |



## Total Cost - 

***32(PCB+Plate+shipping from jlcpcb) + 28.73(components) + 15.04 (Switches) + 20.3 (Key Caps, Stabilizers, Soldering Iron) + 12.8(TAX)
= 109.87 USD***


**Yeah this was expensive but would be like WAYYYYYY more expensive if i chose PCBA**


## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
