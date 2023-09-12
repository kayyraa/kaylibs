def create(title, geo, label, anchor, text, color, font, size, icon, path, cTitle, error, ppath, label2, text2, color2, font2, size2, anchor2):
    while True:
        import tkinter as tk
        from time import sleep
        from os import system
        sleep(0.05)
        window = tk.Tk()
        window.title(str(title))
        window.geometry(geo)
        window.resizable(False, False)
        
        system("title " + cTitle)
        
        if label:
            label = tk.Label(window, text=str(text), font=(font, size, "bold"), fg=color)
            label.pack(anchor=anchor)
            
        if label2:
            labe = tk.Label(window, text=str(text2), font=(font2, size2), fg=color2, wraplength=524)
            labe.pack(anchor=anchor2)
            
        if icon:
            window.iconbitmap(path)
            
        if error:
            pt = tk.PhotoImage(file=ppath)
            lbl = tk.Label(window, image=pt).place(anchor=anchor, y=30, x=435)
            
        def on_closing():
            window.destroy()
            exit()
        
        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.mainloop()
    
def exampleWindow():
    import tkinter as tk
    window = tk.Tk()
    window.title("Visual Code Window")
    window.geometry("512x512")
    window.resizable(False, False)
    
    def on_closing():
        window.destroy()
        exit()
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
    
def showError(title, geo, icon, path, resize, label, text, anchor, font, size, photo, ppath, px, py):
    import tkinter as tk
    window = tk.Tk()
    window.title(title)
    window.geometry(geo)
    if icon:
        window.iconbitmap(path)
    if resize:
        window.resizable(False, False)
    if label:
        lbl = tk.Label(window, text=str(text), font=(str(font), int(size)))
        lbl.pack()
    if photo:
        pht = tk.Label(window, image=ppath, anchor=anchor).place(x=int(px), y=int(py), anchor=anchor)
        
    window.mainloop()
            
def loop():
    from time import sleep
    sleep(99*99)