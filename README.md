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
`pics/` - images used in the README and documentation
`Electronic cad/` - 3d model of PCB from EasyEDA 


## Schematic
<img width="632" height="403" alt="image" src="https://github.com/user-attachments/assets/3fb0678b-10f9-4dc3-aec9-3ae926a29cf6" />

<img width="322" height="265" alt="image" src="https://github.com/user-attachments/assets/2ad9c0a6-1501-45e6-a3aa-ee1c7be764d0" />

<img width="700" height="194" alt="image" src="https://github.com/user-attachments/assets/ad948597-ea5a-4027-aca0-a1ab8234e2df" />


## PCB 

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



## BOM- Bill Of Materials





## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
