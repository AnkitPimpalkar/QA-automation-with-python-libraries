# Lead Sheet QA Automation Tool

A professional tool designed to automate the quality assurance process for performance marketing lead sheets. This program connects to a Google Sheet, validates key data fields, and highlights any discrepancies so that manual QA work can be completed in minutes rather than hours.

---

## Overview

The Lead Sheet QA Automation Tool performs the following tasks:
- **Data Validation:** Checks pincodes, phone numbers, and call notes to ensure they meet required standards.
- **Visual Feedback:** Highlights invalid entries in red and cells with edited content in yellow, making it easy to spot errors.
- **Efficiency Boost:** Reduces a two-hour manual review process down to two minutes.
- **Secure & Cost-Effective:** Uses trusted Python libraries and standard APIs to maintain data security without a high cost.

---

## Features

- **Google Sheets Integration:** Connects directly to your Google Sheet using a service account for secure API access.
- **Flexible Validators:** Dynamically loads validators based on configuration, ensuring each field (e.g., pincodes, phone numbers) is properly checked.
- **Call Note Enhancement:** Uses grammar checking and formatting to improve call note clarity.
- **Customizable:** Easily extend or modify validators by updating the configuration file.

---

## Prerequisites

Before running the program, ensure you have the following:
- **Python 3.x:** The program is developed in Python.
- **Java Runtime:** Required for grammar correction through the LanguageTool library (if running locally).
- **Google API Credentials:** A valid service account credentials JSON file to connect to Google Sheets.
- **Configuration Files:** 
  - `config/sheet_url.txt` – Contains the URL of the Google Sheet.
  - `config/credentials.json` – Your Google API service account credentials.
  - `config/valid_pins.txt` – A list of valid pincodes.
  - `config/validators_config.json` – Configuration details for the validators.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/lead-sheet-qa-tool.git
   cd lead-sheet-qa-tool
   ```

2. **Install Dependencies:**
   Create a virtual environment (optional but recommended) and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   - `gspread` – For Google Sheets connectivity.
   - `oauth2client` – For service account authentication.
   - `language_tool_python` – For grammar and spelling correction in call notes ( for language_tool_python, a Java runtime is needed if you run it locally)

---

## Configuration

Ensure the following files are in the `config` directory:
- **`credentials.json`:** Your Google API service account credentials.
- **`sheet_url.txt`:** Contains the URL of the Google Sheet you wish to process.
- **`valid_pins.txt`:** A plain text file listing valid pincodes.
- **`validators_config.json`:** JSON file defining which validators to load and their respective settings (e.g., column names, regex patterns).

---

## How to Run

To execute the program, simply run:

```bash
python run.py
```

The script will:
1. Load the necessary configurations.
2. Connect to the specified Google Sheet.
3. Validate the data using the defined validators.
4. Update the sheet by highlighting invalid entries.

---

## How It Works

- **Connection & Data Retrieval:**  
  The tool connects to your Google Sheet using the provided credentials and retrieves all data for validation.

- **Validation Process:**  
  Each validator checks specific columns:
  - **Pincode Validator:** Verifies if pincodes exist in the list of valid pincodes.
  - **Phone Number Validator:** Confirms that phone numbers match the expected format.
  - **Call Note Validator:** Corrects grammar and applies formatting to call notes.

- **Feedback & Update:**  
  Invalid or modified entries are highlighted directly in the Google Sheet (red for errors, yellow for edits).

---

## Future Enhancements

An AI-enhanced version is in development to further improve accuracy and extend validation capabilities. This upcoming model will offer even more refined checks while maintaining the simplicity for non-technical users.

---

## Support

For any questions or issues, please feel free to open an issue in the repository or contact the maintainer.

---

Enjoy a streamlined, efficient QA process that saves time and reduces errors in your performance marketing lead sheets!
