# 📄 Paper Analyzer - AI-Powered Academic Paper Assessment System

**An intelligent thesis evaluation platform integrating Claude AI for professional academic assessment and feedback.**

---

## 🎯 Project Overview

### Problem Statement
Academic paper evaluation is a critical but time-consuming task:
- ❌ Manual review takes **6-12 hours per thesis**
- ❌ Evaluation criteria **lack standardization** across different reviewers
- ❌ Students receive **limited, inconsistent feedback** for improvement
- ❌ Limited scalability for institutions evaluating hundreds of papers

### Our Solution
**Paper Analyzer** automates and standardizes academic evaluation through:
- ⚡ **Automated Analysis** - Complete thesis review in 1-2 minutes
- 📊 **Standardized Scoring** - 6-dimensional rubric-based evaluation
- 💡 **Professional Insights** - AI-generated improvement recommendations
- 🎓 **Institutional Quality** - Production-ready backend architecture

---

## ✨ Key Features

### 1. **Intelligent PDF Processing**
- Automatic extraction of thesis content and structure
- Title, chapter, and section identification
- Figure/chart detection and counting
- Metadata and statistical analysis
- Multi-language support

### 2. **Smart Text Chunking**
- Recursive document splitting (2000 chars/chunk)
- Context preservation (200-char overlap)
- Token count estimation
- Langchain integration for LLM optimization

### 3. **Claude AI Integration**
- Claude 3.5 Sonnet engine
- Deep content analysis
- Academic rigor assessment
- Research depth evaluation
- Teaching application analysis

### 4. **Professional Scoring System**
**6-Dimensional Evaluation Framework (Total: 100 points)**
- **Format & Compliance (10%)** - Formatting, page numbers, references
- **Structural Integrity (15%)** - Introduction, literature, methodology, conclusion
- **Theoretical Foundation (25%)** - Frameworks, concepts, theoretical innovation
- **Methodology (25%)** - Research methods, sampling, data analysis
- **Innovation & Application (15%)** - Novelty, practical guidance value
- **Academic Writing (10%)** - Expression, logic flow, terminology

---

## 🏗️ System Architecture

```
User Upload PDF
        ↓
   PDF Parser (pdfplumber)
        ↓
  Text Chunking (Langchain)
        ↓
Claude AI Analysis (Anthropic API)
        ↓
  Rubric Evaluation (6 dimensions)
        ↓
Report Generation (python-docx)
        ↓
   Result Export
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Claude API Key (free $5 credit available)

### Installation

**Step 1: Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/paper-analyzer.git
cd paper-analyzer
```

**Step 2: Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure API Key**
```bash
cp .env.example .env
# Edit .env and add your Claude API key
nano .env
```

**Step 5: Start the Server**
```bash
# Method A: Using startup script
chmod +x start.sh
./start.sh

# Method B: Manual startup
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📁 Project Structure

```
paper-analyzer/
├── backend/                          # Backend application
│   ├── main.py                       # FastAPI application & routes
│   ├── config.py                     # Configuration management
│   ├── pdf_parser.py                 # PDF extraction & parsing
│   ├── chunking.py                   # Intelligent text chunking
│   ├── analyzer.py                   # Claude AI integration
│   ├── rubric.py                     # Scoring system (6 dimensions)
│   └── __init__.py
│
├── frontend/                         # Web interface
│   └── index.html                    # Main UI with drag-drop upload
│
├── data/                             # Data directories
│   ├── uploads/                      # Temporary PDF storage
│   └── rubrics/                      # Custom evaluation rubrics
│
├── requirements.txt                  # Python dependencies
├── .env.example                      # Example environment variables
├── README_EN.md                      # Complete documentation
├── QUICKSTART.md                     # Quick start guide
├── START_HERE.md                     # Getting started guide
└── LICENSE                           # MIT License
```

## 🔑 API端点

| 方法 | 端点 | 说明 |
|------|------|------|
| GET | `/` | API信息 |
| GET | `/health` | 健康检查 |
| GET | `/rubrics` | 获取评分标准 |
| POST | `/upload` | 上传并分析论文 |
| POST | `/generate-report` | 生成报告（开发中） |

## 💡 使用示例

### Python客户端

```python
import requests

# 上传论文
with open("my_paper.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(
        "http://localhost:8000/upload",
        files=files
    )
    
result = response.json()
print(f"总分: {result['analysis']['overall_score']}")
print(f"反馈: {result['analysis']['professional_feedback']}")
```

### cURL

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@paper.pdf"
```

## 📊 评分维度

当前支持的评分标准（数学教育/教学论）：

1. **格式规范** (10%) - 页面设置、目录、页码、参考文献
2. **结构完整性** (15%) - 引言、文献、方法、结论、图表
3. **理论基础** (25%) - 理论框架、概念界定、理论创新
4. **方法论** (25%) - 研究方法、样本、数据、统计分析
5. **创新性与应用** (15%) - 新颖性、指导意义、可行性
6. **学术写作** (10%) - 表述、逻辑、术语、摘要质量

## 🔄 开发路线图

### Phase 1 (✅ 当前)
- [x] PDF解析和文本提取
- [x] 文本分块处理
- [x] Claude API集成
- [x] 基础API框架

### Phase 2 (开发中)
- [ ] 向量数据库集成（pgvector）
- [ ] 相似度查重功能
- [ ] Word/PDF报告生成
- [ ] 评分标准自定义

### Phase 3 (计划中)
- [ ] React前端界面
- [ ] 用户认证系统
- [ ] 批量处理功能
- [ ] 数据库存储历史
- [ ] 云端部署

## 🤖 自定义评分标准

创建自己的评分标准：

```python
from backend.rubric import create_rubric_config

custom_rubric = {
    "your_dimension": {
        "name": "维度名称",
        "weight": 0.20,
        "max_score": 20,
        "criteria": ["标准1", "标准2", "标准3"]
    }
}

create_rubric_config("my_rubric", custom_rubric)
```

## ⚠️ 注意事项

1. **API Key安全** - 不要将.env文件提交到git
2. **文件大小限制** - 默认最大50MB
3. **PDF格式** - 支持text-based PDF，scanned PDF需要OCR处理
4. **Token消耗** - 平均每篇论文消耗5000-10000 tokens

## 📈 成本估算

| 场景 | Token消耗 | 成本（¥） |
|------|----------|----------|
| 单篇短论文 | 5000 | ~0.15 |
| 单篇长论文 | 10000 | ~0.30 |
| 批量10篇 | 80000 | ~2.40 |

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 License

MIT License

## 💬 反馈与支持

如有问题，请在项目Issues中提交，或联系开发者。

---

**开始使用：** `python backend/main.py` 🚀
