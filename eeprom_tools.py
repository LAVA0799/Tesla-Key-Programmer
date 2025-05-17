import time

def read_eeprom(chip, port):
    print(f"[INFO] قراءة بيانات EEPROM من الشريحة {chip} عبر المنفذ {port} ...")
    # مثال تجريبي - هنا تضع كود القراءة الفعلي حسب نوع المبرمجة
    time.sleep(1)
    print("[DONE] تمّت القراءة بنجاح (بيانات وهمية)!")

def write_eeprom(chip, port):
    print(f"[INFO] كتابة بيانات EEPROM على الشريحة {chip} عبر المنفذ {port} ...")
    # مثال تجريبي - هنا تضع كود الكتابة الفعلي حسب نوع المبرمجة
    time.sleep(1)
    print("[DONE] تمّت الكتابة بنجاح!")