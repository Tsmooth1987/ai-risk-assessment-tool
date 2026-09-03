"""
AI Risk Assessment Tool - Configuration
ISO/IEC 42001 AI Management System Control Definitions
"""

# ISO/IEC 42001 Control Categories and Mappings
ISO_42001_CONTROLS = {
    "policy": {
        "name": "AI Policy",
        "description": "AI governance policy and commitment",
        "controls": [
            "AI_GOV_001": "AI governance policy established",
            "AI_GOV_002": "Roles and responsibilities defined",
            "AI_GOV_003": "AI risk management process",
            "AI_GOV_004": "AI objectives aligned with business",
        ]
    },
    "organization": {
        "name": "AI Organization",
        "description": "Organizational structure and roles",
        "controls": [
            "AI_ORG_001": "AI governance committee established",
            "AI_ORG_002": "AI roles and responsibilities defined",
            "AI_ORG_003": "AI competency and training",
            "AI_ORG_004": "AI accountability mechanisms",
        ]
    },
    "planning": {
        "name": "AI Planning",
        "description": "AI system planning and risk assessment",
        "controls": [
            "AI_PLAN_001": "AI risk assessment conducted",
            "AI_PLAN_002": "AI objectives defined",
            "AI_PLAN_003": "AI impact assessment",
            "AI_PLAN_004": "AI stakeholders identified",
        ]
    },
    "support": {
        "name": "AI Support",
        "description": "Resources and support for AI systems",
        "controls": [
            "AI_SUP_001": "AI resources allocated",
            "AI_SUP_002": "AI documentation maintained",
            "AI_SUP_003": "AI training programs",
            "AI_SUP_004": "AI communication protocols",
        ]
    },
    "operation": {
        "name": "AI Operation",
        "description": "AI system operation and monitoring",
        "controls": [
            "AI_OPS_001": "AI operation procedures defined",
            "AI_OPS_002": "AI monitoring implemented",
            "AI_OPS_003": "AI change management",
            "AI_OPS_004": "AI incident response",
        ]
    },
    "performance": {
        "name": "AI Performance",
        "description": "AI system performance evaluation",
        "controls": [
            "AI_PERF_001": "AI performance metrics defined",
            "AI_PERF_002": "AI effectiveness evaluation",
            "AI_PERF_003": "AI continuous improvement",
            "AI_PERF_004": "AI benchmarking",
        ]
    },
    "risk_assessment": {
        "name": "AI Risk Assessment",
        "description": "AI risk identification and management",
        "controls": [
            "AI_RISK_001": "AI risk identification process",
            "AI_RISK_002": "AI risk analysis methods",
            "AI_RISK_003": "AI risk treatment planning",
            "AI_RISK_004": "AI risk monitoring",
        ]
    },
    "improvement": {
        "name": "AI Improvement",
        "description": "Continuous improvement of AI systems",
        "controls": [
            "AI_IMP_001": "AI improvement opportunities",
            "AI_IMP_002": "AI corrective actions",
            "AI_IMP_003": "AI lessons learned",
            "AI_IMP_004": "AI innovation",
        ]
    },
    "auditing": {
        "name": "AI Auditing",
        "description": "AI system audit and review",
        "controls": [
            "AI_AUD_001": "AI internal audit process",
            "AI_AUD_002": "AI management review",
            "AI_AUD_003": "AI compliance monitoring",
            "AI_AUD_004": "AI audit reporting",
        ]
    },
    "governance": {
        "name": "AI Governance",
        "description": "AI governance oversight and control",
        "controls": [
            "AI_GOV_001": "AI governance framework",
            "AI_GOV_002": "AI compliance mechanisms",
            "AI_GOV_003": "AI oversight processes",
            "AI_GOV_004": "AI reporting",
        ]
    }
}

# Risk Scoring Criteria
RISK_SCORING = {
    "CRITICAL": {
        "score_range": (90, 100),
        "description": "Immediate action required",
        "color": "#DC2626",
        "factors": ["high_bias_risk", "data_breach_risk", "regulatory_violation"]
    },
    "HIGH": {
        "score_range": (70, 89),
        "description": "Action required within 30 days",
        "color": "#F59E0B",
        "factors": ["medium_bias_risk", "privacy_concerns", "compliance_gaps"]
    },
    "MEDIUM": {
        "score_range": (40, 69),
        "description": "Action required within 90 days",
        "color": "#3B82F6",
        "factors": ["process_gaps", "documentation_issues", "monitoring_needs"]
    },
    "LOW": {
        "score_range": (0, 39),
        "description": "Monitor and improve",
        "color": "#10B981",
        "factors": ["minor_improvements", "best_practices", "optimization"]
    }
}

# AI System Classification
AI_SYSTEM_TYPES = {
    "machine_learning": {
        "name": "Machine Learning",
        "risk_factor": 1.2,
        "control_requirements": ["operation", "performance", "risk_assessment"]
    },
    "deep_learning": {
        "name": "Deep Learning",
        "risk_factor": 1.5,
        "control_requirements": ["operation", "performance", "risk_assessment", "governance"]
    },
    "generative_ai": {
        "name": "Generative AI",
        "risk_factor": 2.0,
        "control_requirements": ["all"]  # All control categories
    },
    "computer_vision": {
        "name": "Computer Vision",
        "risk_factor": 1.3,
        "control_requirements": ["operation", "performance", "auditing"]
    },
    "natural_language": {
        "name": "Natural Language Processing",
        "risk_factor": 1.1,
        "control_requirements": ["operation", "performance", "risk_assessment"]
    },
    "decision_support": {
        "name": "Decision Support Systems",
        "risk_factor": 1.4,
        "control_requirements": ["operation", "governance", "auditing"]
    }
}

# AWS Configuration
AWS_CONFIG = {
    "region": "us-east-1",
    "lambda": {
        "runtime": "python3.11",
        "timeout": 300,
        "memory": 512
    },
    "s3": {
        "report_bucket": "ai-risk-assessment-reports",
        "report_prefix": "reports/"
    },
    "dynamodb": {
        "ai_systems_table": "ai-systems-inventory"
    }
}

# Report Configuration
REPORT_CONFIG = {
    "format": "excel",
    "include_executive_summary": True,
    "include_detailed_findings": True,
    "include_remediation": True,
    "include_appendix": True
}