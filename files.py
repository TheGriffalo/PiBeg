import os
if os.path.exists("/home/pi/text_file"):
    print("File exists")
    os.remove("/home/pi/text_file")


#with open("/home/pi/text_file", "w") as f:
    #print(f.read())
    #for line in f:
        #print(line)
    #f.write("new_text\n")
    
    