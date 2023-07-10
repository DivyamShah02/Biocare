import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt

class SendMail:
    def __init__(self):
        # SMTP server and port for GoDaddy
        self.smtp_server = 'smtpout.secureserver.net'
        self.smtp_port = 465
        # Sender's email credentials
        self.sender_email = 'support@bakershub.in'
        temp_tem = 'Navkar@108'
        self.sender_password = temp_tem
        
    def send_activation(self,email,link):
        self.recipient_email = email

        # Email subject and content
        self.subject = 'Activate Your Account Now!'
        self.username = "Biocare Support"
        self.body = f'''<h4>Welcome to Biocare! To get started, you need to activate your account by clicking the link below: <br><a href="{link}">Click Here</a> to activate your account.</h4><br><p>Use this link if 'Click Here' doesn't works: {link}</p>'''

        try:
            # Create the email message
            self.message = MIMEMultipart()
            self.message['From'] = f'{self.username} <{self.sender_email}>'
            self.message['To'] = self.recipient_email
            self.message['Subject'] = self.subject
            self.message.attach(MIMEText(self.body, 'html'))

            # Set up the SMTP connection and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                # Login to the email account
                server.login(self.sender_email, self.sender_password)

                # Send the email
                server.sendmail(self.sender_email, self.recipient_email, self.message.as_string())
            
            return True
                
        except:
            return False
       
    def send_distributor_activated(self,email,name):
        self.recipient_email = email

        # Email subject and content
        self.subject = 'Distributor Account Activated!'
        self.username = "Biocare Support"
        self.body = f'''<h4>
Dear {name},<br><br>

We are thrilled to inform you that your distributor account with Biocare has been successfully activated! Congratulations and welcome to our esteemed network of distributors.
<br><br>
With your newly activated account, you now have access to a wide range of tools, resources, and opportunities that will help you thrive in your role as a distributor. We are confident that you will excel and achieve great success within our network.
<br><br>
As a distributor, you play a vital role in our business, and we value the contributions you will make to our growth and success. We are committed to supporting you every step of the way, and our team is here to provide you with any assistance you may need.
<br><br>
We encourage you to explore the features available in your account and familiarize yourself with the various tools and materials at your disposal. Feel free to reach out to our dedicated distributor support team at support@biocare.us if you have any questions or require further guidance.
<br><br>
Once again, congratulations on becoming an activated distributor! We are excited to embark on this journey with you and look forward to witnessing your achievements.
<br><br>
Best regards,<br><br>

Karan Vekaria<br>
CEO & Founder<br>
Biocare</h4>'''

        try:
            # Create the email message
            self.message = MIMEMultipart()
            self.message['From'] = f'{self.username} <{self.sender_email}>'
            self.message['To'] = self.recipient_email
            self.message['Subject'] = self.subject
            self.message.attach(MIMEText(self.body, 'html'))

            # Set up the SMTP connection and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                # Login to the email account
                server.login(self.sender_email, self.sender_password)

                # Send the email
                server.sendmail(self.sender_email, self.recipient_email, self.message.as_string())
            
            return True
                
        except:
            return False
    
    def send_distributor_inprocess(self,email,name):
        self.recipient_email = email

        # Email subject and content
        self.subject = 'Distribution Account Registration Received: Account Activation Process'
        self.username = "Biocare Support"
        self.body = f'''<h4>
Dear {name},<br><br>
Thank you for registering for a distribution account with Biocare. We are excited to have you join our network of distributors and explore the opportunities that lie ahead.
<br><br>
We would like to inform you that your registration has been received successfully. Our team will now carefully review your profile and verify the provided information to ensure compliance with our distribution policies and guidelines.
<br><br>
The account activation process typically takes approximately 3 to 4 business days. During this time, we will assess your qualifications and suitability as a distributor. Rest assured that we are working diligently to complete this process as quickly as possible, while ensuring that all necessary checks are conducted thoroughly.
<br><br>
Once your account is successfully activated, we will send you a follow-up email containing the necessary information and instructions to access your distribution account. You will then be able to take advantage of the resources, benefits, and support that our distribution program offers.
<br><br>
We appreciate your patience and understanding as we process your application. We believe that your association with Biocare as a distributor will be mutually beneficial, and we look forward to welcoming you officially to our network.
<br><br>
Best regards,<br><br>

Karan Vekaria<br>
CEO & Founder<br>
Biocare</h4>'''

        try:
            # Create the email message
            self.message = MIMEMultipart()
            self.message['From'] = f'{self.username} <{self.sender_email}>'
            self.message['To'] = self.recipient_email
            self.message['Subject'] = self.subject
            self.message.attach(MIMEText(self.body, 'html'))

            # Set up the SMTP connection and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                # Login to the email account
                server.login(self.sender_email, self.sender_password)

                # Send the email
                server.sendmail(self.sender_email, self.recipient_email, self.message.as_string())
            
            return True
                
        except:
            return False
        
        