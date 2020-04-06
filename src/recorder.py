import pyaudio
import wave


class Recorder : 
    def __init__(self, chunk=1024, format=pyaudio.paInt16, channels=2, rate=44100, p=pyaudio.PyAudio()):
        # self.main = tkinter.Tk()
        # self.collections = []
        # self.main.geometry('500x300')
        # self.main.title('Record')
        
        
        self.FORMAT = format
        self.CHANNELS = channels
        self.RATE = rate
        self.CHUNK = chunk
        self.p = p
        self.frames = []
        

        self.STARTED = False
        self.PAUSED = False

        # self.buttons = tkinter.Frame(self.main, padx=120, pady=20)

        # # Pack Frame
        # self.buttons.pack(fill=tk.BOTH)



        # # Start and Stop buttons
        # self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='START', command=lambda: self.start())
        # self.strt_rec.grid(row=0, column=0, padx=50, pady=5)

        # # text = 'PAUSE' if self.status == 1 else 'RESUME'
        # # command = lambda: self.pause() if self.status == 1 else lambda: self.resume()
        # self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, 
        #     text='PAUSE',
        #     command=lambda: self.pause()
        # )
        # self.strt_rec.grid(row=1, column=0, padx=50, pady=5)
        # self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, 
        #     text='RESUME',
        #     command=lambda: self.resume()
        # )
        # self.strt_rec.grid(row=1, column=1, padx=50, pady=5)
        # self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='STOP', command=lambda: self.stop())
        # self.stop_rec.grid(row=2, column=0, columnspan=1, padx=50, pady=5)
        # self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='WRITE', command=lambda: self.write('abc.wav'))
        # self.stop_rec.grid(row=2, column=1, columnspan=1, padx=50, pady=5)

        # self.main.mainloop()

    def start(self) : 
        print('START', (self.STARTED, self.PAUSED))
        if not self.STARTED:
            self.STARTED = True
            self.stream = self.p.open(
                format=self.FORMAT, 
                channels=self.CHANNELS, 
                rate=self.RATE, 
                input=True, 
                frames_per_buffer=self.CHUNK
            )


        elif self.PAUSED: 
            self.PAUSED = False
            self.stream.start_stream()
        
        # while self.STARTED and not self.PAUSED:
        #     data = self.stream.read(self.CHUNK)
        #     self.frames.append(data)
        #     self.main.update()

    def get_data(self):
        data = self.stream.read(self.CHUNK)
        self.frames.append(data)

    def pause(self) : 
        print('PAUSE', (self.STARTED, self.PAUSED))
        self.PAUSED = True 
        self.stream.stop_stream()
    
    def resume(self) : 
        self.start()
    
    def stop(self) : 
        print('STOP', (self.STARTED, self.PAUSED))
        self.STARTED = False
        self.PAUSED = False
        self.stream.close()
        

    def write(self, path) : 
        wf = wave.open(path, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        self.frames = []

