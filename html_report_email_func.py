import smtplib
from email.message import EmailMessage

# Configuration
sender = 'pandiarajs2000@gmail.com'
receiver = 'pandiarajs2000@gmail.com'
password = 'spandi2000'

# Create the email
msg = EmailMessage()
msg['Subject'] = 'Allure Test Report'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('Hi,\n\nPlease find the attached Allure test report.\n\nRegards.')

# Attach the report zip
with open('allure-results.zip', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='zip', filename=file_name)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent successfully.")
