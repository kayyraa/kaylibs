# Roblox Lua
class Lua:
    def wait(seconds):
        from time import sleep
        sleep(seconds)
    
    def timeout(milliseconds):
        from time import sleep
        sleep(milliseconds / 1000)
        
    def loadstring(url, run):
        if run:
            import urllib3
            http = urllib3.PoolManager()
            response = http.request('GET', url)
            loadedstring = response.data.decode('utf-8')
            exec(loadedstring)
            
    def title(title):
        from os import system
        system("title " + str(title))
     
# JavaScript   
class JavaScript:
    class event:
        def create(type, name, code):
            event_type = str(type)
            event_name = str(name)
            event_code = str(code)
        
        def createrun(type, name, ran, stroke, delay, code, run):
            from time import sleep
            event_type = str(type)
            event_name = str(name)
            event_ranned_for = 0
            event_ran_for = ran
            event_stroke = stroke
            event_delay = delay
            event_code = str(code)
            
            if event_delay != 0:
                sleep(event_delay)
            
            if run:
                if event_ran_for == 0:
                    if event_type == "code":
                            exec(event_code)
                            
                if event_ran_for != 0:
                    while True:
                        sleep(event_stroke)
                        event_ranned_for = event_ranned_for + 1
                        if event_type == "code":
                            exec(event_code)
                        
                        if event_ranned_for == event_ran_for:
                            break
                
    class document:
        def title(title):
            from os import system
            system("title " + str(title))
    
    def setTimeOut(milliseconds):
        from time import sleep
        sleep(milliseconds / 1000)

# Roblox Luau           
class Luau:
    class file:
        def Get(path, lines):
            if bool(lines) == True:
                open(path, "r").readlines()
            open(path, "r")
            
        def Set(path, lines):
            if bool(lines) == True:
                open(path, "w").writelines()
            open(path, "w")
            
    class run:
        def loadstring(url, run):
            if run:
                import urllib3
                http = urllib3.PoolManager()
                response = http.request('GET', url)
                loadedstring = response.data.decode('utf-8')
                if run == True:
                    exec(loadedstring)
                if run == False:
                    return
                
        def loadfile(path, run):
            if run:
                file = open(path, "r")
                exec(str(file))
                
    def wait(seconds):
        from time import sleep
        sleep(seconds)

# Tkinter Plus   
class TkinterPlus:
    class window:
        def create(self, title, geo):
            import tkinter as tk
            window = tk.Tk()
            window.title(str(title))
            window.geometry(geo)
            window.mainloop()

# urllib4 Module           
class urllib4:
    def open(url, open):
        if open:
            import webbrowser
            webbrowser.open(url)
            
    def load(url):
        import requests
        response = requests.get(str(url))
        if response.status_code == 200:
            raw_code = response.text
            exec(raw_code)
        else:
            print(f"Failed to retrieve content from {url}")
            exit(1)
  
# Batch File Class          
class Batch:
    class User:
        def GetUserName():
            from os import getlogin
            import getpass
            user_name = getlogin() 
            return str(user_name)
        
        def GetPCName():
            from socket import gethostname
            host_name = gethostname()
            return str(host_name)
    
    def echo(text, run):
        if run:
            print(str(text))
        
    def title(title):
        from os import system
        system("title " + str(title))
        
    def timeout(mode, seconds, tmode):
        from time import sleep
        if mode == "/t" and tmode == "/nobreak":
            valid = True
            if bool(valid) == True:
                sleep(seconds)
                
    def start(path):
        open(path)
        
    def taskkill(program_name):
        from os import system
        system(f'taskkill /F /IM {program_name}')
        
    def create(extension, name, write, content, run):
        if run:
            file_name = str(name) + str(extension)
            file_write = bool(write)
            file_content = str(content)
    
            if file_write:
                with open(file_name, "a") as file:
                    file.write(file_content)
                
    def rename(path, name):
        from os import rename
        rename(path, str(name))
        
    def remove(path):
        from os import remove
        remove(path)
        
# Python+
class PythonPlus:
    class FileManagement:
        def Delete(path):  
            from os import remove
            remove(path)
            
        def Rename(path, name):
            from os import rename
            rename(path, str(name))
    
    def wait(seconds):
        from time import sleep
        sleep(seconds)
        
    def title(title):
        from os import system
        system("title " + str(title))
        
    def clear():
        from os import system
        system('cls')
        
    def create(extension, name, write, content, run):
        if run:
            file_name = str(name) + str(extension)
            file_write = bool(write)
            file_content = str(content)
    
            if file_write:
                with open(file_name, "a") as file:
                    file.write(file_content)
        
    def start(path):
        open(path)
        
    def title(title):
        from os import system
        system("title " + str(title))