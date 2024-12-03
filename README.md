# VRV Log Analysis Script

## Project Overview

The **VRV Log Analysis Script** is a tool designed to efficiently process and analyze log files, extracting meaningful insights and presenting the results in a user-friendly format. This project is part of the **Log Analysis Assignment** for the **VRV Organization**, aimed at creating a streamlined approach to log data processing and reporting. 

---

## Features

- **Automated Log Analysis**: Processes raw log files to extract relevant information.
- **Customizable Configuration**: Easily modify the script to suit different log formats or analysis requirements.
- **Efficient Reporting**: Generates concise and organized results for better readability.
- **Modular Structure**: Simplified project structure to enhance usability and maintainability.

---

## How It Works

1. **Input**: The script takes raw log files as input (e.g., `.txt` or `.log` files).
2. **Processing**: It parses and processes the logs to extract specific metrics, patterns, or statistics.
3. **Output**: The analysis results are presented in a readable format, such as a CSV file or terminal output.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.9 or later
- Required Python packages (listed in `requirements.txt`)

To set up the necessary environment, you can use the provided `environment.yml` file or install the dependencies manually.

---

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/vrv-log-analysis.git
cd vrv-log-analysis
```

### Step 2: Set Up the Environment

#### Using Conda (Recommended)

The project provides an environment configuration file (`environment.yml`). You can set up the environment by running:

```bash
conda env create -f environment.yml
conda activate vrv_env
```

#### Using pip

If you're not using Conda, you can install the required packages via pip. First, make sure you have Python 3.9 or later installed, and then run:

```bash
pip install -r requirements.txt
```

### Step 3: Prepare Your Log Files

Place your log files in the `data/` folder within the project directory.

---

## Usage

### Running the Script

Once the environment is set up and the log files are ready, you can run the log analysis script using the following command:

```bash
python scripts/log_analysis.py --input data/ --output results/
```

This will process the log files in the `data/` folder and save the results in the `results/` folder.

#### Command-Line Arguments

- `--input`: Path to the folder containing the log files (default: `data/`).
- `--output`: Path to the folder where the processed results will be saved (default: `results/`).

### Results

After running the script, the processed results will be saved in the `results/` folder in a CSV or text format, depending on the configuration. You can analyze these outputs to derive insights from the logs.

---

## Project Structure:

```
vrv-log-analysis/
├── data/                    # Folder to place raw log files
├── results/                 # Folder for saving results
├── environment.yml          # Conda environment configuration file
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── scripts/                 # Python script for log analysis
    └── log_analysis.py      # Main code
```

---

## Example Log File Format

Ensure your log files follow a general format, such as:

```
[2024-12-03 10:00:00] INFO: User logged in - UserID: 12345
[2024-12-03 10:05:00] ERROR: Database connection failed
```

---

## Acknowledgements

This project is part of the **Log Analysis Assignment** for **VRV Organization**. Thanks to the team for providing the requirements and allowing the development of this tool.
```