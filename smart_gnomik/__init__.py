import sys
#import clr
#clr.AddReference("/home/mautoz/CSharp/TuyaNet.dll") # ИЗМЕНИТЕ НА ВАШУ ПАПКУ С ПРОГРАММОЙ
#clr.AddReference("/home/mautoz/CSharp/Newtonsoft.Json.dll") # ИЗМЕНИТЕ НА ВАШУ ПАПКУ С ПРОГРАММОЙ
import queue
import sounddevice as sd
import vosk
import os
#import os
#from com.clusterrr.TuyaNet import TuyaDevice, TuyaCommand
#from System import Threading, Collections
import requests
#from wakeonlan import send_magic_packet
#import paramiko
#import OPi.GPIO as gpio
#from time import sleep

from .pc_controls import *
from .tuya_devices import *
from .web_devices import *
from .voice_recognition import *

class SmartGnomik():
    #def test(self, q):
    #    return q+1
    
    def __init__(self, model_name="vosk-model-small-ru-0.22", words=["гном"]):
        if type(words) == str:
            words = [words]
        self.activation_words = words
        self.devices = []
        self.model_name = model_name
        self.tuya_libs_imported = False
        self.pc_libs_imported = False
        self.led_libs_imported = False
        self.lib_dir = os.getcwd()
    def set_model_dir(self, lib_dir): # sets dir of a library
        if lib_dir[-1] == '/' or lib_dir[-1] == "\\":
            lib_dir = lib_dir[:-1]
        self.lib_dir = lib_dir

    def set_activation_words(self, words): # changes activation word/words
        if type(words) == str:
            words = [words]
        self.activation_words = words

    def add_command(device, action_words, command): # adds a voice command to the list of voice commands for specific device
        if type(action_words) == str:
            action_words = [action_words]
        device_found = False
        for i in range(len(self.devices)):
            if self.devices[i][0] == device:
                self.devices[i][1].append([command, action_words])
                device_found = True
                break
        if device_found == False:
            self.devices.append([device, [[command, action_words]]])
        
    def set_pc(self, ip, device_names, mac_addr, username, password, port=22): # sets PC credentials
        if not self.pc_libs_imported:
            #TRY EXCEPT HERE
            #"LIBRARY IMPORT FAILED: wakeonlan or paramiko"
            from wakeonlan import send_magic_packet
            import paramiko
            self.pc_libs_imported = True
        self.pc = PC(self, ip, device_names, mac_addr, username, password, port)
        return pc
        
    def set_tuya_device(self, ip, device_names, local_key, device_ID): # sets tuya device credentials
        if not self.tuya_libs_imported:
            if self.lib_dir:
                #TRY EXCEPT HERE
                #"LIBRARY IMPORT FAILED: clr or com.clusterrr.TuyaNet"
                import clr
                clr.AddReference(f"{self.lib_dir}/TuyaNet.dll") 
                clr.AddReference("{self.lib_dir}/Newtonsoft.Json.dll")
                from com.clusterrr.TuyaNet import TuyaDevice, TuyaCommand
                from System import Threading, Collections
                self.tuya_libs_imported = True
            else:
                print("When using Tuya Devices you should call set_dir(path_to_lib) before set_tuya_device()")
                return "When using Tuya Devices you should call set_dir(path_to_lib) before set_tuya_device()"
        self.new_tuya_device = TuyaDevice(self, ip, device_names, local_key, device_ID)
        devices.append(new_tuya_device)
        return self.new_tuya_device
    
    def set_web_device(self, ip, device_names): # sets web device's ip address (esp for example)
        new_web_device = WebDevice(self, ip, device_names)
        return web_device

    def set_esp(self, ip, device_names): # sets esp's ip address
        return set_web_device(ip, device_names)

    def set_ac(self, ip, device_names): # sets ac's ip address
        return set_web_device(ip, device_names)

    def set_heater(self, ip, device_names): #sets heater's ip address
        return set_web_device(ip, device_names)
        
    def set_orangepi_LED(self, pin=-1):
        if not self.led_libs_imported:
            import OPi.GPIO as gpio
            from time import sleep
            self.led_libs_imported = True
        self.blink = True
        self.LED_pin = pin

    def blink_LED(self):
        if self.blink == True:
            if self.LED_pin == -1:
                for i in range(3):
                    os.system("echo '1' > /sys/class/leds/orangepi:red:status/brightness")
                    sleep(0.1)
                    os.system("echo '0' > /sys/class/leds/orangepi:red:status/brightness")
                    sleep(0.2)
            else:
                gpio.setboard(gpio.PC2)
                gpio.setmode(gpio.BOARD)
                gpio.setup(self.LED_pin, gpio.OUT)
                for i in range(3):
                    gpio.output(self.LED_pin, 1)
                    sleep(0.1)
                    gpio.output(self.LED_pin, 0)
                    sleep(0.2)

    def recognize_command(self, recognized_text):
        name_found = False
        if not self.command_executed:
            for word in self.activation_words:
                if word in recognized_text:
                    name_found = True
        if name_found:
            for device in self.devices: # for device in devices
                for name in device[0].device_names: # for every name of the device
                    if name in recognized_text: # if name appears in the text
                        for command in device[1]: # for every command 
                            for word in command[1]: # for every word that corresponds to the command
                                if word in recognized_text: # if one of device names and one of words corresponding to a command are in recognized text:
                                    device[0].send_command(command[0])
                                        
                                if self.command_executed:
                                    break
                            if self.command_executed:
                                break
                    if self.command_executed:
                        break
                if self.command_executed:
                    break
                
    def start(self):
        VoiceRecognition(self, model_name)




































