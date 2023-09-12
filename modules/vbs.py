"""
## VBScript
"""

def create(fileName, content, looped, run, deleteafterrun):
    from afterburner import burn, make, makedir, start
    
    vbs_content = ""
    
    if looped:
        vbs_content += "do\n"
        vbs_content += f'MsgBox "{content}"\n'
        vbs_content += "loop\n"
    else:
        vbs_content = f'MsgBox "{content}"\n'
    
    with open(f"{fileName}.vbs", "w") as vbsFile:
        vbsFile.write(vbs_content)
    
    if run:
            try:
                start(fileName, "vbs", 0)
            except Exception as e:
                print(f"Error running {vbsFile}: {e}")

            if deleteafterrun:
                burn(f"{fileName}.vbs", 2)
    else:
        print(f"Failed to create {vbsFile}.")