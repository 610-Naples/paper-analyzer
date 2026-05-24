import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application Configuration"""
    DEBUG = os.getenv("DEBUG", "True") == "True"
    PORT = int(os.getenv("PORT", 8000))
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 50000000))
    
    # Claude API Configuration
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # File Upload Configuration
    UPLOAD_DIR = "data/uploads"
    RUBRIC_DIR = "data/rubrics"
    
    # Text Chunking Configuration
    CHUNK_SIZE = 2000
    CHUNK_OVERLAP = 200

config = Config()
