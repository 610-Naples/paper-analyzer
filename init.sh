#!/bin/bash
# 项目初始化脚本

echo "🚀 论文智能评估系统 - 初始化"
echo "======================================="

# 检查Python版本
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python版本: $python_version"

# 创建虚拟环境
echo "📦 创建虚拟环境..."
python3 -m venv venv
source venv/bin/activate

# 升级pip
echo "⬆️  升级pip..."
pip install --upgrade pip

# 安装依赖
echo "📚 安装依赖包..."
pip install -r requirements.txt

# 复制环境变量
if [ ! -f .env ]; then
    echo "📝 创建.env文件..."
    cp .env.example .env
    echo "⚠️  请编辑 .env 文件添加你的 ANTHROPIC_API_KEY"
fi

# 创建必要目录
mkdir -p data/uploads
mkdir -p data/rubrics

echo ""
echo "✅ 初始化完成！"
echo ""
echo "下一步："
echo "1. 编辑 .env 文件添加 API Key"
echo "2. 运行: cd backend && python -m uvicorn main:app --reload"
echo "3. 访问: http://localhost:8000/docs"
echo ""
