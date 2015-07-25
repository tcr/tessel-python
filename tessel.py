class LED():
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def write(self, value):
        f = open(self.path, 'wb')
        f.write('1' if value else '0')
        f.close()

led = [
    LED('red', '/sys/devices/leds/leds/tessel:red:error/brightness'),
    LED('amber', '/sys/devices/leds/leds/tessel:amber:wlan/brightness'),
    LED('green', '/sys/devices/leds/leds/tessel:green:user1/brightness'),
    LED('blue', '/sys/devices/leds/leds/tessel:blue:user2/brightness')
]
