from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_volume(self, volume: int):
        pass

class TV(Device):
    def __init__(self):
        self.is_on = False
        self.volume = 10

    def turn_on(self):
        print(f"TV is turned on!")

    def turn_off(self):
        print(f"TV is turned off!")

    def set_volume(self, volume):
        self.volume = volume
        print(f"TV volume set to {self.volume}!")

class Radio(Device):
    def __init__(self):
        self.is_on = False
        self.volume = 5

    def turn_on(self):
        print(f"Radio is turned on!")

    def turn_off(self):
        print(f"Radio is turned off!")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Radio volume set to {self.volume}!")

class Remote(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def power(self):
        pass

class BasicRemote(Remote):
    def __init__(self,device: Device):
        super().__init__(device)

    def power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

class AdvancedRemote(Remote):
    def __init__(self,device: Device):
        super().__init__(device)

    def power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)

if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    print("\n--- Using Basic Remote with TV ---")
    basic_remote = BasicRemote(tv)
    basic_remote.power()
    basic_remote.power()

    print("\n--- Using Advanced Remote with Radio ---")
    adv_remote = AdvancedRemote(radio)
    adv_remote.power()
    adv_remote.volume_up()
    adv_remote.volume_down()
    adv_remote.power()