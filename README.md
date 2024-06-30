# Zendesk Field Update

## Overview

`update_field.py` is a Python script designed to update a single custom field's options in a Zendesk using data from an Excel file. This helps when the owner of the field is not a Zendesk admin but requires fast additions to be made. My end users add fields to an Excel sheet, the tag is autocreated via Excel function. This script fetches current custom field options from the Zendesk API, compares them with the values in the Excel file, and updates the options in Zendesk if there are new entries.

### Prerequisites

	•	Python 3.x, developed with anaconda base 2.5.4
	•	Required Python packages:
	•	requests
	•	pandas
	•	openpyxl (for reading Excel files)

### Configuration

Before running the script, ensure you have the following information configured securely:

	1.	Email: Your Zendesk account email.
	2.	API Token: Your Zendesk API token.
	3.	Subdomain: Your Zendesk subdomain.

These should be stored in a separate configuration file or environment variables. For this script, it assumes you have a config.py file that contains:

```python
email = 'your_email'
api_token = 'your_api_token'
subdomain = 'your_subdomain'
```

### File Path

Make sure to update the file path to your Excel file in the script:

```python
file_path = 'path/to/your/ticket-fields-department_position.xlsx'
```

This can work with network drives joined as local drives for collaboration such as Google Drive, OneDrive or Dropbox. Web links also work.
