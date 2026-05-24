"""FastAPI主应用"""
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pathlib import Path

from .config import config
from .pdf_parser import parse_pdf
from .chunking import chunk_paper
from .analyzer import PaperAnalyzer
from .rubric import RubricEvaluator

# 初始化FastAPI应用
app = FastAPI(title="论文智能评估系统", version="0.1.0")

# CORS配置（允许前端跨域请求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建必要的目录
Path(config.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
Path(config.RUBRIC_DIR).mkdir(parents=True, exist_ok=True)

# 初始化分析引擎
analyzer = PaperAnalyzer(config.ANTHROPIC_API_KEY)
rubric_evaluator = RubricEvaluator()


@app.get("/")
async def root():
    """API根路由"""
    return {
        "name": "论文智能评估系统",
        "version": "0.1.0",
        "endpoints": {
            "上传论文": "POST /upload",
            "获取支持的评分标准": "GET /rubrics",
            "检查API状态": "GET /health"
        }
    }


@app.get("/health")
async def health_check():
    """检查API和Claude连接状态"""
    api_key_present = bool(config.ANTHROPIC_API_KEY)
    
    return {
        "status": "healthy" if api_key_present else "error",
        "api_key_configured": api_key_present,
        "message": "服务正常运行" if api_key_present else "缺少ANTHROPIC_API_KEY"
    }


@app.get("/rubrics")
async def list_rubrics():
    """获取可用的评分标准"""
    default_rubric = rubric_evaluator.get_default_rubric()
    
    return {
        "available_rubrics": ["default"],
        "default_rubric": {
            name: {
                "name": data["name"],
                "weight": data["weight"],
                "max_score": data["max_score"],
                "criteria": data["criteria"]
            }
            for name, data in default_rubric.items()
        }
    }


@app.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    """上传并分析论文"""
    
    # 验证文件格式
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="只支持PDF格式文件")
    
    # 验证文件大小
    contents = await file.read()
    if len(contents) > config.MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="文件过大（最大50MB）")
    
    try:
        # 保存临时文件
        upload_path = Path(config.UPLOAD_DIR) / file.filename
        with open(upload_path, 'wb') as f:
            f.write(contents)
        
        # 解析PDF
        paper_data = parse_pdf(str(upload_path))
        
        # 分块处理
        chunks = chunk_paper(paper_data["text"])
        
        # LLM分析
        analysis_results = analyzer.analyze_paper(paper_data)
        
        # 构建响应
        response = {
            "filename": file.filename,
            "upload_status": "success",
            "paper_info": {
                "title": paper_data["structure"].get("title"),
                "chapters": len(paper_data["structure"].get("chapters", [])),
                "figures": paper_data["figures_tables"]["total_figures"],
                "tables": paper_data["figures_tables"]["total_tables"],
                "estimated_length": len(paper_data["text"]),
                "chunks": len(chunks)
            },
            "analysis": {
                "format_check": analysis_results["format_check"],
                "content_analysis": analysis_results["content_analysis"],
                "figures_tables": analysis_results["figures_tables_evaluation"],
                "rubric_scores": analysis_results["academic_rubric_scores"][:-1],  # 排除总分
                "overall_score": analysis_results["academic_rubric_scores"][-1],  # 总分
                "similarity_check": analysis_results["similarity_report"],
                "professional_feedback": analysis_results["professional_feedback"]
            }
        }
        
        # 删除临时文件
        os.remove(upload_path)
        
        return JSONResponse(content=response, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"处理失败: {str(e)}")


@app.post("/generate-report")
async def generate_report(analysis_data: dict):
    """生成Word/PDF报告（后续实现）"""
    # TODO: 集成python-docx生成Word报告
    return {
        "status": "coming_soon",
        "message": "报告生成功能开发中..."
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)
