"""
AI Risk Assessment Tool - Main Assessment Engine
Integrates ISO/IEC 42001 controls, AI system classification, and risk scoring
"""

from typing import Dict, List, Optional
from datetime import datetime
import json

from iso_42001_controls import (
    get_all_controls,
    get_controls_by_category,
    get_control_categories
)
from ai_system_classifier import AISystemClassifier, AISystemType
from risk_scoring import RiskScoringEngine, RiskScore
from report_generator import ReportGenerator


class AIRiskAssessment:
    """Main AI risk assessment engine"""
    
    def __init__(self):
        self.classifier = AISystemClassifier()
        self.risk_engine = RiskScoringEngine()
        self.report_generator = ReportGenerator()
        self.assessment_results = {}
    
    def conduct_assessment(
        self,
        system_name: str,
        system_description: str,
        system_features: Dict,
        implemented_controls: List[str],
        assessment_metadata: Optional[Dict] = None
    ) -> Dict:
        """
        Conduct comprehensive AI risk assessment
        
        Args:
            system_name: Name of the AI system
            system_description: Description of the AI system
            system_features: Dictionary of system features
            implemented_controls: List of implemented control IDs
            assessment_metadata: Optional metadata about the assessment
        
        Returns:
            Dictionary with complete assessment results
        """
        # Step 1: Classify the AI system
        classification = self.classifier.classify_system(
            system_description,
            system_features
        )
        
        # Step 2: Determine required controls
        system_type = AISystemType(classification["system_type"])
        required_control_categories = self.classifier.get_control_requirements(system_type)
        required_controls = self._get_controls_for_categories(required_control_categories)
        
        # Step 3: Calculate control coverage
        control_coverage = self.risk_engine.calculate_control_coverage(
            implemented_controls,
            required_controls
        )
        
        # Step 4: Identify compliance gaps
        compliance_gaps = self._identify_compliance_gaps(
            implemented_controls,
            required_controls
        )
        
        # Step 5: Calculate composite risk factor
        composite_risk_factor = self.classifier.calculate_composite_risk_factor(
            system_type,
            system_features
        )
        
        # Step 6: Assess additional risk factors
        additional_risks = self.classifier.assess_additional_risk_factors(system_features)
        
        # Step 7: Calculate overall risk score
        risk_score = self.risk_engine.calculate_risk_score(
            control_coverage,
            composite_risk_factor,
            compliance_gaps,
            additional_risks
        )
        
        # Step 8: Compile assessment results
        assessment = {
            "system_name": system_name,
            "system_description": system_description,
            "assessment_date": datetime.now().isoformat(),
            "metadata": assessment_metadata or {},
            
            # Classification results
            "classification": classification,
            "composite_risk_factor": composite_risk_factor,
            
            # Control assessment
            "required_controls": required_controls,
            "implemented_controls": implemented_controls,
            "control_coverage": control_coverage,
            "compliance_gaps": compliance_gaps,
            
            # Risk assessment
            "risk_score": risk_score.score,
            "severity": risk_score.severity.value,
            "risk_description": risk_score.description,
            "risk_color": risk_score.color,
            "risk_factors": risk_score.factors,
            "recommendations": risk_score.recommendations,
            
            # Additional risk factors
            "additional_risk_factors": additional_risks
        }
        
        return assessment
    
    def _get_controls_for_categories(self, categories: List[str]) -> List[str]:
        """
        Get control IDs for specified categories
        
        Args:
            categories: List of control category names
        
        Returns:
            List of control IDs
        """
        if "all" in categories:
            return list(get_all_controls().keys())
        
        control_ids = []
        for category in categories:
            category_controls = get_controls_by_category(category)
            control_ids.extend(category_controls.keys())
        
        return control_ids
    
    def _identify_compliance_gaps(
        self,
        implemented_controls: List[str],
        required_controls: List[str]
    ) -> List[str]:
        """
        Identify compliance gaps between required and implemented controls
        
        Args:
            implemented_controls: List of implemented control IDs
            required_controls: List of required control IDs
        
        Returns:
            List of missing control IDs with descriptions
        """
        implemented_set = set(implemented_controls)
        required_set = set(required_controls)
        
        missing_controls = required_set - implemented_set
        all_controls = get_all_controls()
        
        gaps = []
        for control_id in missing_controls:
            control = all_controls.get(control_id)
            if control:
                gaps.append(f"{control_id}: {control.title}")
        
        return gaps
    
    def generate_assessment_summary(self, assessment: Dict) -> str:
        """
        Generate executive summary of assessment results
        
        Args:
            assessment: Assessment results dictionary
        
        Returns:
            Executive summary text
        """
        summary = f"""
AI Risk Assessment Executive Summary
=====================================

System: {assessment['system_name']}
Assessment Date: {assessment['assessment_date']}

CLASSIFICATION
--------------
System Type: {assessment['classification']['system_name']}
Risk Factor: {assessment['composite_risk_factor']}
Confidence: {assessment['classification']['classification_confidence']:.0%}

COMPLIANCE STATUS
----------------
Control Coverage: {assessment['control_coverage']}%
Required Controls: {len(assessment['required_controls'])}
Implemented Controls: {len(assessment['implemented_controls'])}
Compliance Gaps: {len(assessment['compliance_gaps'])}

RISK ASSESSMENT
---------------
Overall Risk Score: {assessment['risk_score']}
Severity Level: {assessment['severity']}
Risk Description: {assessment['risk_description']}

KEY RISK FACTORS
--------------
"""
        for factor in assessment['risk_factors']:
            summary += f"- {factor}\n"
        
        summary += "\nRECOMMENDATIONS\n---------------\n"
        for recommendation in assessment['recommendations']:
            summary += f"- {recommendation}\n"
        
        return summary
    
    def batch_assessment(
        self,
        systems: List[Dict]
    ) -> List[Dict]:
        """
        Conduct risk assessment for multiple AI systems
        
        Args:
            systems: List of system dictionaries with assessment parameters
        
        Returns:
            List of assessment results
        """
        results = []
        for system in systems:
            assessment = self.conduct_assessment(
                system_name=system.get("name"),
                system_description=system.get("description"),
                system_features=system.get("features", {}),
                implemented_controls=system.get("implemented_controls", []),
                assessment_metadata=system.get("metadata", {})
            )
            results.append(assessment)
        
        return results
    
    def export_to_json(self, assessment: Dict, filename: str) -> None:
        """
        Export assessment results to JSON file
        
        Args:
            assessment: Assessment results dictionary
            filename: Output filename
        """
        with open(filename, 'w') as f:
            json.dump(assessment, f, indent=2, default=str)
    
    def generate_excel_report(self, assessment: Dict, filename: str) -> None:
        """
        Generate Excel report from assessment results
        
        Args:
            assessment: Assessment results dictionary
            filename: Output filename
        """
        self.report_generator.generate_report(assessment, filename)
    
    def get_assessment_statistics(self, assessments: List[Dict]) -> Dict:
        """
        Calculate statistics across multiple assessments
        
        Args:
            assessments: List of assessment results
        
        Returns:
            Dictionary with assessment statistics
        """
        if not assessments:
            return {}
        
        total_systems = len(assessments)
        high_risk_count = sum(1 for a in assessments if a['severity'] in ['CRITICAL', 'HIGH'])
        medium_risk_count = sum(1 for a in assessments if a['severity'] == 'MEDIUM')
        low_risk_count = sum(1 for a in assessments if a['severity'] == 'LOW')
        
        avg_control_coverage = sum(a['control_coverage'] for a in assessments) / total_systems
        avg_risk_score = sum(a['risk_score'] for a in assessments) / total_systems
        
        return {
            "total_systems": total_systems,
            "high_risk_count": high_risk_count,
            "medium_risk_count": medium_risk_count,
            "low_risk_count": low_risk_count,
            "average_control_coverage": round(avg_control_coverage, 1),
            "average_risk_score": round(avg_risk_score, 1),
            "risk_distribution": {
                "CRITICAL": sum(1 for a in assessments if a['severity'] == 'CRITICAL'),
                "HIGH": sum(1 for a in assessments if a['severity'] == 'HIGH'),
                "MEDIUM": sum(1 for a in assessments if a['severity'] == 'MEDIUM'),
                "LOW": sum(1 for a in assessments if a['severity'] == 'LOW')
            }
        }


