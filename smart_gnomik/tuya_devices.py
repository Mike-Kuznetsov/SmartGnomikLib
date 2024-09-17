import clr

class TuyaDevice():        
    def __init__(self, gnomik, ip, device_names, local_key, device_ID):
        clr.AddReference(f"{gnomik.lib_dir}/TuyaNet.dll") 
        clr.AddReference(f"{gnomik.lib_dir}/Newtonsoft.Json.dll")
        global TD
        global TuyaCommand
        global Threading
        global Collections
        from com.clusterrr.TuyaNet import TuyaDevice as TD
        from com.clusterrr.TuyaNet import TuyaCommand
        from System import Threading, Collections
        self.source = Threading.CancellationTokenSource()
        self.gnomik = gnomik
        self.ip = ip
        self.local_key = local_key
        self.device_ID = device_ID
        if type(device_names) == str:
            device_names = [device_names]
        self.device_names = device_names
        
    def turn_on(self):
        self.device = TD(ip = self.ip, localKey = self.local_key, deviceId = self.device_ID)
        self.device.SendAsync(self.device.EncodeRequest(TuyaCommand.CONTROL, self.device.FillJson("{\"dps\":{\"1\":true}}")), cancellationToken = self.source.Token)
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()
        
    def turn_off(self):
        self.device = TD(ip = self.ip, localKey = self.local_key, deviceId = self.device_ID)
        self.device.SendAsync(self.device.EncodeRequest(TuyaCommand.CONTROL, self.device.FillJson("{\"dps\":{\"1\":false}}")), cancellationToken = self.source.Token)
        self.gnomik.command_executed = True
        self.gnomik.blink_LED()

    def add_command(self, action_words, command):
        self.gnomik.add_command(self, action_words, command)
        
    def send_command(self, request):
        if request == "turn_on" or request == "on":
            self.turn_on()
        elif request == "turn_off" or request == "off":
            self.turn_off()
        else:
            self.device = TD(ip = self.ip, localKey = self.local_key, deviceId = self.device_ID)
            self.device.SendAsync(self.device.EncodeRequest(TuyaCommand.CONTROL, self.device.FillJson(request)), cancellationToken = self.source.Token)
            self.gnomik.command_executed = True
            self.gnomik.blink_LED()
