import os
if os.path.exists("/home/pi/Documents/Python_programs/Activity_08.py"):
    print("File exists")
    
    os.system("cp /home/pi/Documents/Python_programs/Activity_08.py /home/pi/Documents/Python_programs/Activity_09.py")
    if os.path.exists("/home/pi/Documents/Python_programs/Activity_09.py"):
        print("File Activity_09.py created from Activity_08.py")
        
else:
    print("File not found")
#with open("/home/piDocuments/Python_programs/Activity_08.py"):