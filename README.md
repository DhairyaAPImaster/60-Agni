# Agni - the 60% keyboard
### by Dhairya


## About The Keyboard

**Agni is a custom 60% keyboard i have been working on for a few days. It is wired and connects to the laptop via USB-C. It also has an OLED on the top right corner to display data such as time, keyboard settings, etc.**



## Features 

- **60% default keyboard layout** - I chose this as it wouldf allow me to type easily and faster withought having to move my hand a lot.
- **Powered by a RP2040 at its core** - This runs the software required and allows the keyboard signals to be understood by the computer. It also runs the software to control the RGB lights and the OLED screen. 
- **Individual RGB lights for each Key** - So i added individual LED lights under each switch to give it better control to the lighting.


## Repo Structure 

`src/` - source files for PCB and CAD
- `src/easyeda/` - EasyEDA source files
  - `src/easyeda/keyboard plate/` - src files for the keybard plate PCB
- `src/freecad/` - mechanical CAD sources
`production/` - **for fabrication outputs**
- `production/pcb/` - PCB fabrication files (Gerbers, BOM, Pick & Place)
- `production/cad/` - 3D printing files
- `production/keyboard plate pcb/` -  Plate PCB Gerbers 
- `pics/` - images used in the README and documentation
- `Electronic cad/` - 3d model of PCB from EasyEDA 


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
<img width="592" height="365" alt="Screenshot 2026-06-04 154056" src="https://github.com/user-attachments/assets/d53250ec-fead-4bb5-9bf3-f66082d70a76" />
<img width="1186" height="632" alt="Screenshot 2026-06-02 180231" src="https://github.com/user-attachments/assets/2461789b-3ee0-40ab-b48b-f77d3294aa43" />
<img width="1919" height="1079" alt="Screenshot 2026-06-02 180218" src="https://github.com/user-attachments/assets/0ee9a8ed-7d73-456c-be46-05c85ed1e826" />
<img width="1425" height="846" alt="Screenshot 2026-06-02 180203" src="https://github.com/user-attachments/assets/4fd4a1b7-4695-4013-88c2-166f376d40a9" />
<img width="1330" height="687" alt="Screenshot 2026-06-02 180124" src="https://github.com/user-attachments/assets/f13a62f0-a7cc-4bb0-826a-f60e8f6f4a24" />
<img width="1919" height="1035" alt="Screenshot 2026-06-02 180112" src="https://github.com/user-attachments/assets/07723057-9339-4fe9-8043-167f8fd5a43a" />
<img width="1918" height="1031" alt="Screenshot 2026-06-02 173944" src="https://github.com/user-attachments/assets/eae6c6c1-2a45-4c79-bca7-12006c07f9c3" />
<img width="1416" height="826" alt="Screenshot 2026-06-02 173905" src="https://github.com/user-attachments/assets/c7f86624-9a88-45f1-9ac5-ef877c71b8dc" />
<img width="571" height="693" alt="Screenshot 2026-06-02 172739" src="https://github.com/user-attachments/assets/fbfaf654-afee-4fad-93d4-d38d97311476" />
<img width="1036" height="606" alt="Screenshot 2026-06-02 154645" src="https://github.com/user-attachments/assets/b41b7895-bb78-4914-980f-e4cb112a19f9" />
<img width="1177" height="783" alt="image (3)" src="https://github.com/user-attachments/assets/8b8cee5e-74f8-4bf9-875f-6475e7c64ca4" />
<img width="862" height="562" alt="image (2)" src="https://github.com/user-attachments/assets/c8a943cc-8abf-4e49-a2af-ad647043c02f" />
<img width="1280" height="562" alt="image (1)" src="https://github.com/user-attachments/assets/024a39c4-e4e6-4299-b91d-125224289754" />
<img width="712" height="311" alt="Screenshot 2026-06-05 223108" src="https://github.com/user-attachments/assets/40b79948-08d5-43fb-906d-bc1aa3ef5aba" />
<img width="710" height="422" alt="Screenshot 2026-06-05 223635" src="https://github.com/user-attachments/assets/55ce60c2-4a08-4c4e-b044-96bf26c28c20" />
<img width="959" height="500" alt="Screenshot 2026-06-05 223629" src="https://github.com/user-attachments/assets/299e8c96-8b86-4b02-837c-3f506c52ba1f" />
<img width="650" height="305" alt="Screenshot 2026-06-05 223526" src="https://github.com/user-attachments/assets/44c8de14-adc5-48a0-8203-f3ffaa8a4a23" />



## CAD

<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/83b73c1b-093d-4017-9541-a2dab579d4b4" />

<img width="562" height="290" alt="image" src="https://github.com/user-attachments/assets/86726fd7-fff2-4026-bca5-511899e38ed7" />

<img width="526" height="289" alt="image" src="https://github.com/user-attachments/assets/b238aca4-6953-442a-91d9-bf81edd12e2d" />


- ***Required 3d Printed parts***

