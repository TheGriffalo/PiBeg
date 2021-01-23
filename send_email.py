import yagmail

password = ""

with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()
    
yag = yagmail.SMTP("griffalolabs@gmail.com", password)

yag.send(to = "paul@griffin.me.uk",
         subject = "second email",
         contents = "Hello from Fray Bentos",
         attachments = "/home/pi/file_to_join.txt")

print("Email sent")
