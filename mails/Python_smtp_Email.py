import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("trss1823@gmail.com","life goes on")

subject="Python Message"
body="This is tutorial of sending Email using Python Script in simple steps"

message="Subject:{}\n\n{}".format(subject,body)
#print(message)
listOfAddress=["monkeymindbusiness@gmail.com"]
ob.sendmail("swetha1823",listOfAddress,message)
print(" Your Email has been sent successfully....")
ob.quit()
