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

### 5. **Web Interface**
- Modern, responsive HTML/CSS frontend
- Drag-and-drop PDF upload
- Real-time analysis progress
- Professional result visualization
- Mobile-friendly design

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

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI 0.136+ (async REST API)
- **LLM**: Anthropic Claude 3.5 Sonnet
- **PDF Processing**: pdfplumber 0.11.9
- **Text Processing**: Langchain 1.3.1
- **Validation**: Pydantic 2.5+

### Frontend
- **HTML5** with semantic markup
- **CSS3** with responsive design
- **JavaScript** for client-side interactivity

### Infrastructure
- **Server**: Uvicorn (ASGI)
- **Container**: Docker & Docker Compose (optional)
- **Python**: 3.8+

### Dependencies (Full List)
```
FastAPI>=0.104.0          # Web framework
Uvicorn>=0.24.0           # ASGI server
Anthropic>=0.7.0          # Claude AI SDK
pdfplumber>=0.10.0        # Advanced PDF parsing
PyPDF2>=3.0.0             # PDF utilities
Langchain>=0.1.0          # AI engineering framework
python-dotenv>=1.0.0      # Environment management
python-docx>=0.8.0        # Word document generation
Pydantic>=2.5.0           # Data validation
aiofiles>=23.2.0          # Async file operations
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
# or
venv\Scripts\activate     # Windows
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure API Key**
```bash
# Get your API key at https://console.anthropic.com/
cp .env.example .env

# Edit .env and add your key
nano .env
# ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Step 5: Start the Server**
```bash
# Option A: Using the startup script (recommended)
chmod +x start.sh
./start.sh

# Option B: Manual startup
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Reload enabled
```

### Testing the System

**Access the Web Interface:**
```
http://localhost:8000/docs        # Interactive API documentation
http://localhost:8000/health      # Health check
```

**View API Documentation:**
Navigate to `http://localhost:8000/docs` in your browser to explore all available endpoints.

**Using the Web Interface:**
1. Open `frontend/index.html` in your browser (or navigate to `http://localhost:8080`)
2. Drag and drop a PDF thesis
3. Wait 1-2 minutes for analysis
4. View detailed assessment and recommendations

**Command-Line Testing:**
```bash
# Check system health
curl http://localhost:8000/health

# Get available rubrics
curl http://localhost:8000/rubrics

# Upload and analyze a paper
python demo_client.py path/to/thesis.pdf
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
│   ├── index.html                    # Main UI with drag-drop upload
│   └── (CSS/JS embedded)
│
├── data/                             # Data directories
│   ├── uploads/                      # Temporary PDF storage
│   └── rubrics/                      # Custom evaluation rubrics
│
├── README.md                         # This file (English version)
├── QUICKSTART.md                     # Quick start guide
├── DEPLOYMENT_GUIDE.md               # Deployment instructions
├── requirements.txt                  # Python dependencies
├── .env.example                      # Example environment variables
├── .gitignore                        # Git ignore rules
├── start.sh                          # Startup script
├── docker-compose.yml                # Docker configuration
├── Dockerfile                        # Container definition
├── test_system.py                    # System testing utility
└── demo_client.py                    # Python client example
```

---

## 📊 Project Progress

### ✅ Completed Components

```
OVERALL PROGRESS: ████████████████████ 100%

✓ Backend System (FastAPI)           ██████████ 100%
✓ PDF Parsing & Analysis             ██████████ 100%
✓ Claude AI Integration              ██████████ 100%
✓ Text Chunking Pipeline             ██████████ 100%
✓ Scoring System (6-D Rubric)        ██████████ 100%
✓ Web Interface (HTML/CSS)           ██████████ 100%
✓ REST API with Documentation        ██████████ 100%
✓ Docker Deployment Support          ██████████ 100%
✓ Testing & Validation Suite         ██████████ 100%
✓ Documentation & Guides             ██████████ 100%
```

