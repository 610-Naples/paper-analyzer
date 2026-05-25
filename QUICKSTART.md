# 🚀 Quick Start Guide

Get the Paper Analyzer system running in 3 minutes.

## Step 1️⃣: Get Claude API Key

Visit [https://console.anthropic.com/](https://console.anthropic.com/) to get a free API Key

New accounts receive **$5 free credits** - enough to test 200+ paper analyses.

## Step 2️⃣: Configure Environment Variables

```bash
cd /Users/siyuzhang/Desktop/KM/paper-analyzer

# Edit .env file
nano .env
```

Replace with your API Key:
```
ANTHROPIC_API_KEY=sk-ant-your-api-key-here
DEBUG=True
PORT=8000
```

### Step 3️⃣: Start Backend Service

```bash
# Activate virtual environment
source venv/bin/activate

# Navigate to backend directory
cd backend

# Start FastAPI service
python -m uvicorn main:app --reload
```

Expected output:
```
✓ Uvicorn running on http://127.0.0.1:8000
✓ Reload enabled
```

### Step 4️⃣: Test API

**Open a new terminal window:**

```bash
# Check API health status
curl http://localhost:8000/health

# View interactive API documentation
open http://localhost:8000/docs
```

### Step 5️⃣: Upload Paper for Analysis

**Option 1: Using Web Interface**

```bash
# Open frontend page in browser
open /Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html
```

Or visit: `file:///Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html`

**Option 2: Using Python Script**

```python
import requests

# Upload paper
with open("your_paper.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(
        "http://localhost:8000/upload",
        files=files
    )

# View analysis results
result = response.json()
print(f"Overall Score: {result['analysis']['overall_score']['final_score']}")
```

**Option 3: Using cURL**

```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@/path/to/your/paper.pdf"
```

---

## 📊 System Architecture Diagram

```
┌─────────────────────────────────────────┐
│       User Uploads PDF                   │
│    (Web Frontend / API Client)           │
└────────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────┐
    │  FastAPI Backend    │
    │  Service (main.py)  │
    └────┬────────┬──────┬┘
         │        │      │
    ┌────▼──┐┌────▼──┐┌──▼─────┐
    │PDF    ││Text   ││LLM     │
    │Parser ││Chunking││Analysis│
    │(parse)││(chunk) ││(Claude)│
    └────┬──┘└────┬──┘└──┬─────┘
         │        │      │
         └────┬───┴──┬───┘
              │      │
         ┌────▼──┐┌──▼──────────┐
         │Rubric ││Generate     │
         │Scoring││Report       │
         └────┬──┘└──┬──────────┘
              │      │
              └──┬───┘
                 │
            ┌────▼──────────┐
            │Return JSON    │
            │Result         │
            │(Analysis)     │
            └───────────────┘
```

---

## 🧪 System Testing

Verify all components are working correctly:

```bash
cd /Users/siyuzhang/Desktop/KM/paper-analyzer
source venv/bin/activate
python test_system.py
```

Expected output:
```
==================================================
Paper Intelligence Assessment System - System Check
==================================================

✓ Configuration Test
✓ Directory Structure Check
✓ Scoring System Test
✓ Text Chunking Test
✓ API Configuration Check

✅ All checks passed! System is ready.
```

---

## 📁 Project Structure Overview

```
paper-analyzer/
├── backend/
│   ├── main.py              ← FastAPI application entry
│   ├── config.py            ← Configuration management
│   ├── pdf_parser.py        ← PDF parsing
│   ├── chunking.py          ← Text chunking
│   ├── analyzer.py          ← LLM analysis engine
│   └── rubric.py            ← Scoring system
├── frontend/
│   └── index.html           ← Web upload interface
├── data/
│   ├── uploads/             ← Uploaded papers storage
│   └── rubrics/             ← Custom scoring standards
├── venv/                    ← Python virtual environment
├── requirements.txt         ← Project dependencies
├── .env                     ← Environment variables (API Key etc.)
├── .env.example             ← Environment variables template
├── test_system.py           ← System test script
├── init.sh                  ← Initialization script
└── README.md                ← Complete documentation
```

---

## 🎯 Core Functionality Workflow

### Paper Upload → Analysis → Return Results

```
┌──────────────┐
│  Upload PDF  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│1. PDF Parsing                │
│  • Extract full text         │
│  • Identify titles, chapters │
│  • Detect figure count       │
│  • Extract metadata          │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│2. Text Chunking              │
│  • Split into chunks (2000   │
│    characters per chunk)     │
│  • Preserve context overlap  │
│  • Estimate token count      │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│3. LLM Analysis               │
│  • Call Claude API           │
│  • Analyze paper quality     │
│  • Evaluate academic rigor   │
│  • Assess innovative value   │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│4. Scoring System             │
│  • Calculate 6 dimension     │
│    scores                    │
│  • Compute overall score     │
│  • Determine grade (A-F)     │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│5. Return Results             │
│  • JSON format analysis      │
│  • Detailed feedback         │
│  • Suggestions for           │
│    improvement               │
└──────────────────────────────┘
```

---

## 🔑 6 Scoring Dimensions

### 1. Format Specification (10%)
- Proper formatting and layout
- Page numbering and margins
- Reference citation accuracy

### 2. Structural Completeness (15%)
- Clear introduction section
- Comprehensive literature review
- Well-defined methodology
- Proper conclusion and discussion

### 3. Theoretical Foundation (25%)
- Sound theoretical framework
- Clear conceptual definitions
- Novel theoretical insights

### 4. Methodology (25%)
- Appropriate research methods
- Representative sample selection
- Rigorous data analysis
- Valid conclusions

### 5. Creative Application (15%)
- Novel contributions to field
- Practical value and impact
- Potential for real-world application

### 6. Academic Writing (10%)
- Clear and professional writing
- Proper technical terminology
- Logical flow and organization
- Minimal grammatical errors

---

## ⚡ Quick Troubleshooting

### Issue: API Key Error
```bash
# Make sure .env file has correct format
cat .env
# Should show: ANTHROPIC_API_KEY=sk-ant-xxx...
```

### Issue: Port 8000 Already in Use
```bash
# Kill existing process
lsof -i :8000
kill -9 <PID>

# Or change port in backend/main.py
# Change: app.run(port=8000)
# To: app.run(port=8001)
```

### Issue: Virtual Environment Not Activated
```bash
# Make sure to activate venv first
source venv/bin/activate

# Check activation (should show (venv) in prompt)
which python
```

---

## 📞 Support & Documentation

- **Complete Guide**: See [README_EN.md](README_EN.md)
- **Deployment Guide**: See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **API Documentation**: Visit `http://localhost:8000/docs` when server is running
- **Issues**: Create GitHub Issues for bug reports

---

## 🎉 You're Ready!

You now have a fully functional AI-powered paper evaluation system. Start uploading papers and analyzing them with Claude's advanced capabilities!

**Happy analyzing!** 📄✨
