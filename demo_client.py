#!/usr/bin/env python3
"""
The Python client example of the intelligent paper evaluation system uses this script to test the API functionality or as an integration example
"""

import requests
import json
import sys
from pathlib import Path
from typing import Dict, Optional


class PaperAnalyzerClient:
   
    
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url
        self.session = requests.Session()
    
    def health_check(self) -> Dict:
    
        try:
            response = self.session.get(f"{self.api_url}/health")
            return response.json()
        except Exception as e:
            return {"error": str(e), "status": "unreachable"}
    
    def get_rubrics(self) -> Dict:
 
        response = self.session.get(f"{self.api_url}/rubrics")
        return response.json()
    
    def upload_paper(self, pdf_path: str) -> Dict:
    
        if not Path(pdf_path).exists():
            return {"error": f"file don't exist: {pdf_path}"}
        
        if not pdf_path.endswith('.pdf'):
            return {"error": "only allowed PDF version"}
        
        try:
            with open(pdf_path, 'rb') as f:
                files = {'file': f}
                response = self.session.post(
                    f"{self.api_url}/upload",
                    files=files,
                    timeout=300  
                )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"API error {response.status_code}",
                    "details": response.text
                }
        
        except Exception as e:
            return {"error": f"upload failed: {str(e)}"}
    
    def print_analysis_results(self, result: Dict) -> None:
      
        if "error" in result:
            print(f" error: {result['error']}")
            return
        
        print("\n" + "="*60)
        print("📄 paper analysis result")
        print("="*60)
        
   
        if "paper_info" in result:
            info = result["paper_info"]
            print("\n📋 basic info")
            print(f"  title：{info.get('title', 'N/A')}")
            print(f"  chapter：{info['chapters']} 个")
            print(f"  figure：{info['figures']} 个")
            print(f"  table：{info['tables']} 个")
            print(f"  time：{info.get('estimated_length', 0)//300} words")
        
   
        analysis = result.get("analysis", {})
        if "overall_score" in analysis:
            score = analysis["overall_score"]
            print("\n⭐ overall score")
            print(f"  score：{score.get('final_score', 'N/A')}/100")
            print(f"  rank：{score.get('grade', 'N/A')}")
        

        if "rubric_scores" in analysis:
            print("\n📊every dimension: ")
            for score in analysis["rubric_scores"]:
                if score.get('section') != 'final_score':
                    actual = score.get('actual_score', 0)
                    max_s = score.get('max_score', 0)
                    name = score.get('name', 'unknown')
                    weight = score.get('weight', 0)
                    mark = "✓" if actual >= max_s * 0.8 else "△" if actual >= max_s * 0.6 else "✗"
                    print(f"  {mark} {name:12} {actual:5.1f}/{max_s:5.1f} (weight{weight*100:3.0f}%)")
        
   
        if "format_check" in analysis:
            fmt = analysis["format_check"]
            print("\n✅ template check")
            print(f"  content integrity：{'yes' if fmt.get('toc_present') else 'no'}")
            if fmt.get("issues"):
                print(f"  question：{', '.join(fmt['issues'])}")
            else:
                print("  question：no")
        
     
        if "figures_tables" in analysis:
            ft = analysis["figures_tables"]
            print("\n📈 figure evaluate")
            print(f"  figure number：{ft['figure_count']}")
            print(f"  table number：{ft['table_count']}")
            if ft.get("recommendations"):
                print("  advice：")
                for rec in ft["recommendations"][:3]:
                    if rec.strip():
                        print(f"    • {rec.strip()}")
        

        if "professional_feedback" in analysis:
            feedback = analysis["professional_feedback"]
            print("\n💡 suggestion by supervisor")
        
            if len(feedback) > 300:
                print(f"  {feedback[:300]}...")
            else:
                print(f"  {feedback}")
        
        print("\n" + "="*60 + "\n")


def main():
   
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Intelligent Evaluation System for Papers - Command-line Client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
example：
  # check api status
  python3 demo_client.py --health
  
  # get scoring standard
  python3 demo_client.py --rubrics
  
  # analyse paper
  python3 demo_client.py --analyze paper.pdf
  
  # output JSON format
  python3 demo_client.py --analyze paper.pdf --json
        """
    )
    
    parser.add_argument('--health', action='store_true', help='check api status')
    parser.add_argument('--rubrics', action='store_true', help='get scoring standard')
    parser.add_argument('--analyze', metavar='PDF_PATH', help='analyse paper in PDF version')
    parser.add_argument('--json', action='store_true', help='output JSON format')
    parser.add_argument('--url', default='http://localhost:8000', help='API addresss (default 8000 port)')
    
    args = parser.parse_args()
    
   
    if not any([args.health, args.rubrics, args.analyze]):
        parser.print_help()
        return
    
    client = PaperAnalyzerClient(args.url)
    
 
    if args.health:
        print("\n🔍 check API healthy status...")
        health = client.health_check()
        
        if "error" in health:
            print(f" API cannot connect: {health['error']}")
            print(f"   Please ensure that the service is running: python -m uvicorn backend.main:app --reload")
            sys.exit(1)
        else:
            status = health.get('status')
            print(f"✓ server status: {status}")
            if health.get('api_key_configured'):
                print("✓ API Key already settled")
            else:
                print("⚠ API Key havn't be done，please refresh.env file")
    

    elif args.rubrics:
        print("\n📖 get marketing rubric...")
        rubrics = client.get_rubrics()
        
        if args.json:
            print(json.dumps(rubrics, ensure_ascii=False, indent=2))
        else:
            print("\n Available scoring criteria:")
            for name, section in rubrics.get("default_rubric", {}).items():
                print(f"\n  {section['name']} (weight: {section['weight']*100:.0f}%)")
                for criterion in section['criteria'][:2]:
                    print(f"    • {criterion}")
                if len(section['criteria']) > 2:
                    print(f"    • ... and {len(section['criteria'])-2} item")
    

    elif args.analyze:
        print(f"\nupload paper: {args.analyze}")
        print("It is being analyzed (which may take 1-2 minutes）...")
        
        result = client.upload_paper(args.analyze)
        
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            client.print_analysis_results(result)


if __name__ == "__main__":
    main()
