import logging
import smtplib
from email.mime.text import MIMEText

# Set up logging
logging.basicConfig(level=logging.INFO)

class ResponseEngine:
    def __init__(self, notification_email=None):
        self.responses = []
        self.notification_email = notification_email

    def respond_to_threat(self, threat):
        """Respond to a detected threat based on its type."""
        if threat['type'] == "Quantum Attack":
            self.handle_quantum_attack(threat)
        elif threat['type'] == "Data Breach":
            self.handle_data_breach(threat)
        elif threat['type'] == "Anomaly":
            self.handle_anomaly(threat)
        else:
            self.default_response(threat)

    def handle_quantum_attack(self, threat):
        """Handle a quantum attack threat."""
        response = f"Initiating countermeasures for: {threat['message']}"
        self.responses.append(response)
        logging.warning(response)
        self.send_notification(response)
        # Placeholder for actual countermeasure logic

    def handle_data_breach(self, threat):
        """Handle a data breach threat."""
        response = f"Data breach detected! Initiating lockdown procedures."
        self.responses.append(response)
        logging.warning(response)
        self.send_notification(response)
        # Placeholder for actual lockdown logic

    def handle_anomaly(self, threat):
        """Handle an anomalous behavior threat."""
        response = f"Anomaly detected: {threat['message']}. Investigating..."
        self.responses.append(response)
        logging.warning(response)
        self.send_notification(response)
        # Placeholder for investigation logic

    def default_response(self, threat):
        """Default response for unclassified threats."""
        response = f"Unclassified threat detected: {threat['message']}. Taking no action."
        self.responses.append(response)
        logging.info(response)

    def send_notification(self, message):
        """Send a notification via email."""
        if self.notification_email:
            try:
                msg = MIMEText(message)
                msg['Subject'] = 'Security Alert'
                msg['From'] = 'alert@securitysystem.com'
                msg['To'] = self.notification_email

                with smtplib.SMTP('smtp.example.com', 587) as server:
                    server.starttls()
                    server.login('your_email@example.com', 'your_password')
                    server.send_message(msg)
                logging.info("Notification sent successfully.")
            except Exception as e:
                logging.error(f"Failed to send notification: {e}")

    def get_responses(self):
        """Return the list of responses."""
        return self.responses

    def clear_responses(self):
        """Clear the list of responses."""
        self.responses = []
        logging.info("Responses cleared.")

# Example usage
if __name__ == "__main__":
    response_engine = ResponseEngine(notification_email='admin@example.com')
    
    # Simulate responding to threats
    threats = [
        {"type": "Quantum Attack", "message": "Quantum attack detected on server."},
        {"type": "Data Breach", "message": "Unauthorized access to sensitive data."},
        {"type": "Anomaly", "message": "Unusual login activity detected."}
    ]
    
    for threat in threats:
        response_engine.respond_to_threat(threat)
    
    # Print all responses
    for response in response_engine.get_responses():
        print(response)
