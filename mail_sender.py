import smtplib
import ssl
import getpass
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Configuration
SENDER_EMAIL = "ShahandPatelgroup@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL

def create_email_content(receiver_email):
    """
    Creates the MIME object with HTML banner and embedded image.
    """
    msg = MIMEMultipart("related")
    msg["Subject"] = "Welcome to Ask_SPG! 🚀 Your Smart Solution Partner"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    # HTML content with inline CSS
    html = """
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; margin: 0;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          
          <!-- Banner / Header -->
          <div style="background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 30px; text-align: center; color: white;">
             <!-- Logo Image (Content-ID method) -->
             <img src="cid:ask_spg_logo" alt="Ask_SPG Logo" style="width: 100px; height: auto; border-radius: 50%; border: 3px solid white; margin-bottom: 15px;">
             <h1 style="margin: 0; font-size: 24px;">Welcome to Ask_SPG! 👋</h1>
             <p style="margin: 5px 0 0; opacity: 0.9;">You Ask, We Deliver Smart Solutions.</p>
          </div>

          <!-- Body Content -->
          <div style="padding: 30px; color: #333333; line-height: 1.6;">
            <h2 style="color: #0d47a1; margin-top: 0;">💡 Share your requirement with us.</h2>
            <p style="font-size: 16px;">We’ll provide the best solution <strong>quickly & reliably</strong>.</p>
            
            <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 20px 0;">
            
            <h3 style="margin-bottom: 15px;">📌 Our Services Include:</h3>
            <ul style="list-style: none; padding: 0; font-size: 15px;">
              <li style="margin-bottom: 10px;">✈️ <strong>Travel</strong> – Best flights & packages</li>
              <li style="margin-bottom: 10px;">🏨 <strong>Hotels</strong> – Comfortable stays</li>
              <li style="margin-bottom: 10px;">🛠️ <strong>Local Services</strong> – Reliable help nearby</li>
              <li style="margin-bottom: 10px;">💻 <strong>IT & Office</strong> – Tech support & setup</li>
              <li style="margin-bottom: 10px;">📦 <strong>Product Sourcing</strong> – Find what you need</li>
              <li style="margin-bottom: 10px;">🏗️ <strong>Interiors</strong> – Design & renovation</li>
              <li style="margin-bottom: 10px;">🚗 <strong>Vehicles</strong> – Transport solutions</li>
              <li style="margin-bottom: 10px;">✨ <strong>& More!</strong></li>
            </ul>

            <div style="background-color: #e3f2fd; padding: 15px; border-radius: 5px; margin-top: 25px; border-left: 5px solid #1976d2;">
               <strong>Need a Quotation?</strong><br>
               Contact us below and we will help you get the best rates for your travel or service needs.
            </div>
          </div>

          <!-- Footer -->
          <div style="background-color: #333333; color: #ffffff; padding: 20px; text-align: center; font-size: 14px;">
            <p style="margin: 0 0 10px;">📩 <strong>Contact Us</strong></p>
            <p style="margin: 5px 0;">Instagram: <a href="https://instagram.com/ask_spg" style="color: #64b5f6; text-decoration: none;">@Ask_SPG</a></p>
            <p style="margin: 5px 0;">Email: <a href="mailto:ShahandPatelgroup@gmail.com" style="color: #64b5f6; text-decoration: none;">ShahandPatelgroup@gmail.com</a></p>
            <p style="margin-top: 20px; font-size: 12px; opacity: 0.6;">&copy; 2024 Ask_SPG. All rights reserved.</p>
          </div>

        </div>
      </body>
    </html>
    """
    
    # Attach HTML
    msg.attach(MIMEText(html, "html"))

    # Attach Image
    logo_path = "ask_spg_logo.png"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            img_data = f.read()
            image = MIMEImage(img_data)
            image.add_header("Content-ID", "<ask_spg_logo>")
            image.add_header("Content-Disposition", "inline", filename="ask_spg_logo.png")
            msg.attach(image)
    else:
        print("Warning: Logo image not found. Email will send without logo.")

    return msg

def send_test_email():
    print("--- Ask_SPG Auto Mail Sender ---")
    print(f"Sender: {SENDER_EMAIL}")
    
    password = getpass.getpass("Enter your Google App Password: ")
    receiver_email = input("Enter Recipient Email (to test): ")

    if not password or not receiver_email:
        print("Error: Missing password or recipient.")
        return

    try:
        context = ssl.create_default_context()
        print("\nConnecting to Gmail Server...")
        
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, password)
            print("Message created...")
            message = create_email_content(receiver_email)
            
            print("Sending email...")
            server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
            
        print(f"\n✅ Email successfully sent to {receiver_email}!")
        
    except Exception as e:
        print(f"\n❌ Error sending email: {e}")
        print("Tip: Ensure you are using an 'App Password', not your regular login password.")

if __name__ == "__main__":
    send_test_email()
