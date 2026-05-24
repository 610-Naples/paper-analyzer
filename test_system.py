"""快速测试脚本 - 验证系统功能"""
import os
import sys
from pathlib import Path

# 添加后端路径
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from config import config
from pdf_parser import PDFParser
from chunking import TextChunker
from rubric import RubricEvaluator


def test_config():
    """测试配置"""
    print("✓ 配置测试")
    print(f"  - DEBUG: {config.DEBUG}")
    print(f"  - PORT: {config.PORT}")
    print(f"  - MAX_FILE_SIZE: {config.MAX_FILE_SIZE / 1024 / 1024}MB")
    print(f"  - CHUNK_SIZE: {config.CHUNK_SIZE}")
    print()


def test_rubric():
    """测试评分系统"""
    print("✓ 评分系统测试")
    evaluator = RubricEvaluator()
    rubric = evaluator.rubric
    
    print("  支持的评分维度:")
    for name, section in rubric.items():
        print(f"  - {section['name']} (权重: {section['weight']*100}%)")
    print()


def test_text_chunking():
    """测试文本分块"""
    print("✓ 文本分块测试")
    
    sample_text = """
    第一章 研究背景
    
    本研究针对当代数学教育的核心问题进行深入分析。近年来，数学教育的有效性受到广泛关注。
    本章将详细介绍研究背景、研究意义和研究问题。
    
    1.1 研究背景
    
    在信息技术快速发展的时代，数学教育面临新的挑战。传统的教学方法需要创新和改进。
    """ * 5  # 重复以获得足够长度的文本
    
    chunker = TextChunker()
    chunks = chunker.chunk_text(sample_text)
    
    print(f"  - 文本长度: {len(sample_text)} 字符")
    print(f"  - 分块数量: {len(chunks)}")
    print(f"  - 平均块大小: {sum(c['length'] for c in chunks) // len(chunks)} 字符")
    print()


def test_api_connection():
    """测试API连接"""
    print("✓ API配置检查")
    
    api_key = config.ANTHROPIC_API_KEY
    if api_key:
        masked_key = api_key[:10] + "..." + api_key[-5:]
        print(f"  - API Key已配置: {masked_key}")
    else:
        print("  - ⚠️  API Key未配置，请更新 .env 文件")
    print()


def test_directories():
    """测试目录结构"""
    print("✓ 目录结构检查")
    
    dirs_to_check = [
        config.UPLOAD_DIR,
        config.RUBRIC_DIR,
    ]
    
    for dir_path in dirs_to_check:
        path = Path(dir_path)
        exists = path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {dir_path}")
        if not exists:
            path.mkdir(parents=True, exist_ok=True)
            print(f"    已创建")
    print()


def main():
    """运行所有测试"""
    print("=" * 50)
    print("论文智能评估系统 - 系统检查")
    print("=" * 50)
    print()
    
    try:
        test_config()
        test_directories()
        test_rubric()
        test_text_chunking()
        test_api_connection()
        
        print("=" * 50)
        print("✅ 所有检查通过！系统准备就绪。")
        print("")
        print("启动方式:")
        print("  cd backend")
        print("  python -m uvicorn main:app --reload")
        print("")
        print("访问API文档:")
        print("  http://localhost:8000/docs")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ 检查失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
