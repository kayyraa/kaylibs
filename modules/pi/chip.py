def create(name, version, ram, bit, hz, should_print, physical_copy):
    from os import remove
    
    chip_name    = str(name)
    chip_hert    = int(hz)
    chip_ram     = int(ram)
    chip_bit     = int(bit)
    chip_version = int(version)
    
    title(chip_name)
    
    if should_print:
        print(chip_name)
        print(chip_hert)
        print(chip_ram)
        print(chip_bit)
        print(chip_version)
        
    if physical_copy:
        try:
            remove(f"{chip_name}.txt")
        except:
            print("An error accurred")
        
        with open(f"{chip_name}.txt", "a+") as chip:
            chip.write(f"chip_name: {chip_name}")
            chip.write("\n")
            chip.write(f"chip_hz: {chip_hert}")
            chip.write("\n")
            chip.write(f"chip_ram: {chip_ram}")
            chip.write("\n")
            chip.write(f"chip_bit: {chip_bit}")
            chip.write("\n")
            chip.write(f"chip_vers: {chip_version}")
        
    main_loop()
        
def main_loop():
    from time import sleep
    sleep(99*99)
    
def title(title):
    from os import system
    system("title " + str(title))