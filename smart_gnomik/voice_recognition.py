
class VoiceRecognition():
    
    def __init__(self, gnomik, model_name):
        self.q = queue.Queue()
        self.device = None
        self.device_info = sd.query_devices(self.device, 'input')
        self.samplerate = int(self.device_info['default_samplerate'])
        self.vmodel = vosk.Model(model_name)
        self.audio_processing()
        self.gnomik = gnomik

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def audio_processing(self):
        with sd.RawInputStream(samplerate=self.samplerate, blocksize = 8000, device=self.device, dtype='int16',
                                        channels=1, callback=self.callback):
            rec = vosk.KaldiRecognizer(self.vmodel, self.samplerate)
            self.gnomik.command_executed = False
            print("listening")
            while True:
                try:
                    data = self.q.get()
                    if rec.AcceptWaveform(data):
                        gnomik.recognize_command(rec.Result()[14:-3])
                        gnomik.command_executed = False
                    else:
                        gnomik.recognize_command(rec.PartialResult()[17:-3])
                except Exception as e:
                    print(e)
