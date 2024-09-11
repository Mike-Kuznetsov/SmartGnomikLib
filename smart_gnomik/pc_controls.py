from wakeonlan import send_magic_packet
import paramiko

class PC():
    def __init__(self, gnomik, ip, device_names, mac_addr, username, password, port=22):
        #self.voice_recognizer = voice_recognizer
        #self.blink_LED = blink_LED
        self.gnomik = gnomik
        self.ip_address = ip
        self.mac = mac_addr
        self.username = username
        self.password = password
        self.port = port
        if type(device_names) == str:
            device_names = [device_names]
        self.device_names = device_names
        
    def turn_on(self):
        send_magic_packet(self.mac)
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()
        
    def turn_off(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=PC_ip_address, username=PC_username, password=PC_password, port=PC_port)
        stdin, stdout, stderr = client.exec_command('shutdown -s -t 00 -f')
        client.close()
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()
        
    def reboot(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=PC_ip_address, username=PC_username, password=PC_password, port=PC_port)
        stdin, stdout, stderr = client.exec_command('shutdown -r -t 00 -f')
        client.close()
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()

    def send_command(self, request):
        if request == "turn_on" or request == "on":
            self.turn_on()
        elif request == "turn_off" or request == "off":
            self.turn_off()
        elif request == "reboot" or request == restart:
            self.reboot()
        else:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=PC_ip_address, username=PC_username, password=PC_password, port=PC_port)
            stdin, stdout, stderr = client.exec_command(request)
            client.close()
            self.gnomik.command_executed = True
            self.gnomik.blink_LED()
