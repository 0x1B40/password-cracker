# Password Cracker Tool

A penetration testing tool built with Python and Selenium WebDriver designed to test the security of web authentication systems through automated brute force password attempts.

## ⚠️ Legal Disclaimer

**This tool is intended for educational and authorized penetration testing purposes only.** Unauthorized use against systems without explicit permission is illegal and unethical. The developers are not responsible for any misuse of this software. Always ensure you have written permission before testing any system.

## Features

- Automated brute force password testing
- Selenium WebDriver integration for browser automation
- Sequential password attempt strategy (0-9999)
- Real-time logging of attempts
- Chrome browser compatibility

## Prerequisites

- Python 3.6+
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd password-cracker
   ```

2. Install required Python packages:
   ```bash
   pip install selenium
   ```

3. Download the ChromeDriver executable that matches your Chrome browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

4. Place the `chromedriver.exe` file in the same directory as `login.py`

## Usage

1. **Configure the target**: Edit `login.py` and fill in the required fields:
   - Target website URL
   - Username field ID
   - Password field ID/name
   - Login button ID
   - Any additional form elements

2. **Set credentials**: Update the username and initial configuration in the script

3. **Run the tool**:
   ```bash
   python login.py
   ```

The tool will automatically attempt passwords from 0000 to 9999 and log the progress.

## Configuration

Before running, you must configure the following in `login.py`:

- **Browser URL**: Set the target website URL
- **Element IDs**: Update all element locators (username field, password field, buttons)
- **Username**: Set the target username to test against

## Output

The tool provides real-time console output showing:
- Current timestamp
- Password attempt number
- Success/failure status

## Limitations

- Sequential brute force (0-9999 range only)
- Single-threaded execution
- Requires manual configuration for each target
- Dependent on stable element locators

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security Notice

This tool demonstrates common web application vulnerabilities. Use responsibly and only on systems you own or have permission to test. Consider implementing rate limiting, CAPTCHAs, and account lockout mechanisms in your own applications to prevent such attacks.

