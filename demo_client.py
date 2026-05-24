#!/usr/bin/env python3
"""
论文智能评估系统 - Python客户端示例

使用这个脚本来测试API功能，或作为集成示例
"""

import requests
import json
import sys
from pathlib import Path
from typing import Dict, Optional


class PaperAnalyzerClient:
    """论文分析API客户端"""
    
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url
        self.session = requests.Session()
    
    def health_check(self) -> Dict:
        """检查API健康状态"""
        try:
            response = self.session.get(f"{self.api_url}/health")
            return response.json()
        except Exception as e:
            return {"error": str(e), "status": "unreachable"}
    
    def get_rubrics(self) -> Dict:
        """获取评分标准"""
        response = self.session.get(f"{self.api_url}/rubrics")
        return response.json()
    
    def upload_paper(self, pdf_path: str) -> Dict:
        """上传并分析论文"""
        if not Path(pdf_path).exists():
            return {"error": f"文件不存在: {pdf_path}"}
        
        if not pdf_path.endswith('.pdf'):
            return {"error": "只支持PDF格式"}
        
        try:
            with open(pdf_path, 'rb') as f:
                files = {'file': f}
                response = self.session.post(
                    f"{self.api_url}/upload",
                    files=files,
                    timeout=300  # 5分钟超时
                )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"API错误 {response.status_code}",
                    "details": response.text
                }
        
        except Exception as e:
            return {"error": f"上传失败: {str(e)}"}
    
    def print_analysis_results(self, result: Dict) -> None:
        """漂亮地打印分析结果"""
        if "error" in result:
            print(f"❌ 错误: {result['error']}")
            return
        
        print("\n" + "="*60)
        print("📄 论文分析结果")
        print("="*60)
        
        # 论文信息
        if "paper_info" in result:
            info = result["paper_info"]
            print("\n📋 基本信息")
            print(f"  标题：{info.get('title', 'N/A')}")
            print(f"  章节：{info['chapters']} 个")
            print(f"  图片：{info['figures']} 个")
            print(f"  表格：{info['tables']} 个")
            print(f"  约长：{info.get('estimated_length', 0)//300} 字")
        
        # 总体评分
        analysis = result.get("analysis", {})
        if "overall_score" in analysis:
            score = analysis["overall_score"]
            print("\n⭐ 总体评分")
            print(f"  分数：{score.get('final_score', 'N/A')}/100")
            print(f"  等级：{score.get('grade', 'N/A')}")
        
        # 各维度评分
        if "rubric_scores" in analysis:
            print("\n📊 各维度评分")
            for score in analysis["rubric_scores"]:
                if score.get('section') != 'final_score':
                    actual = score.get('actual_score', 0)
                    max_s = score.get('max_score', 0)
                    name = score.get('name', '未知')
                    weight = score.get('weight', 0)
                    mark = "✓" if actual >= max_s * 0.8 else "△" if actual >= max_s * 0.6 else "✗"
                    print(f"  {mark} {name:12} {actual:5.1f}/{max_s:5.1f} (权重{weight*100:3.0f}%)")
        
        # 格式检查
        if "format_check" in analysis:
            fmt = analysis["format_check"]
            print("\n✅ 格式检查")
            print(f"  目录完整：{'是' if fmt.get('toc_present') else '否'}")
            if fmt.get("issues"):
                print(f"  问题：{', '.join(fmt['issues'])}")
            else:
                print("  问题：无")
        
        # 图表评估
        if "figures_tables" in analysis:
            ft = analysis["figures_tables"]
            print("\n📈 图表评估")
            print(f"  图数量：{ft['figure_count']}")
            print(f"  表数量：{ft['table_count']}")
            if ft.get("recommendations"):
                print("  建议：")
                for rec in ft["recommendations"][:3]:
                    if rec.strip():
                        print(f"    • {rec.strip()}")
        
        # 专业反馈
        if "professional_feedback" in analysis:
            feedback = analysis["professional_feedback"]
            print("\n💡 专业建议")
            # 截断长反馈
            if len(feedback) > 300:
                print(f"  {feedback[:300]}...")
            else:
                print(f"  {feedback}")
        
        print("\n" + "="*60 + "\n")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="论文智能评估系统 - 命令行客户端",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  # 检查API状态
  python3 demo_client.py --health
  
  # 获取评分标准
  python3 demo_client.py --rubrics
  
  # 分析论文
  python3 demo_client.py --analyze paper.pdf
  
  # 输出JSON格式
  python3 demo_client.py --analyze paper.pdf --json
        """
    )
    
    parser.add_argument('--health', action='store_true', help='检查API健康状态')
    parser.add_argument('--rubrics', action='store_true', help='获取评分标准')
    parser.add_argument('--analyze', metavar='PDF_PATH', help='分析指定PDF论文')
    parser.add_argument('--json', action='store_true', help='输出JSON格式')
    parser.add_argument('--url', default='http://localhost:8000', help='API地址 (默认8000端口)')
    
    args = parser.parse_args()
    
    # 如果没有参数，显示帮助
    if not any([args.health, args.rubrics, args.analyze]):
        parser.print_help()
        return
    
    client = PaperAnalyzerClient(args.url)
    
    # 检查健康状态
    if args.health:
        print("\n🔍 检查API状态...")
        health = client.health_check()
        
        if "error" in health:
            print(f"❌ API无法连接: {health['error']}")
            print(f"   请确保服务运行: python -m uvicorn backend.main:app --reload")
            sys.exit(1)
        else:
            status = health.get('status')
            print(f"✓ 服务状态: {status}")
            if health.get('api_key_configured'):
                print("✓ API Key已配置")
            else:
                print("⚠ API Key未配置，请更新.env文件")
    
    # 获取评分标准
    elif args.rubrics:
        print("\n📖 获取评分标准...")
        rubrics = client.get_rubrics()
        
        if args.json:
            print(json.dumps(rubrics, ensure_ascii=False, indent=2))
        else:
            print("\n可用的评分标准:")
            for name, section in rubrics.get("default_rubric", {}).items():
                print(f"\n  {section['name']} (权重: {section['weight']*100:.0f}%)")
                for criterion in section['criteria'][:2]:
                    print(f"    • {criterion}")
                if len(section['criteria']) > 2:
                    print(f"    • ... 还有 {len(section['criteria'])-2} 项")
    
    # 分析论文
    elif args.analyze:
        print(f"\n📤 上传论文: {args.analyze}")
        print("⏳ 正在分析（可能需要1-2分钟）...")
        
        result = client.upload_paper(args.analyze)
        
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            client.print_analysis_results(result)


if __name__ == "__main__":
    main()
