from nio.block.base import Block
from nio.properties import VersionProperty
from nio.signal.base import Signal
import smbus

class IRThermometer(Block):

    version = VersionProperty('0.1.0')

    def __init__(self):
        super().__init__()
        self.bus = smbus.SMBus(1)
        self.address = 0x5a

    def process_signals(self, signals):
        for signal in signals:
            word = bus.read_word_data(self.address, 0x07)
        kelvin = word * 0.02
        celcius = kelvin - 273
        fahrenheit = (9 / 5 * celcius) + 32
        signal = Signal({
            "raw": str(word),
            "kelvin": str(kelvin),
            "celcius": str(celcius),
            "fahrenheit": str(fahrenheit)
        })
        self.notify_signals([signal])