# Example usage and testing
if __name__ == "__main__":
    try:
        assessor = AIRiskAssessment()
        
        # Test single assessment
        test_system = {
            "name": "Customer Service Chatbot",
            "description": "A generative AI chatbot that handles customer service inquiries and provides product recommendations",
            "features": {
                "personal_data": True,
                "high_user_impact": True,
                "regulated_industry": False,
                "fully_autonomous": False,
                "human_in_loop": True
            },
            "implemented_controls": [
                "AI_GOV_001",  # AI Governance Policy
                "AI_ORG_002",  # AI Roles and Responsibilities
                "AI_PLAN_001",  # AI Risk Assessment
                "AI_OPS_002",  # AI Monitoring
                "AI_RISK_003"   # AI Risk Treatment Planning
            ],
            "metadata": {
                "assessor": "Terence Webster",
                "department": "IT Security"
            }
        }
        
        assessment = assessor.conduct_assessment(
            system_name=test_system["name"],
            system_description=test_system["description"],
            system_features=test_system["features"],
            implemented_controls=test_system["implemented_controls"],
            assessment_metadata=test_system["metadata"]
        )
        
        print("=" * 60)
        print("AI RISK ASSESSMENT RESULT")
        print("=" * 60)
        print(assessor.generate_assessment_summary(assessment))
        
        # Export to JSON
        assessor.export_to_json(assessment, "assessment_result.json")
        print("\nAssessment exported to assessment_result.json")
        
        # Generate Excel report
        assessor.generate_excel_report(assessment, "ai_risk_assessment_report.xlsx")
        print("Excel report generated: ai_risk_assessment_report.xlsx")
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install openpyxl")