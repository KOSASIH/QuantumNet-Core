import logging
import json
import os
import yaml
from datetime import datetime

# Configure logging
def setup_logging(log_file='orchestrator.log', log_level=logging.INFO):
    """Set up logging configuration."""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging is set up.")

def log_event(event, level=logging.INFO):
    """Log an event for monitoring purposes."""
    if level == logging.INFO:
        logging.info(event)
    elif level == logging.WARNING:
        logging.warning(event)
    elif level == logging.ERROR:
        logging.error(event)
    elif level == logging.CRITICAL:
        logging.critical(event)
    else:
        logging.debug(event)

def load_configuration(file_path):
    """Load configuration settings from a JSON or YAML file."""
    if not os.path.exists(file_path):
        logging.error(f"Configuration file not found: {file_path}")
        return None

    try:
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                config = json.load(file)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                config = yaml.safe_load(file)
            else:
                logging.error("Unsupported file format. Please use JSON or YAML.")
                return None
        logging.info("Configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return None

def get_environment_config(env='development'):
    """Load environment-specific configuration."""
    config_file = f'config_{env}.yaml'
    return load_configuration(config_file)

def track_event(event_name, details):
    """Track an event with additional details."""
    event_log = {
        'event_name': event_name,
        'details': details,
        'timestamp': datetime.now().isoformat()
    }
    log_event(f"Event tracked: {event_log}")

# Example usage
if __name__ == "__main__":
    setup_logging()
    log_event("Orchestrator started.")
    config = load_configuration('config.yaml')
    if config:
        log_event(f"Loaded configuration: {config}")
