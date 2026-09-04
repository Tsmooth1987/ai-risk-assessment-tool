"""
Risk Scoring Engine
Calculates severity scores for AI systems based on ISO/IEC 42001 compliance assessment
"""

from enum import Enum
from typing import Dict, List, Tuple
from dataclasses import dataclass


class SeverityLevel(Enum):
    """Severity levels for AI governance risks"""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass
class RiskScore:
    """Risk score data structure"""
    score: float
    severity: SeverityLevel
    color: str
    description: str
    factors: List[str]
    recommendations: List[str]


class RiskScoringEngine:
    """Engine for calculating AI governance risk scores"""
    
    def __init__(self):
        self.severity_thresholds = {
            SeverityLevel.CRITICAL: (90, 100),
            SeverityLevel.HIGH: (70, 89),
            SeverityLevel.MEDIUM: (40, 69),
            SeverityLevel.LOW: (0, 39)
        }
        
        self.severity_colors = {
            SeverityLevel.CRITICAL: "#DC2626",  # Red
            SeverityLevel.HIGH: "#F59E0B",      # Orange
            SeverityLevel.MEDIUM: "#3B82F6",    # Blue
            SeverityLevel.LOW: "#10B981"       # Green
        }
        
        self.severity_descriptions = {
            SeverityLevel.CRITICAL: "Immediate action required",
            SeverityLevel.HIGH: "Action required within 30 days",
            SeverityLevel.MEDIUM: "Action required within 90 days",
            SeverityLevel.LOW: "Monitor and improve"
        }
    
    def calculate_risk_score(
        self,
        control_coverage: float,
        system_risk_factor: float,
        compliance_gaps: List[str],
        additional_factors: Dict
    ) -> RiskScore:
        """
        Calculate overall risk score for an AI system
        
        Args:
            control_coverage: Percentage of ISO/IEC 42001 controls implemented (0-100)
            system_risk_factor: Risk factor from system classification (1.0-3.0)
            compliance_gaps: List of identified compliance gaps
            additional_factors: Dictionary of additional risk factors
        
        Returns:
            RiskScore object with calculated risk assessment
        """
        # Base score calculation
        base_score = self._calculate_base_score(control_coverage, system_risk_factor)
        
        # Adjust for compliance gaps
        gap_penalty = self._calculate_gap_penalty(compliance_gaps)
        
        # Adjust for additional factors
        factor_adjustment = self._calculate_factor_adjustment(additional_factors)
        
        # Calculate final score
        final_score = base_score + gap_penalty + factor_adjustment
        
        # Ensure score is within 0-100 range
        final_score = max(0, min(100, final_score))
        
        # Determine severity level
        severity = self._determine_severity(final_score)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(severity, compliance_gaps)
        
        # Identify key risk factors
        factors = self._identify_risk_factors(
            control_coverage,
            system_risk_factor,
            compliance_gaps,
            additional_factors
        )
        
        return RiskScore(
            score=round(final_score, 1),
            severity=severity,
            color=self.severity_colors[severity],
            description=self.severity_descriptions[severity],
            factors=factors,
            recommendations=recommendations
        )
    
    def _calculate_base_score(self, control_coverage: float, system_risk_factor: float) -> float:
        """
        Calculate base risk score from control coverage and system risk factor
        
        Args:
            control_coverage: Percentage of controls implemented (0-100)
            system_risk_factor: Risk factor from classification (1.0-3.0)
        
        Returns:
            Base risk score
        """
        # Lower control coverage = higher risk
        coverage_risk = (100 - control_coverage) * 0.5
        
        # Higher system risk factor = higher risk
        system_risk = (system_risk_factor - 1.0) * 20
        
        return coverage_risk + system_risk
    
    def _calculate_gap_penalty(self, compliance_gaps: List[str]) -> float:
        """
        Calculate penalty for compliance gaps
        
        Args:
            compliance_gaps: List of identified compliance gaps
        
        Returns:
            Gap penalty score
        """
        # More gaps = higher penalty
        gap_count = len(compliance_gaps)
        
        # Progressive penalty
        if gap_count == 0:
            return 0
        elif gap_count <= 3:
            return gap_count * 2
        elif gap_count <= 6:
            return gap_count * 3
        else:
            return gap_count * 4
    
    def _calculate_factor_adjustment(self, additional_factors: Dict) -> float:
        """
        Calculate adjustment based on additional risk factors
        
        Args:
            additional_factors: Dictionary of additional risk factors
        
        Returns:
            Factor adjustment score
        """
        adjustment = 0
        
        # Data sensitivity
        if additional_factors.get("data_sensitivity", 1.0) > 1.3:
            adjustment += 5
        
        # User impact
        if additional_factors.get("user_impact", 1.0) > 1.3:
            adjustment += 5
        
        # Regulatory requirements
        if additional_factors.get("regulatory_requirements", 1.0) > 1.3:
            adjustment += 7
        
        # Autonomy level
        if additional_factors.get("autonomy_level", 1.0) > 1.3:
            adjustment += 3
        
        return adjustment
    
    def _determine_severity(self, score: float) -> SeverityLevel:
        """
        Determine severity level based on score
        
        Args:
            score: Risk score (0-100)
        
        Returns:
            SeverityLevel enum value
        """
        for severity, (min_score, max_score) in self.severity_thresholds.items():
            if min_score <= score <= max_score:
                return severity
        
        return SeverityLevel.LOW
    
    def _generate_recommendations(self, severity: SeverityLevel, compliance_gaps: List[str]) -> List[str]:
        """
        Generate recommendations based on severity and compliance gaps
        
        Args:
            severity: Severity level
            compliance_gaps: List of compliance gaps
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        # Severity-based recommendations
        if severity == SeverityLevel.CRITICAL:
            recommendations.append("Immediate risk mitigation required")
            recommendations.append("Engage executive leadership for oversight")
            recommendations.append("Consider temporary system suspension")
        elif severity == SeverityLevel.HIGH:
            recommendations.append("Develop comprehensive remediation plan")
            recommendations.append("Implement additional monitoring and controls")
            recommendations.append("Establish timeline for compliance")
        elif severity == SeverityLevel.MEDIUM:
            recommendations.append("Develop improvement plan")
            recommendations.append("Enhance documentation and procedures")
            recommendations.append("Schedule regular compliance reviews")
        else:  # LOW
            recommendations.append("Continue monitoring and improvement")
            recommendations.append("Document best practices")
            recommendations.append("Plan for scalability")
        
        # Gap-specific recommendations
        for gap in compliance_gaps:
            if "policy" in gap.lower():
                recommendations.append("Review and update AI governance policies")
            elif "training" in gap.lower():
                recommendations.append("Enhance AI competency and training programs")
            elif "monitoring" in gap.lower():
                recommendations.append("Implement continuous monitoring systems")
            elif "documentation" in gap.lower():
                recommendations.append("Improve AI system documentation")
        
        return recommendations
    
    def _identify_risk_factors(
        self,
        control_coverage: float,
        system_risk_factor: float,
        compliance_gaps: List[str],
        additional_factors: Dict
    ) -> List[str]:
        """
        Identify key risk factors contributing to the score
        
        Args:
            control_coverage: Control coverage percentage
            system_risk_factor: System risk factor
            compliance_gaps: Compliance gaps
            additional_factors: Additional risk factors
        
        Returns:
            List of identified risk factors
        """
        factors = []
        
        # Control coverage factor
        if control_coverage < 50:
            factors.append(f"Low control coverage ({control_coverage}%)")
        elif control_coverage < 75:
            factors.append(f"Moderate control coverage ({control_coverage}%)")
        
        # System risk factor
        if system_risk_factor > 1.8:
            factors.append(f"High system risk factor ({system_risk_factor})")
        elif system_risk_factor > 1.4:
            factors.append(f"Elevated system risk factor ({system_risk_factor})")
        
        # Compliance gaps
        if len(compliance_gaps) > 5:
            factors.append(f"Multiple compliance gaps ({len(compliance_gaps)})")
        elif len(compliance_gaps) > 2:
            factors.append(f"Several compliance gaps ({len(compliance_gaps)})")
        
        # Additional factors
        if additional_factors.get("data_sensitivity", 1.0) > 1.3:
            factors.append("High data sensitivity")
        if additional_factors.get("user_impact", 1.0) > 1.3:
            factors.append("High user impact")
        if additional_factors.get("regulatory_requirements", 1.0) > 1.3:
            factors.append("Stringent regulatory requirements")
        if additional_factors.get("autonomy_level", 1.0) > 1.3:
            factors.append("High autonomy level")
        
        return factors if factors else ["No significant risk factors identified"]
    
    def calculate_control_coverage(self, implemented_controls: List[str], required_controls: List[str]) -> float:
        """
        Calculate percentage of required controls that are implemented
        
        Args:
            implemented_controls: List of implemented control IDs
            required_controls: List of required control IDs
        
        Returns:
            Coverage percentage (0-100)
        """
        if not required_controls:
            return 100.0
        
        implemented_set = set(implemented_controls)
        required_set = set(required_controls)
        
        implemented_required = len(implemented_set.intersection(required_set))
        coverage = (implemented_required / len(required_set)) * 100
        
        return round(coverage, 1)


# Example usage and testing
if __name__ == "__main__":
    engine = RiskScoringEngine()
    
    # Test risk calculation
    control_coverage = 65.0  # 65% of controls implemented
    system_risk_factor = 1.8  # High risk system
    compliance_gaps = [
        "Missing AI governance policy",
        "No AI risk assessment conducted",
        "Insufficient monitoring",
        "Lack of incident response procedures"
    ]
    additional_factors = {
        "data_sensitivity": 1.4,
        "user_impact": 1.3,
        "regulatory_requirements": 1.0,
        "autonomy_level": 1.2
    }
    
    risk_score = engine.calculate_risk_score(
        control_coverage,
        system_risk_factor,
        compliance_gaps,
        additional_factors
    )
    
    print("Risk Assessment Result:")
    print(f"Score: {risk_score.score}")
    print(f"Severity: {risk_score.severity.value}")
    print(f"Description: {risk_score.description}")
    print(f"Color: {risk_score.color}")
    print(f"\nRisk Factors:")
    for factor in risk_score.factors:
        print(f"  - {factor}")
    print(f"\nRecommendations:")
    for recommendation in risk_score.recommendations:
        print(f"  - {recommendation}")