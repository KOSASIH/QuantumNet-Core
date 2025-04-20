import logging
import re
import json

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("security_events.log"),
        logging.StreamHandler()
    ]
)

def log_event(event, level=logging.INFO):
    """Log security events with different severity levels."""
    if level == logging.INFO:
        logging.info(f"Security Event: {event}")
    elif level == logging.WARNING:
        logging.warning(f"Security Event: {event}")
    elif level == logging.ERROR:
        logging.error(f"Security Event: {event}")
    else:
        logging.debug(f"Security Event: {event}")

def validate_data(data, expected_type=str, max_length=255, regex_pattern=None):
    """Validate incoming data for security checks.

    :param data: The data to validate.
    :param expected_type: The expected type of the data (default is str).
    :param max_length: Maximum allowed length of the data.
    :param regex_pattern: Optional regex pattern for additional validation.
    :raises ValueError: If validation fails.
    :return: True if validation passes.
    """
    if not isinstance(data, expected_type):
        raise ValueError(f"Data must be of type {expected_type.__name__}.")
    
    if len(data) > max_length:
        raise ValueError(f"Data exceeds maximum length of {max_length} characters.")
    
    if regex_pattern and not re.match(regex_pattern, data):
        raise ValueError("Data does not match the required format.")
    
    return True

def sanitize_input(data):
    """Sanitize input data to prevent injection attacks."""
    if isinstance(data, str):
        return re.sub(r'[<>]', '', data)  # Remove angle brackets
    return data

def generate_event_report(events):
    """Generate a structured report of security events.

    :param events: List of events to include in the report.
    :return: JSON formatted string of the report.
    """
    report = {
        "event_count": len(events),
        "events": events
    }
    return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        log_event("System started.")
        validate_data("Valid input data", max_length=50)
        sanitized_data = sanitize_input("<script>alert('XSS');</script>")
        log_event(f"Sanitized data: {sanitized_data}")

        # Generate a report of events
        events = [
            {"event": "User  login", "status": "success"},
            {"event": "File access", "status": "denied"}
        ]
        report = generate_event_report(events)
        log_event(f"Event Report: {report}")
    except ValueError as e:
        log_event(f"Validation error: {e}", level=logging.ERROR)
