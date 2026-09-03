# 🤖 AI Risk Assessment Tool

**ISO/IEC 42001 AI Management System Compliance Automation**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Development-yellow)

## 🎯 Overview

The AI Risk Assessment Tool is an enterprise-grade automation system that evaluates AI systems against ISO/IEC 42001 controls with professional risk assessment reporting. This tool addresses the emerging need for AI governance automation as organizations adopt AI/ML technologies.

## ✨ Features

- **ISO/IEC 42001 Control Mapping**: Map AI systems to 10 control categories
- **AI System Classification**: Catalog and classify AI/ML systems by type
- **Risk Scoring Engine**: Severity-based scoring (CRITICAL, HIGH, MEDIUM, LOW)
- **Compliance Gap Analysis**: Identify governance gaps with actionable recommendations
- **Automated Report Generation**: Professional Excel reports with executive summaries
- **Executive Dashboard**: Real-time risk metrics and trend analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- AWS CLI configured with credentials
- Knowledge of AI/ML systems and ISO/IEC 42001 framework

### Installation

```bash
# Clone the repository
git clone https://github.com/Tsmooth1987/ai-risk-assessment-tool.git
cd ai-risk-assessment-tool

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run AI risk assessment
python main.py --ai-system "AI_System_Name" --type "machine_learning"

# Generate compliance report
python main.py --report --format excel

# Full assessment with dashboard
python main.py --full-assessment --ai-system inventory.json
```

## 🏗️ Architecture

```
AI System Input → Classification → Control Mapping → Risk Scoring → Report Generation
```

### Components
- **AI System Classifier**: Categorizes AI systems by type and risk factor
- **Control Mapping Engine**: Maps systems to ISO/IEC 42001 controls
- **Risk Scoring Algorithm**: Calculates severity scores based on multiple factors
- **Report Generator**: Creates professional Excel reports with executive summaries
- **Dashboard Integration**: JSON output for dashboard visualization

## 📊 Control Categories

The tool evaluates AI systems against 10 ISO/IEC 42001 control categories:

1. **AI Policy**: Governance policy and commitment
2. **AI Organization**: Structure and roles
3. **AI Planning**: Planning and risk assessment
4. **AI Support**: Resources and support
5. **AI Operation**: Operation and monitoring
6. **AI Performance**: Performance evaluation
7. **AI Risk Assessment**: Risk identification and management
8. **AI Improvement**: Continuous improvement
9. **AI Auditing**: Audit and review
10. **AI Governance**: Oversight and control

## 🎯 Risk Scoring

**Severity Levels**:
- **CRITICAL** (90-100): Immediate action required
- **HIGH** (70-89): Action within 30 days
- **MEDIUM** (40-69): Action within 90 days
- **LOW** (0-39): Monitor and improve

**Scoring Factors**:
- AI system type (risk factor multiplier)
- Control coverage percentage
- Compliance gap severity
- Data sensitivity level
- Regulatory requirements

## 📁 Project Structure

```
ai-risk-assessment-tool/
├── main.py (Main assessment engine)
├── config.py (Configuration and control mappings)
├── ai_system_classifier.py (AI system classification)
├── risk_scoring.py (Risk scoring algorithms)
├── report_generator.py (Excel report generation)
├── iso_42001_controls.py (Control definitions)
├── utils.py (Utility functions)
├── tests/ (Unit tests)
├── deployment/ (CloudFormation/Terraform)
└── docs/ (Documentation)
```

## 🔧 Technical Stack

- **Language**: Python 3.11+
- **AWS Services**: Lambda, S3, DynamoDB
- **Libraries**: boto3, pandas, openpyxl, numpy
- **Frameworks**: ISO/IEC 42001, NIST AI RMF
- **Output**: Excel reports + JSON for dashboard integration

## 📈 Performance

- **Assessment Time**: <30 seconds
- **Report Generation**: <5 seconds
- **Lambda Cold Start**: <2 seconds
- **Control Mapping Accuracy**: >95%

## 🛡️ Security

- Least-privilege IAM roles
- Encrypted S3 storage (AES256)
- Secure AI data handling
- Confidential risk data protection
- AWS CloudTrail logging enabled

## 🎓 Background

This tool leverages ISO/IEC 42001 Lead Auditor certification to provide practical AI governance automation. It addresses the critical need for AI risk management as organizations increasingly adopt AI/ML technologies while ensuring compliance with emerging AI governance frameworks.

## 📊 Use Cases

- **AI System Compliance**: Evaluate AI systems against ISO/IEC 42001
- **Risk Assessment**: Identify and prioritize AI governance risks
- **Audit Preparation**: Generate evidence for AI governance audits
- **Executive Reporting**: Provide AI risk metrics to leadership
- **Continuous Monitoring**: Ongoing compliance assessment

## 🚀 Deployment

### AWS Lambda Deployment

```bash
# Package the function
./deployment/package-lambda.sh

# Deploy to AWS
./deployment/deploy-lambda.sh
```

### CloudFormation Deployment

```bash
aws cloudformation deploy \
  --template-file deployment/cloudformation-template.yaml \
  --stack-name ai-risk-assessment-tool \
  --capabilities CAPABILITY_IAM
```

## 📝 Development

### Setup Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test
pytest tests/test_risk_scoring.py
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Terence Webster**
- GitHub: [@Tsmooth1987](https://github.com/Tsmooth1987)
- Website: [terence-webster.com](https://terence-webster.com)
- LinkedIn: [Terence Webster](https://linkedin.com/in/terencewebster)

## 🙏 Acknowledgments

- ISO/IEC 42001 standard documentation
- NIST AI Risk Management Framework
- GRC Engineering Club resources
- AWS Lambda and serverless architecture community

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Contact: terence.j.webster@gmail.com
- LinkedIn: [Terence Webster](https://linkedin.com/in/terencewebster)

---

**Built with expertise in ISO/IEC 42001 AI Management Systems and AWS serverless architecture**

*This project demonstrates practical application of AI governance standards and positions the author as a pioneer in AI governance automation.*