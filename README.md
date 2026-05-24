# 论文智能评估系统 📄

一个集成Claude AI的专业学位论文评估助手，为数学教育、教学论等学科提供深度的学术评价和改进建议。

##  功能特性

- ✅ **PDF解析与结构识别** - 自动提取标题、章节、目录、图表
- ✅ **文本智能分块** - 优化处理方式便于LLM分析
- ✅ **专业评分体系** - 基于教学论/数学教育专家的Rubric评分
- ✅ **Claude AI分析** - 深度内容分析、专业建议
- ✅ **格式检查** - 检查目录、页码、参考文献等规范性
- ✅ **图表评估** - 评估图表数量和适配度
- ✅ **相似度检查** - 初步查重建议
- ✅ **生成报告** - 导出评估结果（开发中）

## 📋 系统架构

```
User Upload PDF
         ↓
    PDF Parser (解析)
         ↓
   Text Chunking (分块)
         ↓
    Claude LLM Analysis (LLM分析)
         ↓
  Rubric Evaluator (评分)
         ↓
  Report Generator (报告生成)
         ↓
   Export (Word/PDF)
```

## 🛠️ 快速开始

### 1. 环境配置

```bash
# 克隆项目
cd /Users/siyuzhang/Desktop/KM/paper-analyzer

# 创建Python虚拟环境
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置Claude API

```bash
# 复制环境变量文件
cp .env.example .env

# 编辑 .env 文件，添加你的API Key
# ANTHROPIC_API_KEY=sk-ant-xxx
```

### 3. 启动服务

```bash
# 进入后端目录
cd backend

# 运行FastAPI服务
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

服务将在 `http://localhost:8000` 运行

### 4. 测试API

```bash
# 查看API文档
open http://localhost:8000/docs

# 检查健康状态
curl http://localhost:8000/health

# 获取评分标准
curl http://localhost:8000/rubrics
```

## 📁 项目结构

```
paper-analyzer/
├── backend/
│   ├── main.py              # FastAPI应用入口
│   ├── config.py            # 配置文件
│   ├── pdf_parser.py        # PDF解析模块
│   ├── chunking.py          # 文本分块模块
│   ├── analyzer.py          # LLM分析引擎
│   └── rubric.py            # 评分系统
├── frontend/                # 前端（React/Vue）
│   └── (待开发)
├── data/
│   ├── uploads/             # 上传的PDF存储
│   └── rubrics/             # 自定义评分标准
├── requirements.txt         # Python依赖
├── .env.example             # 环境变量示例
└── README.md
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
