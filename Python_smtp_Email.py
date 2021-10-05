import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("YourEmail@gmail.com","******")

subject="python message"
body="this is tutorial of sending email using python script in simple steps"

message="Subject:{}\n\n{}".format(subject,body)
#print(message)
listOfAddress=["monkeymindbusiness@gmail.com"]
ob.sendmail("swetha1823",listOfAddress,message)
print("send successfully....")
ob.quit()
