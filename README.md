# Battery Notification System for Windows

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/sumanthpagadala/Battery-Status/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/sumanthpagadala/Battery-Status.svg)](https://github.com/sumanthpagadala/Battery-Status/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sumanthpagadala/Battery-Status.svg)](https://github.com/sumanthpagadala/Battery-Status/network)
[![GitHub issues](https://img.shields.io/github/issues/sumanthpagadala/Battery-Status.svg)](https://github.com/sumanthpagadala/Battery-Status/issues)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Autostart on Windows](#autostart-on-windows)
- [Changing File Extension to .pyw](#changing-file-extension-to-pyw)
- [Usage Considerations](#usage-considerations)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Introduction

The Battery Notification System for Windows is a Python-based application that helps you manage your laptop's battery life by providing timely notifications. This project was initiated to address the common issue of forgetting to unplug the charger, which can lead to unnecessary damage to the battery life. By monitoring the battery level and displaying notifications, this system reminds users to unplug their chargers when the battery is fully charged, improving battery health and overall device usage.

## Installation

To use the Battery Notification System for Windows, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your_username/your_project.git
   ```

2. Install the required dependencies:

   ```shell
   pip install psutil plyer
   ```

## How It Works

The Battery Notification System uses the `psutil` library to retrieve the battery information and the `plyer` library to display notifications. The code continuously monitors the battery percentage and checks for two conditions: when the battery is fully charged (100%) and when it falls below a certain threshold (configured to 20% in this project).

When the battery reaches 100%, a notification is displayed, reminding the user to unplug the charger. Similarly, when the battery falls below 20%, another notification is displayed, suggesting that the user consider charging the device.

## Autostart on Windows

To automatically start the Battery Notification System on Windows startup, follow these steps:

1. Press `Win + R` to open the Run dialog.

2. Type `shell:startup` and press Enter. This opens the Windows startup folder.

3. Drag and drop the `battery.py` (or `battery.pyw` if you changed the file extension) script into the startup folder. This ensures that the script runs every time you start your computer.

## Changing File Extension to .pyw

If you prefer not to see a terminal window every time the script runs, you can change the file extension from `.py` to `.pyw`. This can be done using the following command in the command prompt or terminal:

```shell
ren battery.py battery.pyw
```

The `.pyw` extension indicates that the script should run as a "Pythonw" program, which hides the terminal window during execution.

## Usage Considerations

If you have a gaming laptop or a specific use case where the battery needs to be constantly charged, you can modify the sleep time or temporarily disable the notifications. Adjust the `sleep` duration in the script to increase or decrease the interval between battery checks. Additionally, you can comment out or remove the lines responsible for displaying the notifications to temporarily disable them during your preferred activities.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your_username/your_project/blob/main/LICENSE) file for more details.

## Acknowledgments

We would like to express our gratitude to the open-source community for their contributions and the developers of the `psutil` and `plyer` libraries, which have made this project possible.

## Contact

For any questions or inquiries, please feel free to reach out to the project maintainer at your_email@example.com.

---

**Note:** This project is for educational purposes only and should not replace the built-in battery management features provided by your operating system. Always follow the recommendations of your device manufacturer for battery usage and management.
