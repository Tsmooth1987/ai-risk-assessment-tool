"""
ISO/IEC 42001 AI Management System Control Definitions
Implementation of the 10 control categories with detailed control definitions
"""

class ISO42001Control:
    """Base class for ISO/IEC 42001 controls"""
    
    def __init__(self, control_id, title, description, category, risk_weight):
        self.control_id = control_id
        self.title = title
        self.description = description
        self.category = category
        self.risk_weight = risk_weight  # 1.0-3.0 impact on risk score
        self.evidence_requirements = []
        self.testing_methods = []
    
    def add_evidence_requirement(self, requirement):
        """Add evidence requirement for this control"""
        self.evidence_requirements.append(requirement)
    
    def add_testing_method(self, method):
        """Add testing method for this control"""
        self.testing_methods.append(method)
    
    def to_dict(self):
        """Convert control to dictionary"""
        return {
            'control_id': self.control_id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'risk_weight': self.risk_weight,
            'evidence_requirements': self.evidence_requirements,
            'testing_methods': self.testing_methods
        }


# ISO/IEC 4201 Control Definitions
ISO_42001_CONTROLS = {
    # Category 1: AI Policy
    "AI_GOV_001": ISO42001Control(
        "AI_GOV_001",
        "AI Governance Policy",
        "Organization has established a comprehensive AI governance policy that commits to responsible AI development and use",
        "policy",
        2.0
    ),
    "AI_GOV_002": ISO42001Control(
        "AI_GOV_002",
        "Roles and Responsibilities",
        "AI governance roles and responsibilities are defined and assigned across the organization",
        "policy",
        1.5
    ),
    "AI_GOV_003": ISO42001Control(
        "AI_GOV_003",
        "AI Risk Management",
        "AI risk management process is established and integrated into organizational risk management",
        "policy",
        2.5
    ),
    "AI_GOV_004": ISO42001Control(
        "AI_GOV_004",
        "AI Objectives Alignment",
        "AI objectives are defined and aligned with organizational objectives",
        "policy",
        1.5
    ),
    
    # Category 2: AI Organization
    "AI_ORG_001": ISO42001Control(
        "AI_ORG_001",
        "AI Governance Committee",
        "AI governance committee is established with appropriate authority and expertise",
        "organization",
        2.0
    ),
    "AI_ORG_002": ISO42001Control(
        "AI_ORG_002",
        "AI Roles and Responsibilities",
        "AI roles and responsibilities are defined, documented, and communicated",
        "organization",
        1.5
    ),
    "AI_ORG_003": ISO42001Control(
        "AI_ORG_003",
        "AI Competency and Training",
        "AI competency requirements are defined and training programs are established",
        "organization",
        1.8
    ),
    "AI_ORG_004": ISO42001Control(
        "AI_ORG_004",
        "AI Accountability Mechanisms",
        "Accountability mechanisms for AI systems are established and implemented",
        "organization",
        1.8
    ),
    
    # Category 3: AI Planning
    "AI_PLAN_001": ISO42001Control(
        "AI_PLAN_001",
        "AI Risk Assessment",
        "AI risk assessment is conducted for all AI systems before development and deployment",
        "planning",
        2.5
    ),
    "AI_PLAN_002": ISO42001Control(
        "AI_PLAN_002",
        "AI Objectives Definition",
        "AI system objectives are defined with measurable success criteria",
        "planning",
        1.5
    ),
    "AI_PLAN_003": ISO42001Control(
        "AI_PLAN_003",
        "AI Impact Assessment",
        "AI impact assessment is conducted to identify potential impacts on stakeholders",
        "planning",
        2.0
    ),
    "AI_PLAN_004": ISO42001Control(
        "AI_PLAN_004",
        "AI Stakeholder Identification",
        "AI stakeholders are identified and their interests are considered",
        "planning",
        1.5
    ),
    
    # Category 4: AI Support
    "AI_SUP_001": ISO42001Control(
        "AI_SUP_001",
        "AI Resources Allocation",
        "Appropriate resources are allocated for AI system development and operation",
        "support",
        1.5
    ),
    "AI_SUP_002": ISO42001Control(
        "AI_SUP_002",
        "AI Documentation",
        "AI systems are documented with comprehensive information throughout their lifecycle",
        "support",
        1.8
    ),
    "AI_SUP_003": ISO42001Control(
        "AI_SUP_003",
        "AI Training Programs",
        "AI training programs are established for personnel working with AI systems",
        "support",
        1.5
    ),
    "AI_SUP_004": ISO42001Control(
        "AI_SUP_004",
        "AI Communication Protocols",
        "Communication protocols for AI systems are established and documented",
        "support",
        1.5
    ),
    
    # Category 5: AI Operation
    "AI_OPS_001": ISO42001Control(
        "AI_OPS_001",
        "AI Operation Procedures",
        "AI system operation procedures are defined, documented, and followed",
        "operation",
        1.8
    ),
    "AI_OPS_002": ISO42001Control(
        "AI_OPS_002",
        "AI Monitoring",
        "AI systems are monitored for performance, security, and compliance",
        "operation",
        2.0
    ),
    "AI_OPS_003": ISO42001Control(
        "AI_OPS_003",
        "AI Change Management",
        "AI system changes are managed through controlled change management process",
        "operation",
        2.0
    ),
    "AI_OPS_004": ISO42001Control(
        "AI_OPS_004",
        "AI Incident Response",
        "AI incident response procedures are established and tested",
        "operation",
        2.5
    ),
    
    # Category 6: AI Performance
    "AI_PERF_001": ISO42001Control(
        "AI_PERF_001",
        "AI Performance Metrics",
        "AI system performance metrics are defined and monitored",
        "performance",
        1.5
    ),
    "AI_PERF_002": ISO42001Control(
        "AI_PERF_002",
        "AI Effectiveness Evaluation",
        "AI system effectiveness is evaluated against defined objectives",
        "performance",
        1.8
    ),
    "AI_PERF_003": ISO42001Control(
        "AI_PERF_003",
        "AI Continuous Improvement",
        "AI systems are continuously improved based on performance data and lessons learned",
        "performance",
        1.5
    ),
    "AI_PERF_004": ISO42001Control(
        "AI_PERF_004",
        "AI Benchmarking",
        "AI system performance is benchmarked against industry standards and best practices",
        "performance",
        1.5
    ),
    
    # Category 7: AI Risk Assessment
    "AI_RISK_001": ISO42001Control(
        "AI_RISK_001",
        "AI Risk Identification",
        "AI risks are systematically identified throughout the AI system lifecycle",
        "risk_assessment",
        2.5
    ),
    "AI_RISK_002": ISO42001Control(
        "AI_RISK_002",
        "AI Risk Analysis Methods",
        "AI risks are analyzed using appropriate methods and tools",
        "risk_assessment",
        2.0
    ),
    "AI_RISK_003": ISO42001Control(
        "AI_RISK_003",
        "AI Risk Treatment Planning",
        "AI risk treatment plans are developed and implemented",
        "risk_assessment",
        2.0
    ),
    "AI_RISK_004": ISO42001Control(
        "AI_RISK_004",
        "AI Risk Monitoring",
        "AI risks are monitored and reassessed on a regular basis",
        "risk_assessment",
        1.8
    ),
    
    # Category 8: AI Improvement
    "AI_IMP_001": ISO42001Control(
        "AI_IMP_001",
        "AI Improvement Opportunities",
        "AI system improvement opportunities are identified and acted upon",
        "improvement",
        1.5
    ),
    "AI_IMP_002": ISO42001Control(
        "AI_IMP_002",
        "AI Corrective Actions",
        "Corrective actions are implemented for nonconformities and incidents",
        "improvement",
        2.0
    ),
    "AI_IMP_003": ISO42001Control(
        "AI_IMP_003",
        "AI Lessons Learned",
        "Lessons learned from AI system development and operation are captured and applied",
        "improvement",
        1.5
    ),
    "AI_IMP_004": ISO42001Control(
        "AI_IMP_004",
        "AI Innovation",
        "Innovation in AI systems is encouraged and supported within governance framework",
        "improvement",
        1.2
    ),
    
    # Category 9: AI Auditing
    "AI_AUD_001": ISO42001Control(
        "AI_AUD_001",
        "AI Internal Audit Process",
        "Internal audit process for AI systems is established and conducted regularly",
        "auditing",
        1.8
    ),
    "AI_AUD_002": ISO42001Control(
        "AI_AUD_002",
        "AI Management Review",
        "AI system management reviews are conducted at planned intervals",
        "auditing",
        1.5
    ),
    "AI_AUD_003": ISO42001Control(
        "AI_AUD_003",
        "AI Compliance Monitoring",
        "AI system compliance is monitored and reported to management",
        "auditing",
        1.8
    ),
    "AI_AUD_004": ISO42001Control(
        "AI_AUD_004",
        "AI Audit Reporting",
        "AI audit reports are generated and distributed to stakeholders",
        "auditing",
        1.5
    ),
    
    # Category 10: AI Governance
    "AI_GOV_001": ISO42001Control(
        "AI_GOV_001",
        "AI Governance Framework",
        "AI governance framework is established and maintained",
        "governance",
        2.0
    ),
    "AI_GOV_002": ISO42001Control(
        "AI_GOV_002",
        "AI Compliance Mechanisms",
        "AI compliance mechanisms are implemented and tested",
        "governance",
        1.8
    ),
    "AI_GOV_003": ISO42001Control(
        "AI_GOV_003",
        "AI Oversight Processes",
        "AI oversight processes are established and executed",
        "governance",
        1.8
    ),
    "AI_GOV_004": ISO42001Control(
        "AI_GOV_004",
        "AI Reporting",
        "AI governance reports are generated and provided to stakeholders",
        "governance",
        1.5
    ),
}


def get_control_by_id(control_id):
    """Get control by ID"""
    return ISO_42001_CONTROLS.get(control_id)


def get_controls_by_category(category):
    """Get all controls in a category"""
    return {
        k: v for k, v in ISO_42001_CONTROLS.items()
        if v.category == category
    }


def get_all_controls():
    """Get all ISO/IEC 42001 controls"""
    return ISO_42001_CONTROLS


def get_control_categories():
    """Get all control categories"""
    categories = {}
    for control_id, control in ISO_42001_CONTROLS.items():
        if control.category not in categories:
            categories[control.category] = []
        categories[control.category].append(control_id)
    return categories