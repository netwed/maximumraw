from flask import Flask, request, jsonify
import csv
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'maximumraw@gmail.com'
EMAIL_PASSWORD = 'fjjk000000Zarsno7v()@!)!'
RECIPIENT_EMAIL = 'johnn.anthony@gmail.com'

# CSV file to store user data
CSV_FILE = 'user_data.csv'

# Initialize CSV with headers if it doesn't exist
def initialize_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'IP Address', 'Browser', 'Platform', 'Language', 'Screen Resolution', 'Timezone', 'Referrer'])
    except FileExistsError:
        pass

initialize_csv()

@app.route('/collect-data', methods=['POST'])
def collect_data():
    # Parse user data from request
    user_data = request.json
    ip_address = request.remote_addr
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Log user data to CSV
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            ip_address,
            user_data.get('browser', 'N/A'),
            user_data.get('platform', 'N/A'),
            user_data.get('language', 'N/A'),
            user_data.get('screenResolution', 'N/A'),
            user_data.get('timezone', 'N/A'),
            user_data.get('referrer', 'N/A'),
        ])

    # Send email with CSV attachment
    send_email(CSV_FILE)

    return jsonify({'message': 'User data collected and logged successfully!'})

def send_email(file_path):
    # Email subject and body
    subject = 'New User Data Log'
    body = 'Attached is the latest user data log in CSV format.'

    # Set up email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach CSV file
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={file_path}',
    )
    msg.attach(part)

    # Send email via SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
