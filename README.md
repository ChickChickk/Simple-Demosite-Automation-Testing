# Selenium DemoQA Form Automation

## Description
This project automates the DemoQA Practice Form using Python, Selenium, and Pytest.  
It fills out the form, uploads a file, submits it, and verifies successful submission.

<img width="1425" height="782" alt="demoqa" src="https://github.com/user-attachments/assets/cb2dc8a2-786c-4ad9-9a0e-50707b05af4d" />

## Features
- Text field automation
- Button selection
- Date picker handling
- Subject input selection
- Checkbox selection
- File upload (image)
- State and city dropdown selection
- Form submission
- Success modal validation

## Test Process

Open https://demoqa.com/automation-practice-form --> Fill out the forms --> Submit --> Close and Refresh

## Important Information

To know the name of each element, we will need to Inspect the name one by one and search for the ID.

Example:
<img width="1439" height="731" alt="example" src="https://github.com/user-attachments/assets/bab62388-f6bf-4d1f-bfe4-2126eae8d2a8" />

## Tech Stack
- Python
- Selenium
- Pytest

## Requirements
- Python 3.10+
- Google Chrome

## Test Target
DemoQA Automation Practice Form

## Mac Setup
```bash
git clone https://github.com/ChickChickk/Simple-Demosite-Automation-Testing.git
cd Simple-Demosite-Automation-Testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
