import smbus2

def read_eeprom(chip, port):
    # مثال مبسط: قراءة من 24C16 على I2C رقم 1 والعنوان 0x50
    bus = smbus2.SMBus(int(port))
    address = 0x50  # غيّر العنوان حسب نوع الشريحة
    data = []
    for i in range(256):  # حجم البيانات
        data.append(bus.read_byte_data(address, i))
    print(f"[DONE] قرأت {len(data)} بايت من EEPROM: {data}")
