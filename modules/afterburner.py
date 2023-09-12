def burn(path, time):
    from os import remove
    from time import sleep
    sleep(time)
    remove(path=path)
    
def make(path, time):
    from time import sleep
    sleep(time)
    open(path, "a")
    
def makedir(name, time):
    from time import sleep
    from os import makedirs
    sleep(time)
    makedirs(name=name)
    
def start(fileName, fileExtension, time):
    from time import sleep
    from os import system
    sleep(time)
    system(f'start "" {fileName}.{fileExtension}')