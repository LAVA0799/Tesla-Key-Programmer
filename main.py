import argparse
from eeprom_tools import read_eeprom, write_eeprom
from canbus_tools import can_program_key
from key_utils import extract_keys

def main():
    parser = argparse.ArgumentParser(description="Tesla Key Programmer - قراءة وبرمجة مفاتيح تسلا")
    parser.add_argument('--eeprom-read', action='store_true', help='قراءة بيانات EEPROM')
    parser.add_argument('--eeprom-write', action='store_true', help='كتابة بيانات EEPROM')
    parser.add_argument('--chip', type=str, help='نوع شريحة EEPROM (مثال: 24C16)')
    parser.add_argument('--port', type=str, help='منفذ البرمجة (مثال: COM3 أو /dev/ttyUSB0)')
    parser.add_argument('--can-program-key', action='store_true', help='برمجة بطاقة أو مفتاح عبر CAN-BUS')
    parser.add_argument('--vin', type=str, help='رقم هيكل السيارة (VIN)')
    parser.add_argument('--key-data', type=str, help='مسار ملف بيانات المفتاح الجديد')
    parser.add_argument('--extract-keys', type=str, help='تحليل دامب لاستخراج بيانات المفاتيح')
    args = parser.parse_args()

    if args.eeprom_read:
        read_eeprom(args.chip, args.port)
    elif args.eeprom_write:
        write_eeprom(args.chip, args.port)
    elif args.can_program_key:
        can_program_key(args.vin, args.key_data)
    elif args.extract_keys:
        extract_keys(args.extract_keys)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
