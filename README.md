# M3U To MP3 Converter
Program Retired -> Re-Written C# version
## Required Packages:
- SAUIGeo (SAU) : `pip install SAUIGeo` -> Link https://pypi.org/manage/project/sauigeo/releases/
---
## Requirements for M3U Converter:
- Python (3.11+) - (If using Source Code)
---
## How to use
- Open the python program
- Select the M3U in the appropiate absolute path (check "How to ensure M3U file is in right place") for more info
- The "Select Save Location" button is where the playlist files should be stored on completion.
---
## How to ensure M3U file is in the right place
- Right click on the M3U file and open with notepad
- Ensure that the directory it is pointing to is reachable.
- For example:
    - "../song/song.mp3"
    - You can ignore ../ in the program and instead just put all the song folders and M3U file in one path!
    - If you are unsure an error log file will be made.
---
## Important:
Releases are only full number versions **V1.xx** (Such as V1.3, 1.4, etc)!<br>
Versions like V1.03.1 **WILL NOT RECIEVE A RELEASE!**<br>
New SAU system released with V1.04.1 - Previous Versions don't require it!
## Versions:
### V1.04.2:
- Fixed poor program communication.
### V1.04.1 + SAU1.03.1:
- Added new UI system - SAU
    - Program to Standardise App Ui (SAU)
    - SAU is a theme management system.
    - SAU uses .json to store a theme, which means that it's very easy to change UI elements.
- Added new menus into menu bar
    - Settings and Help
#### V1.03.1:
- Fixed MinSize of the window
### V1.03:
- Finally released the program after testing.
