# AI-Powered Password Generator

## Overview
This project is an **AI-powered password generator** with a **Graphical User Interface (GUI)** built using **Tkinter**. It generates strong passwords using **Shannon entropy** to measure their strength and **AI-based randomness** to ensure security.

## Features
- ✅ **AI-powered password generation** for strong security
- ✅ **Entropy calculation** to measure password strength
- ✅ **Customizable length, digits, and special characters**
- ✅ **Avoids ambiguous characters** (e.g., `l`, `I`, `0`, `O`)
- ✅ **Copy password to clipboard** for convenience

## Installation
### Prerequisites
Ensure you have **Python 3.11+** installed on your system.

### Install Dependencies
Run the following command to install the required dependencies:
```bash
pip install numpy pyperclip
```

## Usage
Run the script with:
```bash
python password_generator.py
```
A GUI window will appear, allowing you to:
1. Set the password length
2. Include/exclude digits and special characters
3. Generate and copy the password with a click

## How It Works
1. **AI-based randomness**: Uses NumPy's probability distribution for generating passwords.
2. **Shannon Entropy Calculation**: Ensures high password strength before finalizing.
3. **Regeneration if Weak**: If entropy is below a certain threshold, it regenerates a stronger password.

## Example Output
```
Generated Password: T%w9Gx!8KkLz#3F@
Entropy Score: 4.85 (Higher is better)
```

## Future Improvements
🚀 Convert this into a **Flask web app**
🚀 Add **password saving & encryption**
🚀 Implement **dark mode for GUI**

## License
This project is **open-source** under the **MIT License**.

---
**Developed with ❤️ by geco97**

