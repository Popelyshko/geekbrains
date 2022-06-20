import os

def round_to_10(i):
    last_digit = i%10 
    if last_digit >= 5:
        return i + (10-last_digit)
    return i-last_digit

def process_dir(scan_name: str, base: dict):
     for entity_dir in os.scandir(scan_name):
        if entity_dir.is_file():
            key: str = str(round_to_10(os.path.getsize(entity_dir.path)))
            if base.get(key) is not None:
                base[key] = int(base[key]) + 1
            else:
                base[key] = 1
        if entity_dir.is_dir():
            process_dir(entity_dir.path, base)

base: dict = {}

process_dir(".", base)
print (base)