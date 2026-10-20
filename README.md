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



## PCB
### Schematic & Routing


<table>
  <tr align="center">
    <td><img src="https://github.com/user-attachments/assets/b8373c54-8b4d-447c-9030-a490d280065e" width="3000" alt="schematic1"></td>
  </tr>
  
<table>  
  </tr>
  
  <td align="center">
    <center><b> The Switches </b></center> 
    <img src="https://github.com/user-attachments/assets/08171371-c653-4dd1-8574-386e1589639b" width="500" alt="schematic1">
    <center><b> Front Layer Routing </b></center>  
    <img src="https://github.com/user-attachments/assets/9815128c-d353-45f5-a5b5-4423fd33db91" width="1000" alt="PCB front">  
  <td align="center">
     <center><b> The RGBs </b></center> 
     <img src="https://github.com/user-attachments/assets/dc78b738-6e8c-487d-a492-112369d29792" width="500" alt="schematic1">
     <center><b> Back Layer Routing </b></center>  
     <img src="https://github.com/user-attachments/assets/e752917d-6c10-4dd2-a1b9-8def7d42fdf6" width="1000" alt="PCB back">
  
  </tr>
  <table align="center">
  <tr align="center">
  <td><img src="https://github.com/user-attachments/assets/e4c9e635-907b-41a7-b0ec-ed0d222508d4" width="400" alt="MCU zoom"></td>
  </tr>
  </table>
</table>




## Renders and CAD

<table>
  </tr>
    <td><img src="https://github.com/user-attachments/assets/83b73c1b-093d-4017-9541-a2dab579d4b4" width="500" alt="Render25"></td>
    <td><img src="https://github.com/user-attachments/assets/86726fd7-fff2-4026-bca5-511899e38ed7" width="500" alt="Render24"></td>
    <td><img src="https://github.com/user-attachments/assets/7a216c62-20f0-40ac-a93f-ce510c443c80" width="500" alt="Render26"></td>
  </tr>
  </tr>
    <td><img src="https://github.com/user-attachments/assets/ca8aa95b-fc8a-49e7-8ba8-890c046fb755" width="500" alt="Render23"></td>
    <td><img src="https://github.com/user-attachments/assets/03d7c890-9ce9-44a0-b2d9-a6fcaa4b3285" width="500" alt="Render22"></td>
    <td><img src="https://github.com/user-attachments/assets/485d4f06-0681-4f18-a14b-7d370bd21791" width="500" alt="Render17"></td>   
  </tr>
   
</table>



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
<img src="https://cdn.hackclub.com/019e9ba0-ede9-71d3-934f-7710117e75ba/image.png" width="500" alt="image"/>

<br/>
<br/>

- ***JLCPCB GERBER VEIWER-***

<br/>
<br/>

  -  **2d -**
<img src="https://cdn.hackclub.com/019e9ba2-2d9b-7b47-9245-ebba229ec75a/image.png" width="500" alt="image"/>

<br/>
<br/>

  -  **3d -**
<img src="https://cdn.hackclub.com/019e9ba2-fe02-7c81-841b-a491804c0286/image.png" width="500" alt="image"/>



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


## BOM - Bill Of Materials

