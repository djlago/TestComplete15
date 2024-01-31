def Test():
  if SendMail("ClareJ@clarejeffersoncorp.com", "mail.johnsmithcorp.com", "John Smith", "JohnS@johnsmithcorp.com", "Notification", "Hello Clare, Your application is nice.", "C:\\File1.txt", "C:\\File2.txt"):
    Log.Message("Mail was sent")
  else:
    Log.Warning("Mail was not sent")