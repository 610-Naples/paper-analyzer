# 🚀 快速开始指南

## 3分钟启动系统

### 1️⃣ 获取Claude API Key

访问 [https://console.anthropic.com/](https://console.anthropic.com/) 获取免费的API Key

### 2️⃣ 配置环境变量

```bash
cd /Users/siyuzhang/Desktop/KM/paper-analyzer

# 编辑 .env 文件
nano .env
```

替换为你的API Key：
```
ANTHROPIC_API_KEY=sk-ant-your-api-key-here
DEBUG=True
PORT=8000
```

### 3️⃣ 启动后端服务

```bash
# 激活虚拟环境
source venv/bin/activate

# 进入后端目录
cd backend

# 启动FastAPI服务
python -m uvicorn main:app --reload
```

输出应该显示：
```
✓ Uvicorn running on http://127.0.0.1:8000
✓ Reload enabled
```

### 4️⃣ 测试API

**新开一个终端窗口：**

```bash
# 检查API健康状态
curl http://localhost:8000/health

# 查看交互式API文档
open http://localhost:8000/docs
```

### 5️⃣ 上传论文进行分析

**方式1：使用Web界面**

```bash
# 在浏览器中打开前端页面
open /Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html
```

或者访问：`file:///Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html`

**方式2：使用Python脚本**

```python
import requests

# 上传论文
with open("your_paper.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(
        "http://localhost:8000/upload",
        files=files
    )

# 查看分析结果
result = response.json()
print(f"总分: {result['analysis']['overall_score']['final_score']}")
```

**方式3：使用cURL**

```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@/path/to/your/paper.pdf"
```

---

## 📊 系统架构图

```
┌─────────────────────────────────────────┐
│       用户上传PDF                        │
│    (Web前端 / API客户端)                 │
└────────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────┐
    │  FastAPI后端服务    │
    │  (main.py)          │
    └────┬────────┬──────┬┘
         │        │      │
    ┌────▼──┐┌────▼──┐┌──▼─────┐
    │PDF解析││文本分块││LLM分析 │
    │(parse││(chunk)││(Claude)│
    └────┬──┘└────┬──┘└──┬─────┘
         │        │      │
         └────┬───┴──┬───┘
              │      │
         ┌────▼──┐┌──▼────────┐
         │Rubric││生成报告    │
         │评分  ││(Report)   │
         └────┬──┘└──┬────────┘
              │      │
              └──┬───┘
                 │
            ┌────▼──────────┐
            │返回JSON结果   │
            │(Analysis)     │
            └───────────────┘
```

---

## 🧪 系统测试

验证所有组件是否正常运行：

```bash
cd /Users/siyuzhang/Desktop/KM/paper-analyzer
source venv/bin/activate
python test_system.py
```

预期输出：
```
==================================================
论文智能评估系统 - 系统检查
==================================================

✓ 配置测试
✓ 目录结构检查
✓ 评分系统测试
✓ 文本分块测试
✓ API配置检查

✅ 所有检查通过！系统准备就绪。
```

---

## 📁 项目结构概览

```
paper-analyzer/
├── backend/
│   ├── main.py              ← FastAPI应用入口
│   ├── config.py            ← 配置管理
│   ├── pdf_parser.py        ← PDF解析
│   ├── chunking.py          ← 文本分块
│   ├── analyzer.py          ← LLM分析引擎
│   └── rubric.py            ← 评分系统
├── frontend/
│   └── index.html           ← Web上传界面
├── data/
│   ├── uploads/             ← 上传的论文存储
│   └── rubrics/             ← 自定义评分标准
├── venv/                    ← Python虚拟环境
├── requirements.txt         ← 项目依赖
├── .env                     ← 环境变量（API Key等）
├── .env.example             ← 环境变量模板
├── test_system.py           ← 系统测试脚本
├── init.sh                  ← 初始化脚本
└── README.md                ← 完整文档
```

---

## 🎯 核心功能流程

### 论文上传 → 分析 → 返回结果

```
┌──────────────┐
│  上传PDF     │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│1. PDF解析                    │
│  • 提取全文                  │
│  • 识别标题、章节            │
│  • 检测图表数量              │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│2. 文本分块                   │
│  • 智能分割（2000字/块）     │
│  • Token估算                 │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│3. LLM分析（Claude）          │
│  • 内容质量评估              │
│  • 格式规范检查              │
│  • 图表适配度评价            │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│4. 专业评分                   │
│  • 按Rubric打分              │
│  • 权重计算                  │
│  • 生成总分                  │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│5. 生成报告                   │
│  • JSON结构化结果            │
│  • 可导出Word/PDF（开发中）  │
└──────────────────────────────┘
```

---

## 🔧 常见问题

### Q1: 启动时出现 "ModuleNotFoundError"

**A:** 确保虚拟环境已激活：
```bash
source /Users/siyuzhang/Desktop/KM/paper-analyzer/venv/bin/activate
```

### Q2: API Key配置不生效

**A:** 检查 `.env` 文件：
1. 确保文件在项目根目录
2. 格式正确：`ANTHROPIC_API_KEY=sk-ant-xxx`
3. 重启FastAPI服务

### Q3: PDF解析失败

**A:** 确保：
- PDF是text-based（扫描图片不支持，需OCR处理）
- 文件大小 < 50MB
- PDF格式正确

### Q4: 分析很慢或超时

**A:** 
- 默认使用claude-3-5-sonnet（速度平衡模型）
- 长论文（>10000字）可能需要1-2分钟
- 可在 `analyzer.py` 中改用更快的模型

---

## 📞 下一步开发

### Phase 2（本周）
- [ ] 添加Word/PDF报告导出
- [ ] 实现更精细的相似度检查
- [ ] 创建自定义评分标准编辑界面

### Phase 3（下周）
- [ ] 导入向量数据库（pgvector）
- [ ] React/Vue前端界面完善
- [ ] 用户认证系统
- [ ] 云端部署

---

## 💡 提示

**优化Token使用：**
```python
# 不需要完整论文，可以只分析关键部分
text = text[:5000]  # 前5000字通常已足够评估
```

**自定义评分标准：**
```bash
# 编辑自己的rubric配置
data/rubrics/my_rubric.json
```

**调试模式：**
```bash
# 启用详细日志
DEBUG=true python -m uvicorn backend/main:app --reload --log-level debug
```

---

**现在，系统已完全准备就绪！🎉 祝你使用愉快！**
