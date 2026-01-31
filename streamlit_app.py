
import streamlit as st
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

# Page Config
st.set_page_config(page_title="Ask_SPG Mail Sender", page_icon="🚀")

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def create_email_content(sender_email, receiver_email):
    """
    Creates the MIME object with HTML banner using the updated B2B content.
    """
    msg = MIMEMultipart("related")
    msg["Subject"] = "Partnership Opportunity with Ask_SPG 🚀 We bring you Customers!"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # HTML content with inline CSS (Updated Blue Theme)
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
          <div style="padding: 30px; color: #333333; line-height: 1.6;">
            <p style="font-size: 18px; color: #0d47a1; margin-top: 0;"><strong>Hello Business Partner,</strong></p>
            <p>We are <strong>Ask_SPG</strong>, a service aggregator that connects customers with the best service providers in the market.</p>
            
            <h3 style="color: #0d47a1; margin-bottom: 5px;">🤝 How we assist you:</h3>
            <p style="margin-top: 0;">We receive numerous travel and holiday inquiries from our client base daily. We act as a <strong>mediator</strong> to filter and verify these requirements.</p>

            <h3 style="color: #0d47a1; margin-bottom: 5px;">🚀 Our Proposal:</h3>
            <p style="margin-top: 0;">We would like to <strong>redirect these customer requirements to you</strong>.<br>
            When we share a requirement, we request that you provide us with your <strong>best quotation/package</strong>. If your service and rates match our customer's expectations, we close the deal for you.</p>

            <div style="background-color: #e3f2fd; padding: 15px; border-radius: 5px; margin: 25px 0; border-left: 5px solid #1976d2; color: #0d47a1;">
               <strong>Ready to receive inquiries?</strong><br>
               <span style="color: #333;">Reply to this email letting us know you are interested, and we will start sharing relevant travel requirements with you immediately.</span>
            </div>

            <hr style="border: 0; border-top: 1px solid #bbdefb; margin: 20px 0;">
            
            <h3 style="margin-bottom: 15px; font-size: 16px; color: #0d47a1; text-align: center;">📌 Ask_SPG Areas of Work:</h3>
            <ul style="list-style: none; padding: 0; font-size: 14px; color: #0d47a1; display: flex; flex-wrap: wrap; justify-content: center;">
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">✈️ Travel & Holidays</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🏨 Hotel Bookings</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🛠️ Local Services</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">💻 IT Solutions</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">📦 Product Sourcing</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🏗️ Interiors</li>
              <li style="background: #e3f2fd; padding: 8px 15px; border-radius: 15px; border: 1px solid #90caf9; margin: 5px;">🚗 Vehicle Transport</li>
            </ul>
          </div>

          <!-- Footer -->
          <div style="background-color: #333333; color: #ffffff; padding: 20px; text-align: center; font-size: 14px;">
            <p style="margin: 0 0 10px;">📩 <strong>Contact Us</strong></p>
            <p style="margin: 5px 0;">Instagram: <a href="https://instagram.com/ask_spg" style="color: #64b5f6; text-decoration: none;">@Ask_SPG</a></p>
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

    # Attach Image (Local Check)
    logo_filename = "ask_spg_logo.png"
    if os.path.exists(logo_filename):
        with open(logo_filename, "rb") as f:
            img_data = f.read()
            image = MIMEImage(img_data)
            image.add_header("Content-ID", "<ask_spg_logo>")
            image.add_header("Content-Disposition", "inline", filename=logo_filename)
            msg.attach(image)
    
    return msg

def main():
    st.title("🚀 Ask_SPG Mail Sender")
    st.markdown("Send bulk emails to partners with the **Ask_SPG B2B Template**.")

    # Sidebar for Credentials
    with st.sidebar:
        st.header("🔑 Credentials")
        sender_email = st.text_input("Sender Email", value="ShahandPatelgroup@gmail.com")
        password = st.text_input("App Password", type="password", help="Use your Google App Password")
        
        st.info("Don't share your App Password with anyone.")

    # Main Area
    st.subheader("1. Recipient List")
    uploaded_file = st.file_uploader("Upload CSV (must contain 'Email' column)", type=["csv"])
    
    manual_emails = st.text_area("Or paste emails manually (comma separated):", placeholder="client1@gmail.com, client2@yahoo.com")

    # Image Uploader for Logo (Optional but good for dynamic logo)
    st.subheader("2. Branding")
    logo_file = st.file_uploader("Upload Logo (ask_spg_logo.png)", type=["png", "jpg"])
    if logo_file:
        with open("ask_spg_logo.png", "wb") as f:
            f.write(logo_file.getbuffer())
        st.success("Logo uploaded!")

    if st.button("Send Emails ✉️", type="primary"):
        if not password:
            st.error("Please enter your App Password in the sidebar.")
            return

        # Gather emails
        email_list = []
        if uploaded_file:
            import pandas as pd
            try:
                df = pd.read_csv(uploaded_file)
                if "Email" in df.columns:
                    email_list.extend(df["Email"].dropna().tolist())
                else:
                    st.error("CSV must have an 'Email' column.")
            except Exception as e:
                st.error(f"Error reading CSV: {e}")
        
        if manual_emails:
            manual_list = [e.strip() for e in manual_emails.split(",") if "@" in e]
            email_list.extend(manual_list)
        
        email_list = list(set(email_list)) # Remove duplicates

        if not email_list:
            st.warning("No valid emails found to send.")
            return

        # Sending Process
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                status_text.text("Connecting to Gmail...")
                server.login(sender_email, password)
                
                for i, receiver in enumerate(email_list):
                    status_text.text(f"Sending to {receiver} ({i+1}/{len(email_list)})...")
                    
                    msg = create_email_content(sender_email, receiver)
                    server.sendmail(sender_email, receiver, msg.as_string())
                    
                    progress_bar.progress((i + 1) / len(email_list))
            
            status_text.success(f"✅ Successfully sent {len(email_list)} emails!")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error during sending: {e}")

if __name__ == "__main__":
    main()
