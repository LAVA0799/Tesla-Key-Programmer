# Tesla Key Programmer

برنامج مفتوح المصدر لقراءة وبرمجة مفاتيح وبطاقات سيارات تسلا (Model 3) عبر وحدات EEPROM وواجهة CAN-BUS.  
يدعم العمل مع مبرمجات مثل CH341A، Raspberry Pi Pico W، وأدوات CAN-BUS مفتوحة المصدر أو تجارية.

---

## المميزات

- قراءة وكتابة شرائح EEPROM (أنواع 24Cxx/25xx) عبر I2C/SPI.
- دعم واجهات CAN-BUS لبرمجة المفاتيح أو البطاقات الجديدة.
- تحليل الدامب (dump) الصادر من وحدة BCM أو Gateway.
- أدوات مساعدة لقراءة البيانات من وحدات MCU (للمتقدمين).
- واجهة سطر أوامر سهلة الاستخدام، مع إمكانية التطوير لواجهة رسومية لاحقًا.

---

## المتطلبات

- Python 3.8 أو أحدث.
- مكتبات: `python-can`, `pyserial`, `smbus2`, أو ما يلزم حسب المبرمجة.
- مبرمجة CH341A أو Raspberry Pi Pico W أو وحدة CAN-USB.
- أجهزة تسلا Model 3 (تجريبية).

---

## بدء الاستخدام

1. **انسخ المستودع:**
   ```bash
   git clone https://github.com/<LAVA0799>/tesla-key-programmer.git
   cd tesla-key-programmer
   ```

2. **ثبت المتطلبات:**
   ```bash
   pip install -r requirements.txt
   ```

3. **شغل البرنامج:**
   ```bash
   python main.py
   ```

---

## الهيكل العام للمشروع

```plaintext
/tesla-key-programmer
  |-- README.md
  |-- main.py
  |-- eeprom_tools.py
  |-- canbus_tools.py
  |-- key_utils.py
  |-- requirements.txt
```

---

## الاستخدام السريع

- لقراءة EEPROM:
  ```bash
  python main.py --eeprom-read --chip 24C16 --port COM3
  ```

- لبرمجة بطاقة جديدة عبر CAN-BUS:
  ```bash
  python main.py --can-program-key --vin <VIN> --key-data <file.bin>
  ```

---

## تحذيرات

- جميع العمليات تتم على مسؤوليتك الشخصية.
- تأكد من عمل نسخة احتياطية لأي بيانات قبل أي تعديل.
- قد تحتاج لصلاحيات متقدمة أو أدوات خارجية للوصول إلى بعض بيانات وحدات تسلا.
- المشروع للأغراض التعليمية فقط.

---

## المساهمة

نرحب بمساهماتكم!  
افتح Issue أو Pull Request لأي تطوير أو إضافة.

---

## الترخيص

MIT License
