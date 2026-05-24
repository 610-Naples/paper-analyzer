import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """应用配置"""
    DEBUG = os.getenv("DEBUG", "True") == "True"
    PORT = int(os.getenv("PORT", 8000))
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 50000000))
    
    # Claude API配置
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # 文件上传配置
    UPLOAD_DIR = "data/uploads"
    RUBRIC_DIR = "data/rubrics"
    
    # 分块配置
    CHUNK_SIZE = 2000
    CHUNK_OVERLAP = 200

config = Config()
