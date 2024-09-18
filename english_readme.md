# SmartGnomikLib
### Smart Home Controller

This library lets you control your smart devices via voice commands.     
As a controller device you can use Orange Pi or Raspberry Pi.
Also you can make non-smart devices smart by installing ESP8266/ESP32 in them.

Vids about library and devices are here [Russian]: https://youtube.com/@ESPdev      
Main channel [Russian]: https://youtube.com/c/MautozTech

### Using this library you can control different types of devices:
- Devices that can be controlled via GET-requests (web-requests)      
  (for example ESP8266/ESP32 boards/devices)
- Devices compatible with Tuya platform
- PC

Image with preconfigured Armbian and program for Orange Pi PC2 (and other compatible devices): [Google Drive](https://drive.google.com/file/d/128jVv7pF3YjIEn2ycC7YM1Svyow9LUSr)      

Support developer / Free investment lifehacks [Russian]: https://pomoex.ru

### Installing and configuring OS:
1. <details> 
      <summary>Download Armbian (or another) image</summary>
  
      ```
      Armbian 20.08 like mine: https://drive.google.com/file/d/1FFzEcmnzOcK9rwSuBZPOyZdQ0BdvRMhi
      ```
   </details>
2. <details> 
      <summary>If you want: Configure CPU frequency</summary>
  
      ```
      Use command "armbian-config", select System >> CPU Frequency.
      I set min freq. to 480 MHz, max freq. to 1200 MHz and "On demand" mode, you can set higher max freq.
      ```
   </details> 
3. <details> 
      <summary>If you want: Install desktop environment</summary>

      ```
      If you've downloaded OS without desktop environment, you can install it using commands:
      "apt update"
      "apt install lubuntu-desktop -y"
      ```
   </details> 
4. <details> 
      <summary>Turn on microphone</summary>

      ```
      If your built-in OrangePi mic doesn't work, execute "alsamixer" command, press F4, select mic using arrows and press space to turn it on.
      If there are two mics, you can turn on both. Then press CTRL+S to save and CTRL+C to close the alsamixer.
      ```
   </details>
5. <details> 
      <summary>Check the microphone</summary>
  
      ```
      To check the microphone connect headphones to an OrangePi and use "arecord | aplay" command,
      sound from microphone will play in your headphones.
      ```
   </details>
6. <details> 
      <summary>Turn on autologin without password</summary>
      - Solution for Lubuntu: Create "/etc/sddm.conf" file with following content:
  
      ```
      [Autologin]      
      User=[YOUR USERNAME]      
      Session=Lubuntu.desktop      
      Relogin=true      
      ```
   </details>
   
### Downloading and configuring the program:
1. Download this library, unpack an archive
2. Start setup.sh
3. <details> 
      <summary>Download language model</summary>
      
      ```
      Model is too heavy for Github, 40 MB. So you need to download it buy yourself.
      You need to put directory with model into directory with program (for example with example.py)
      Link: https://alphacephei.com/vosk/models
      Name of the model i use: "vosk-model-small-ru-0.22" (you can choose English but it has to be small enough to be used on your device)
      ```
    </details>   
5. Write the code or edit example.py
6. <details> 
      <summary>Configure program auto-start</summary>
      - In Lubuntu you can do it in Session Settings, you need to add the following command in auto-start. If you have different path to a program, change it.
  
      ```
      cd /home/orangepi/Desktop/SmartGnomik && python3 example.py
      ```
   </details>
7. <details> 
      <summary>Configure LED blinking</summary>
  
      ```
      LED will blink 3 times after command execution
      It works only on Orange Pi because i don't have Raspberry Pi to write a code for it and to test it.
      If you have Raspberry Pi and you want your LED to blink you can edit the library to fit your needs.
      
      To control GPIO contacts (and to make LED blinking) program must have root access.
      The right way to do this:
      1. Make root user owner of entire directory (chown -R root [DIR NAME or PATH])
      2. Set access settings (chmod -R 755 [DIR NAME or PATH])
      3. Create a script which will start your program
         and put this script into "/usr/bin" dir (sg_autostart.sh - example of a script)
      4. Add your script to auto-start list (In Lubuntu you can do it in "Session settings").
         Command that needs to be executed on start - "sudo sg_autostart.sh"
      5. Use "visudo" command and add to the end of the file:
         "[YOUR USENAME] ALL=(ALL:ALL) NOPASSWD:/usr/bin/sg_autostart.sh"
      ```
   </details>
### Program example (with russian model/words but code is the same):
```
from smart_gnomik import SmartGnomik

model_name = "vosk-model-small-ru-0.22" # Name of the voice model. Directory with model should be in the same directory where this program is.
activation_words = ['гном'] # Word after saying which voice recognition activates. Like "Okay google"

sg = SmartGnomik(model_name, activation_words)

# sg.set_activation_words(activation_words)

# You can specify the path to the Tuya lib and other libs if they are not in the "{current dir}/libs" directory.
# sg.set_dir(r'/home/orangepi/Desktop/SmartGnomik/libs')

# If you call this function LED will blink after command execution
# Works only with Orange Pi. You need to change the library if you want to work it with Raspberry.
# Models: PC2, ZERO, ZEROPLUS2H5, ZEROPLUS2H3, PCPCPLUS, PRIME
# If your model is not on the list you can try to use built-in LED
# To do this call this function without specifying model and pin
sg.set_orangepi_LED(model="PC2", pin=7) 

# The library uses paramiko and wake-on-lan to control your PC
ip = "192.168.0.1"
device_names = ["комп"] # КОМПьютер
mac_addr = "AA:BB:CC:DD:EE:FF"
username = "Username"
password = "top_secret_password"
pc = sg.set_pc(ip, device_names, mac_addr, username, password, port=22)
pc.add_command(action_words=["вкл"], command = 'turn_on')
pc.add_command(action_words=["выкл"], command = 'turn_off')
pc.add_command(action_words=["резаг"], command = 'reboot') #пеРЕЗАГрузи

# The library uses C#lib TuyaNet by Alexey Clusterrr to control Tuya devices
ip = "192.168.0.2"
device_names = ["розет"] # РОЗЕТка
local_key = "Local_Key"
device_ID = "Device_ID"
tuya1 = sg.set_tuya_device(ip, device_names, local_key, device_ID)
tuya1.add_command(action_words=["вкл"], command = 'turn_on')
tuya1.add_command(action_words=["выкл"], command = 'turn_off')

esp1 = sg.set_web_device(ip="192.168.0.3", device_names=["ламп", "свет", "люст"]) #ЛЮСтра 1.128
esp1.add_command(action_words=["вкл"], web_request = 'turn_on')
esp1.add_command(action_words=["выкл"], web_request = 'turn_off')

esp2 = sg.set_ac(ip="192.168.0.4", device_names=["конд"]) # КОНДиционер
esp2.add_command(action_words=["вкл"], web_request = 'turn_on')
esp2.add_command(action_words=["выкл"], web_request = 'turn_off')

sg.start()
```

### Future plans:
1. <details> 
      <summary>Integrate this library into pip</summary>
  
      ```
      It hasn't been done from the start because there are dependencies that needed to be installed manually via apt.
      Pip can't do this automatically and i thought it would be easier for users to download this library
      from Github and execute setup.sh script that will install everything.
      ```
2. Make writing complicated scripts easier
3. Make the feature that will allow to control your devices via global internet and not just via voice.

### In addition:
- Before executing bash scripts (.sh) you need to make them executable using command:
"chmod +x [NAME OF THE SCIPT]"
- Support developer / Free investment lifehacks [Russian]: https://pomoex.ru
- Contact me: mikesprogramms@gmail.com
- I will try to also keep english version of the description updated
