"""PDF文档解析模块"""
import pdfplumber
import re
from typing import List, Dict, Optional


class PDFParser:
    """PDF解析器"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.content = None
        self.metadata = {}
        
    def extract_text(self) -> str:
        """提取PDF全文"""
        text = ""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                self.metadata = pdf.metadata
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            raise Exception(f"PDF解析失败: {str(e)}")
        
        self.content = text
        return text
    
    def extract_structure(self) -> Dict:
        """提取文档结构（标题、章节等）"""
        if not self.content:
            self.extract_text()
        
        structure = {
            "title": self._extract_title(),
            "chapters": self._extract_chapters(),
            "tables_of_content": self._extract_toc(),
            "metadata": self.metadata
        }
        return structure
    
    def extract_figures_and_tables(self) -> Dict:
        """提取图表信息"""
        if not self.content:
            self.extract_text()
        
        figures = re.findall(r"(?:图|Figure|Fig\.)\s*[:：]?\s*([^\n]+)", self.content)
        tables = re.findall(r"(?:表|Table|Tab\.)\s*[:：]?\s*([^\n]+)", self.content)
        
        return {
            "figures": figures,
            "tables": tables,
            "total_figures": len(figures),
            "total_tables": len(tables)
        }
    
    def _extract_title(self) -> Optional[str]:
        """提取标题"""
        lines = self.content.split('\n')
        # 假设标题在前10行中，最长的一般是标题
        candidates = [l.strip() for l in lines[:10] if l.strip()]
        if candidates:
            return max(candidates, key=len)
        return None
    
    def _extract_chapters(self) -> List[str]:
        """提取章节标题"""
        # 匹配常见的章节格式：第X章、Chapter X、1. 等
        pattern = r"^(?:第[一二三四五六七八九十0-9]+章|Chapter\s+\d+|\d+\.|##\s+)(.+)$"
        chapters = []
        for line in self.content.split('\n'):
            if re.match(pattern, line.strip()):
                chapters.append(line.strip())
        return chapters
    
    def _extract_toc(self) -> List[str]:
        """提取目录"""
        lines = self.content.split('\n')
        toc = []
        in_toc = False
        
        for line in lines[:50]:  # 通常目录在前50行
            line = line.strip()
            if '目录' in line or 'Content' in line or 'TABLE OF CONTENT' in line:
                in_toc = True
            elif in_toc and line and not line.isdigit():
                toc.append(line)
            elif in_toc and (line.startswith("1.") or line.startswith("第一")):
                break
        
        return toc


def parse_pdf(pdf_path: str) -> Dict:
    """便捷函数：解析PDF"""
    parser = PDFParser(pdf_path)
    text = parser.extract_text()
    
    return {
        "text": text,
        "structure": parser.extract_structure(),
        "figures_tables": parser.extract_figures_and_tables(),
        "page_count": len(text.split('\n\n'))  # 粗略估算
    }
