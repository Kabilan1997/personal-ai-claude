"""Configuration management"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # API Settings
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Model Settings
    MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased")
    MODEL_MAX_LENGTH = int(os.getenv("MODEL_MAX_LENGTH", 512))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 150))
    
    # Memory Settings
    CONVERSATION_MEMORY_SIZE = int(os.getenv("CONVERSATION_MEMORY_SIZE", 20))
    DB_PATH = os.getenv("DB_PATH", "./data/conversations.db")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "./logs/ai.log")
    
    @classmethod
    def to_dict(cls):
        """Get all config as dictionary"""
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if not key.startswith('_') and key.isupper()
        }
