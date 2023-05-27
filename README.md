# wtc-lms Updater

## Introduction
The wtc-lms Updater is a Python script designed to check the version of the wtc-lms program and update it if necessary. This script automates the process of checking for updates and ensures that the wtc-lms program is always up to date and also this is only for linux.

## Features
- Checks the current version of wtc-lms installed on the system.
- Compares the downloaded version with the installed version and updates if necessary.
- Provides an option to choose the installation location for the updated wtc-lms program.
- Verifies the update by comparing the versions before and after the update.

## Prerequisites
- Python 3.5 or above.
- The wtc-lms program must be installed on the system.
- Internet connection to download the latest version of wtc-lms.

## Installation
1. Clone the repository to your local machine


## Usage
1. Open a terminal.

2. Change to the project directory:
```bash
cd LMS_UPDATE
```

3. Run the script:

```bash
python update_wtc-lms.py
```

4. Follow the prompts and instructions provided by the script.

## Configuration
The script accepts an optional argument `path_location` which allows you to specify the location for the downloaded wtc-lms program. By default, it is set to "Downloads/".

To change the default `path_location`, open the `update_wtc-lms.py` file and modify the `path_location` parameter in the `update_lms()` function.
