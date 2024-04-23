import random
import time

class TV():
    def __init__(self, color, size) -> None:
        self.color = color
        self.size = size
        self.channels = {}
        self.channel = None
        self.volume = 0
        self.running = True
        self.setup()
        
    def __repr__(self) -> str:
        return str(f"TV {self.color} - {self.size} (Polegadas) - {self.channel} (Canal Atual) - {self.volume} (Volume Atual)")
        
    def setup(self):
        self.sintonize()
        
    def change_channel(self, target):
        self.channel = self.channels[target]
        
    def change_volume(self, amount):
        self.volume += amount
        if self.volume + amount <= 0:
            self.volume = 0
        if self.volume + amount >= 100:
            self.volume = 100
        
    def turn_off(self):
        self.running = False
        
    def sintonize(self):
        num_channels = 32
        self.channels = {f"Canal {i+1}": random.randint(1, 1000) for i in range(num_channels)}
        
    def run(self):
        while True:
            if self.running == False:
                print("Desligando")
                break
            print("TV Rodando")
            print(self)
            print("Sleeping for 10s")
            time.sleep(10)
        
tv = TV("black", 32)
tv.run()