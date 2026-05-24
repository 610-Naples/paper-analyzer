"""文本分块模块"""
from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """文本分块处理"""
    
    def __init__(self, chunk_size: int = 2000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", "！", "？", ",", "，", " ", ""]
        )
    
    def chunk_text(self, text: str) -> List[Dict]:
        """将文本分块"""
        chunks = self.splitter.split_text(text)
        
        # 返回带有元数据的分块
        return [
            {
                "index": i,
                "text": chunk,
                "length": len(chunk),
                "tokens_estimate": len(chunk) // 4  # 粗略估算
            }
            for i, chunk in enumerate(chunks)
        ]
    
    def chunk_by_section(self, text: str, sections: List[str]) -> Dict[str, List[Dict]]:
        """按章节分块"""
        chunked_sections = {}
        
        for section in sections:
            # 简化：按章节名称分割（实际应更精确）
            parts = text.split(section)
            if len(parts) > 1:
                section_text = parts[1].split('\n')[0:500]  # 限制长度
                section_text = '\n'.join(section_text)
                chunked_sections[section] = self.chunk_text(section_text)
        
        return chunked_sections


def chunk_paper(text: str, chunk_size: int = 2000, chunk_overlap: int = 200) -> List[Dict]:
    """便捷函数：分块论文"""
    chunker = TextChunker(chunk_size, chunk_overlap)
    return chunker.chunk_text(text)
