"""
Configuration Management

Handles logging, environment variables, and API configuration.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_URL = os.getenv("CAMS_API_URL", "https://mcp.camsbiometrics.com/api")
API_TIMEOUT = float(os.getenv("API_TIMEOUT", "30.0"))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "cams_mcp.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", "10485760"))  # 10MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))


def setup_logging():
    """Configure logging with rotation."""
    log_dir = Path.home() / ".cams_mcp" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / LOG_FILE
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    logging.info("📝 Logging configured successfully")
    logging.info(f"📂 Log file: {log_file}")


def check_and_rotate_log():
    """Check if log rotation is needed (called before each tool invocation)."""
    # Rotation is handled automatically by RotatingFileHandler
    pass
