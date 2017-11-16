import requests
import mechanize
import os

os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         
""")
print ("You Don't Have Server")
print ("Buy One http://deep3.club/buy.php")
site= raw_input("Server-> ")
print " ", site



#CHecking Website if online
os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         
""")

print("Checking ..")
request = requests.get(site)
if request.status_code == 200:
    print("Server probally is working")
else:
    print('Your Server is not working ')
    quit()

#ending mail from shell
print(' ')
br = mechanize.Browser()
br.open(site)
br.select_form(nr=0)
br.form['senderEmail'] = senderemail = raw_input("Sender Email-> ")
print "SenderEmail: ", senderemail
br.form['senderName'] = sendername = raw_input("Sender Name-> ")
os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         

""")
print "senderEmail: ", senderemail
print "SenderName: ", sendername
br.form['subject'] = subject = raw_input("Subject-> ")
os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         

""")
print "senderEmail: ", senderemail
print "SenderName: ", sendername
print "Subject: ", subject
br.form['messageLetter'] = message = raw_input("Message-> ")
os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         

""")
print "senderEmail: ", senderemail
print "SenderName: ", sendername
print "Subject: ", subject
print "Message: ", message
br.form['emailList'] = email = raw_input('Email->')
os.system('clear')
print ("""
______                 _____  ___  ___  ___  _ _           
|  _  \               |____ | |  \/  | / _ \(_) |          
| | | |___  ___ _ __      / / | .  . |/ /_\ \_| | ___ _ __ 
| | | / _ \/ _ \ '_ \     \ \ | |\/| ||  _  | | |/ _ \ '__|
| |/ /  __/  __/ |_) |.___/ / | |  | || | | | | |  __/ |   
|___/ \___|\___| .__/ \____/  \_|  |_/\_| |_/_|_|\___|_|   
               | |            By IcoDz & Manisso                              
               |_|                                         

""")
print "senderEmail: ", senderemail
print "SenderName: ", sendername
print "Subject: ", subject
print "Message: ", message
print "Email:", email
req = br.submit()
print("DONE")

