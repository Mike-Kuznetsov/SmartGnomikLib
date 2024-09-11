from smart_gnomik import SmartGnomik
model_name = "vosk-model-small-ru-0.22"
activation_words = ['гном']

sg = SmartGnomik(model_name, activation_words)
#sg.set_activation_words(activation_words)
#sg.set_model_dir(dir="/home/mautoz/Desktop/SmartGnomik”)
sg.set_orangepi_LED(pin=7)

ip = "192.168.0.1"
device_names = ["Комп"] # КОМПьютер
mac_addr = "AA:BB:CC:DD:EE:FF"
username = "Username"
password = "top_secret_password"
pc1 = sg.set_pc(ip, device_names, mac_addr, username, password, port=22)
pc1.add_command(action_words=["вкл"], command = “turn_on”) #ВКЛючи
pc1.add_command(action_words=["выкл"], command = “turn_off”) #ВЫКЛючи
pc1.add_command(action_words=["резаг"], command = “reboot”) #пеРЕЗАГрузи

ip = "192.168.0.2"
device_names = ["розет"] # РОЗЕТка
device_ID = "Device_ID"
local_key = "Local_Key"
tuya1 = sg.set_tuya_device(ip, device_names, local_key, device_ID)
tuya1.add_command(action_words=["вкл"], command = “turn_on”)
tuya1.add_command(action_words=["выкл"], command = “turn_off”)

esp1 = sg.set_web_device(ip="192.168.0.3", device_names=["ламп", "свет", "люст"]) #ЛЮСтра
esp1.add_command(action_words=["вкл"], web_request = “turn_on”)
esp1.add_command(action_words=["выкл"], web_request = “turn_off”)

esp2 = sg.setAC(ip="192.168.0.4", device_names=["конд"]) # КОНДиционер
esp2.add_command(action_words=["вкл"], web_request = “turn_on”)
esp2.add_command(action_words=["выкл"], web_request = “turn_off”)

sg.start()
