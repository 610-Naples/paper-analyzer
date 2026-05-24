"""评分标准（Rubric）系统"""
import json
from typing import Dict, List
from pathlib import Path


class RubricEvaluator:
    """论文评分系统"""
    
    def __init__(self, rubric_name: str = "default"):
        self.rubric_name = rubric_name
        self.rubric = self._load_rubric()
    
    def _load_rubric(self) -> Dict:
        """加载评分标准"""
        # 默认评分标准（教学论/数学教育专业）
        if self.rubric_name == "default":
            return self.get_default_rubric()
        
        # 尝试从文件加载自定义标准
        rubric_path = Path(f"data/rubrics/{self.rubric_name}.json")
        if rubric_path.exists():
            with open(rubric_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return self.get_default_rubric()
    
    @staticmethod
    def get_default_rubric() -> Dict:
        """数学教育/教学论论文默认评分标准"""
        return {
            "format": {
                "name": "格式规范",
                "weight": 0.10,
                "max_score": 10,
                "criteria": [
                    "页面设置（页边距、行距、字体）",
                    "目录完整性",
                    "页码格式",
                    "参考文献格式统一"
                ]
            },
            "structure": {
                "name": "结构完整性",
                "weight": 0.15,
                "max_score": 15,
                "criteria": [
                    "引言充分阐述研究背景",
                    "文献综述全面系统",
                    "研究方法清晰明确",
                    "结论总结有力",
                    "图表配置合理"
                ]
            },
            "theory": {
                "name": "理论基础",
                "weight": 0.25,
                "max_score": 25,
                "criteria": [
                    "理论框架完善",
                    "关键概念界定清晰",
                    "理论与实践的结合",
                    "引用权威文献",
                    "理论创新性"
                ]
            },
            "methodology": {
                "name": "方法论",
                "weight": 0.25,
                "max_score": 25,
                "criteria": [
                    "研究方法适当",
                    "样本选取科学",
                    "数据收集方法可行",
                    "统计分析正确",
                    "研究设计严谨"
                ]
            },
            "innovation": {
                "name": "创新性与应用",
                "weight": 0.15,
                "max_score": 15,
                "criteria": [
                    "研究的新颖性",
                    "对教学实践的指导意义",
                    "发现问题的深度",
                    "解决方案的可行性",
                    "实际应用价值"
                ]
            },
            "writing": {
                "name": "学术写作",
                "weight": 0.10,
                "max_score": 10,
                "criteria": [
                    "表述清晰严谨",
                    "逻辑连贯",
                    "术语使用规范",
                    "英文摘要质量"
                ]
            }
        }
    
    def score_section(self, section_name: str, analysis_result: Dict) -> Dict:
        """对一个评分维度打分"""
        if section_name not in self.rubric:
            return {"error": f"未知评分维度: {section_name}"}
        
        section = self.rubric[section_name]
        
        # 这里应该由LLM分析analysis_result来打分
        # 现阶段返回空分数，由后续LLM模块填充
        score = {
            "section": section_name,
            "name": section["name"],
            "max_score": section["max_score"],
            "weight": section["weight"],
            "actual_score": 0,  # 由LLM分析填充
            "feedback": "",  # 由LLM分析填充
            "criteria_scores": {
                criterion: 0 for criterion in section["criteria"]
            }
        }
        return score
    
    def calculate_total_score(self, section_scores: List[Dict]) -> Dict:
        """计算总分"""
        total_weighted_score = 0
        total_weight = 0
        
        for section_score in section_scores:
            if "actual_score" in section_score:
                weight = section_score.get("weight", 0)
                score = section_score.get("actual_score", 0)
                total_weighted_score += score * weight
                total_weight += weight
        
        final_score = total_weighted_score / total_weight if total_weight > 0 else 0
        
        return {
            "final_score": round(final_score, 2),
            "max_score": 100,
            "grade": self._get_grade(final_score)
        }
    
    @staticmethod
    def _get_grade(score: float) -> str:
        """根据分数返回等级"""
        if score >= 90:
            return "优秀 (A)"
        elif score >= 80:
            return "良好 (B)"
        elif score >= 70:
            return "中等 (C)"
        elif score >= 60:
            return "及格 (D)"
        else:
            return "不及格 (F)"


def create_rubric_config(name: str, criteria: Dict) -> None:
    """创建自定义评分标准"""
    rubric_path = Path(f"data/rubrics/{name}.json")
    rubric_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(rubric_path, 'w', encoding='utf-8') as f:
        json.dump(criteria, f, ensure_ascii=False, indent=2)