<img width="953" height="539" alt="image" src="https://github.com/user-attachments/assets/adf19bfc-f17b-4f6c-841c-520e911f6592" />

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
- Step 10 - Add to cart and order the PCB!! **(if you are Hand soldering the components you will need to buy them from some other place i am using LCSC as they have cheap components and a very vast library of components and also automated finding if u upload the BOM which is like really helpfull since this project has a lot of components)**

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
| No. | Quantity | Comment | Designator | Footprint | Value | Manufacturer Part | Manufacturer | Supplier Part | Supplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 75 | 100nF | C1,C70,C71,C72,C73,C74,C75,C76,C77,C78,C79,C80,C81,C82,C83,C84,C85,C86,C87,C88,C89,C90,C91,C92,C93,C94,C95,C96,C97,C98,C99,C100,C101,C102,C103,C104,C105,C106,C107,C108,C109,C110,C111,C112,C113,C114,C115,C116,C117,C118,C119,C120,C121,C122,C123,C124,C125,C126,C127,C128,C129,C130,C131,C132,C133,C134,C135,C136,C137,C138,C139,C140,C141,C142,C143 | C0805 | 100nF |  |  |  | 
| 2 | 2 | 15pF | C65,C66 | C0805 | 15pF |  |  |  | 
| 3 | 2 | 10uF | C67,C68 | C0805 | 10uF |  |  |  | 
| 4 | 61 | 1N4148W-7-F | D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43,D44,D45,D46,D47,D48,D49,D50,D51,D52,D53,D54,D55,D56,D57,D58,D59,D60,D61 | SOD-123_L2.7-W1.6-LS3.7-RD-1 | 1N4148W-7-F |  | DIODES(美台) | C83528 | LCSC |
| 5 | 61 | SK6812MINI-E | LED1,LED2,LED3,LED4,LED5,LED6,LED7,LED8,LED9,LED10,LED11,LED12,LED13,LED14,LED15,LED16,LED17,LED18,LED19,LED20,LED21,LED22,LED23,LED24,LED25,LED26,LED27,LED28,LED29,LED30,LED31,LED32,LED33,LED34,LED35,LED36,LED37,LED38,LED39,LED40,LED41,LED42,LED43,LED44,LED45,LED46,LED47,LED48,LED49,LED50,LED51,LED52,LED53,LED54,LED55,LED56,LED57,LED58,LED59,LED60,LED61 | LED-SMD_4P-L3.2-W2.8-LS5.9_SK6812MINI-E |  | SK6812MINI-E | 欧思科光电 | C5149201 | LCSC |
| 6 | 1 | PZ200V-11-04P | OLED1 | HDR-TH_4P-P2.00-V-M |  | PZ200V-11-04P | XFCN(兴飞) | C541858 | LCSC |
| 7 | 2 | 4.7K | R1,R72 | R0805 | 4.7K |  |  |  | 
| 8 | 2 | 5.1K | R65,R66 | R0805 | 5.1K |  |  |  | 
| 9 | 2 | 27ohm | R67,R68 | R0805 | 27ohm |  |  |  | 
| 10 | 2 | 10K | R70,R71 | R0805 | 10K |  |  |  | 
| 11 | 61 | 100 | R73,R74,R75,R76,R77,R78,R79,R80,R81,R82,R83,R84,R85,R86,R87,R88,R89,R90,R91,R92,R93,R94,R95,R96,R97,R98,R99,R100,R101,R102,R103,R104,R105,R106,R107,R108,R109,R110,R111,R112,R113,R114,R115,R116,R117,R118,R119,R120,R121,R122,R123,R124,R125,R126,R127,R128,R129,R130,R131,R132,R133 | R0805 | 100 |  |  |  | 
| 12 | 2 | KH-6X6X5H-STM | SW3,SW4 | SW-SMD_4P-L6.0-W6.0-P4.50-LS9.0_H5.0 | KH-6X6X5H-STM | kinghelm(金航标) | C2837531 | LCSC |
| 13 | 61 | CPG151101S03 | SW5,SW6,SW7,SW8,SW9,SW10,SW11,SW12,SW13,SW14,SW15,SW16,SW17,SW18,SW19,SW20,SW21,SW22,SW23,SW24,SW25,SW26,SW27,SW28,SW29,SW30,SW31,SW32,SW33,SW34,SW35,SW36,SW37,SW38,SW39,SW40,SW41,SW42,SW43,SW44,SW45,SW46,SW47,SW48,SW49,SW50,SW51,SW52,SW53,SW54,SW55,SW56,SW57,SW58,SW59,SW60,SW61,SW62,SW63,SW64,SW65 | KEY-TH_CPG1511F01S0X | CPG151101S03 | Kailh(凯华) | C404350 | LCSC |
| 14 | 1 | RP2040 | U2 | LQFN-56_L7.0-W7.0-P0.4-EP | RP2040 | Raspberry Pi(树莓派) | C2040 | LCSC |
| 15 | 1 | W25Q16JVSSIQ | U3 | SOIC-8_L5.3-W5.3-P1.27-LS8.0-BL | W25Q16JVSSIQ | Winbond(华邦) | C131025 | LCSC |
| 16 | 1 | 12MHz | U4 | CRYSTAL-SMD_4P-L3.2-W2.5-BL | 12MHz | ABM8-272-T3 | ABRACON | C20625731 | LCSC |
| 17 | 1 | AMS1117-3.3 | U5 | SOT-89-3_L4.5-W2.5-P1.50-LS4.2-BR | AMS1117-3.3 | GOODWORK(固得沃克) | C6067465 | LCSC |
| 18 | 1 | TYPE-C 16PIN 2MD(073) | USB1 | USB-C-SMD_TYPE-C-16PIN-2MD-073 | TYPE-C 16PIN 2MD(073) | SHOU HAN(首韩) | C2765186 | LCSC |



## Total Cost - 

***31.96(PCB) + 59.99(components) + 14.93 (Switches) + 20.14 (Key Caps, Stabilizers, Soldering Iron) + 40 (TAX + Shipping of 3d printed case from printing legion)
= 167.02 USD
U might be wondering why are is the TAX soooo high well thats cause India imposes heavy import tax on chinese goods ( 39- 40% on total value including shipping) so yeah.***


**Yeah this was expensive but would be like 30-40 USDD more expensive if i chose PCBA**


## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