| # | Component | Qty | Unit Price (USD) | Subtotal (USD) | Source |
|---:|---|---:|---:|---:|---|
| 1 | Gateron G Pro 3.0 Black Switches | 7 | $1.99 | $13.90 | [Meckeys](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-g-pro-3-0-switch/) |
| 2 | SK6812 MINI-E RGB LEDs | 200 pcs (1 pack) | $0.091/LED | $18.23 | [Desertcart](https://www.desertcart.in/products/792846066-200pcs-sk6812-mini-e-rgb-similar-ws2812b-sk6812-3228-smd) |
| 3 | ZORBES 130-Key Topographic Keycap Set | 1 | $10.50 | $10.50 | [Amazon](https://www.amazon.in/ZORBES%C2%AE130-Key-Topographic-Minimalist-Mechanical-Keyboard/dp/B0GFNPXVJL/ref=asc_df_B0GFNPXVJL?mcid=33fd7e7f39dd3c89b190bd378877b5be&tag=googleshopdes-21&linkCode=df0&hvadid=710150529821&hvpos=&hvnetw=g&hvrand=12383538402096910029&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062077&hvtargid=pla-2485351987562&hvocijid=12383538402096910029-B0GFNPXVJL-&hvexpln=0&gad_source=1&th=1) |
| 4 | Durock Plate Mount Stabilizers V3 (6.25U + 4×2U) | 1 set | $3.99 | $3.99 | [GenesisPC](https://www.genesispc.in/products/durock-plate-mount-stabilizers-6-25u-4x2u-black) |
| 5 | Raspberry Pi RP2040 MCU | 1 | $0.67 | $0.67 | [Robu.in](https://robu.in/product/raspberry-pi-rp2040/?gad_source=1&gad_campaignid=19974686076&gbraid=0AAAAADvLFWf_R1sTux_TmVupPlPWzmUc3&gclid=CjwKCAjw_9bWBhBGEiwAomyTIp0sHv-Dled86FNq8si2NKOjMXT6584Ut5bwzzMYilZOCYqb8uxrmxoCS9kQAvD_BwE) |
| 6 | Winbond W25Q16JWSNIQ 16-Mbit SPI NOR Flash | 1 | $3.31 | $3.31 | [Robu](https://robu.in/product/w25q16jwsniq-winbond-elec-16mbit-spi-133mhz-soic-8-nor-flash-rohs/) |
| 7 | YXC YSX321SL 12 MHz Crystal, 12 pF | 1 | $0.21 | $0.21 | [Robu](https://robu.in/product/ysx321sl-12mhz-12pf-10ppm-4pins-smd-smt-metal-surface-quartz-crystal-pack-of-2/) |
| 8 | AMS1117-3.3V Voltage Regulator | 2 | $0.095 | $0.19 | [Robu](https://robu.in/product/ams1117-3-3v-1a-sot-223-voltage-regulator-ic-pack-of-5-ics/) |
| 9 | USB-C 6-Pin Female SMD Connector | 2 | $0.63 | $1.26 | [Robu](https://robu.in/product/type-c-31-m-16-hroparts-1-6p-female-type-c-smd-usb/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTImS8JJx_1dcy8OhNFxiNLYgdR8fdaIEOQnwv9N5uM7Xu1CSRziaW0xoCbb4QAvD_BwE) |
| 10 | 0805 5.1 kΩ Resistor | 25 | $0.0049 | $0.12 | [robu](https://robu.in/product/rc0805jr-075k1l-yageo-smd-chip-resistor-5-1-kohm-%C2%B1-5-125-mw-0805-2012-metric-thick-film-general-purpose/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTItVNAmL8ud3l0oR2NcBUsKY3upMPlydpC5po_xbzjzIUe72o4xY5fRoCpb0QAvD_BwE) |
| 11 | 1N4148W SOD-123 Switching Diode | 61 | $0.0150 | $0.92 | [robu](https://robu.in/product/1n4148w-slkor-75v-1v-4ns-150ma-sod-123-switching-diodes-rohs/) |
| 12 | 6×6 mm SMD Tactile Switch | 5 | $0.0315 | $0.16 | [robu](https://robu.in/product/tsd003a06526a02-bzcn-6mm-6-5mm-50ma-round-button-standing-paste-6mm-260gf-12v-smd-tactile-switches-rohs/) |
| 13 | 0805 100 nF X7R Capacitor | 75 | $0.0090 | $0.68 | [robu](https://robu.in/product/cc0805kkx7r0bb104-yageo-100v-100nf-x7r-%c2%b110-0805-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/) |
| 14 | 0805 15 pF C0G Capacitor | 37 | $0.0032 | $0.12 | [robu](https://robu.in/product/cc0805jrnpo9bn150-yageo-smd-multilayer-ceramic-capacitor-15-pf-50-v-0805-2012-metric-%c2%b1-5-c0g-np0-cc-series/) |
| 15 | 0805 10 µF X7R Capacitor | 5 | $0.0275 | $0.14 | [robu](https://robu.in/product/10uf-10000nf-25-v-capacitor-0805-smd-package-pack-of-10/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTIuFTjV51TC_Q0pSxvgOzf-jQgy7thWSs5EMZjCHNMMxL01c9guiQUxoC2u4QAvD_BwE) |
| 16 | 0805 4.7 kΩ Resistor | 30 | $0.0039 | $0.12 | [robu](https://robu.in/product/rc0805jr-074k7l-yageo-res-thick-film-0805-4-7k-ohm-5-0-125w1-8w-%C2%B1100ppm-c-pad-smd-t-r/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTIgNwqP0vozdwI0nCqHD3W6yTnRFVlT1DM-9fzsBtOlxpVjiluZNZRBoCDzAQAvD_BwE) |
| 17 | 0805 5.1 kΩ Resistor | 10 | $0.0134 | $0.13 | [robu](https://robu.in/product/rc0805fr-075k1l-yageo-res-thick-film-0805-5-1k-ohm-1-0-125w1-8w-%C2%B1100ppm-c-pad-smd-t-r/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTIqT30USjnw0u-sbCqHCgRd9YPlO66PgZy0WKoPSx6rrgcaZZNmjKwxoC1zMQAvD_BwE) |
| 18 | 0805 10 kΩ Resistor | 3 | $0.0368 | $0.11 | [robu](https://robu.in/product/ac0805fr-0710kl-yageo-res-thick-film-0805-10k-ohm-1-0-125w1-8w-%c2%b1100ppm-c-pad-smd-t-r-automotive-aec-q200/) |
| 19 | 0805 100 Ω Resistor | 61 | $0.0086 | $0.53 | [robu](https://robu.in/product/ac0805fr-07100rl-yageo-res-thick-film-0805-100-ohm-1-0-125w1-8w-%C2%B1100ppm-c-pad-smd-t-r-automotive-aec-q200/?gad_source=1&gad_campaignid=17416544847&gbraid=0AAAAADvLFWcXltn1WxX2ksNJxKfcHdn7S&gclid=CjwKCAjw_9bWBhBGEiwAomyTIoFnihmnT3pOZvPHf5xgs4FeStJvhCwl_DMdwoVWpyWopQPQk-n5HxoCAqQQAvD_BwE) |
| 20 | 0805 27 Ω Resistor | 60 | $0.0018 | $0.11 | [robu](https://robu.in/product/rc0805fr-0727rl-yageo-smd-chip-resistor-27-ohm-%C2%B1-1-125-mw-0805-2012-metric-thick-film-general-purpose/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdRNkR22LDjLdAY60rEt47Dr&gclid=CjwKCAjw_9bWBhBGEiwAomyTIpEJ_z28kI0mWdvpRXCDY8xi99n8M2YDRVe1qBzodJP4EoTm4YqGqRoCRU0QAvD_BwE) |
| 21 | 0.91" 128×32 I²C OLED Display | 1 | $1.59 | $1.59 | [robu](https://robu.in/product/blue-oled-display-module/?gad_source=1&gad_campaignid=17416544847&gbraid=0AAAAADvLFWcXltn1WxX2ksNJxKfcHdn7S&gclid=CjwKCAjw_9bWBhBGEiwAomyTIuoqUw8-unboGXwYIwoXmIueTpUEYWfMhrPvIzaD8IqgiWYjOs6LNxoCSZsQAvD_BwE) |
| 22 | Agni Keyboard PCB | 5 | $3.62 | $18.10 | [JLCPCB](https://cart.jlcpcb.com/quote) |
| 23 | Agni Keyboard Plate PCB | 5 | $3.00 | $15.00 | [JLCPCB](https://cart.jlcpcb.com/quote) |
| | **Components Subtotal** | | | **$90.09** | |
| | **Tax** | | | **$19.78** | |
| | **Grand Total** | | | **$109.87** | |

**Yeah this was expensive but would be like WAYYYYYY more expensive if i chose PCBA**


## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
- **[INERTIA-102](https://github.com/Gusus169/INERTIA-102-The-Mechanical-Keyboard)** - Image formating
