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
- `src/freecad/` - mechanical CAD sources
`production/` - **for fabrication outputs**
- `production/pcb/` - PCB fabrication files (Gerbers, BOM, Pick & Place)
- `production/cad/` - 3D printing files
- `production/keyboard plate pcb/` -  Plate PCB Gerbers 
`pics/` - images used in the README and documentation
`Electronic cad/` - 3d model of PCB from EasyEDA 


## Schematic




## PCB 





## CAD





- ***Required 3d Printed parts***





## BOM- Bill Of Materials





## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
