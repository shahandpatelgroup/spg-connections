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
    msg["Subject"] = "Partnership Opportunity with Ask_SPG 🚀 We bring you Customers!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    # HTML content with inline CSS (Updated B2B Content)
    html = """
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; margin: 0;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
          
          <!-- Banner / Header -->
          <div style="background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 30px; text-align: center; color: white;">
             <!-- Logo Image (Content-ID method) -->
             <img src="cid:ask_spg_logo" alt="Ask_SPG Logo" style="width: 100px; height: auto; border-radius: 50%; border: 3px solid white; margin-bottom: 15px;">
             <h1 style="margin: 0; font-size: 24px;">Partner with Ask_SPG 👋</h1>
             <p style="margin: 5px 0 0; opacity: 0.9;">Connecting You with Ready-to-Buy Customers.</p>
          </div>

          <!-- Body Content -->
          <div style="padding: 30px; color: #333333; line-height: 1.6; font-size: 18px;">
            <p style="font-size: 22px; color: #0d47a1; margin-top: 0; text-align: center;"><strong>Hello Business Partner,</strong></p>
            <p style="text-align: center; margin-bottom: 30px;">
              We are <strong>Ask_SPG</strong>, your bridge to qualified customers.
            </p>
            
            <!-- Why Partner Section -->
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; margin-bottom: 25px;">
                <h3 style="color: #0d47a1; margin-top: 0; text-align: center; margin-bottom: 15px;">🚀 Why Partner with Ask_SPG?</h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <span style="font-size: 18px; margin-right: 10px;">✅</span> 
                        <span><strong>Zero Marketing Cost:</strong> We bring ready-to-buy customers to you.</span>
                    </li>
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <span style="font-size: 18px; margin-right: 10px;">✅</span> 
                        <span><strong>Verified Leads:</strong> No time-wasting; only genuine inquiries.</span>
                    </li>
                    <li style="margin-bottom: 0px; display: flex; align-items: center;">
                        <span style="font-size: 18px; margin-right: 10px;">✅</span> 
                        <span><strong>High Conversion:</strong> We filter prospects to match your specific services.</span>
                    </li>
                </ul>
            </div>

            <p style="text-align: center; font-size: 18px;">
                We act as a <strong>mediator</strong>. We send you the requirement -> You send the best quote -> We close the deal.
            </p>

            <!-- CTA Section -->
            <div style="text-align: center; margin: 30px 0;">
                <div style="background-color: #e3f2fd; padding: 20px; border-radius: 8px; display: inline-block; width: 80%;">
                    <p style="margin: 0 0 10px; font-weight: bold; color: #0d47a1;">Interested in growing with us?</p>
                    <a href="mailto:ShahandPatelgroup@gmail.com?subject=Partnership%20Interest" style="background-color: #1976d2; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; font-weight: bold; display: inline-block;">Reply "I'm Interested"</a>
                </div>
            </div>

            <hr style="border: 0; border-top: 1px solid #bbdefb; margin: 30px 0;">
            
            <h3 style="margin-bottom: 15px; font-size: 20px; color: #0d47a1; text-align: center;">📌 Ask_SPG Areas of Work:</h3>
            <ul style="list-style: none; padding: 0; font-size: 16px; color: #0d47a1; text-align: center;">
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">✈️ Travel & Holidays</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🏔️ Indian Treks</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🛠️ Local Services</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">💻 IT Solutions</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">📦 Product Sourcing</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🏗️ Interiors</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🚗 Vehicle Buy/Sell</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🏠 Real Estate</li>
              <li style="display: inline-block; background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🎉 Event Planning</li>
            </ul>
          </div>

          <!-- Instagram Button (New) -->
          <div style="text-align: center; background-color: #ffffff; padding-bottom: 30px;">
             <a href="https://instagram.com/ask_spg" style="background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; font-family: sans-serif; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
               📷 Follow us on Instagram
             </a>
          </div>

          <!-- Footer -->
          <div style="background-color: #333333; color: #ffffff; padding: 20px; text-align: center; font-size: 14px;">
            <p style="margin: 0 0 10px;">📩 <strong>Contact Us</strong></p>
            <p style="margin: 5px 0;">Email: <a href="mailto:ShahandPatelgroup@gmail.com" style="color: #64b5f6; text-decoration: none;">ShahandPatelgroup@gmail.com</a></p>
            
            <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">
               To opt out of future partnership opportunities, please reply with "UNSUBSCRIBE".
            </p>

            <p style="margin-top: 20px; font-size: 12px; opacity: 0.6;">&copy; 2026 Ask_SPG. All rights reserved.</p>
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