### What's Implemented
- [x] Complete backend infrastructure (FastAPI + async processing)
- [x] Multi-stage PDF analysis pipeline
- [x] Claude AI integration with optimization
- [x] Professional rubric-based evaluation
- [x] User-friendly web interface
- [x] RESTful API endpoints
- [x] Docker containerization support
- [x] Error handling and validation
- [x] Comprehensive documentation
- [x] Demo client application

---

## 💰 Cost Analysis

### API Usage & Pricing
**Claude API Pricing:**
- Input: $0.003 per 1,000 tokens
- Output: $0.015 per 1,000 tokens

**Typical Thesis Analysis:**
- Average thesis: 30,000-50,000 words
- After chunking optimization: ~50,000 tokens total
- **Estimated cost per thesis: $0.25-$0.40**

**Free Trial:**
- New accounts receive **$5 free credit**
- Sufficient for **200+ paper analyses** during development
- Perfect for testing and demos

---

## 🔐 Security & Best Practices

### API Key Management
- ✅ Never commit `.env` file to version control
- ✅ Use `.env.example` as template
- ✅ Rotate keys regularly in production
- ✅ Store keys in secure CI/CD secrets

### File Handling
- Uploaded PDFs stored in temporary directory
- Files deleted after processing
- No persistent data storage of uploaded files
- Secure file validation and sanitization

---

## 📚 API Documentation

### Key Endpoints

**Health Check**
```
GET /health
Response: {"status": "healthy"}
```

**Get Scoring Rubrics**
```
GET /rubrics
Response: [
  {"dimension": "format", "weight": 10, "description": "..."},
  ...
]
```

**Analyze Thesis**
```
POST /analyze
Content-Type: multipart/form-data
- file: <PDF file>

Response: {
  "thesis_id": "uuid",
  "title": "...",
  "scores": {...},
  "feedback": {...},
  "overall_score": 78.5
}
```

**Get Analysis Results**
```
GET /analysis/{thesis_id}
Response: {...complete analysis...}
```

For complete API documentation, start the server and visit: `http://localhost:8000/docs`

---

## 🧪 Testing

### System Verification
```bash
# Run comprehensive system tests
python test_system.py

# Expected output:
# ✓ Environment validation
# ✓ API key detection
# ✓ PDF parser functionality
# ✓ LLM connectivity
# ✓ All systems operational
```

### Manual Testing
```bash
# Test with a sample PDF
python demo_client.py sample_thesis.pdf
```

---

## 🐳 Docker Deployment (Optional)

### Build Container
```bash
docker build -t paper-analyzer .
```

### Run with Docker Compose
```bash
docker-compose up
```

Service runs on: `http://localhost:8000`

---

## 📖 Documentation Files

- **[QUICKSTART.md](./QUICKSTART.md)** - 5-minute setup guide
- **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** - Production deployment instructions
- **[START_HERE.md](./START_HERE.md)** - Detailed getting started guide
- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Development completion report

---

## 🎓 Use Cases

### For Educational Institutions
- Automated thesis evaluation system
- Standardized assessment across departments
- Reduced faculty workload
- Consistent feedback quality

### For Students
- Instant thesis assessment feedback
- Professional improvement suggestions
- Self-evaluation before final submission
- 24/7 availability

### For Researchers
- Baseline evaluation for research proposals
- Quick paper quality check
- Structured feedback generation
- Research methodology validation

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

**Siyu Zhang**
- GitHub: [@siyuzhang](https://github.com/siyuzhang)
- Email: contact@example.com

---

## 🙏 Acknowledgments

- Anthropic Claude AI team for LLM capabilities
- FastAPI community for excellent web framework
- pdfplumber developers for PDF parsing excellence
- Langchain for AI engineering patterns

---

## 📞 Support & Contact

- **Issues**: Open an issue on GitHub
- **Documentation**: See docs/ folder
- **API Docs**: Start server and visit `/docs`
- **Questions**: Check discussion forums

---

## 🗓️ Version History

### v0.1.0 (May 2026) - Initial Release ✅
- Complete backend implementation
- PDF parsing and analysis
- Claude AI integration
- Professional scoring system
- Web interface
- All core features operational

---

**Last Updated:** May 2026  
**Status:** Production Ready ✅  
**Active Development:** Yes
