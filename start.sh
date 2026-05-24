#!/bin/bash
# 论文智能评估系统 - 快速启动脚本

set -e  # 遇到错误立即退出

PROJECT_DIR="/Users/siyuzhang/Desktop/KM/paper-analyzer"

echo "╔════════════════════════════════════════════╗"
echo "║   论文智能评估系统 - 快速启动              ║"
echo "║   Paper Analyzer - Quick Start              ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# 检查API Key
if ! grep -q "ANTHROPIC_API_KEY=sk-ant" "$PROJECT_DIR/.env" 2>/dev/null; then
    echo "⚠️  警告：API Key未配置！"
    echo "请按以下步骤操作："
    echo ""
    echo "1. 访问: https://console.anthropic.com/"
    echo "2. 获取 API Key"
    echo "3. 编辑 $PROJECT_DIR/.env"
    echo "   替换: ANTHROPIC_API_KEY=sk-ant-your-key"
    echo ""
    read -p "已配置API Key？(y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "⚠️  跳过启动，请先配置API Key"
        exit 1
    fi
fi

# 进入项目目录
cd "$PROJECT_DIR"

# 激活虚拟环境
echo "📦 激活虚拟环境..."
source venv/bin/activate

# 进入后端目录
cd backend

# 启动服务
echo ""
echo "🚀 启动后端服务... (http://127.0.0.1:8000)"
echo ""
echo "访问以下地址：" 
echo "  📚 API文档:   http://127.0.0.1:8000/docs"
echo "  🔍 API健康:   http://127.0.0.1:8000/health"
echo "  📄 前端界面:  file://$PROJECT_DIR/frontend/index.html"
echo ""
echo "按 Ctrl+C 停止服务"
echo "-------------------------------------------"
echo ""

python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
