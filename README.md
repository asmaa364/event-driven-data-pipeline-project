# 📊 Event-Driven Data Processing Pipeline

This project demonstrates an end-to-end **event-driven data pipeline** built on AWS using S3, Lambda, and CI/CD automation with GitHub Actions. The pipeline captures uploaded data, processes it, and generates automated daily summary reports.

---

## 📁 Project Structure

├── .github/workflows/ # CI/CD pipeline definition
├── iac/ # Infrastructure as Code (e.g., IAM, S3, Lambda setup)
├── lambda/ # Lambda function source code
│ └── process_data.py
├── sample-input/ # Sample input files
├── scripts/ # Report generation scripts
│ └── generate_report.py
├── report-template.html # HTML template for the report
├── report.html # Auto-generated summary report
├── buildspec.yml # Build instructions (for CodeBuild compatibility)
└── README.md # Project documentation
---

## ⚙️ Features

- 📥 **S3 Trigger**: Data files uploaded to S3 automatically trigger a Lambda function.
- 🧠 **Lambda Processing**: Processes raw data and stores results.
- 📝 **Report Generation**: A daily report is generated in HTML format.
- 🚀 **CI/CD with GitHub Actions**: Automates testing and deployment on code changes.
- 🔒 **IAM & Least Privilege**: Secure role-based access to AWS services.

---

## 🚀 How It Works

1. **Upload a File** ➝ Triggers an S3 event.
2. **Lambda Executes** ➝ Processes and stores the result.
3. **CI/CD Workflow** ➝ Builds and updates the report.
4. **HTML Report** ➝ Generated from processed data using a template.

---

## 🧪 CI/CD Workflow (GitHub Actions)

The GitHub Actions workflow automatically:

- Installs dependencies (if any)
- Runs tests (if included)
- Generates or updates the HTML report
- Pushes the result back to the repository (via a commit)

✅ Latest status: **Passed**
❌ Previous failed builds are preserved for transparency.

---

## 📦 Deployment (Optional)

You can deploy the infrastructure using tools like AWS CloudFormation or Terraform, as defined in the `iac/` directory.


