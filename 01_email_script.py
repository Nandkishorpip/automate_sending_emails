import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("nandkishorpipraj@gmail.com","")
subject = "sending email using python"
body = "sending email using python script in simple steps"
message = "Subject:{}\n\n{}".format(subject,body)
listOfAddress=["piprajsagar@gmail.com"]
ob.sendmail("nandkishorpipraj@gmail.com",listOfAddress,message)
print("send email successfully")
ob.quit()
