# This is an example of a program of a Smart Home Controller 
# Это пример программы контроллера умного дома

# Smart Gnomik Library: https://github.com/Mike-Kuznetsov/SmartGnomikLib
# Видео про библиотеку и устройства тут: https://youtube.com/@espdev
# Основной канал: https://youtube.com/c/MautozTech

# Licensed under GNU GPL V3: This program is a free software, you are free to use or modify the code. No warranty.

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
