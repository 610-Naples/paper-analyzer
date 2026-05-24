"""LLM分析引擎 - Claude集成"""
import json
from typing import Dict, List, Optional
from anthropic import Anthropic
from .rubric import RubricEvaluator


class PaperAnalyzer:
    """论文分析引擎"""
    
    def __init__(self, api_key: str):
        self.client = Anthropic()
        self.rubric_evaluator = RubricEvaluator()
        self.conversation_history = []
    
    def analyze_paper(self, paper_data: Dict) -> Dict:
        """综合分析论文"""
        text = paper_data.get("text", "")
        structure = paper_data.get("structure", {})
        figures_tables = paper_data.get("figures_tables", {})
        
        results = {
            "format_check": self._check_format(structure),
            "content_analysis": self._analyze_content(text),
            "figures_tables_evaluation": self._evaluate_figures_tables(figures_tables, text),
            "academic_rubric_scores": self._score_by_rubric(text, structure),
            "similarity_report": self._check_similarity(text),
            "professional_feedback": self._generate_feedback(text, structure),
        }
        
        return results
    
    def _check_format(self, structure: Dict) -> Dict:
        """检查格式规范"""
        return {
            "title_present": bool(structure.get("title")),
            "toc_present": bool(structure.get("chapters")),
            "metadata": structure.get("metadata", {}),
            "issues": self._identify_format_issues(structure)
        }
    
    def _analyze_content(self, text: str) -> Dict:
        """LLM内容分析"""
        prompt = f"""请分析这篇论文的内容质量，主要关注以下几个方面：
1. 研究问题的明确性
2. 文献综述的完整性
3. 研究方法的合理性
4. 结论的科学性

论文内容（前2000字）：
{text[:2000]}

请用JSON格式返回分析结果。"""
        
        response = self._call_claude(prompt)
        return {
            "analysis": response,
            "model": "claude-3-haiku"
        }
    
    def _evaluate_figures_tables(self, figures_tables: Dict, text: str) -> Dict:
        """评估图表的适配度"""
        num_figures = figures_tables.get("total_figures", 0)
        num_tables = figures_tables.get("total_tables", 0)
        
        prompt = f"""评估这篇论文的图表合理性：
- 图数量：{num_figures}
- 表数量：{num_tables}
- 文本长度：约{len(text)}字

请评估：
1. 图表数量是否合适
2. 图表标题是否清晰
3. 图表与内容的相关性
4. 缺少哪些关键图表

返回建议清单。"""
        
        response = self._call_claude(prompt)
        return {
            "figure_count": num_figures,
            "table_count": num_tables,
            "evaluation": response,
            "recommendations": self._parse_recommendations(response)
        }
    
    def _score_by_rubric(self, text: str, structure: Dict) -> List[Dict]:
        """按照专业rubric评分"""
        scores = []
        
        for section_name in self.rubric_evaluator.rubric.keys():
            score = self.rubric_evaluator.score_section(section_name, {"text": text})
            
            # 使用LLM对该维度实际打分
            section_score = self._llm_score_section(section_name, text)
            score["actual_score"] = section_score["score"]
            score["feedback"] = section_score["feedback"]
            
            scores.append(score)
        
        # 计算总分
        total = self.rubric_evaluator.calculate_total_score(scores)
        scores.append(total)
        
        return scores
    
    def _llm_score_section(self, section_name: str, text: str) -> Dict:
        """用LLM对评分维度打分"""
        section = self.rubric_evaluator.rubric[section_name]
        max_score = section["max_score"]
        
        prompt = f"""请为这篇论文的"{section['name']}"维度打分（满分{max_score}分）。

评分标准：
{json.dumps(section['criteria'], ensure_ascii=False, indent=2)}

论文关键内容：
{text[:3000]}

请返回：
1. 给出的分数（0-{max_score}）
2. 评分理由（2-3句话）
3. 改进建议"""
        
        response = self._call_claude(prompt)
        
        # 解析LLM响应提取分数和反馈
        score = self._parse_score_from_response(response, max_score)
        
        return {
            "score": score,
            "feedback": response[:200],  # 简化处理
            "raw_response": response
        }
    
    def _check_similarity(self, text: str) -> Dict:
        """检查论文相似度（调用查重API）"""
        # 注：实际应用应接入真实查重服务（如turnitin）
        prompt = f"""分析这段文字的潜在抄袭风险：

{text[:1000]}

请指出：
1. 可能需要进一步检查的地方
2. 引用是否规范
3. 是否存在过度释义的疑虑"""
        
        response = self._call_claude(prompt)
        return {
            "status": "needs_external_check",
            "ai_analysis": response,
            "note": "建议上传到Turnitin或检测系统进一步验证"
        }
    
    def _generate_feedback(self, text: str, structure: Dict) -> str:
        """生成专业反馈"""
        prompt = f"""作为教学论/数学教育的研究指导教授，请为这篇硕士论文提供专业建议：

论文标题：{structure.get('title', '未知')}
章节：{structure.get('chapters', [])[:3]}

内容摘要：
{text[:2000]}

请从以下角度给出建议：
1. 研究问题的学术价值
2. 教学实践的指导意义
3. 主要亮点
4. 需要改进的关键问题
5. 下一步研究方向"""
        
        return self._call_claude(prompt)
    
    def _call_claude(self, prompt: str) -> str:
        """调用Claude API"""
        try:
            self.conversation_history.append({
                "role": "user",
                "content": prompt
            })
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                system="你是一位经验丰富的教学论和数学教育研究的教授。请用中文提供专业、深入的学术分析和建议。",
                messages=self.conversation_history
            )
            
            content = response.content[0].text
            self.conversation_history.append({
                "role": "assistant",
                "content": content
            })
            
            return content
        
        except Exception as e:
            return f"API调用错误: {str(e)}"
    
    @staticmethod
    def _identify_format_issues(structure: Dict) -> List[str]:
        """识别格式问题"""
        issues = []
        if not structure.get("title"):
            issues.append("缺少标题")
        if not structure.get("chapters"):
            issues.append("缺少章节标题")
        return issues
    
    @staticmethod
    def _parse_recommendations(response: str) -> List[str]:
        """解析建议"""
        # 简化处理：将响应按行分割
        return [line.strip() for line in response.split('\n') if line.strip()]
    
    @staticmethod
    def _parse_score_from_response(response: str, max_score: int) -> int:
        """从LLM响应中提取分数"""
        import re
        match = re.search(r'(\d+)\s*分', response)
        if match:
            score = int(match.group(1))
            return min(score, max_score)
        return max_score // 2  # 默认返回中等分
