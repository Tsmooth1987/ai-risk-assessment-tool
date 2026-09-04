"""
AI System Classifier
Classifies AI systems by type and assigns risk factors for ISO/IEC 42001 compliance assessment
"""

from enum import Enum
from typing import Dict, List, Optional


class AISystemType(Enum):
    """AI System Types with risk factors"""
    MACHINE_LEARNING = "machine_learning"
    DEEP_LEARNING = "deep_learning"
    GENERATIVE_AI = "generative_ai"
    COMPUTER_VISION = "computer_vision"
    NATURAL_LANGUAGE = "natural_language"
    DECISION_SUPPORT = "decision_support"


class AISystemClassifier:
    """Classifies AI systems and determines appropriate control requirements"""
    
    def __init__(self):
        self.system_types = {
            AISystemType.MACHINE_LEARNING: {
                "name": "Machine Learning",
                "risk_factor": 1.2,
                "control_categories": ["operation", "performance", "risk_assessment"],
                "description": "Traditional ML models using structured data",
                "typical_use_cases": ["classification", "regression", "clustering"]
            },
            AISystemType.DEEP_LEARNING: {
                "name": "Deep Learning",
                "risk_factor": 1.5,
                "control_categories": ["operation", "performance", "risk_assessment", "governance"],
                "description": "Neural networks with multiple layers",
                "typical_use_cases": ["image recognition", "speech recognition", "natural language processing"]
            },
            AISystemType.GENERATIVE_AI: {
                "name": "Generative AI",
                "risk_factor": 2.0,
                "control_categories": ["all"],  # All control categories required
                "description": "AI systems that generate new content",
                "typical_use_cases": ["text generation", "image generation", "code generation"]
            },
            AISystemType.COMPUTER_VISION: {
                "name": "Computer Vision",
                "risk_factor": 1.3,
                "control_categories": ["operation", "performance", "auditing"],
                "description": "AI systems that process visual data",
                "typical_use_cases": ["object detection", "image classification", "facial recognition"]
            },
            AISystemType.NATURAL_LANGUAGE: {
                "name": "Natural Language Processing",
                "risk_factor": 1.1,
                "control_categories": ["operation", "performance", "risk_assessment"],
                "description": "AI systems that process text and speech",
                "typical_use_cases": ["sentiment analysis", "translation", "chatbots"]
            },
            AISystemType.DECISION_SUPPORT: {
                "name": "Decision Support Systems",
                "risk_factor": 1.4,
                "control_categories": ["operation", "governance", "auditing"],
                "description": "AI systems that support decision-making",
                "typical_use_cases": ["risk assessment", "recommendation systems", "diagnostic tools"]
            }
        }
    
    def classify_system(self, system_description: str, system_features: Dict) -> Dict:
        """
        Classify an AI system based on description and features
        
        Args:
            system_description: Text description of the AI system
            system_features: Dictionary of system features (e.g., data types, algorithms, etc.)
        
        Returns:
            Dictionary with classification results and control requirements
        """
        # Analyze system description and features
        system_type = self._determine_system_type(system_description, system_features)
        risk_factor = self.system_types[system_type]["risk_factor"]
        control_categories = self.system_types[system_type]["control_categories"]
        
        return {
            "system_type": system_type.value,
            "system_name": self.system_types[system_type]["name"],
            "risk_factor": risk_factor,
            "control_categories": control_categories,
            "description": self.system_types[system_type]["description"],
            "typical_use_cases": self.system_types[system_type]["typical_use_cases"],
            "classification_confidence": self._calculate_confidence(system_description, system_features)
        }
    
    def _determine_system_type(self, description: str, features: Dict) -> AISystemType:
        """
        Determine AI system type based on description and features
        
        Args:
            description: System description
            features: System features dictionary
        
        Returns:
            AISystemType enum value
        """
        description_lower = description.lower()
        
        # Check for generative AI indicators
        if any(keyword in description_lower for keyword in 
               ["generate", "create", "synthetic", "generative", "llm", "gpt", "transformer"]):
            return AISystemType.GENERATIVE_AI
        
        # Check for deep learning indicators
        if any(keyword in description_lower for keyword in 
               ["neural network", "deep learning", "cnn", "rnn", "transformer", "bert"]):
            return AISystemType.DEEP_LEARNING
        
        # Check for computer vision indicators
        if any(keyword in description_lower for keyword in 
               ["image", "vision", "facial", "object detection", "computer vision"]):
            return AISystemType.COMPUTER_VISION
        
        # Check for natural language indicators
        if any(keyword in description_lower for keyword in 
               ["nlp", "text", "language", "sentiment", "translation", "chatbot"]):
            return AISystemType.NATURAL_LANGUAGE
        
        # Check for decision support indicators
        if any(keyword in description_lower for keyword in 
               ["decision", "recommendation", "diagnostic", "risk assessment", "support"]):
            return AISystemType.DECISION_SUPPORT
        
        # Default to machine learning
        return AISystemType.MACHINE_LEARNING
    
    def _calculate_confidence(self, description: str, features: Dict) -> float:
        """
        Calculate confidence score for classification
        
        Args:
            description: System description
            features: System features
        
        Returns:
            Confidence score between 0.0 and 1.0
        """
        confidence = 0.7  # Base confidence
        
        # Increase confidence if description is detailed
        if len(description) > 50:
            confidence += 0.1
        
        # Increase confidence if features are provided
        if features:
            confidence += 0.1
        
        # Cap at 1.0
        return min(confidence, 1.0)
    
    def get_control_requirements(self, system_type: AISystemType) -> List[str]:
        """
        Get required control categories for a given system type
        
        Args:
            system_type: AISystemType enum value
        
        Returns:
            List of required control categories
        """
        if system_type == AISystemType.GENERATIVE_AI:
            # All categories required for generative AI
            return [
                "policy", "organization", "planning", "support",
                "operation", "performance", "risk_assessment",
                "improvement", "auditing", "governance"
            ]
        else:
            return self.system_types[system_type]["control_categories"]
    
    def assess_additional_risk_factors(self, system_features: Dict) -> Dict:
        """
        Assess additional risk factors based on system features
        
        Args:
            system_features: Dictionary of system features
        
        Returns:
            Dictionary of additional risk factors and their impact
        """
        risk_factors = {
            "data_sensitivity": 1.0,
            "user_impact": 1.0,
            "regulatory_requirements": 1.0,
            "autonomy_level": 1.0
        }
        
        # Assess data sensitivity
        if system_features.get("personal_data", False):
            risk_factors["data_sensitivity"] = 1.3
        if system_features.get("health_data", False):
            risk_factors["data_sensitivity"] = 1.5
        if system_features.get("financial_data", False):
            risk_factors["data_sensitivity"] = 1.4
        
        # Assess user impact
        if system_features.get("high_user_impact", False):
            risk_factors["user_impact"] = 1.4
        if system_features.get("critical_decisions", False):
            risk_factors["user_impact"] = 1.5
        
        # Assess regulatory requirements
        if system_features.get("regulated_industry", False):
            risk_factors["regulatory_requirements"] = 1.3
        if system_features.get("eu_ae_compliance", False):
            risk_factors["regulatory_requirements"] = 1.4
        
        # Assess autonomy level
        if system_features.get("fully_autonomous", False):
            risk_factors["autonomy_level"] = 1.5
        if system_features.get("human_in_loop", False):
            risk_factors["autonomy_level"] = 1.2
        
        return risk_factors
    
    def calculate_composite_risk_factor(self, system_type: AISystemType, system_features: Dict) -> float:
        """
        Calculate composite risk factor combining system type and feature risks
        
        Args:
            system_type: AISystemType enum value
            system_features: Dictionary of system features
        
        Returns:
            Composite risk factor
        """
        base_risk = self.system_types[system_type]["risk_factor"]
        additional_risks = self.assess_additional_risk_factors(system_features)
        
        # Calculate composite risk
        composite_risk = base_risk
        for factor, multiplier in additional_risks.items():
            composite_risk *= multiplier
        
        return round(composite_risk, 2)


# Example usage and testing
if __name__ == "__main__":
    classifier = AISystemClassifier()
    
    # Test classification
    test_system = {
        "description": "A generative AI system that creates marketing content and product descriptions",
        "features": {
            "personal_data": False,
            "high_user_impact": True,
            "regulated_industry": False,
            "fully_autonomous": False
        }
    }
    
    result = classifier.classify_system(
        test_system["description"],
        test_system["features"]
    )
    
    print("AI System Classification Result:")
    print(f"System Type: {result['system_name']}")
    print(f"Risk Factor: {result['risk_factor']}")
    print(f"Control Categories: {result['control_categories']}")
    print(f"Confidence: {result['classification_confidence']}")
    
    # Calculate composite risk
    composite_risk = classifier.calculate_composite_risk_factor(
        AISystemType.GENERATIVE_AI,
        test_system["features"]
    )
    print(f"Composite Risk Factor: {composite_risk}")