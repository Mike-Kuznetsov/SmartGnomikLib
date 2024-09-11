class WebDevice():
    
    def __init__(self, gnomik, ip, device_names):
        self.gnomik = gnomik
        self.ip = ip
        if type(device_names) == str:
            device_names = [device_names]
        self.device_names = device_names
        
    """def turn_on_device(self):
        r = requests.get(f'http://{self.ip}/turn_on')
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()
        
    def turn_off_device(self):
        r = requests.get(f'http://{self.ip}/turn_on')
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()"""

    def send_command(self, request):
        r = requests.get(f'http://{self.ip}/{request}')
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()

    """def change_temperature(self, value):
        url = f'http://{self.ip}/changeTemp'
        params = {'temp': value}
        r = requests.get(url, params=params)
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()"""

    def add_command(self, action_words, command):
        self.gnomik.add_command(self, action_words, command)
        
