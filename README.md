# Password Variant Generator

## Overview
The **Password Variant Generator** is a Python script that generates multiple variants of a given password. It is designed to help penetration testers, ethical hackers, and security enthusiasts create custom wordlists for password-cracking tools like Hashcat and John the Ripper. The tool generates variants by adding numbers, special characters, and generating case combinations, making it easier to test the strength and resilience of passwords.

## Features
- **Appends Numbers:** Adds numbers (`0-9`) to the end of the original password.
- **Appends Special Characters:** Includes special characters (`!@#$%^&*_+.?`) at the end of the password.
- **Case Combinations:** Generates all possible uppercase and lowercase combinations of the password.
- **Inserts Characters:** Inserts numbers and special characters at random positions within the password.
- **Customizable Length:** Allows users to set a maximum length for generated variants.

## Installation
1. Make sure you have **Python 3** installed. You can download it from [Python's official website](https://www.python.org/downloads/).
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-variant-generator.git
   ```
3. Navigate to the project directory:
   ```bash
   cd password-variant-generator
   ```

## Usage
To use the Password Variant Generator, run the script with the following command:
```bash
python3 password_generator.py -p <original_password> -l <max_length>
```

### Command-Line Arguments
- `-p` or `--password`: **(Required)** The original password from which variants will be generated.
- `-l` or `--length`: **(Optional)** The maximum length of the password variants. Defaults to `20`.

### Example
```bash
python3 password_generator.py -p Password123 -l 15
```
This command generates variants of "Password123" with a maximum length of 15 characters and saves them to `password_variants.txt`.

## Output
The tool will create a file named `password_variants.txt` containing all the generated password variants. You can use this file directly with password-cracking tools like Hashcat or John the Ripper.

## How It Works
1. **Generates Basic Variants:** Appends numbers (e.g., `Password1234`) and special characters (e.g., `Password123!`) to the end of the password.
2. **Creates Case Combinations:** Converts the password into all possible uppercase and lowercase combinations (e.g., `password123`, `PASSWORD123`, `PassWord123`).
3. **Inserts Characters:** Adds numbers and special characters at random positions within the password to create more variations.
4. **Ensures Length Compliance:** Generates only variants that adhere to the specified maximum length.

## Integrating with Hashcat or John the Ripper
Once you’ve generated your wordlist, you can use it with popular password-cracking tools:

- **Hashcat:**
  ```bash
  hashcat -a 0 -m <hash_type> hash.txt password_variants.txt
  ```
- **John the Ripper:**
  ```bash
  john --wordlist=password_variants.txt hash.txt
  ```

## Requirements
- Python 3.x
- No additional libraries are required.

## Contributing
Contributions, suggestions, and feedback are always welcome! If you have any ideas for improvement or want to fix a bug, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is intended for educational and ethical hacking purposes only. Do not use it for unauthorized password cracking or illegal activities. Always obtain proper authorization before testing any system.

## Contact
For any questions or support, feel free to reach out:
- GitHub: [Fausto-Grilo](https://github.com/Fausto-Grilo)
